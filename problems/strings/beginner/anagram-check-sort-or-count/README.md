# Anagram Check (Sort or Count)

Two strings are **anagrams** if one can be rearranged into the other — they contain
exactly the same characters with exactly the same frequencies, just in a different
order (e.g. `"listen"` and `"silent"`).

The core technique gives you two interchangeable ways to test this:

1. **Sort** both strings and compare. If the sorted character sequences are equal,
   the strings are anagrams. Simple to write, but costs `O(n log n)` per string.
2. **Count** (frequency table). Tally how many times each character appears in each
   string (an array of size 26 for lowercase letters, or a hash map for arbitrary
   characters) and compare the two tables. This runs in `O(n)` time.

## When to reach for it

- You need to decide whether two strings are permutations of each other.
- You need a canonical **signature** that is identical for every anagram of a word
  (the sorted string, or a tuple of character counts) so you can group or dedupe.
- You are sliding a fixed-length window across a string and repeatedly asking
  "does this window's character multiset match the pattern?" — maintain a running
  count and compare.

## Typical complexity

| Method | Time | Space |
| --- | --- | --- |
| Sort & compare | `O(n log n)` | `O(n)` (or `O(1)` extra if sorted in place) |
| Count & compare | `O(n)` | `O(k)` where `k` = alphabet size (`O(1)` for fixed alphabet) |

Counting is asymptotically faster and is the standard "optimal" answer; sorting is a
perfectly good, easy-to-remember fallback that is often fast enough.

## Problems

| # | Problem | Summary | Difficulty |
| --- | --- | --- | --- |
| 1 | [Valid Anagram](problem-01-valid-anagram/PROBLEM.md) | Decide whether one string is an anagram of another. | Easy |
| 2 | [Remove Adjacent Anagrams](problem-02-remove-adjacent-anagrams/PROBLEM.md) | Repeatedly delete a word that is an anagram of its predecessor. | Easy |
| 3 | [Minimum Steps to Make Two Strings Anagram](problem-03-min-steps-to-anagram/PROBLEM.md) | Count the fewest character replacements to make `t` an anagram of `s`. | Medium |
| 4 | [Group Anagrams](problem-04-group-anagrams/PROBLEM.md) | Bucket strings into groups that are anagrams of one another. | Medium |
| 5 | [Find All Anagrams in a String](problem-05-find-all-anagrams-in-a-string/PROBLEM.md) | Return every start index where a permutation of `p` occurs in `s`. | Medium |
