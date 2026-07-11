# Backtracking on Grid

**Backtracking on a grid** is a systematic, depth-first search over the cells of a 2-D
board (or an abstract board like a chessboard) in which we *make a choice* at a cell,
*recurse* deeper, and then *undo* the choice ("un-mark", "un-place", "restore") before
trying the next candidate. It is the classic **choose -> explore -> un-choose** pattern
applied to matrix-shaped state.

## What it is

At every step you stand on some cell (or some position such as a chessboard row) and you
have a small set of candidate moves. For each candidate you:

1. **Check feasibility** — is the move inside the grid and consistent with the constraints
   built so far (not already visited, no queen attacking, digit not already used in the
   row/column/box, letter matches the target word, ...)?
2. **Choose** — apply the move by mutating shared state (mark the cell visited, place the
   queen, write the digit).
3. **Recurse** — solve the smaller remaining sub-problem.
4. **Un-choose (backtrack)** — restore the shared state exactly as it was so a *sibling*
   branch starts from a clean slate.

Because the state is restored on the way back up, a single mutable board can be reused for
the entire search instead of copying it at every node — this is what makes backtracking
memory-cheap compared to naive brute force.

## When to reach for it

Reach for grid backtracking when the problem asks you to **find one / count all / list all**
configurations of a matrix that satisfy local constraints, and greedy or DP does not apply
because choices interact non-locally. Typical signals:

- "Does the word exist in the board?" (Word Search)
- "Place N non-attacking queens / fill the Sudoku." (constraint satisfaction)
- "Visit every empty cell exactly once." (Hamiltonian-path flavor)
- The search space is exponential but heavy **pruning** (feasibility checks, ordering,
  a Trie) makes it tractable in practice.

## Typical complexity

- **Time:** exponential in the number of choices in the worst case. For an `m x n` grid
  with up to `k` neighbor moves and depth `L`, DFS from every start is `O(m * n * k^L)`.
  Constraint problems like N-Queens are `O(N!)` and Sudoku is `O(9^(empty cells))` in the
  worst case, but pruning collapses this dramatically on real inputs.
- **Space:** `O(L)` recursion stack plus the (reused) board and any auxiliary sets for
  constraint tracking — typically `O(m * n)` or `O(N)`.

The recurring idea: **the correctness comes from exhaustively trying every candidate, and
the performance comes from aggressive pruning + restoring state instead of copying it.**

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Word Search](problem-01-word-search/PROBLEM.md) | Medium | DFS from each cell, mark/unmark visited cells to trace a word. |
| 2 | [Unique Paths III](problem-02-unique-paths-iii/PROBLEM.md) | Hard | Count paths that walk over **every** empty cell exactly once. |
| 3 | [N-Queens](problem-03-n-queens/PROBLEM.md) | Hard | Place N non-attacking queens row by row, undo on conflict. |
| 4 | [Sudoku Solver](problem-04-sudoku-solver/PROBLEM.md) | Hard | Fill every empty cell with a valid digit, backtrack on dead ends. |
| 5 | [Word Search II](problem-05-word-search-ii/PROBLEM.md) | Hard | Backtracking driven by a Trie to find many words at once. |
