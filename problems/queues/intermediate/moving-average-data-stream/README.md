# Moving Average from Data Stream

A sliding-window average over a stream is a textbook fixed-size queue: enqueue each new value and, when the window overflows, dequeue the oldest and subtract it from a running sum. Each update and query is O(1).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Moving Average from Data Stream](problem-01-moving-average/PROBLEM.md) | Fixed-window queue | Easy |
| 2 | [Number of Sub-arrays of Size K and Average >= Threshold](problem-02-subarrays-average-threshold/PROBLEM.md) | Fixed-window running sum | Medium |
| 3 | [Maximum Number of Vowels in a Substring of Given Length](problem-03-max-vowels-in-substring/PROBLEM.md) | Fixed-window running count | Medium |
| 4 | [Grumpy Bookstore Owner](problem-04-grumpy-bookstore-owner/PROBLEM.md) | Fixed-window gain maximization | Medium |
| 5 | [Maximum Points You Can Obtain from Cards](problem-05-max-points-from-cards/PROBLEM.md) | Fixed-window minimum | Medium |
