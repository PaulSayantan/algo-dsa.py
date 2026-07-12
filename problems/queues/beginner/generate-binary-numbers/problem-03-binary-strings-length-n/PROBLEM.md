# Generate All Binary Strings of Length N

**Difficulty:** Easy

**Source:** Classic — enumerate all fixed-length binary strings with a queue

## Description

Given an integer `n`, return every binary string of length exactly `n`, generated with a queue. Seed the queue with the empty string `""`; each step dequeues a string `s`. If `len(s) == n`, record `s`; otherwise enqueue `s + "0"` and `s + "1"`. Because the queue drains shorter prefixes before longer ones, the completed strings come out in ascending (lexicographic) order.

Constraints: `0 <= n <= 16`. For `n = 0` the only string is the empty string `""`.

## Examples

### Example 1

```
Input:  n = 2
Output: ["00", "01", "10", "11"]
```

**Explanation:** All four 2-bit strings, emitted in order once every prefix reaches length 2.

## Hint

Same queue-as-frontier trick as generating binary numbers, but seed with `""` and only emit a string once it reaches length `n`.
