# Open the Lock

**Difficulty:** Medium

**Source:** LeetCode 752 — Open the Lock

## Description

A lock has 4 circular wheels, each showing a single digit `0`-`9`; the wheels wrap around (`9 -> 0` and `0 -> 9`). The lock starts at `"0000"`. One move rotates a single wheel one step up or down. `deadends` is a list of states the lock must never display (reaching one jams it). Given the list `deadends` and a string `target`, return the minimum number of moves to reach `target` from `"0000"`, or `-1` if it is impossible.

Constraints: each string is 4 digits; `1 <= len(deadends) <= 500`; `target` and `"0000"` may themselves be deadends.

## Examples

### Example 1

```
Input:  deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
```

**Explanation:** A shortest sequence is `0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202`, avoiding every deadend.

### Example 2

```
Input:  deadends = ["8888"], target = "0009"
Output: 1
```

**Explanation:** Turn the last wheel down once: `0000 -> 0009`.

## Hint

Treat each 4-digit combination as a graph node with 8 neighbors (each wheel +/-1); BFS from `"0000"` skipping deadends, and the layer that first reaches `target` is the minimum move count.
