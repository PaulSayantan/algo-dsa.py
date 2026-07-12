# Baseball Game (Deque as a Stack)

**Difficulty:** Easy

**Source:** LeetCode 682 — Baseball Game

## Description

You are given a list of string `operations` recording a baseball game's scores. Process each operation onto a running record and return the sum of all scores that remain. Each `op` is one of:

- an integer string `"x"` — record a new score `x`;
- `"+"` — record a new score equal to the sum of the previous **two** scores;
- `"D"` — record a new score equal to **double** the previous score;
- `"C"` — invalidate (remove) the previous score.

Every operation refers only to scores that currently exist. Use a deque as a **stack** (push/pop the right end): `"+"` and `"D"` peek the recent scores, `"C"` pops, and integers push. Return the total of the record after all operations.

## Examples

### Example 1

```
Input:  operations = ["5", "2", "C", "D", "+"]
Output: 30
```

**Explanation:** push 5, push 2, "C" removes 2 (record [5]), "D" pushes 10 (record [5, 10]), "+" pushes 15 (record [5, 10, 15]); sum = 30.

## Hint

Treat the record as a stack on a deque: `append` for new scores, `pop` for `"C"`, and index the right end (`dq[-1]`, `dq[-2]`) for `"D"` and `"+"`.
