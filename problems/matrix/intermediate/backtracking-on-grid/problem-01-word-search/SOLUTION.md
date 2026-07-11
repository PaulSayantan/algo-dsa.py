# Word Search — Solution

## Brute Force

The naive idea is to enumerate every possible path of length `len(word)` in the grid and
check whether any of them spells the word. From each of the `m * n` cells there are up to 4
directions, so a path of length `L` gives roughly `4^L` candidate paths per starting cell.

- **Time:** `O(m * n * 4^L)` where `L = len(word)` — with no early termination this
  explores every path of that length.
- **Space:** `O(L)` for the path being built (plus a copy of visited state if you copy the
  board at each step, which is wasteful).

The generate-all-paths framing is essentially the same as the optimal DFS but without
pruning; the real work is recognizing that we can prune the instant a letter mismatches.

## Optimal Approach (Backtracking on Grid)

Run a depth-first search that grows the matched prefix one cell at a time and prunes as
soon as a candidate fails.

**Algorithm**

1. For each cell `(r, c)` in the board, start a DFS trying to match `word[0]`.
2. `dfs(r, c, i)` attempts to match `word[i]` at cell `(r, c)`:
   - If `(r, c)` is out of bounds, or `board[r][c] != word[i]`, return `False`.
   - If `i == len(word) - 1`, we matched the last character — return `True`.
   - **Choose:** mark `(r, c)` as used (overwrite with a sentinel like `#`, or use a
     `visited` set).
   - **Explore:** recurse into the four neighbors with `i + 1`; if any returns `True`,
     propagate `True`.
   - **Un-choose:** restore `board[r][c]` to its original letter before returning.
3. Return `True` if any starting cell yields a full match.

**Why it is correct.** DFS explores every path that keeps matching the prefix of `word`.
The used-cell marking guarantees the "no cell reused" rule holds along the current path,
and restoring it on backtrack ensures that constraint is *only* enforced within a single
path, never leaking between sibling branches. Since we try every valid continuation, if a
valid path exists we will find it; if none exists, all branches fail and we return `False`.

**Reference implementation**

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[i]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"          # choose: mark used
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            board[r][c] = tmp          # un-choose: restore
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
```

- **Time:** `O(m * n * 4^L)` worst case (`L = len(word)`). In practice the letter-mismatch
  pruning cuts this to a tiny fraction, and after the first branch each step has at most 3
  new directions (you never go back), so it is closer to `O(m * n * 3^L)`.
- **Space:** `O(L)` recursion depth. The in-place `#` marking uses no extra grid; a
  `visited` set would add `O(L)` more.

## Key Insights & Edge Cases

- **Restore on backtrack.** Forgetting to reset `board[r][c]` is the single most common bug —
  it permanently "consumes" cells and breaks sibling branches.
- **In-place marking vs. visited set.** Overwriting with a sentinel avoids allocating a set,
  but you must be sure the sentinel can never equal a real letter. A separate `visited` grid
  is safer if letters could include your sentinel.
- **Early exit.** Return `True` up the whole stack the moment a full match is found; do not
  keep searching.
- **Optional micro-pruning:** if the multiset of characters in `word` is not a subset of the
  board's character counts, you can return `False` immediately. You can also start the search
  from the rarer of `word[0]` / `word[-1]` (reversing the word) to prune faster.
- **Single-cell / single-char edge cases** (`board = [["a"]]`, `word = "a"`) fall out
  naturally: the base case `i == len(word) - 1` (or `i == len(word)`) fires immediately.
