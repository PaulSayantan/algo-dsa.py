# Greedy

**Category:** paradigms / paradigm

**One-line:** Make the locally optimal choice at each step when it yields a global optimum.

## What is it?

A **greedy algorithm** builds up a solution piece by piece, always choosing the
option that looks best *right now* — the locally optimal choice — never
reconsidering past decisions. It commits and moves on.

This is dramatically simpler than exploring all possibilities (brute force) or
caching overlapping subproblems (dynamic programming). But it only produces a
*correct* global optimum for problems with special structure. Greedy is a
scalpel, not a hammer: when it applies, it is beautifully fast; when it doesn't,
it silently returns a wrong answer.

## When to reach for it

Look for these signals:

- **Optimization** — "maximize", "minimize", "least number of", "largest possible".
- **Greedy-choice property** — a globally optimal solution can be reached by making
  a locally optimal choice at each step (you never need to undo a choice).
- **Optimal substructure** — after making the greedy choice, what remains is a
  smaller instance of the same problem.
- **A natural ordering** — sorting by start/end time, by ratio, by frequency, or a
  running scan often exposes the right greedy order.

The two classic proof techniques are the **exchange argument** (show any optimal
solution can be transformed into the greedy one without getting worse) and the
**"greedy stays ahead"** argument (show greedy is never behind an optimal solution
at any step).

> Caution: many optimization problems *look* greedy but are not (e.g. 0/1 knapsack).
> Always convince yourself the greedy-choice property holds — a counterexample kills it.

## Typical complexity

- **Time:** usually `O(n log n)` when a sort drives the choices, or `O(n)` for a
  single linear scan. Often the sort dominates.
- **Space:** typically `O(1)` extra (a few running variables) up to `O(n)` if you
  need auxiliary counts/heaps.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Assign Cookies](problem-01-assign-cookies/PROBLEM.md) | Sort both sides, match smallest cookie to least greedy child | Easy |
| 2 | [Jump Game](problem-02-jump-game/PROBLEM.md) | Track the farthest reachable index in one scan | Medium |
| 3 | [Gas Station](problem-03-gas-station/PROBLEM.md) | Reset start when running tank goes negative | Medium |
| 4 | [Non-overlapping Intervals](problem-04-non-overlapping-intervals/PROBLEM.md) | Interval scheduling: sort by end, keep earliest finisher | Medium |
| 5 | [Task Scheduler](problem-05-task-scheduler/PROBLEM.md) | Schedule the most frequent task first; fill idle slots | Medium |
