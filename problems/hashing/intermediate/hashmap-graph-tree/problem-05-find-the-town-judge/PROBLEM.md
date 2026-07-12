# Find the Town Judge

**Difficulty:** Easy

**Source:** LeetCode 997 — Find the Town Judge

## Description

In a town of `n` people, the judge trusts nobody, everybody (except the judge) trusts the judge, and there is exactly one judge. Given the `trust` pairs `[a, b]` (a trusts b), return the judge's label or -1.

## Examples

### Example 1

```
Input:  n=2, trust=[[1,2]]
Output: 2
```

## Hint

Judge has indegree n-1 and outdegree 0; track both with maps.
