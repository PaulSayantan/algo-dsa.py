# Pair / K-Sum Counting with Frequencies

Instead of the O(n^2) double loop, count qualifying pairs directly from a frequency table. Three recurring shapes: (1) pairs of **equal keys** — a group of size `f` contributes `f*(f-1)/2` pairs; (2) **complement** counting — as you scan, add the number of previously-seen values that complete the target (equal diff, target sum, or a canonical group key); (3) **cross-group products** — hash all pair-sums of one half, then look up negations from the other half. The unifying idea is that many pair conditions reduce to 'same normalized key', so a `Counter` over that key turns counting into simple arithmetic.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Number of Good Pairs](problem-01-number-of-good-pairs/PROBLEM.md) | Equal-key pairs: f*(f-1)/2 | Easy |
| 2 | [Count Pairs With Absolute Difference K](problem-02-count-pairs-abs-diff-k/PROBLEM.md) | Complement counting (x-k, x+k) | Easy |
| 3 | [Count Nice Pairs in an Array](problem-03-count-nice-pairs/PROBLEM.md) | Equal-key pairs on num - rev(num) | Medium |
| 4 | [4Sum II](problem-04-4sum-ii/PROBLEM.md) | Cross-group pair-sum hashing | Medium |
| 5 | [Number of Pairs of Interchangeable Rectangles](problem-05-interchangeable-rectangles/PROBLEM.md) | Cross-group products on reduced-ratio key | Medium |
