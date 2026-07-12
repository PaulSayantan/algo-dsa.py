# 132 Pattern Detection

A 132 pattern is indices i<j<k with nums[i] < nums[k] < nums[j]. Scanning right to left with a decreasing monotonic stack lets you track the largest possible '2' (a value that had a bigger '3' to its right); if any earlier element is smaller than that '2', a 132 pattern exists. O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [132 Pattern](problem-01-132-pattern/PROBLEM.md) | Right-to-left '2' tracking | Medium |
