# Complement Lookup / Two Sum

The foundational hashing pattern for pair problems: scan left to right and, for each element `x`, ask the hash table whether the **complement** it needs (`target - x`, or `x ± k`) has already been seen. Storing values (or their counts / indices) as you go turns the naive O(n²) double loop into a single O(n) pass. It powers Two Sum, k-difference counting, and — by hashing pair sums — even 4-tuple problems.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Two Sum](problem-01-two-sum/PROBLEM.md) | Complement lookup, value->index | Easy |
| 2 | [Number of Good Pairs](problem-02-number-of-good-pairs/PROBLEM.md) | Running frequency count | Easy |
| 3 | [K-diff Pairs in an Array](problem-03-k-diff-pairs/PROBLEM.md) | Distinct-value complement (x + k) | Medium |
| 4 | [Count Number of Pairs With Absolute Difference K](problem-04-count-pairs-abs-diff-k/PROBLEM.md) | Two-sided complement (x-k, x+k) | Easy |
| 5 | [4Sum II](problem-05-4sum-ii/PROBLEM.md) | Map of pair sums | Medium |
| 6 | [Count Pairs Summing to Target](problem-06-count-pairs-summing-to-target/PROBLEM.md) | Complement count in one pass | Easy |
