# Group Anagrams (Hashing Signature)

## What it is

The **hashing signature** technique solves a family of string problems by mapping
each string to a *canonical key* (a "signature") such that two strings share the
same key **if and only if** they are equivalent under the relation the problem
cares about (anagram, cyclic shift, isomorphism, etc.). Once you have a
signature function, you drop every string into a hash map keyed by its signature.
Strings that collide in the same bucket are, by construction, equivalent.

The classic instance is **anagrams**: two words are anagrams exactly when they
contain the same multiset of characters. Two signatures capture this:

- **Sorted-string signature** — sort the characters of the word.
  `"eat" -> "aet"`, `"tea" -> "aet"`. Cost `O(k log k)` per word of length `k`.
- **Count signature** — a length-26 (or length-alphabet) tuple of character
  frequencies, e.g. `"eat" -> (1,0,0,0,1,...,1,...)`. Cost `O(k)` per word.

The same idea generalizes: the signature is just "whatever normal form makes
equivalent things identical." For shifted strings it is the tuple of
consecutive-character differences; for pattern matching it is the
first-occurrence normalization; for the "close strings" relation it is the
sorted multiset of character *frequencies*.

## When to reach for it

- You are asked to **group**, **count**, or **detect** items that are equal
  under a permutation / relabeling / shift, not under literal equality.
- The words "anagram", "rearrangement", "same characters", "isomorphic",
  "shifted", or "frequencies match" appear in the prompt.
- You want `O(n)` grouping instead of `O(n^2)` pairwise comparison.

## Typical complexity

For `n` strings of maximum length `k` over an alphabet of size `A`:

| Signature | Time to build all keys | Extra space |
|-----------|------------------------|-------------|
| Sorted string | `O(n * k log k)` | `O(n * k)` |
| Count tuple | `O(n * k)` (or `O(n * (k + A))`) | `O(n * k)` |

Hash-map insertion/lookup adds `O(1)` expected per string, so total grouping is
dominated by signature construction.

## Problems

| # | Problem | Signature used | Difficulty |
|---|---------|----------------|------------|
| 1 | [Valid Anagram](problem-01-valid-anagram/PROBLEM.md) | Compare two count signatures | Easy |
| 2 | [Group Anagrams](problem-02-group-anagrams/PROBLEM.md) | Sorted-string / count key into a hash map | Medium |
| 3 | [Find All Anagrams in a String](problem-03-find-all-anagrams-in-a-string/PROBLEM.md) | Sliding-window count signature | Medium |
| 4 | [Group Shifted Strings](problem-04-group-shifted-strings/PROBLEM.md) | Consecutive-difference signature | Medium |
| 5 | [Find and Replace Pattern](problem-05-find-and-replace-pattern/PROBLEM.md) | First-occurrence normalization signature | Medium |
| 6 | [Determine if Two Strings Are Close](problem-06-determine-if-two-strings-are-close/PROBLEM.md) | Sorted count-of-counts signature | Medium |
