# Number of Recent Calls

**Difficulty:** Easy

**Source:** LeetCode 933 — Number of Recent Calls

## Description

Implement `RecentCounter`. `ping(t)` records a request at time `t` (strictly increasing) and returns the number of requests in the inclusive window `[t - 3000, t]`.

## Examples

### Example 1

```
Input:  ping 1,100,3001,3002
Output: 1,2,3,3
```

## Hint

Queue of timestamps; on each ping, pop from the front while front < t-3000; return the size.
