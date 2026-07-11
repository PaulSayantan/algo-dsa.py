# Fruit Into Baskets

**Difficulty:** Medium

**Source:** LeetCode 904 — Fruit Into Baskets

## Description

You are visiting a farm with a single row of fruit trees, represented by an
integer array `fruits`, where `fruits[i]` is the **type** of fruit the `i`-th tree
produces.

You have **two baskets**, and each basket can hold **only one type** of fruit
(any amount). You must follow these rules:

- You pick exactly one fruit from every tree, moving **right** and never skipping
  a tree, starting from any tree you like.
- Once you start, you keep picking until you reach a tree whose fruit cannot fit
  in either basket (i.e. it would require a **third** type), at which point you
  stop.

Return the **maximum number of fruits** you can pick. In other words, find the
length of the **longest contiguous subarray** containing **at most 2 distinct
values**.

## Constraints

- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

## Examples

### Example 1

```
Input:  fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees; only types {1, 2} appear, which fit in
             the two baskets.
```

### Example 2

```
Input:  fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2] (types {1,2}), length 3. Starting at
             tree 0 would give types {0,1,2} — three types — so we could not
             include all of [0,1,2,2].
```

### Example 3

```
Input:  fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2] (types {2,3}), length 4.
```

## Hint

Use a **Sliding Window (variable size)** with a count map of fruit types. Grow the
window while it contains at most 2 distinct types; when a 3rd type appears, shrink
from the left until one type is fully evicted.
