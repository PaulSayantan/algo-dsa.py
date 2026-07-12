# First N Numbers Using Only Digits 1 and 2

**Difficulty:** Easy

**Source:** Classic — generate numbers over a two-symbol alphabet with a queue

## Description

Given an integer `n`, return the first `n` positive integers whose decimal digits are drawn only from `{1, 2}`, in increasing numeric order, as a list of integers. This is the "generate binary numbers" queue trick with the alphabet `{"1", "2"}` instead of `{"0", "1"}`: seed the queue with `"1"` and `"2"`, then repeatedly dequeue a string `s`, record `int(s)`, and enqueue `s + "1"` and `s + "2"`.

Constraints: `1 <= n <= 1000`.

## Examples

### Example 1

```
Input:  n = 7
Output: [1, 2, 11, 12, 21, 22, 111]
```

**Explanation:** Level-order over the alphabet `{1, 2}` yields the single-digit values first, then the two-digit ones, and so on.

## Hint

Same queue-as-frontier idea as generating binary numbers, but seed with both `"1"` and `"2"` and append `"1"`/`"2"` (not `"0"`/`"1"`) to each dequeued prefix.
