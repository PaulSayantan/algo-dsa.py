# Word Search II

**Difficulty:** Hard

**Source:** LeetCode 212 — Word Search II

## Description

Given an `m x n` board of characters and a list of strings `words`, return **all words on
the board**.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent
cells are horizontally or vertically neighboring. The **same cell may not be used more than
once** in a single word. The same word may appear on the board along different paths, but it
should be returned at most once.

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of `words` are unique.

## Examples

### Example 1

```
Input:
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

**Explanation:**
- `"oath"`: o(0,0) -> a(0,1) -> t(1,1) -> h(2,1). Found.
- `"eat"`: e(1,0)... actually e(1,3) -> a(1,2) -> t(1,1). Found.
- `"pea"`: there is no `p` on the board. Not found.
- `"rain"`: `r(2,3)` has no adjacent `a` continuing to `in`. Not found.

(The output order does not matter; `["oath","eat"]` is equally valid.)

### Example 2

```
Input:
board = [["a","b"],
         ["c","d"]]
words = ["abcb"]

Output: []
```

**Explanation:** To spell `"abcb"` we would need to reuse the cell holding `b`, but a cell
cannot be used twice in one word, so `"abcb"` cannot be formed.

## Hint

Build a **Trie (Prefix Tree)** from all `words`, then run DFS backtracking from every board
cell, descending the Trie in lockstep. The Trie lets you prune a search path the instant the
prefix on the board matches no word, and lets you collect any word as soon as you reach its
end node.
