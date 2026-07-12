# Value-to-Index Mapping

A hash map's superpower is O(1) *reverse* lookup: given a value, instantly recover where (or to what) it maps. This technique stores value -> position, value -> rank, or value -> value bijections. It underlies designing a hash map itself, checking two strings are isomorphic (a consistent one-to-one character map), pattern matching, and reordering one array by another's positions. Two maps (both directions) enforce a true bijection.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design HashMap](problem-01-design-hashmap/PROBLEM.md) | Key -> slot index | Easy |
| 2 | [Isomorphic Strings](problem-02-isomorphic-strings/PROBLEM.md) | Two-way char bijection | Easy |
| 3 | [Word Pattern](problem-03-word-pattern/PROBLEM.md) | Char<->word bijection | Easy |
| 4 | [Relative Sort Array](problem-04-relative-sort-array/PROBLEM.md) | Value -> rank sort key | Easy |
| 5 | [Minimum Index Sum of Two Lists](problem-05-minimum-index-sum-two-lists/PROBLEM.md) | Name -> index lookup | Easy |
| 6 | [Shortest Distance to a Character](problem-06-shortest-distance-to-a-character/PROBLEM.md) | Nearest-position sweeps | Easy |
