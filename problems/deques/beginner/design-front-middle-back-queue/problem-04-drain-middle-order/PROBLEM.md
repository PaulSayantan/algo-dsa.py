# Drain a Queue From the Middle

**Difficulty:** Easy

**Source:** Classic — repeated popMiddle emptying order

## Description

Given a list `nums` treated as the contents of a front-middle-back queue (index `0` is the front), repeatedly apply `popMiddle` until the queue is empty and return the list of removed values **in the order they were removed**. Each `popMiddle` removes the element at index `(len - 1) // 2` of the *current* contents — the frontmost of the two middles when the size is even.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3, 4, 5]
Output: [3, 2, 4, 1, 5]
```

**Explanation:** Remove index `2` (`3`) -> `[1,2,4,5]`; index `1` (`2`) -> `[1,4,5]`; index `1` (`4`) -> `[1,5]`; index `0` (`1`) -> `[5]`; index `0` (`5`).

## Hint

Each step pops index `(len - 1) // 2` of what remains — the front-middle rule applied over and over.
