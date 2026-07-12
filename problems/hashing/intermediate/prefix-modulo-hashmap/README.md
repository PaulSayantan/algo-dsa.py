# Prefix Modulo Hashing

For divisibility-by-`k` questions, hash the prefix sum's **remainder** instead of its value. If two prefix boundaries share the same remainder `((cur % k) + k) % k`, the subarray between them has a sum divisible by `k`. Store remainder *frequencies* to count such subarrays, or the *earliest index* of each remainder to find the longest one. Normalizing the remainder into `[0, k)` keeps negatives correct.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Subarray Sums Divisible by K](problem-01-subarray-sums-divisible-by-k/PROBLEM.md) | Remainder frequency map | Medium |
| 2 | [Continuous Subarray Sum](problem-02-continuous-subarray-sum/PROBLEM.md) | Earliest remainder, length>=2 | Medium |
| 3 | [Make Sum Divisible by P](problem-03-make-sum-divisible-by-p/PROBLEM.md) | Shortest remainder-matching subarray | Medium |
| 4 | [Count Subarrays Divisible by K](problem-04-count-subarrays-divisible-by-k/PROBLEM.md) | Remainder pair counting | Medium |
| 5 | [Longest Subarray Divisible by K](problem-05-longest-subarray-divisible-by-k/PROBLEM.md) | Earliest remainder, longest gap | Medium |
