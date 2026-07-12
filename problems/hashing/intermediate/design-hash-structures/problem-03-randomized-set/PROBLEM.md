# Insert Delete GetRandom O(1)

**Difficulty:** Medium

**Source:** LeetCode 380 — Insert Delete GetRandom O(1)

## Description

Design a set supporting average O(1) `insert(val)` (returns whether newly added), `remove(val)` (returns whether present), and a uniform `getRandom()`. (Here we exercise only the deterministic `insert`, `remove`, and `size` behavior.)

## Examples

### Example 1

```
Input:  insert(1) then insert(1)
Output: true, then false
```

## Hint

value->index map + array; to remove, swap the target with the last element then pop.
