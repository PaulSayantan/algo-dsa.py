# Sliding Window (Fixed Size)

The **fixed-size sliding window** technique maintains a "window" of exactly `k`
consecutive elements as it moves across an array or string from left to right.
Instead of recomputing a metric (sum, average, count, frequency map, ...) from
scratch for every window — which would be O(n·k) — you compute it once for the
first window and then **update it incrementally**: as the window slides one step
right, you *add* the element that just entered on the right and *subtract* the
element that just left on the left. This turns an O(n·k) brute force into a single
O(n) pass.

## When to reach for it

- The problem asks about **contiguous** subarrays or substrings of a **fixed
  length `k`** (max/min sum, max average, count of qualifying windows, etc.).
- The window metric is **cheaply updatable** on a slide — sums, counts, and
  frequency tables all satisfy this (add one, remove one).
- You catch yourself writing a nested loop that re-scans `k` elements for every
  starting index. That inner loop is exactly the redundant work the window removes.

Contrast with the *variable-size* sliding window (where the window grows and shrinks
based on a condition). Here the width `k` never changes — only the position does.

## The core pattern

```
window_metric = metric(first k elements)      # initialize on arr[0..k-1]
best = window_metric
for right in range(k, n):
    window_metric += arr[right]                # element entering on the right
    window_metric -= arr[right - k]            # element leaving on the left
    best = combine(best, window_metric)        # e.g. max/min/count
```

## Complexity

| Aspect | Cost |
|--------|------|
| Time | **O(n)** — every element enters and leaves the window exactly once |
| Space | **O(1)** for numeric metrics; **O(σ)** when tracking a frequency map over an alphabet of size σ |

Compared to the O(n·k) brute force of summing each window independently, the sliding
window is a strict improvement whenever `k > 1`.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Maximum Sum Subarray of Size K](problem-01-maximum-sum-subarray-size-k/PROBLEM.md) | Find the largest sum among all contiguous subarrays of length `k`. | Easy |
| 2 | [Maximum Average Subarray I](problem-02-maximum-average-subarray-i/PROBLEM.md) | Return the maximum average of any contiguous subarray of length `k` (LeetCode 643). | Easy |
| 3 | [Max Vowels in a Substring of Length K](problem-03-max-vowels-substring-length-k/PROBLEM.md) | Count the most vowels in any length-`k` substring (LeetCode 1456). | Medium |
| 4 | [Subarrays of Size K with Average ≥ Threshold](problem-04-subarrays-average-ge-threshold/PROBLEM.md) | Count length-`k` subarrays whose average meets a threshold (LeetCode 1343). | Medium |
| 5 | [Find All Anagrams in a String](problem-05-find-all-anagrams-in-string/PROBLEM.md) | Find every start index where a permutation of `p` occurs in `s` (LeetCode 438). | Medium |
| 6 | [Maximum Points You Can Obtain from Cards](problem-06-max-points-from-cards/PROBLEM.md) | Take `k` cards from the two ends to maximize points via a complement window (LeetCode 1423). | Medium-Hard |
