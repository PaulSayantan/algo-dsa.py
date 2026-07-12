# Reverse the First K Elements of a Queue

**Difficulty:** Easy

**Source:** Classic — reverse first K of a queue

## Description

Given a queue represented as a list `q` (front is index `0`) and an integer `k`,
reverse the order of the first `k` elements while leaving the remaining elements
in their original order. Return the resulting list. Use a stack: dequeue the
first `k` elements onto a stack, then pop them back to the front in reversed
order and append the untouched tail.

Constraints: `0 <= k <= len(q)`.

## Examples

### Example 1

```
Input:  q = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

**Explanation:** Push `1,2,3`; popping gives `3,2,1`, then keep `4,5` as-is.

### Example 2

```
Input:  q = [1, 2, 3, 4, 5], k = 5
Output: [5, 4, 3, 2, 1]
```

**Explanation:** Reversing all five elements reverses the whole queue.

## Hint

Push the first `k` elements onto a stack; popping them yields those `k` in reversed order, then tack on the rest unchanged.
