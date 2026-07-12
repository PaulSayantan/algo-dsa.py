# Number of Good Pairs

**Difficulty:** Easy

**Source:** LeetCode 1512 — Number of Good Pairs

## Description

Given an integer array `nums`, a pair `(i, j)` is good if `nums[i] == nums[j]` and `i < j`. Return the number of good pairs. Each value with frequency `f` contributes `f*(f-1)/2` pairs.

## Examples

### Example 1

```
Input:  nums = [1,2,3,1,1,3]
Output: 4
```

**Explanation:** Good pairs: three among the 1's and one among the 3's.

### Example 2

```
Input:  nums = [1,1,1,1]
Output: 6
```

**Explanation:** All C(4,2) = 6 pairs are good.

## Hint

Counter the values; sum f*(f-1)//2 over all frequencies.
