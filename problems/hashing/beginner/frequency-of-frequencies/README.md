# Frequency-of-Frequencies

Counting how often each value occurs is the first move of countless hashing problems, but the real insight often lives one level up: reason about the **distribution of those counts**. Are all the occurrence-counts distinct? How many complete copies of a target word do the letter supplies allow? Which value's count is off by one? A `Counter` (or a fixed-size bucket array when the value range is small) turns these into a couple of linear passes.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Unique Number of Occurrences](problem-01-unique-number-of-occurrences/PROBLEM.md) | Distinct occurrence counts | Easy |
| 2 | [Maximum Number of Balloons](problem-02-maximum-number-of-balloons/PROBLEM.md) | Count ratios (supply/demand) | Easy |
| 3 | [Set Mismatch](problem-03-set-mismatch/PROBLEM.md) | Count == 2 and count == 0 | Easy |
| 4 | [Check If N and Its Double Exist](problem-04-check-if-n-and-its-double-exist/PROBLEM.md) | Seen-set complement lookup | Easy |
| 5 | [How Many Numbers Are Smaller Than the Current Number](problem-05-smaller-numbers-than-current/PROBLEM.md) | Count buckets + prefix sum | Easy |
