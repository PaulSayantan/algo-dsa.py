# Minimum Window Covering a Multiset Target

**Difficulty:** Medium

**Source:** Classic — minimum window covering a target multiset

## Description

Given an integer array `nums` and a target list `target` (interpreted as a multiset with multiplicities), return the length of the shortest contiguous window of `nums` that contains every element of `target` with at least its required multiplicity. Return `0` if no such window exists (or if `target` is empty).

## Examples

### Example 1

```
Input:  nums = [1,2,2,3], target = [2,2]
Output: 2
```

**Explanation:** The window [2,2] covers two 2's in length 2.

### Example 2

```
Input:  nums = [7,3,7,3,7], target = [3,3]
Output: 3
```

**Explanation:** The 3's are at indices 1 and 3; the covering window [3,7,3] has length 3.

## Hint

This is Minimum Window Substring on integers; use need = Counter(target) + a 'missing' counter, return the length.
