# Task Scheduler

**Difficulty:** Medium

**Source:** LeetCode 621 (Task Scheduler)

## Description

You are given an array of CPU `tasks`, each represented by an uppercase English
letter, and a non-negative integer `n`. Each task takes **one unit of time** to run.
For each unit of time, the CPU can either run **one** task or stay **idle**.

The only constraint is a **cooldown**: two identical tasks must be separated by at
least `n` units of time. In other words, after running a task, at least `n` other
units (running different tasks or idling) must pass before that same task can run
again.

Return the **minimum number of time units** the CPU needs to finish all the given
tasks.

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter (`A`–`Z`).
- `0 <= n <= 100`

## Examples

### Example 1

```
Input:  tasks = ["A", "A", "A", "B", "B", "B"], n = 2
Output: 8
```

Explanation: One optimal schedule is `A → B → idle → A → B → idle → A → B`. Each `A`
is at least 2 units apart, likewise each `B`. That uses 8 time units, which is the
minimum, so the answer is **8**.

### Example 2

```
Input:  tasks = ["A", "C", "A", "B", "D", "B"], n = 1
Output: 6
```

Explanation: A valid schedule is `A → B → C → D → A → B` with no idling — every pair
of identical tasks is at least 1 apart. All 6 tasks run back to back, so the answer
is **6**.

### Example 3

```
Input:  tasks = ["A", "A", "A", "B", "B", "B"], n = 0
Output: 6
```

Explanation: With no cooldown (`n = 0`), the CPU never idles and simply runs all 6
tasks in a row, so the answer is **6**.

## Hint

Use a **Greedy** idea: schedule the **most frequent** task first and space its copies
`n + 1` apart, then slot the remaining tasks into the gaps. The most frequent task
determines the skeleton of the schedule; a closed-form based on its count usually
gives the answer directly.
