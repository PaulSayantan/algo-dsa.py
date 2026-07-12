# Sum of Subarray Minimums / Maximums

Instead of enumerating all O(n²) subarrays, count each element's *contribution*: a monotonic stack finds, for every element, how many subarrays it is the minimum (or maximum) of — the product of the distances to the nearest smaller element on each side. Summing value × leftCount × rightCount gives the total in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Sum of Subarray Minimums](problem-01-sum-of-subarray-minimums/PROBLEM.md) | Contribution counting | Medium |
| 2 | [Sum of Subarray Ranges](problem-02-sum-of-subarray-ranges/PROBLEM.md) | Max-sum minus min-sum | Medium |
