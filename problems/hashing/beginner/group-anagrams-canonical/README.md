# Group Anagrams / Canonical Signature

Many problems ask you to group or compare objects that are 'the same up to some transformation'. The pattern is to compute a **canonical signature** — a value that is identical for equivalent objects and different otherwise — and use it as a hash-map key. For anagrams the signature is the sorted letters (or a 26-length count vector); for shifted strings it is the gaps between consecutive letters mod 26. Because both the group order and the order within a group are arbitrary, the references sort each group and the list of groups so the oracle is exact.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Group Anagrams](problem-01-group-anagrams/PROBLEM.md) | Sorted-letters signature | Medium |
| 2 | [Valid Anagram](problem-02-valid-anagram/PROBLEM.md) | Frequency-map equality | Easy |
| 3 | [Group Shifted Strings](problem-03-group-shifted-strings/PROBLEM.md) | Gap-vector signature | Medium |
| 4 | [Groups of Special-Equivalent Strings](problem-04-groups-of-special-equivalent-strings/PROBLEM.md) | Even/odd count signature | Medium |
| 5 | [Determine if Two Strings Are Close](problem-05-determine-if-two-strings-are-close/PROBLEM.md) | Char-set + freq-multiset | Medium |
