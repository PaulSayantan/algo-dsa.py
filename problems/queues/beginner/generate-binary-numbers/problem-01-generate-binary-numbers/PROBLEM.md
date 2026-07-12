# Generate Binary Numbers from 1 to N

**Difficulty:** Easy

**Source:** Classic — generate binary numbers with a queue

## Description

Given an integer `n`, return the binary representations of the numbers `1, 2, …, n` as a list of strings, generated with a queue. Start the queue with `"1"`; each step dequeues a string (appending it to the output) and enqueues that string followed by `"0"` and by `"1"`.

## Examples

### Example 1

```
Input:  n = 5
Output: ["1", "10", "11", "100", "101"]
```

## Hint

Queue seeded with "1": pop s, record it, push s+"0" and s+"1". Repeat n times.
