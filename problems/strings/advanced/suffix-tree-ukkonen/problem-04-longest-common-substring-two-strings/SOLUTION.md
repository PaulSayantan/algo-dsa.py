# Solution — Longest Common Substring of Two Strings

## Brute Force

Enumerate every substring of `s1` and test membership in `s2`:

```python
best = ""
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        w = s1[i:j]
        if w in s2 and len(w) > len(best):
            best = w
```

`O(n1^2)` substrings, each `in`-check `O(n2)`, so `O(n1^2 * n2)`. The classic
**dynamic-programming** solution — `dp[i][j] = longest common suffix of
s1[:i], s2[:j]` — is `O(n1 * n2)` time and space, fine for a few thousand
characters but too slow/heavy near `5 * 10^4` each (`2.5 * 10^9` cells).

## Optimal Approach (Generalized Suffix Tree via Ukkonen)

**Key idea.** Build one suffix tree that contains the suffixes of *both* strings
— a **generalized suffix tree**. Do it by building an ordinary suffix tree over
the concatenation

```
text = s1 + '#' + s2 + '$'
```

using **two distinct terminals** `#` and `$` that appear nowhere in the inputs.
The `#` prevents any suffix of `s1` from "bleeding" into `s2`, and `$` makes the
whole thing explicit.

Tag each leaf by its source: a suffix whose start index is **before** the
position of `#` came from `s1`; otherwise it came from `s2`. Now:

```
longest common substring = deepest internal node whose subtree
                           contains at least one s1-leaf AND one s2-leaf
```

Its path label — trimmed at the first separator, since a genuine common
substring cannot contain `#` or `$` — is the answer.

### Steps

1. Concatenate `text = s1 + '#' + s2 + '$'` and build the suffix tree with
   **Ukkonen's algorithm** in `O(n1 + n2)`.
2. DFS bottom-up. Each node returns a 2-bit mask: bit 0 set if its subtree has an
   `s1`-leaf, bit 1 set if it has an `s2`-leaf (a leaf's bit is decided by
   comparing its suffix start index to the index of `#`).
3. A node with mask `== 3` (both bits) at string depth `d` represents a substring
   common to both strings. Track the deepest such node; trim its label at the
   first `#`/`$`.
4. Return `""` if no node reaches mask `3` outside the root.

### Why it is correct

If a string `w` is a common substring, it starts some suffix of `s1` and some
suffix of `s2`; both of those suffixes pass through the tree node spelling `w`,
so that node's subtree contains an `s1`-leaf and an `s2`-leaf — mask `3`.
Conversely, a mask-`3` node at depth `d` has, below it, a suffix from each source
sharing the first `d` characters, so those `d` characters (up to the first
separator) form a common substring. The longest common substring is thus the
deepest mask-`3` node. The separators guarantee the shared prefix cannot straddle
the boundary, so the label we return is a real common substring of both inputs.

### Reference implementation

Reuse the `SuffixTree` class from Problem 1 (with `leaf_idx` on leaves):

```python
class Solution:
    def longestCommonSubstring(self, s1, s2):
        SEP, TERM = "\x01", "\x00"          # two distinct terminals
        text = s1 + SEP + s2 + TERM
        st = SuffixTree(text)
        t = st.t
        sep_pos = len(s1)                    # index of SEP
        best_len = 0
        best_start = 0

        def some_leaf(node):
            cur = node
            while cur.children:
                cur = next(iter(cur.children.values()))
            return cur.leaf_idx

        def dfs(node, depth):
            nonlocal best_len, best_start
            if not node.children:                       # leaf
                return 1 if node.leaf_idx < sep_pos else 2
            mask = 0
            for child in node.children.values():
                edge_len = st._edge_end(child) - child.start
                mask |= dfs(child, depth + edge_len)
            if mask == 3 and node is not st.root and depth > best_len:
                start = some_leaf(node)
                seg = text[start:start + depth]
                cut = len(seg)
                for i, c in enumerate(seg):             # trim at first separator
                    if c == SEP or c == TERM:
                        cut = i
                        break
                if cut > best_len:
                    best_len = cut
                    best_start = start
            return mask

        dfs(st.root, 0)
        return "" if best_len == 0 else text[best_start:best_start + best_len]
```

### Complexity

- Build: `O(n1 + n2)` time / space (Ukkonen over the concatenation).
- DFS: `O(n1 + n2)` — the tree has linearly many nodes.
- Overall: **`O(n1 + n2)` time and space**, versus `O(n1 * n2)` for DP.

## Key Insights & Edge Cases

- **Two distinct terminals matter.** Using the *same* separator for the join and
  the end (or reusing an alphabet character) can merge suffixes across the
  boundary and produce a spurious "common substring" that spans both strings.
- **Tag leaves by position, not by rescanning.** Comparing each leaf's suffix
  start index against the position of `#` is `O(1)` per leaf.
- **Trim at separators.** A mask-`3` node's raw path label can extend a little
  past the boundary in edge cases; always cut at the first `#`/`$` before
  measuring/returning.
- **No common character** → no non-root node reaches mask `3` → return `""`
  (e.g. `"abcde"` vs `"fghij"`).
- **Generalizes to k strings.** Use `k` distinct terminals and a `k`-bit mask;
  the deepest node whose subtree covers all `k` sources is the longest substring
  common to all of them (this is the standard way to solve the "longest substring
  common to all `k` strings" problem).
- **Recursion depth:** convert the DFS to an explicit stack for very long inputs.
