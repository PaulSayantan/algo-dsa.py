"""Execute solution/reference code and evaluate cases against it.

Both a learner's ``solution.py`` and a reference block extracted from
SOLUTION.md are loaded the same way: their top-level definitions are executed
into a fresh module namespace (with the ``if __name__ == "__main__"`` block
stripped so no printing/side effects happen at import). A case is graded by
replaying its ``setup`` statements then evaluating its ``call_src`` in a copy of
that namespace.
"""

from __future__ import annotations

import ast
import contextlib
import io
from typing import Any, Dict

from .parsing.solution_md import PREAMBLE


@contextlib.contextmanager
def _silence():
    """Suppress stdout/stderr while executing solution/reference code.

    Some reference snippets and solutions print demo output at import time or on
    call; that noise must not leak into the runner's output or reports.
    """
    devnull = io.StringIO()
    with contextlib.redirect_stdout(devnull), contextlib.redirect_stderr(devnull):
        yield


class LoadError(Exception):
    """Raised when solution/reference source cannot be turned into a namespace."""


def _strip_main(tree: ast.Module) -> ast.Module:
    body = []
    for node in tree.body:
        if isinstance(node, ast.If):
            test = node.test
            names = set()
            if isinstance(test, ast.Compare):
                for part in [test.left, *test.comparators]:
                    if isinstance(part, ast.Name):
                        names.add(part.id)
                    elif isinstance(part, ast.Constant) and isinstance(part.value, str):
                        names.add(part.value)
            if "__name__" in names and "__main__" in names:
                continue
        body.append(node)
    tree.body = body
    return tree


def make_namespace(source: str, *, preamble: str = "", name: str = "sol") -> Dict[str, Any]:
    """Return a namespace dict populated by executing ``source`` (minus main)."""
    full = preamble + source if preamble else source
    try:
        tree = ast.parse(full)
    except SyntaxError as e:
        raise LoadError(f"syntax error: {e}") from e
    tree = _strip_main(tree)
    ns: Dict[str, Any] = {"__name__": name}
    try:
        with _silence():
            exec(compile(tree, filename=f"<{name}>", mode="exec"), ns)  # noqa: S102
    except Exception as e:  # noqa: BLE001 - surfacing any import/def-time error
        raise LoadError(f"{type(e).__name__}: {e}") from e
    return ns


def make_reference_namespace(
    reference_code: str, *, needed_names=None, stateful_names=None
) -> Dict[str, Any]:
    """Namespace for a SOLUTION.md reference block (with dependency preamble).

    SOLUTION.md reference code is documentation-style and often defines a *free
    function* (e.g. ``def search(nums, target): ...``) even though the problem's
    cases call it through a ``Solution`` wrapper (``sol.search(...)``). When the
    cases need a name the reference doesn't define, we synthesize a lightweight
    stateless adapter class whose methods delegate to the matching free
    functions, so one reference form grades against either calling convention.

    ``stateful_names`` lists classes the cases construct *with arguments* (e.g.
    ``KthLargest(3, [...])``). A stateless free-function adapter cannot honor
    such constructor state, so we deliberately do NOT synthesize those — the
    dependent cases then error and are reported as ``unverifiable`` instead of
    being mis-flagged as content bugs.
    """
    ns = make_namespace(reference_code, preamble=PREAMBLE, name="ref")
    if needed_names:
        _install_adapters(ns, reference_code, needed_names, stateful_names or set())
    return ns


def _install_adapters(ns: Dict[str, Any], reference_code: str, needed_names, stateful_names) -> None:
    """Synthesize stateless class wrappers for calls the reference doesn't satisfy."""
    try:
        tree = ast.parse(reference_code)
    except SyntaxError:
        return
    free_funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    defined_classes = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}

    for name in needed_names:
        if name in ns or name in defined_classes or name in stateful_names:
            continue
        # A capitalized name used like a class (e.g. Solution) that isn't defined:
        # build a class exposing every free function as a method (self ignored).
        if name and name[0].isupper() and free_funcs:
            methods = {fname: _as_method(ns[fname]) for fname in free_funcs if fname in ns}
            if methods:
                methods["__init__"] = _flexible_init()
                ns[name] = type(name, (), methods)


def _as_method(func):
    def method(self, *args, **kwargs):  # noqa: ANN001
        return func(*args, **kwargs)

    return method


def _flexible_init():
    def __init__(self, *args, **kwargs):  # noqa: ANN001
        # Store constructor args in case a delegated function wants them; harmless
        # for the common stateless `Solution()` case.
        self._args = args
        self._kwargs = kwargs

    return __init__


def collect_needed_names(cases) -> set:
    """Top-level Name identifiers referenced by a case's setup + call source."""
    names: set = set()
    for case in cases:
        for src in [*case.setup, case.call_src]:
            try:
                node = ast.parse(src)
            except SyntaxError:
                continue
            for sub in ast.walk(node):
                if isinstance(sub, ast.Name):
                    names.add(sub.id)
    return names


def collect_stateful_class_names(cases) -> set:
    """Class names the cases construct *with arguments* (``Cls(arg, ...)``).

    Such classes carry constructor state, so a stateless free-function adapter
    would silently produce wrong answers. We surface them so the adapter skips
    them and the dependent cases are reported as unverifiable instead.
    """
    names: set = set()
    for case in cases:
        for src in case.setup:
            try:
                node = ast.parse(src)
            except SyntaxError:
                continue
            for sub in ast.walk(node):
                if (
                    isinstance(sub, ast.Call)
                    and isinstance(sub.func, ast.Name)
                    and sub.func.id
                    and sub.func.id[0].isupper()
                    and (sub.args or sub.keywords)
                ):
                    names.add(sub.func.id)
    return names


def eval_case(namespace: Dict[str, Any], setup: list, call_src: str) -> Any:
    """Replay ``setup`` then evaluate ``call_src`` in a shallow copy of ``namespace``.

    A shallow copy isolates top-level name rebindings between cases while still
    sharing the (stateless) function/class objects. Cases within a design-class
    op-sequence carry cumulative setup, so state is rebuilt per case rather than
    leaked across cases.
    """
    local = dict(namespace)
    with _silence():
        for stmt in setup:
            exec(stmt, local)  # noqa: S102
        return eval(call_src, local)  # noqa: S307
