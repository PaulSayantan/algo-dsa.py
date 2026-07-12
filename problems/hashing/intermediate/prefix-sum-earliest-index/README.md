# Prefix Sum Earliest-Index Map

When the answer is the *longest* qualifying subarray (not a count), store the **earliest index** at which each prefix state first occurs. Since the range length is `i - first[state]`, keeping the earliest occurrence maximizes it — so you record a prefix state only the first time you see it. Seed `first[0] = -1` so a qualifying prefix that starts at index 0 measures its full length.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Maximum Size Subarray Sum Equals k](problem-01-max-size-subarray-sum-equals-k/PROBLEM.md) | Earliest-index prefix map | Medium |
| 2 | [Longest Well-Performing Interval](problem-02-longest-well-performing-interval/PROBLEM.md) | Balance + earliest index | Medium |
| 3 | [Longest Zero-Sum Subarray](problem-03-longest-zero-sum-subarray/PROBLEM.md) | Earliest equal prefix | Medium |
| 4 | [Max Non-Overlapping Subarrays With Sum Target](problem-04-max-nonoverlapping-subarrays/PROBLEM.md) | Greedy prefix cut | Medium |
| 5 | [Longest Subarray With Sum K (Negatives)](problem-05-longest-subarray-sum-k-negatives/PROBLEM.md) | Earliest-index, negatives | Medium |
