# Print Article

**Difficulty:** Medium

Source: HDU 3507 ("Print Article").

## Description

Zero has an old printer that does not work well. He wants to print an article with
`N` words, where word `i` has a positive cost `cost[i]`. The words must be printed in
order, and Zero prints them in **consecutive batches**: each batch is a contiguous
block of one or more words.

Printing a batch made of a contiguous block of words costs

```
( sum of cost over the words in the batch )^2 + M
```

where `M` is a fixed constant. The total printing cost is the sum over all batches.
Zero wants to split the `N` words into consecutive batches so that the **total cost
is minimized**. Print that minimum.

Let `S[i] = cost[1] + cost[2] + ... + cost[i]` be prefix sums (`S[0] = 0`). If `dp[i]`
is the minimum cost to print the first `i` words, then

```
dp[0] = 0
dp[i] = min over 0 <= j < i of ( dp[j] + (S[i] - S[j])^2 + M )
```

and the answer is `dp[N]`. The direct evaluation is `O(N^2)`.

## Constraints

- `1 <= N <= 5 * 10^5`
- `0 <= M <= 1000`
- `0 <= cost[i] <= 100` (all costs are non-negative, so prefix sums are non-decreasing)
- The answer fits in a 64-bit signed integer.

## Examples

### Example 1

```
Input:  N = 5, M = 5, cost = [5, 9, 5, 7, 5]
Output: 230
```

Explanation: Merging words into big batches squares a large sum, which dominates
the small penalty `M = 5`. The optimum keeps every word in its own batch:
`[5], [9], [5], [7], [5]` costs
`(25+5) + (81+5) + (25+5) + (49+5) + (25+5) = 30 + 86 + 30 + 54 + 30 = 230`. No
consecutive partition does better, so the answer is `230`.

### Example 2

```
Input:  N = 3, M = 100, cost = [10, 10, 10]
Output: 600
```

Explanation: Even with the large penalty `M = 100`, squaring a merged sum hurts
more: one batch costs `30^2 + 100 = 1000`; two batches `[10,10],[10]` cost
`(400+100)+(100+100)=700`; three singleton batches cost `3 * (100 + 100) = 600`.
The minimum is `600`.

### Example 3

```
Input:  N = 6, M = 0, cost = [3, 1, 4, 1, 5, 9]
Output: 133
```

Explanation: With `M = 0` there is no penalty for extra batches, and squaring only
punishes large batches, so keeping every word separate is optimal:
`3^2 + 1^2 + 4^2 + 1^2 + 5^2 + 9^2 = 9 + 1 + 16 + 1 + 25 + 81 = 133`.

## Hint

Expand `(S[i] - S[j])^2` to get
`dp[i] = S[i]^2 + M + min_j ( (-2 S[j]) * S[i] + (dp[j] + S[j]^2) )`. This is a
minimum over lines evaluated at `x = S[i]`. Since costs are non-negative the slopes
`-2 S[j]` are non-increasing and the queries `S[i]` are non-decreasing, so a
**monotonic Convex Hull Trick** solves it in `O(N)`.
