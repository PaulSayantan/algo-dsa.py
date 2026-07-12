# Two Sum III — Data Structure Design

**Difficulty:** Easy

**Source:** LeetCode 170 — Two Sum III - Data structure design

## Description

Design a data structure with `add(number)` to store a number and `find(value)` returning whether any pair of stored numbers sums to `value`.

## Examples

### Example 1

```
Input:  add 1,3,5; find(4)
Output: true
```

## Hint

Keep a frequency map; for each x check value-x, requiring count>=2 when x doubles value.
