# Duplicate Detection

Hashing is the natural tool to **detect, count, and locate repeated elements**. A set flags the first repeat; a `dict` of last-seen index adds positional constraints; a `Counter` classifies values by how often they occur (once, twice, missing). This family — find-all-duplicates, set-mismatch, disappeared numbers — all reduces to one linear counting pass. When the answer is a *collection*, return it in a canonical (sorted or index) order so the result is deterministic.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find All Duplicates in an Array](problem-01-find-all-duplicates/PROBLEM.md) | Count == 2 filter | Medium |
| 2 | [Set Mismatch](problem-02-set-mismatch/PROBLEM.md) | Count 2 vs count 0 | Easy |
| 3 | [Find All Numbers Disappeared in an Array](problem-03-find-disappeared-numbers/PROBLEM.md) | Absence from a presence set | Easy |
| 4 | [Unique Number of Occurrences](problem-04-unique-number-of-occurrences/PROBLEM.md) | Counts-of-counts uniqueness | Easy |
| 5 | [Contains Duplicate II](problem-05-contains-duplicate-ii/PROBLEM.md) | Last-seen-index map | Easy |
| 6 | [N-Repeated Element in Size 2N Array](problem-06-n-repeated-element/PROBLEM.md) | First repeat via set | Easy |
