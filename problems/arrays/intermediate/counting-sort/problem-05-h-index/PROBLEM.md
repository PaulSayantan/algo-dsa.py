# H-Index

**Difficulty:** Medium

**Source:** LeetCode 274 — H-Index

## Description

You are given an array of integers `citations` where `citations[i]` is the number of citations
a researcher received for their `i`-th paper. Return the researcher's **h-index**.

The h-index is defined as the maximum value `h` such that the researcher has published at
least `h` papers that have each been cited at least `h` times.

A citation count can never usefully exceed the number of papers `n` (the h-index is capped at
`n`), so you can bucket every paper by its citation count — capping counts at `n` — and then
scan those buckets from the highest citation level downward, accumulating how many papers have
"at least this many" citations.

## Constraints

- `n == citations.length`
- `1 <= n <= 5000`
- `0 <= citations[i] <= 1000`

## Examples

### Example 1

```
Input:  citations = [3,0,6,1,5]
Output: 3
```

**Explanation:** The researcher has 5 papers with 3, 0, 6, 1, and 5 citations. There are 3
papers with at least 3 citations each (the ones with 3, 6, and 5), and the remaining two have
no more than 3 citations, so the h-index is 3.

### Example 2

```
Input:  citations = [1,3,1]
Output: 1
```

**Explanation:** Two papers have at least 1 citation, but not 2 papers have at least 2
citations, so the largest valid `h` is 1.

### Example 3

```
Input:  citations = [0,0]
Output: 0
```

**Explanation:** No paper has even 1 citation, so the h-index is 0.

## Hint

The answer is at most `n`, so cap each citation count at `n` and **Counting Sort** the papers
into `n + 1` buckets by (capped) citation count. Then walk buckets from `n` down to `0`,
keeping a running total of papers seen so far; the first level where that running total is at
least the level itself is the h-index.
