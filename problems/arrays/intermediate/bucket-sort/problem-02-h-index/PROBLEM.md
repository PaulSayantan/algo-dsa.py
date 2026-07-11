# H-Index

**Difficulty:** Medium

**Source:** LeetCode 274 — H-Index

## Description

Given an array of integers `citations` where `citations[i]` is the number of
citations a researcher received for their `i`-th paper, return the researcher's
**h-index**.

The h-index is defined as the maximum value `h` such that the researcher has
published **at least `h` papers that have each been cited at least `h` times**.

## Constraints

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## Examples

### Example 1

```
Input:  citations = [3, 0, 6, 1, 5]
Output: 3
Explanation: The researcher has 5 papers with 3, 0, 6, 1, 5 citations.
Three of them (the papers with 3, 6, and 5 citations) have at least 3 citations
each, and the remaining two have no more than 3 citations. So the h-index is 3.
It cannot be 4, because that would require 4 papers each cited at least 4 times,
and only 2 papers (6 and 5) clear that bar.
```

### Example 2

```
Input:  citations = [1, 3, 1]
Output: 1
Explanation: At least 1 paper (in fact all three) has at least 1 citation, so
h >= 1. There are not 2 papers each cited at least 2 times (only the paper with
3 citations qualifies), so h cannot be 2. The h-index is 1.
```

### Example 3

```
Input:  citations = [0, 0]
Output: 0
Explanation: No paper has any citation, so there is no h >= 1 that works. The
h-index is 0.
```

## Hint

A paper's citation count only matters up to `n` (an h-index can never exceed the
number of papers). Create `n + 1` buckets, drop each paper into the bucket for
`min(citations[i], n)`, then sweep from the highest bucket downward accumulating
paper counts. This **Bucket Sort** avoids sorting and runs in `O(n)`.
