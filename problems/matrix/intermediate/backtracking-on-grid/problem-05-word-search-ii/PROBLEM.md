# Word Search II

**Difficulty:** Hard

**Source:** LeetCode 212 — Word Search II

## Description

Given an `m x n` board of characters and a list of strings `words`, return **all words on
the board**.

Each word must be constructed from letters of sequentially **adjacent** cells, where
adjacent cells are horizontally or vertically neighboring. The **same cell may not be used
more than once** in a single word. Each word in the answer should appear only once, in any
order.

This is the many-words generalization of Word Search (LeetCode 79). Searching for each word
independently is too slow when `words` is large, so the words are stored together in a
**Trie** and a single DFS from each cell walks the board and the Trie simultaneously,
collecting every word it can complete.

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

**Explanation:** "oath" is traced o(0,0) -> a(0,1) -> t(1,1) -> h(2,1), and "eat" is traced
e(1,3) -> a(1,2) -> t(1,1). Each step moves to an adjacent, previously-unused cell. Neither
"pea" nor "rain" can be formed from adjacent cells, so only "eat" and "oath" are returned.

### Example 2

```
Input:
board = [["a","b"],
         ["c","d"]]
words = ["abcb"]

Output: []
```

**Explanation:** "abcb" would need to reuse the cell containing "b", but a cell cannot be
used twice in one word, so no valid path spells it and the answer is empty.

### Example 3

```
Input:
board = [["a"]]
words = ["a","aa"]

Output: ["a"]
```

**Explanation:** "a" is the single cell. "aa" cannot be formed because the only `a` cell
cannot be reused, so just "a" is returned.

## Hint

Use **Backtracking on Grid** driven by a **Trie**: insert every word into a Trie, then DFS
from each cell descending the Trie by the current letter. Mark cells visited/unvisited as
you go, and whenever a Trie node marks the end of a word, add that word to the result.
