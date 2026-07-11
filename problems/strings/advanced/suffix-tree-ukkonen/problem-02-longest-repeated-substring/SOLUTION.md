# Solution — Longest Duplicate Substring

## Brute Force

Enumerate every substring and check whether it appears again:

```python
best = ""
for i in range(n):
    for j in range(i + 1, n + 1):
        t = s[i:j]
        if s.count(t) >= 2 and len(t) > len(best):
            best = t
```

There are `O(n^2)` substrings and each `count`/search is `O(n)`, so this is
`O(n^3)`. A common speedup is **binary search on the length `L`** plus rolling
hashing: for a candidate `L`, hash every length-`L` window and look for a
collision. That is `O(n log n)` *expected* but is randomized (hash collisions
can give wrong answers without a second modulus) — it is LeetCode 1044's usual
"accepted" solution. The suffix tree gives a **deterministic** answer.

## Optimal Approach (Suffix Tree via Ukkonen)

**Key idea.** In the suffix tree of `s$`, a string `w` is the path-label of an
**internal node** exactly when at least two different suffixes share `w` as a
prefix and then diverge — that is, `w` occurs at two different positions. So a
substring is *duplicated* iff its path ends at (or passes through) an internal
**branching** node (a non-root node with `>= 2` children).

The longest duplicated substring is therefore the path-label of the **deepest
internal branching node**, where "depth" is the **string depth** = number of
characters from the root to that node.

### Steps

1. Append a unique terminal and build the suffix tree with **Ukkonen's
   algorithm** in `O(n)`.
2. DFS from the root, accumulating string depth by adding each edge's label
   length.
3. Track the deepest node (other than the root) that has `>= 2` children. Its
   path-label is the answer. To recover the actual characters, take any leaf in
   that node's subtree, giving a start index `p`, and return `s[p : p + depth]`.
4. If no such node exists (only the root branches), return `""`.

### Why it is correct

An internal node `v` at string depth `d` has `>= 2` children, meaning its
path-label `w` (`|w| = d`) is followed by at least two distinct characters
across the suffixes of `s$`. Those are two distinct occurrences of `w` in `s`,
so `w` is duplicated. Conversely, if a substring `w` occurs at two positions
`i != j`, the suffixes at `i` and `j` both start with `w`; the terminal makes
them differ eventually, so their paths split at or below depth `|w|`, meaning
some internal node at depth `>= |w|` exists. Hence the maximum duplicated length
equals the maximum string depth over internal nodes. (Because the terminal `$`
appears once, no internal branching node's label ends inside the sentinel, so
the recovered substring never includes `$`.)

### Reference implementation

Reuse the `SuffixTree` class from Problem 1 (`_edge_end`, `children`,
`leaf_idx`, `root`), then:

```python
class Solution:
    def longestDupSubstring(self, s):
        st = SuffixTree(s + "\x00")
        best_depth = 0
        best_start = 0

        def some_leaf(node):           # any suffix start index below `node`
            cur = node
            while cur.children:
                cur = next(iter(cur.children.values()))
            return cur.leaf_idx

        def dfs(node, depth):
            nonlocal best_depth, best_start
            if node is not st.root and len(node.children) >= 2 and depth > best_depth:
                best_depth = depth
                best_start = some_leaf(node)
            for child in node.children.values():
                edge_len = st._edge_end(child) - child.start
                dfs(child, depth + edge_len)

        dfs(st.root, 0)
        if best_depth == 0:
            return ""
        return s[best_start:best_start + best_depth]
```

### Complexity

- Build: `O(n)` time / `O(n)` space (Ukkonen).
- DFS: `O(n)` — the tree has `O(n)` nodes. Recovering the substring is `O(depth)`.
- Overall: **`O(n)` time, `O(n)` space**, deterministic.

## Key Insights & Edge Cases

- **Internal node ⇔ repeat.** This is the single most useful structural fact
  about suffix trees: internal branching nodes are exactly the repeated
  substrings, and the deepest one is the longest repeat.
- **Overlaps allowed.** Two occurrences correspond to two suffix start indices;
  they may overlap (`"aaaa"` → `"aaa"`). If the problem demanded *non-overlapping*
  repeats you would additionally need the two occurrence positions to differ by
  at least the length, which the plain suffix tree does not enforce.
- **No repeat:** if the only branching node is the root, every first character
  leads to a distinct path and nothing repeats → return `""` (e.g. `"abcd"`).
- **Ties** in length: any deepest internal node is acceptable; the DFS keeps the
  first maximal one it finds.
- **Recover via a leaf.** Because edges store index ranges (not characters), you
  read the actual substring from the original string using any leaf's start index
  and the node's string depth.
- **Recursion depth.** A degenerate string like `"aaaa...a"` produces a deep tree;
  in Python raise the recursion limit or convert the DFS to an explicit stack for
  the largest inputs.
