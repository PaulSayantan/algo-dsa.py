# Students Unable to Eat Lunch

**Difficulty:** Easy

**Source:** LeetCode 1700 — Number of Students Unable to Eat Lunch

## Description

Students stand in a queue and a stack of square/circular sandwiches sits on a counter. `students[i]` is the preference (`0` or `1`) of the student at position `i`, with `students[0]` at the front of the line. `sandwiches[i]` is the type of the `i`-th sandwich in the stack, with `sandwiches[0]` on **top**.

Repeatedly: the student at the front of the line takes the top sandwich if it matches their preference and both leave; otherwise the student goes to the **back** of the line and the sandwich stays. The process stops once no remaining student wants the sandwich currently on top. Return the number of students that are unable to eat.

## Examples

### Example 1

```
Input:  students = [1, 1, 0, 0], sandwiches = [0, 1, 0, 1]
Output: 0
```

**Explanation:** The line keeps rotating until every sandwich is taken, so all students eat.

### Example 2

```
Input:  students = [1, 1, 1, 0, 0, 1], sandwiches = [1, 0, 0, 0, 1, 1]
Output: 3
```

**Explanation:** After the first three sandwiches are taken the top is `0`, but the three students left in line all prefer `1`, so they can never eat.

## Hint

Keep the students in a `deque`; if the front matches the top sandwich pop both, else rotate the student to the back. Stop once a full lap passes with nobody able to take the top.
