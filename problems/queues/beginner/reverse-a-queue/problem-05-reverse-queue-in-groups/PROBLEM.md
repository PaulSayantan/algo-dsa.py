# Reverse a Queue in Groups of K

**Difficulty:** Easy

**Source:** Classic — reverse a queue in groups of size k

## Description

Given a queue as a list (front = index 0) and an integer `k` (`k` ≥ 1), reverse the elements of every consecutive group of `k` elements, and return the resulting list. If the final group has fewer than `k` elements, reverse it as well.

## Examples

### Example 1

```
Input:  q = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
Output: [3, 2, 1, 6, 5, 4, 8, 7]
```

**Explanation:** Groups `[1,2,3]`, `[4,5,6]`, `[7,8]` become `[3,2,1]`, `[6,5,4]`, `[8,7]`.

## Hint

Walk the queue in chunks of k; for each chunk push onto a stack and pop it back to reverse just that block.
