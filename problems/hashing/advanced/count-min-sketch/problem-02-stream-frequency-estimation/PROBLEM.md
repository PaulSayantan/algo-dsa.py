# Frequency Estimation over a Stream

**Difficulty:** Medium

**Source:** Classic — heavy-hitter / stream frequency estimation

## Description

Feed a stream of integers into a Count-Min Sketch one event at a time (each `update(x)` adds 1), then query estimated frequencies. With collision-free inputs the estimate equals the exact number of times each value appeared; unseen values estimate to 0.

## Examples

### Example 1

```
Input:  stream 5,5,7,5,9,7; estimate(5)
Output: 3
```

**Explanation:** 5 appears three times.

### Example 2

```
Input:  estimate(11) (unseen)
Output: 0
```

**Explanation:** 11's counters were never incremented.

## Hint

Each stream event is update(x,1); estimate(x) is the min counter across rows.
