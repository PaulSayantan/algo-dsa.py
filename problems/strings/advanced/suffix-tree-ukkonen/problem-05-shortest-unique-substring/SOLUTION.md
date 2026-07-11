# Solution — Shortest Unique Substring

## Brute Force

Try lengths from short to long; for each length, hash every window and keep the
ones that appear exactly once:

```python
from collections import Counter
n = len(s)
for L in range(1, n + 1):
    cnt = Counter(s[i:i + L] for i in range(n - L + 1))
    uniq = [t for t, c in cnt.items() if c == 1]
    if uniq:
        return uniq[0]     # any length-L unique substring
```

Each length costs `O(n * L)` to build the windows, and in the worst case the
answer length is `O(n)`, giving `O(n^3)` overall (or `O(n^2)` with rolling
hashes, still quadratic). Too slow near `n = 10^5`.

## Optimal Approach (Suffix Tree via Ukkonen)

**Key idea.** In the suffix tree of `s$`, the number of times a substring occurs
equals the number of **leaves** below the point that spells it. A substring is
**unique** iff that point has exactly **one** leaf below it.

Where do "leaf-count 1" points first appear as you descend? Exactly on the
**leaf edges**. An internal node always has `>= 2` children, hence `>= 2` leaves,
so it is never unique. But the moment you step one character onto a leaf edge,
the count drops to `1`. Therefore:

- For each leaf edge, its parent node at string depth `d` has `>= 2` leaves (not
  unique), and stepping one character onto the leaf edge gives a unique substring
  of length `d + 1`.
- The **shortest unique substring** is the minimum of `d + 1` over all leaf
  edges — i.e. it ends one character into the leaf edge attached to the
  **shallowest** internal parent (skipping any candidate whose extra character is
  the sentinel `$`).

### Steps

1. Append a unique terminal and build the suffix tree with **Ukkonen's
   algorithm** in `O(n)`.
2. One DFS to compute `leaf_count(v)` for every node.
3. DFS again tracking each node's string depth `d`. For every child that is a
   **leaf** (leaf-count 1) whose first edge character is *not* the sentinel, the
   candidate unique substring has length `d + 1` and equals
   `s[leaf_start : leaf_start + d + 1]` (recoverable from the leaf edge's start
   index). Keep the minimum length.
4. Return the best substring (never empty: the whole string is always unique).

### Why it is correct

Occurrences = leaves below the spelling point (Problem 1). Unique ⇔ exactly one
leaf below. A string `w` of length `L` is unique and *minimal at its position*
precisely when its length-`(L-1)` prefix still occurs `>= 2` times but `w` itself
occurs once — that transition happens exactly at the first character of a leaf
edge, where the parent (the prefix) has `>= 2` leaves and the child leaf has `1`.
So every "locally shortest" unique substring corresponds to one leaf edge with
length `parent_depth + 1`, and the global shortest is the minimum over all leaf
edges. We skip candidates whose extra character is the sentinel because
`w + "$"` is not a substring of `s`.

Worked check: for `"aabaaab$"`, every single character repeats, so all
depth-0 (root) children lead to subtrees with `>= 2` leaves; the shallowest leaf
edge whose parent is at depth `1` yields length `2`, and the corresponding
substring is `"ba"` — matching the expected output.

### Reference implementation

Reuse the `SuffixTree` class from Problem 1:

```python
class Solution:
    def shortestUniqueSubstring(self, s):
        term = "\x00"
        st = SuffixTree(s + term)
        t = st.t

        leaf_count = {}
        def count_dfs(node):
            if not node.children:
                leaf_count[id(node)] = 1
                return 1
            c = sum(count_dfs(ch) for ch in node.children.values())
            leaf_count[id(node)] = c
            return c
        count_dfs(st.root)

        best_len = None
        best = ""

        def dfs(node, depth):               # depth = string depth of `node`
            nonlocal best_len, best
            for child in node.children.values():
                start = child.start
                if leaf_count[id(child)] == 1 and t[start] != term:
                    cand_len = depth + 1     # parent path + 1 char onto leaf edge
                    if best_len is None or cand_len < best_len:
                        best_len = cand_len
                        best = t[start - depth: start + 1]
                edge_len = st._edge_end(child) - start
                dfs(child, depth + edge_len)

        dfs(st.root, 0)
        return best
```

### Complexity

- Build: `O(n)` time / `O(n)` space (Ukkonen).
- Two DFS passes over `O(n)` nodes: `O(n)`.
- Overall: **`O(n)` time, `O(n)` space**.

## Key Insights & Edge Cases

- **Unique ⇔ single leaf.** Occurrence count is the subtree leaf count; "exactly
  once" means exactly one leaf, which only happens on leaf edges — internal nodes
  always branch and so always repeat.
- **Length is `parent_depth + 1`.** You do not need the whole leaf edge; the
  first character past the branching parent already makes the substring unique.
- **Skip the sentinel.** A leaf edge may start with `$`; the substring
  `prefix + "$"` is not a real substring of `s`, so guard against it. (In such a
  case the real shortest-unique candidate at that position is found via a
  different, longer leaf edge, or via the whole-string leaf.)
- **All characters repeat** (e.g. `"aabaaab"`): the answer has length `>= 2`; the
  algorithm naturally finds the shallowest length-2 unique edge (`"ba"`).
- **Highly repetitive** (e.g. `"aaaa"`): the tree is essentially a path, and the
  only single-leaf point that avoids the sentinel is the whole string, giving
  `"aaaa"`.
- **Always exists.** The full string is always unique, so `best` is never empty
  for non-empty `s`.
- **Recursion depth:** switch to an explicit stack for the longest inputs.
