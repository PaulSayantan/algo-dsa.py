# Solution — Simplify Path

## Brute Force

Scan the raw path character by character, manually carving out each component
between slashes, collapsing runs of `'/'` on the fly, and applying the `.`/`..`
rules to a result list as you go. This works but forces you to detect component
boundaries and skip empty runs by hand — error-prone bookkeeping.

```python
def simplifyPath(path: str) -> str:
    stack = []
    i, n = 0, len(path)
    while i < n:
        while i < n and path[i] == "/":   # skip slash run
            i += 1
        j = i
        while j < n and path[j] != "/":   # read a component
            j += 1
        comp = path[i:j]
        if comp == "..":
            if stack:
                stack.pop()
        elif comp not in ("", "."):
            stack.append(comp)
        i = j
    return "/" + "/".join(stack)
```

- **Time:** `O(n)`.
- **Space:** `O(n)`.

The nested slash-skipping loops are exactly what a split call abstracts away.

## Optimal Approach (String Tokenization / Split)

Split on `'/'` to get components, then process them with a stack:

```python
def simplifyPath(path: str) -> str:
    stack = []
    for comp in path.split("/"):
        if comp == "" or comp == ".":
            continue          # empty token (from // or ends) or current dir
        if comp == "..":
            if stack:         # go up one level if possible
                stack.pop()
        else:
            stack.append(comp)  # a real directory name (incl. "...", "....")
    return "/" + "/".join(stack)
```

**Why it is correct.** `path.split("/")` breaks the path at every slash. Because
the path starts with `/` and may contain `//` or a trailing `/`, this yields some
**empty tokens** — those correspond exactly to redundant slashes and are skipped.
`'.'` is a no-op (current directory) and is skipped. `'..'` pops the most recent
directory (moving up), if any. Every other token is a genuine name and is pushed.
The stack therefore holds the canonical sequence of directories from root, and
`"/" + "/".join(stack)` rebuilds the path with single separators and a leading
slash. When the stack is empty the result is just `"/"` (the root), which is the
required behavior.

**Step by step** for `path = "/a/./b/../../c/"`:

1. `split("/")` → `["", "a", ".", "b", "..", "..", "c", ""]`.
2. `""` skip. `"a"` push → `["a"]`. `"."` skip. `"b"` push → `["a", "b"]`.
3. `".."` pop → `["a"]`. `".."` pop → `[]`. `"c"` push → `["c"]`. `""` skip.
4. Result: `"/" + "c"` = `"/c"`. Done.

For `path = "/home//foo/"`: split → `["", "home", "", "foo", ""]`; skips the
empties; stack `["home", "foo"]`; result `"/home/foo"`.

- **Time:** `O(n)` — one split plus one linear pass; each token is pushed/popped
  at most once.
- **Space:** `O(n)` for the token list and the stack.

## Key Insights & Edge Cases

- **`split("/")` deliberately produces empty tokens** for leading, trailing, and
  doubled slashes. Skipping `""` is how those redundant slashes collapse — this
  is the crux, and it is *why* `split("/")` (not `split()`) is the right call.
- **`..` on an empty stack is a no-op** — you cannot go above root. Guard the pop.
- **`...`, `....`, `_`, digits** are ordinary names, not special. Only the exact
  strings `"."` and `".."` are magic; everything else is pushed as-is.
- **Root edge case:** if every component is consumed (e.g. `"/../"`), the stack is
  empty and the answer is `"/"` — the `"/" + "/".join([])` expression yields
  exactly that.
- No trailing slash ever appears because `join` places separators only *between*
  elements and we prepend a single leading `/`.
