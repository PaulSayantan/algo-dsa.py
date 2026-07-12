# Baseball Game

**Difficulty:** Easy

**Source:** LeetCode 682 — Baseball Game

## Description

You are keeping score for a game with a list of string operations `ops`. Maintain a record of scores; for each operation apply it to the record from most recent to oldest:

- An integer `x` (as a string): record a new score of `x`.
- `"+"`: record a new score equal to the **sum of the previous two** scores.
- `"D"`: record a new score equal to **double** the previous score.
- `"C"`: **remove** (invalidate) the previous score.

It is guaranteed that every operation is valid when applied. Return the **sum** of all scores remaining in the record after applying every operation.

Constraints: `1 <= len(ops) <= 1000`; each entry is `"+"`, `"D"`, `"C"`, or a string integer that fits in a normal `int`.

## Examples

### Example 1

```
Input:  ops = ["5","2","C","D","+"]
Output: 30
```

**Explanation:** Record 5, then 2, then C removes 2 (record: [5]), D doubles 5 -> 10 (record: [5, 10]), `+` adds 5 + 10 -> 15 (record: [5, 10, 15]). Sum = 30.

## Hint

The record is a LIFO stack: `"C"` pops the head, `"D"` / `"+"` peek the top one or two entries and push a new head.
