# Maximum Compatibility Score Sum

**Difficulty:** Medium

**Source:** LeetCode 1947 — "Maximum Compatibility Score Sum".

## Description

There is a survey with `n` yes/no questions. Each question's answer is either `0`
or `1`.

The survey was given to `m` students and `m` mentors. The answers of the `i`-th
student are `students[i]`, and the answers of the `j`-th mentor are `mentors[j]`,
each an array of `n` values in `{0, 1}`.

Each student is assigned to **one** mentor, and each mentor to **one** student
(a one-to-one pairing). The **compatibility score** of a student–mentor pair is
the number of questions for which they gave the **same** answer.

Return the **maximum total compatibility score** over all ways to pair students
with mentors.

## Constraints

- `m == students.length == mentors.length`
- `n == students[i].length == mentors[j].length`
- `1 <= m, n <= 8`
- `students[i][k]` and `mentors[j][k]` are `0` or `1`.

## Examples

### Example 1

```
Input:  students = [[1,1,0],[1,0,1],[0,0,1]]
        mentors  = [[1,0,0],[0,0,1],[1,1,0]]
Output: 8
Explanation: Pair student 0 with mentor 2 (score 3), student 1 with mentor 0
(score 2), student 2 with mentor 1 (score 3). Total = 3 + 2 + 3 = 8, which is
the maximum achievable.
```

### Example 2

```
Input:  students = [[0,0],[0,0],[0,0]]
        mentors  = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: Every student disagrees with every mentor on both questions, so
every pair scores 0. Any pairing sums to 0.
```

### Example 3

```
Input:  students = [[1,1],[1,0]]
        mentors  = [[0,0],[1,1]]
Output: 3
Explanation: Scores — student 0 vs mentor 1 = 2 (both answers match), student 1
vs mentor 0 = 1 (first answer matches). Pairing 0->1 and 1->0 gives 2 + 1 = 3.
The alternative (0->0, 1->1) gives 0 + 1 = 1, so 3 is optimal.
```

## Hint

First build an `m x m` **score matrix** where entry `(i, j)` is the compatibility
of student `i` with mentor `j`. You want the **maximum-weight** perfect matching.
Negate the scores (or subtract each from `n`) and run the **Hungarian Algorithm**
to minimize the negated cost, which maximizes the score.
