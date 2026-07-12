# Binary Numbers in a Range

**Difficulty:** Easy

**Source:** Classic — slice a range out of the queue-generated binary sequence

## Description

Given integers `low` and `high` (`1 <= low <= high`), return the binary representations of the integers `low, low+1, …, high` (inclusive) as a list of strings, generated with a queue. Use the standard generation — seed the queue with `"1"`, then repeatedly dequeue a string `s` and enqueue `s + "0"` and `s + "1"` — running it `high` times, but only collect the strings dequeued at positions `low` through `high` (1-indexed).

Constraints: `1 <= low <= high <= 10^5`.

## Examples

### Example 1

```
Input:  low = 3, high = 6
Output: ["11", "100", "101", "110"]
```

**Explanation:** The queue emits `"1", "10", "11", "100", "101", "110", …`; positions 3–6 are the binary forms of 3, 4, 5, and 6.

## Hint

Run the same queue BFS generation as generating binary numbers, but skip the first `low - 1` dequeues and keep the rest up to position `high`.
