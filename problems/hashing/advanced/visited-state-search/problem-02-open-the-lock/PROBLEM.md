# Open the Lock

**Difficulty:** Medium

**Source:** LeetCode 752 — Open the Lock

## Description

A lock has 4 wheels, each 0-9, starting at `"0000"`. One move turns a single wheel one slot (wrapping 9<->0). Given a list of `deadends` the lock must never display and a `target`, return the minimum number of moves to reach `target`, or -1 if impossible. BFS over the 4-digit strings with a visited set, treating deadends as blocked.

## Examples

### Example 1

```
Input:  deadends=["0201","0101","0102","1212","2002"], target="0202"
Output: 6
```

### Example 2

```
Input:  deadends=["0000"], target="8888"
Output: -1
```

**Explanation:** The start itself is a deadend.

## Hint

BFS from '0000'; each state has 8 neighbors (each wheel +/-1 mod 10); skip deadends and visited.
