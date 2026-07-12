# Baseball Game

**Difficulty:** Easy

**Source:** LeetCode 682 — Baseball Game

## Description

You are keeping the scores for a baseball game with strange rules. You are given a
list of strings `operations`, where `operations[i]` is the `i`-th operation you
must apply to the record, and return the sum of all scores on the record after
applying every operation.

Each operation is one of the following:

- An integer `x` — record a new score of `x`.
- `"+"` — record a new score that is the **sum of the previous two** scores.
- `"D"` — record a new score that is **double the previous** score.
- `"C"` — invalidate (undo) the **previous** score, removing it from the record.

It is guaranteed that every operation is valid when applied (there is always at
least one previous score for `"+"`, `"D"`, and `"C"`, and two previous scores for
`"+"`).

## Examples

### Example 1

```
Input:  operations = ["5", "2", "C", "D", "+"]
Output: 30
```

**Explanation:** Record `5`, then `2` (record `[5, 2]`). `"C"` undoes the `2`
(record `[5]`). `"D"` doubles to `10` (record `[5, 10]`). `"+"` sums the last two
to `15` (record `[5, 10, 15]`). Total `= 5 + 10 + 15 = 30`.

## Hint

Keep the record on a stack. `"C"` is an undo: just pop the last score off.
`"D"`/`"+"` push a new score derived from the current top of the stack.
