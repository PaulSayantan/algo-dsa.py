# Word Search

**Difficulty:** Medium

**Source:** LeetCode 79 — Word Search

## Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word`
exists in the grid.

The word can be constructed from letters of sequentially **adjacent** cells, where adjacent
cells are horizontally or vertically neighboring (up, down, left, right — **not** diagonal).
The **same cell may not be used more than once** in a single word.

You start the search from any cell whose letter equals the first character of `word`, then
step to an unused adjacent cell whose letter equals the next character, and so on until the
entire word is matched.

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of only lowercase and uppercase English letters.

## Examples

### Example 1

```
Input:
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"

Output: true
```

**Explanation:** Path A(0,0) -> B(0,1) -> C(0,2) -> C(1,2) -> E(2,2) -> D(2,1). Each cell is
adjacent to the previous one and each is used only once, so the word "ABCCED" is present.

### Example 2

```
Input:
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"

Output: false
```

**Explanation:** To spell "ABCB" we would reach A(0,0) -> B(0,1) -> C(0,2), but the only
remaining adjacent `B` is the one at (0,1) which is already used. No path can reuse a cell,
so the word cannot be formed.

### Example 3

```
Input:
board = [["a"]]
word = "a"

Output: true
```

**Explanation:** The single cell already equals the whole word.

## Hint

Use **Backtracking on Grid**: launch a DFS from every cell matching `word[0]`, mark the
current cell as used before recursing to its neighbors, and un-mark it when you backtrack so
other paths may reuse it.
