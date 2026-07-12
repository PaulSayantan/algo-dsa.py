# Set Algebra (Union / Intersection / Difference)

A **hash set** turns the classic set operations into linear-time scans: membership is O(1) average, so union, intersection, difference, subset, and disjointness tests all run in O(n) instead of O(n log n) sorting or O(n²) nested loops. The recurring trick is to load one collection into a set and probe it while streaming the other. Because set iteration order is not stable, return **sorted** results (or counts) whenever the answer is a collection, so the output is deterministic.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Intersection of Two Arrays](problem-01-intersection-of-two-arrays/PROBLEM.md) | Set intersection | Easy |
| 2 | [Intersection of Two Arrays II](problem-02-intersection-of-two-arrays-ii/PROBLEM.md) | Multiset intersection | Easy |
| 3 | [Jewels and Stones](problem-03-jewels-and-stones/PROBLEM.md) | Set membership count | Easy |
| 4 | [Find the Difference of Two Arrays](problem-04-find-the-difference-of-two-arrays/PROBLEM.md) | Symmetric set difference | Easy |
| 5 | [Intersection of Three Sorted Arrays](problem-05-intersection-of-three-sorted-arrays/PROBLEM.md) | Triple set intersection | Easy |
