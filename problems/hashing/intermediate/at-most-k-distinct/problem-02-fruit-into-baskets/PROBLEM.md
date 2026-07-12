# Fruit Into Baskets

**Difficulty:** Medium

**Source:** LeetCode 904 — Fruit Into Baskets

## Description

You walk a row of fruit trees `fruits` (integer types) with two baskets, each holding a single fruit type but unlimited count. Starting anywhere, you must pick from every tree until a basket cannot accept a fruit. Return the maximum number of fruits you can collect — i.e. the longest contiguous window with at most two distinct types.

## Examples

### Example 1

```
Input:  fruits = [1,2,1]
Output: 3
```

**Explanation:** We can pick all 3 fruits (types 1 and 2).

### Example 2

```
Input:  fruits = [1,2,3,2,2]
Output: 4
```

**Explanation:** The window [2,3,2,2] collects 4 fruits.

## Hint

Longest window with at most 2 distinct values — variable window + freq map.
