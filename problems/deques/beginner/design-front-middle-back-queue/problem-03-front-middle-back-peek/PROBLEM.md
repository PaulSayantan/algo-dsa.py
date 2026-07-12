# Front Middle Back Queue — Peek Operations

**Difficulty:** Easy

**Source:** Classic — Front/Middle/Back queue with non-destructive peeks

## Description

Design a queue supporting the three inserts `pushFront(v)`, `pushMiddle(v)`, `pushBack(v)` plus three **non-destructive** reads: `peekFront()`, `peekMiddle()`, and `peekBack()`. Each `peek*` returns the value at that position **without removing it**, or `-1` if the queue is empty. When there are two middle positions, the middle is the **frontmost** of the two — `peekMiddle` reads index `(len - 1) // 2`.

## Examples

### Example 1

```
Input:  pushBack(1); pushBack(2); pushBack(3); pushBack(4); peekFront(); peekMiddle(); peekBack()
Output: [1, 2, 4]
```

**Explanation:** State is `[1,2,3,4]`; front is `1`, middle is index `(4-1)//2 = 1` (value `2`), back is `4`. Nothing is removed.

## Hint

peekMiddle reads (never pops) index `(len - 1) // 2` — the front of the two middles when the size is even.
