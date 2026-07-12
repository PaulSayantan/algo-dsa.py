# Remove K Digits / Smallest Result

To make the smallest (or lexicographically best) result after deletions, a monotonic stack greedily drops a larger digit/letter whenever a smaller one arrives and budget remains. This 'pop bigger predecessors' rule builds the optimal answer in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Remove K Digits](problem-01-remove-k-digits/PROBLEM.md) | Greedy digit removal | Medium |
| 2 | [Remove Duplicate Letters](problem-02-remove-duplicate-letters/PROBLEM.md) | Lexicographic dedup | Medium |
| 3 | [Most Competitive Subsequence](problem-03-most-competitive-subsequence/PROBLEM.md) | Size-k monotonic stack | Medium |
| 4 | [Maximum Number After Removing K Digits](problem-04-maximum-number-after-removing-k-digits/PROBLEM.md) | Decreasing drop-stack (maximize) | Medium |
| 5 | [Create Maximum Number](problem-05-create-maximum-number/PROBLEM.md) | Split + merge max subsequences | Medium |
