# Prefix Sum + Hash Map (Frequency)

The most important intermediate hashing family. Maintain a running prefix sum and a Hash Map from each prefix-sum *value* to how many times it has occurred. A subarray ending at the current index sums to `k` exactly when some earlier prefix sum equals `cur - k`, so `count += freq[cur - k]`. Seeding `freq[0] = 1` counts subarrays starting at index 0. This handles negatives and zeros (where a sliding window fails) in one O(n) pass.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Subarray Sum Equals K](problem-01-subarray-sum-equals-k/PROBLEM.md) | Prefix-sum frequency map | Medium |
| 2 | [Binary Subarrays With Sum](problem-02-binary-subarrays-with-sum/PROBLEM.md) | 0/1 prefix-sum counting | Medium |
| 3 | [Count Number of Nice Subarrays](problem-03-count-nice-subarrays/PROBLEM.md) | Parity prefix count | Medium |
| 4 | [Count Subarrays Summing to Target (with Negatives)](problem-04-count-subarrays-target-negatives/PROBLEM.md) | Negative-safe prefix counting | Medium |
| 5 | [Count Zero-Sum Subarrays](problem-05-count-zero-sum-subarrays/PROBLEM.md) | Equal prefix-sum pairs | Medium |
