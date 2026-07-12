# Design Front Middle Back Queue

**Difficulty:** Medium

**Source:** LeetCode 1670 — Design Front Middle Back Queue

## Description

Design a queue supporting `pushFront(v)`, `pushMiddle(v)`, `pushBack(v)`, `popFront()`, `popMiddle()`, and `popBack()`. Each `pop*` returns the removed value, or `-1` if the queue is empty. When there are two middle positions, both push and pop act on the **frontmost** of the two.

## Examples

### Example 1

```
Input:  pushFront(1); pushBack(2); pushMiddle(3); pushMiddle(4); popFront(); popMiddle(); popMiddle(); popBack(); popFront()
Output: [1, 3, 4, 2, -1]
```

**Explanation:** States: [1] -> [1,2] -> [1,3,2] -> [1,4,3,2]; then pops 1, 3, 4, 2, then -1.

## Hint

pushMiddle inserts at index len//2; popMiddle removes index (len-1)//2 — the front of the two middles.
