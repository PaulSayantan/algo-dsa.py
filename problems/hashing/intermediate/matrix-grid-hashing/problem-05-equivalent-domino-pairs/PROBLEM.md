# Number of Equivalent Domino Pairs

**Difficulty:** Easy

**Source:** LeetCode 1128 — Number of Equivalent Domino Pairs

## Description

Dominoes `[a,b]` and `[c,d]` are equivalent if `{a,b} == {c,d}` (same values, order-insensitive). Return the number of pairs `(i, j)` with `i < j` such that domino `i` is equivalent to domino `j`.

## Examples

### Example 1

```
Input:  [[1,2],[2,1],[3,4],[5,6]]
Output: 1
```

## Hint

Canonicalize each domino to (min,max); running count += cnt[key] then cnt[key]+=1.
