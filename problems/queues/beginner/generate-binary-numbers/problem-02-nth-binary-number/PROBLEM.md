# N-th Generated Binary Number

**Difficulty:** Easy

**Source:** Classic — n-th binary number

## Description

Using the same queue-based generation, return the `n`-th binary string (1-indexed) — equivalently, the binary representation of the integer `n` itself. Run the generation `n` times and return the last string dequeued.

## Examples

### Example 1

```
Input:  n = 10
Output: "1010"
```

## Hint

The n-th string emitted equals n in binary; run the queue BFS n times and keep the last pop.
