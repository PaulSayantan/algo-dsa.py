# Word Search — Solution

## Brute Force

Conceptually you want to try every possible path of length `len(word)` through
the grid and check if any spells the word. Enumerating all self-avoiding paths
explicitly (e.g., building the list of every path first, then comparing) is
astronomically expensive: from each start there are up to 3 continuations per
step (you can't turn back onto the cell you came from), giving on the order of
`O(m·n·3^L)` candidate paths, and materializing them wastes memory too.

- **Time:** `O(m · n · 3^L)` where `L = len(word)`.
- **Space:** `O(L)` per path, but enumerating all of them up front is wasteful.

The trick is that DFS with pruning explores the *same* path tree but abandons a
path the instant a letter mismatches, so it never builds the doomed suffixes.

## Optimal Approach (Backtracking / DFS)

Try each cell as a starting point. A DFS `dfs(r, c, k)` asks: "can I match
`word[k:]` starting at cell `(r, c)`?" Mark the cell visited before recursing and
restore it afterward — this in-place marking *is* the undo step.

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, k):
        if k == len(word):
            return True                      # matched every letter
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[k]):
            return False                     # out of bounds or mismatch -> prune
        tmp, board[r][c] = board[r][c], '#'  # choose: mark visited
        found = (dfs(r + 1, c, k + 1) or
                 dfs(r - 1, c, k + 1) or
                 dfs(r, c + 1, k + 1) or
                 dfs(r, c - 1, k + 1))
        board[r][c] = tmp                    # undo: restore the cell
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

**Why it is correct.**

- The base case `k == len(word)` fires only after `word[0..L-1]` have all been
  matched along a connected chain of distinct cells, which is exactly the
  definition of the word existing.
- Marking `board[r][c] = '#'` (a sentinel that matches no letter) before the four
  recursive calls guarantees the current cell cannot be reused deeper in the same
  path; restoring it on the way out frees it for *other* independent paths.
- Bounds/mismatch checks prune instantly, so we only follow prefixes that are
  actually consistent with the word.

**Step by step for `word = "ABCCED"` on the sample board:**

`dfs(0,0,0)` sees 'A' = `word[0]`, marks it, recurses right to `(0,1)`='B' =
`word[1]`, then `(0,2)`='C', then down to `(1,2)`='C', then down to `(2,2)`='E',
then left to `(2,1)`='D' with `k` reaching 6 = `len(word)` → returns `True` up
the chain.

- **Time:** `O(m · n · 3^L)` — `m·n` starts, and after the first step each cell
  has at most 3 unvisited orthogonal neighbors to try.
- **Space:** `O(L)` recursion depth (in-place marking uses no extra grid).

## Key Insights & Edge Cases

- **In-place marking with a sentinel** avoids a separate `visited` matrix; just
  remember to restore the original character on the way out (the undo).
- **First-letter filter** (only start DFS where `board[r][c] == word[0]`) is a
  cheap prune; the code above folds the check into the recursion instead.
- **Optional letter-frequency prune:** if any letter of `word` appears more often
  than it does in the whole board, return `False` immediately. Reversing `word`
  to start the search from its rarer endpoint can also cut branching.
- **Edge cases:** a length-1 word succeeds iff that letter appears anywhere;
  a word longer than `m·n` can never fit and DFS naturally returns `False`.
- **Don't forget to undo** — if you leave cells marked, later starting positions
  will wrongly see them as blocked and you'll get false negatives.
