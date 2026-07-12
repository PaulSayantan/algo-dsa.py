# Max Value in a Queue

**Difficulty:** Medium

**Source:** Classic — LCOF 59-II / max-queue via two stacks

## Description

Design a FIFO queue that supports `push_back(x)` (enqueue), `pop_front()` (dequeue & return the removed value), and `max_value()` (the maximum of all currently-queued elements). Every operation must be amortized O(1). If the queue is empty, `pop_front()` and `max_value()` both return `-1`. Values are integers.

## Examples

### Example 1

```
Input:  push_back 1; push_back 3; max_value; pop_front; max_value
Output: 3, 1, 3
```

**Explanation:** After enqueuing `1` then `3` the max is `3`; dequeuing removes the front `1`, and `3` still remains as the max.

## Hint

Keep an 'in' stack and an 'out' stack where every frame also stores the running max of the elements at or below it; the queue max is the larger of the two stack tops.
