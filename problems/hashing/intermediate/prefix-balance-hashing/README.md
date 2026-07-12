# Prefix Difference / Balance Hashing

Many 'equal counts of X and Y' questions become prefix-sum problems once you encode the two categories as `+1` and `-1` (everything else `0`). Then a subarray has equal counts iff the running **balance** is the same at both of its endpoints — exactly the prefix-sum-equals-target trick with target 0. Hash the balance: an **earliest-index** map maximises length, a **frequency** map counts subarrays. For three or more categories a single scalar no longer captures 'all equal', so normalise the count vector into a tuple of differences (e.g. `(c0-c1, c1-c2)`) and hash that instead — two prefixes share the tuple exactly when the categories in between are perfectly balanced.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Contiguous Array](problem-01-contiguous-array/PROBLEM.md) | 0->-1 balance, earliest-index map | Medium |
| 2 | [Longest Subarray With Equal Counts of Two Values](problem-02-longest-equal-two-values/PROBLEM.md) | +/-1 balance over two chosen values | Medium |
| 3 | [Count Balanced Binary Subarrays](problem-03-count-balanced-binary-subarrays/PROBLEM.md) | 0->-1 balance, frequency map | Medium |
| 4 | [Longest Substring With Equal Vowels and Consonants](problem-04-longest-equal-vowels-consonants/PROBLEM.md) | vowel/consonant +/-1 balance, earliest index | Medium |
| 5 | [Longest Subarray With Equal Counts of Three Categories](problem-05-longest-equal-three-categories/PROBLEM.md) | Normalized difference-tuple prefix, earliest index | Medium |
