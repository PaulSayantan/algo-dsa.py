# Open the Lock

**Difficulty:** Medium

**Source:** LeetCode 752 — Open the Lock

## Description

A lock has 4 circular wheels, each showing a digit `0`-`9`; wheels wrap around (`0` and `9` are adjacent). The lock starts at `"0000"`. One move rotates a single wheel one slot up or down. Given a list of `deadends` (states the lock must never display) and a `target`, return the minimum number of moves to reach `target` from `"0000"`, or `-1` if it is impossible.

## Examples

### Example 1

```
Input:  deadends = ["0201", "0101", "0102", "1212", "2002"], target = "0202"
Output: 6
```

**Explanation:** A shortest path is `0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202`.

### Example 2

```
Input:  deadends = ["8888"], target = "0009"
Output: 1
```

**Explanation:** Turn the last wheel down once: `0000 -> 0009`.

## Hint

BFS simultaneously from `"0000"` and `target`, expanding the smaller frontier of live (non-deadend) states; the answer is the round where the frontiers touch.
