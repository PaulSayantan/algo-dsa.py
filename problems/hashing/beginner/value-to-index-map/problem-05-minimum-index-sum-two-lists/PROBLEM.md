# Minimum Index Sum of Two Lists

**Difficulty:** Easy

**Source:** LeetCode 599 — Minimum Index Sum of Two Lists

## Description

Given two arrays of unique strings `list1` and `list2`, return all the common strings with the **least index sum** (the sum of a string's index in each list). If there is a tie, return every such string. The answer here is returned sorted alphabetically for determinism.

## Examples

### Example 1

```
Input:  list1 = ["Shogun",...], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
```

**Explanation:** Shogun has index sum 0 + 1 = 1, the minimum.

## Hint

Map each name in list1 to its index; scan list2, tracking the minimum idx1 + idx2 and its winners.
