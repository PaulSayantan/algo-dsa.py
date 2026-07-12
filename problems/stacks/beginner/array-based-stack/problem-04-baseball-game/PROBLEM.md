# Baseball Game

**Difficulty:** Easy

**Source:** LeetCode 682 — Baseball Game

## Description

You are keeping a running record of scores. You are given a list of strings `ops`, where each operation is one of:

- An integer (as a string) `x` — record a new score of `x`.
- `"+"` — record a new score that is the sum of the previous two scores.
- `"D"` — record a new score that is double the previous score.
- `"C"` — invalidate and remove the previous score.

It is guaranteed each operation is valid when applied. Return the sum of all scores remaining in the record after applying every operation.

## Examples

### Example 1

```
Input:  ops = ["5", "2", "C", "D", "+"]
Output: 30
```

**Explanation:** Record 5, record 2, cancel the 2, double to 10, then 5+10=15; total 5+10+15=30.

### Example 2

```
Input:  ops = ["1", "C"]
Output: 0
```

**Explanation:** Record 1, then cancel it; nothing remains.

## Hint

Keep an array-based stack of live scores; `"C"` pops, `"D"` pushes 2*top, `"+"` pushes top+second-top.
