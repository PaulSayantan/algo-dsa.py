# Suffix Tree (Ukkonen's Algorithm)

A **suffix tree** for a string `s` (of length `n`) is a compressed trie
(a *Patricia trie*) that stores **every suffix of `s`**. Each edge is labelled
with a substring of `s` (stored as a pair of indices `[start, end)`, not the
actual characters), every internal non-root node has at least two children, and
every suffix of `s` corresponds to exactly one root-to-leaf path. Because edges
are compressed, the whole structure has at most `2n - 1` nodes and uses `O(n)`
space even though it represents all `O(n^2)` substrings.

**Ukkonen's algorithm** builds this tree **online** and in **linear time**
`O(n)` (over a constant-size alphabet, or `O(n log |Σ|)` with balanced-tree
child maps). It processes the text one character at a time, maintaining three
clever ideas that turn a naive `O(n^2)` or `O(n^3)` construction into `O(n)`:

- **Global end / leaf pointers** — all leaf edges share one growing `END`
  value, so extending every leaf by one character (Rule 1) is `O(1)`.
- **The active point** `(active_node, active_edge, active_length)` — remembers
  where the last insertion happened so the next one starts there instead of
  re-walking from the root.
- **Suffix links** — a pointer from an internal node spelling `xα` to the node
  spelling `α`. Following a suffix link jumps to "the same place, one character
  shorter," which is what makes the amortized cost linear.

## When to reach for a suffix tree

Reach for a suffix tree when a problem is about the **set of substrings of a
string** (or of a few strings) and you need more than a single pattern search:

- Count / locate **occurrences** of many patterns in a fixed text (each query in
  `O(m + occ)` after an `O(n)` build).
- **Longest repeated substring** — the deepest internal node.
- **Number of distinct substrings** — the total length of all edge labels.
- **Longest common substring** of two (or more) strings — the deepest internal
  node whose subtree contains leaves from every string (generalized suffix
  tree).
- **Shortest unique substring**, longest common extension, matching statistics,
  and more.

If you only ever need suffix *ordering* or LCP values, a suffix array + Kasai's
algorithm is simpler to code; reach for the suffix tree when the *tree shape*
(internal nodes, subtree leaf counts, deepest branching) is what the problem
needs.

## Complexity

| Operation                                | Time                | Space  |
|------------------------------------------|---------------------|--------|
| Build (Ukkonen, constant alphabet)       | `O(n)`              | `O(n)` |
| Build (general alphabet, map children)   | `O(n log \|Σ\|)`    | `O(n)` |
| Substring / pattern search (length `m`)  | `O(m)`              | —      |
| Report all `occ` occurrences of pattern  | `O(m + occ)`        | —      |
| Longest repeated substring               | `O(n)` (DFS)        | `O(n)` |
| Count distinct substrings                | `O(n)` (DFS)        | `O(n)` |
| Longest common substring of two strings  | `O(n1 + n2)`        | `O(n1 + n2)` |

> **Terminal sentinel.** Suffix-tree algorithms append a unique character
> (`$`, `#`, …) that appears nowhere else in the input. This guarantees no
> suffix is a prefix of another, so every suffix ends at a distinct leaf and the
> tree is "explicit." All problems below rely on this trick.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Count Pattern Occurrences](problem-01-count-pattern-occurrences/PROBLEM.md) | Build the tree once, then count how many times each query pattern occurs in the text | Medium |
| 2 | [Longest Duplicate Substring](problem-02-longest-repeated-substring/PROBLEM.md) | Return the longest substring that appears at least twice (deepest internal node) | Medium |
| 3 | [Count Distinct Substrings](problem-03-count-distinct-substrings/PROBLEM.md) | Count the number of distinct non-empty substrings (sum of edge-label lengths) | Hard |
| 4 | [Longest Common Substring of Two Strings](problem-04-longest-common-substring-two-strings/PROBLEM.md) | Deepest node of a generalized suffix tree whose subtree spans both strings | Hard |
| 5 | [Shortest Unique Substring](problem-05-shortest-unique-substring/PROBLEM.md) | Shortest substring that occurs exactly once (leaf edges of the tree) | Hard |
