# Longest Consecutive Sequence

Put every value into a hash set for O(1) membership, then discover consecutive runs without sorting. The key trick: only begin expanding a run at a **run-start** — a value `x` for which `x-1` is absent from the set. From each start you walk `x, x+1, x+2, ...` while they remain in the set. Every value is visited by the inner walk at most once across all starts, so the total work is O(n) even though there is a nested loop. This same run-start idea answers 'how long', 'how many runs', 'which run', and 'does a run of length k exist'.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Longest Consecutive Sequence](problem-01-longest-consecutive-sequence/PROBLEM.md) | Run-start expansion in a set | Medium |
| 2 | [Count Maximal Consecutive Runs](problem-02-count-consecutive-runs/PROBLEM.md) | Counting run-starts | Easy |
| 3 | [Longest Consecutive Run (Return the Values)](problem-03-longest-consecutive-run-values/PROBLEM.md) | Return the longest run, tie-break smallest start | Medium |
| 4 | [Sum of the Longest Consecutive Run](problem-04-sum-of-longest-run/PROBLEM.md) | Aggregate over the longest run | Medium |
| 5 | [Consecutive Run of Length At Least K](problem-05-has-run-of-length-k/PROBLEM.md) | Existence of a length-k run | Easy |
