# Trie (Prefix Tree)

A **Trie** (pronounced "try", from re**trie**val), also called a **prefix tree**, is a
rooted tree that stores a dynamic set of strings. Each edge is labeled with a single
character, and every node represents the prefix formed by the characters along the path
from the root to that node. A boolean flag on a node marks whether the prefix ending there
is a complete word that was inserted.

## Why a Trie?

Hash sets answer "is this exact string present?" in O(L) but tell you nothing about
*prefixes*. A Trie shines whenever the shape of the keys matters:

- **Prefix queries / autocomplete** — "give me all words starting with `app`".
- **Word dictionaries** — spell checkers, `startsWith` checks, word games.
- **Longest matching prefix** — routing tables, replacing words by their root.
- **Wildcard / pattern matching** — `.` matches any character (DFS over children).
- **Binary tries** — store the bits of integers to answer max-XOR / range queries.

The key win is that strings sharing a common prefix share the same path, so lookups do
work proportional to the query length rather than to the number of stored words.

## Structure

```
class TrieNode:
    children: dict[char, TrieNode]   # or a fixed-size array of 26 for 'a'..'z'
    is_end:   bool                   # True if a word ends at this node
```

## Complexity

Let `L` be the length of the word/query and `N` the number of inserted words.

| Operation                | Time     | Space (per insert) |
|--------------------------|----------|--------------------|
| Insert a word            | O(L)     | up to O(L) new nodes |
| Search exact word        | O(L)     | O(1) |
| Search prefix (startsWith) | O(L)   | O(1) |
| Wildcard search (`.`)    | O(26^k · L) worst case | O(1) |
| Build over all words     | O(total characters) | O(total characters · Σ) |

Space is O(total characters × alphabet-size) in the worst case (nothing shared); shared
prefixes reduce it in practice. Using a `dict` for children keeps memory proportional to
the branches that actually exist.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Implement Trie (Prefix Tree)](problem-01-implement-trie/PROBLEM.md) | Build the core insert / search / startsWith operations | Medium |
| 2 | [Map Sum Pairs](problem-02-map-sum-pairs/PROBLEM.md) | Store values in the Trie and sum over a prefix | Medium |
| 3 | [Replace Words](problem-03-replace-words/PROBLEM.md) | Find the shortest dictionary root that prefixes a word | Medium |
| 4 | [Add and Search Word (Wildcards)](problem-04-add-and-search-word/PROBLEM.md) | Search with `.` wildcards via DFS over children | Medium |
| 5 | [Maximum XOR of Two Numbers in an Array](problem-05-maximum-xor/PROBLEM.md) | Binary Trie of bits to greedily maximize XOR | Medium |
| 6 | [Word Search II](problem-06-word-search-ii/PROBLEM.md) | Trie + DFS backtracking over a grid | Hard |
