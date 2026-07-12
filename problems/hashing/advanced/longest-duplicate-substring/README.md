# Longest Duplicate Substring (Binary Search + Rolling Hash)

If a duplicate substring of length `L` exists, then a duplicate of every shorter length exists too — the property is **monotone** in `L`. That lets us **binary-search** the answer length: for each candidate `L`, roll a hash over every length-`L` window and check whether any two windows collide (verified by a direct comparison to defeat hash collisions). Each check is O(n) and the search adds a `log n` factor, giving O(n log n) overall — far better than the O(n^2) of comparing all substrings.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Longest Duplicate Substring](problem-01-longest-duplicate-substring/PROBLEM.md) | Binary search + rolling hash | Hard |
| 2 | [Longest Repeated Substring Length](problem-02-longest-repeated-substring-length/PROBLEM.md) | Longest repeated substring | Hard |
| 3 | [Repeated DNA Sequences](problem-03-repeated-dna-sequences/PROBLEM.md) | Fixed-length window hashing | Medium |
