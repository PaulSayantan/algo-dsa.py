# Range / Interval DP

**Range (Interval) DP** is a dynamic-programming paradigm where the state is a
*contiguous subinterval* `[i, j]` of a sequence, and the answer for a large
interval is built from answers on strictly smaller sub-intervals. The defining
move is to pick a **split point** or a **special element** `k` inside `(i, j)`
and combine the two resulting pieces.

## The core template

Two recurrence shapes cover almost every interval-DP problem:

1. **Split into two adjacent halves** (matrix-chain style):
   ```
   dp[i][j] = min/max over k in [i, j)  of  dp[i][k] + dp[k+1][j] + cost(i, k, j)
   ```
   Here `k` is the *place where you cut* the interval into `[i..k]` and `[k+1..j]`.

2. **Choose the "last / special" element** (burst-balloons style):
   ```
   dp[i][j] = best over k in (i, j)  of  dp[i][k] + dp[k][j] + gain(i, k, j)
   ```
   Here `k` is the element handled *last*, so its neighbors `i` and `j` are still
   present when its contribution is computed.

## When to reach for it

- The problem is defined on a **linear sequence** (array, string, list of matrices,
  polygon vertices) and the natural subproblem is a **contiguous chunk**.
- The answer depends on **the order in which you merge / remove / partition**
  elements, and merging two adjacent solved pieces has a well-defined cost.
- Greedy fails because a locally cheap merge can force an expensive later merge —
  you must try every split point.
- Classic signals: *"merge adjacent"*, *"burst / remove and gain based on neighbors"*,
  *"minimum cost to combine"*, *"partition into palindromes"*, *"parenthesize"*,
  *"triangulate a polygon"*.

## Complexity

- **States:** `O(n^2)` intervals `[i, j]`.
- **Transition:** trying every split `k` costs `O(n)` per state.
- **Total time:** `O(n^3)` (some problems drop to `O(n^2)` with Knuth's
  optimization or extra state).
- **Space:** `O(n^2)` for the DP table.

## Iteration order (the one thing beginners get wrong)

`dp[i][j]` depends on **shorter** intervals, so you must fill the table by
**increasing interval length** (or iterate `i` downward and `j` upward). Never
loop `i` and `j` naively from `0`.

```python
for length in range(2, n + 1):          # interval length
    for i in range(0, n - length + 1):  # left endpoint
        j = i + length - 1              # right endpoint
        dp[i][j] = combine(...)
```

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Longest Palindromic Subsequence](problem-01-longest-palindromic-subsequence/PROBLEM.md) | Endpoints-match interval DP; a gentle first `dp[i][j]` | Medium |
| 2 | [Minimum Score Triangulation of Polygon](problem-02-minimum-score-triangulation-of-polygon/PROBLEM.md) | Split-point DP over polygon chords | Medium |
| 3 | [Matrix Chain Multiplication](problem-03-matrix-chain-multiplication/PROBLEM.md) | The canonical "where to parenthesize" interval DP | Medium/Hard |
| 4 | [Palindrome Partitioning II](problem-04-palindrome-partitioning-ii/PROBLEM.md) | Interval palindrome table feeding a min-cut DP | Hard |
| 5 | [Burst Balloons](problem-05-burst-balloons/PROBLEM.md) | "Last element to remove" interval DP | Hard |
| 6 | [Strange Printer](problem-06-strange-printer/PROBLEM.md) | Merging equal-endpoint prints across an interval | Hard |
