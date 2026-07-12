# Baseball Game

**Difficulty:** Easy

**Source:** LeetCode 682 — Baseball Game

## Description

You are keeping the scores for a game with strange rules. You are given a list of strings `operations`, where each `operations[i]` is one of the following applied to a record of past scores:

- An integer `x` — record a new score of `x`.
- `"+"` — record a new score equal to the sum of the **previous two** scores.
- `"D"` — record a new score equal to **double** the previous score.
- `"C"` — invalidate the previous score, removing it from the record.

Each operation is valid (there are always enough previous scores when `"+"`, `"D"`, or `"C"` is applied). Return the **sum of all the scores** in the record after applying every operation.

## Examples

### Example 1

```
Input:  operations = ["5","2","C","D","+"]
Output: 30
```

**Explanation:** Record `5`, then `2`; `C` removes `2` leaving `[5]`; `D` doubles `5` to `10` giving `[5,10]`; `+` sums the last two (`5+10=15`) giving `[5,10,15]`. Sum = `30`.

### Example 2

```
Input:  operations = ["1","C"]
Output: 0
```

**Explanation:** Record `1`, then `C` removes it. The record is empty, so the sum is `0`.

## Hint

Treat the record as a stack: push integers, and for `+`/`D`/`C` combine or pop the top scores just like evaluating a postfix stream. Return `sum(stack)`.
