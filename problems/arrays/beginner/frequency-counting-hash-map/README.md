# Frequency Counting (Hash Map)

## What It Is

**Frequency counting** is the technique of tallying how many times each value
(or character) appears in a collection, storing those tallies in a hash map
(`dict` / `Counter`) or, when the value domain is small and fixed, a plain count
array. Once you have the counts, many questions become trivial lookups:

- "Does anything repeat?" -> look for a count `>= 2`.
- "What is the most frequent value?" -> take the max-count entry.
- "Is this a duplicate/anagram/unique character?" -> compare or inspect counts.

## When to Use It

Reach for frequency counting whenever a problem cares about **how often** things
occur rather than their order or position:

- Detecting duplicates or unique elements.
- Comparing two collections as multisets (anagrams, intersections).
- Finding majority / most-frequent / top-k elements.
- Any "count then decide" pattern.

It usually replaces an `O(n^2)` pairwise-comparison brute force with a single
counting pass.

## Complexity

- **Time:** `O(n)` to build the counts (one pass), plus whatever the follow-up
  question costs (often another `O(n)` or `O(k log k)` selection).
- **Space:** `O(k)`, where `k` is the number of distinct keys. For a fixed
  alphabet (e.g. 26 lowercase letters), this is effectively `O(1)` and a count
  array beats a hash map on constant factors.

**Rule of thumb:** trade `O(k)` extra memory to collapse nested scans into a
single linear pass.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Contains Duplicate](problem-01-contains-duplicate/PROBLEM.md) | Detect whether any value appears at least twice. | Easy |
| 2 | [Valid Anagram](problem-02-valid-anagram/PROBLEM.md) | Check if two strings have identical character frequencies. | Easy |
| 3 | [First Unique Character in a String](problem-03-first-unique-character/PROBLEM.md) | Return the index of the first character with count one. | Easy |
| 4 | [Majority Element](problem-04-majority-element/PROBLEM.md) | Find the value appearing more than n/2 times. | Easy |
| 5 | [Intersection of Two Arrays II](problem-05-intersection-of-two-arrays-ii/PROBLEM.md) | Return the multiset intersection using min of counts. | Easy |
| 6 | [Top K Frequent Elements](problem-06-top-k-frequent-elements/PROBLEM.md) | Select the k values with the highest frequencies. | Medium |

Each problem folder contains `PROBLEM.md` (the statement), `solution.py` (an
empty template to fill in), and `SOLUTION.md` (the annotated answer key).
