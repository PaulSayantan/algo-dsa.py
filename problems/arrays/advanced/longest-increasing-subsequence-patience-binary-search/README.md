# Longest Increasing Subsequence — Patience Sorting + Binary Search

## What it is

The **Longest Increasing Subsequence (LIS)** of an array is the longest
subsequence (order preserved, elements not necessarily contiguous) whose values
strictly increase. The naive dynamic program solves it in `O(n^2)`; the
**patience-sorting** insight solves it in `O(n log n)`.

### The core idea (patience sorting)

Deal the array left to right like cards onto piles. Maintain a `tails` array
where `tails[L]` = the **smallest possible tail value** of any increasing
subsequence of length `L + 1` seen so far. This array is always sorted, which
lets you binary search:

- For each value `x`, find the leftmost `tails[pos] >= x` (`bisect_left`).
- If `pos == len(tails)`, append `x` (start a new, longer pile).
- Otherwise overwrite `tails[pos] = x` (a smaller tail for that length is
  always at least as useful for future extensions).

At the end, `len(tails)` is the LIS length. Note that `tails` itself is *not*
generally a valid subsequence — only its length is meaningful.

### Reconstructing the actual subsequence

To recover a witnessing subsequence (not just its length), keep a
**parent-pointer** array: when `x = nums[i]` is placed at position `pos`,
record `parent[i]` = the index currently stored at length `pos - 1`, and store
`i` as the index owning length `pos`. Follow parent pointers back from the
element owning the last (longest) length and reverse.

### Strict vs non-decreasing

- **Strictly increasing** LIS → `bisect_left` (a lower-bound search).
- **Non-decreasing** longest subsequence → `bisect_right` (an upper-bound
  search).

Choosing the wrong one is the single most common bug in this family.

### When to reach for it

- You need an LIS/LDS **length** on `n` up to `~10^5` or more (the `O(n^2)` DP
  is too slow).
- A problem reduces to LIS after a clever **sort** (e.g. 2D chaining / box
  stacking / Russian-doll envelopes).
- "Minimum changes/deletions to make a sequence (non-)decreasing" → answer is
  `length - LIS/LNDS`.
- Peak/mountain problems needing LIS from the left and LDS from the right.

### Complexity

| | Time | Space |
|---|---|---|
| Patience + binary search | `O(n log n)` | `O(n)` |
| Classic DP (for comparison) | `O(n^2)` | `O(n)` |

### Dilworth's theorem (why the pile count is optimal)

By **Dilworth's theorem**, the minimum number of non-increasing subsequences
needed to cover the array equals the length of the longest strictly increasing
subsequence. Patience sorting realizes exactly this decomposition: each pile is
non-increasing, and the number of piles it produces is provably minimal —
which is precisely the LIS length.

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|-----------|---------|
| 1 | [Increasing Triplet Subsequence](problem-01-increasing-triplet-subsequence/PROBLEM.md) | Medium | Detect an increasing subsequence of length 3; the `tails` array capped at size 2 (LC 334). |
| 2 | [Longest Increasing Subsequence](problem-02-longest-increasing-subsequence/PROBLEM.md) | Medium | The canonical LIS length in `O(n log n)`, plus subsequence reconstruction (LC 300). |
| 3 | [Longest Obstacle Course at Each Position](problem-03-longest-obstacle-course-at-each-position/PROBLEM.md) | Hard | Per-index non-decreasing LIS using `bisect_right` (LC 1964). |
| 4 | [Russian Doll Envelopes](problem-04-russian-doll-envelopes/PROBLEM.md) | Hard | Sort width asc / height desc, then LIS on height (LC 354). |
| 5 | [Minimum Removals to Make Mountain Array](problem-05-minimum-removals-to-make-mountain-array/PROBLEM.md) | Hard | LIS from the left + LDS from the right to find the best peak (LC 1671). |
| 6 | [Minimum Operations to Make Array K-Increasing](problem-06-minimum-operations-k-increasing/PROBLEM.md) | Hard | Split into `k` chains; each costs `len - LNDS` via `bisect_right` (LC 2111). |
