# Sliding Window + Frequency Map

Maintain a frequency map (a `Counter`/`defaultdict`) over a moving window and update it incrementally: add the entering character, remove the leaving one. For **fixed-length** windows (anagram / permutation search) you slide one step at a time and compare the window map against a target map. For **variable-length** windows you grow the right edge and shrink the left edge to restore an invariant (no repeats, or at most K distinct). Because each element enters and leaves at most once, the whole scan is O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find All Anagrams in a String](problem-01-find-all-anagrams/PROBLEM.md) | Fixed window, map equality | Medium |
| 2 | [Permutation in String](problem-02-permutation-in-string/PROBLEM.md) | Fixed window, map equality | Medium |
| 3 | [Longest Substring Without Repeating Characters](problem-03-longest-substring-no-repeat/PROBLEM.md) | Variable window, last-seen map | Medium |
| 4 | [Longest Substring with At Most Two Distinct Characters](problem-04-at-most-two-distinct/PROBLEM.md) | Variable window, at most 2 distinct | Medium |
| 5 | [Longest Substring with At Most K Distinct Characters](problem-05-at-most-k-distinct/PROBLEM.md) | Variable window, at most K distinct | Medium |
