# At Most / Exactly K Distinct

A variable-size sliding window plus a frequency map answers a whole family of 'distinct elements' questions. The core subroutine `atMost(k)` counts subarrays with **at most** `k` distinct values: as the right edge advances you shrink the left edge until the window has `<= k` distinct keys, then every subarray ending at `right` and starting anywhere in `[left, right]` is valid — add `right-left+1`. The classic identity `exactly(k) = atMost(k) - atMost(k-1)` then converts the harder exact-count problem into two easy at-most passes.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Subarrays with K Different Integers](problem-01-subarrays-with-k-distinct/PROBLEM.md) | exactly-K via atMost difference | Hard |
| 2 | [Fruit Into Baskets](problem-02-fruit-into-baskets/PROBLEM.md) | Longest at-most-2-distinct window | Medium |
| 3 | [Count Subarrays With At Most K Distinct Integers](problem-03-count-at-most-k-distinct/PROBLEM.md) | atMost counting subroutine | Medium |
| 4 | [Longest Subarray With At Most K Distinct Integers](problem-04-longest-subarray-k-distinct/PROBLEM.md) | Longest at-most-K-distinct window | Medium |
| 5 | [Count Substrings With Exactly K Distinct Characters](problem-05-exactly-k-distinct-substrings/PROBLEM.md) | exactly-K via atMost difference (chars) | Medium |
