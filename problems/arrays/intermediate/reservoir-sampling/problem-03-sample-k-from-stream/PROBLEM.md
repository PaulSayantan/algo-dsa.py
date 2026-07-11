# Sample K Items From a Stream

**Difficulty:** Medium

**Source:** Classic — Vitter's *Algorithm R* (Reservoir Sampling); common systems /
interview problem ("uniformly sample k tweets/log lines from an infinite feed").

## Description

You are given an **iterator/stream** of items whose total length `n` is **not known in
advance** (it may be very large, or the stream may only be consumed once). You are also
given an integer `k`.

Return a list of `k` items chosen **uniformly at random without replacement** from the
stream. Every possible size-`k` subset of the stream must be equally likely, which is
equivalent to requiring that each individual item ends up in the sample with probability
exactly `k/n`.

You must process the stream in a **single pass** and use only `O(k)` additional memory
(you may **not** materialize the entire stream into a list first). If the stream contains
fewer than `k` items, return all of them.

## Constraints

- `1 <= k`
- `0 <= n` (the stream length is unknown until fully consumed).
- Items may be of any type; duplicates in value are allowed and treated as distinct
  stream positions.
- You may read the stream **once**, front to back.

## Examples

### Example 1

```
Input:  stream = [10, 20, 30, 40, 50], k = 2
Output: [30, 50]        # one possible run
```

**Explanation:** With `n = 5`, any 2 of the 5 items form a valid sample; there are
`C(5, 2) = 10` equally likely subsets, each with probability `1/10`. Each individual
item appears in the returned sample with probability `k/n = 2/5`. `[30, 50]` is one such
outcome; another run might yield `[10, 40]`.

### Example 2

```
Input:  stream = [7, 8], k = 5
Output: [7, 8]
```

**Explanation:** The stream has only `2 < 5 = k` items, so the entire stream is returned.
There is nothing to sample away.

## Hint

Fill a reservoir with the first `k` items. For the i-th item after that (1-indexed),
pick a random slot `j` in `[0, i-1]`; if `j < k`, overwrite `reservoir[j]` with the new
item. This is **Reservoir Sampling** (Algorithm R) generalized to `k > 1`.
