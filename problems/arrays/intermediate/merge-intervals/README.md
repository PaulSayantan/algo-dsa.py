# Merge Intervals

**Merge Intervals** is a pattern for problems that manipulate a collection of
intervals `[start, end]`. The core idea is almost always the same:

1. **Sort** the intervals by their `start` value (occasionally by `end`).
2. **Sweep** through them left to right, keeping a "current" running interval.
3. When the next interval **overlaps** the current one (`next.start <= current.end`),
   extend the current interval's end to `max(current.end, next.end)`. Otherwise,
   close off the current interval and start a fresh one.

Once the intervals are sorted, a single linear pass is enough because any
interval that could overlap a given one must appear adjacent to it in sorted
order. That is the key invariant that makes the technique work.

## When to reach for it

- You are given a list of ranges/intervals and asked to **combine**, **insert**,
  **count**, or **find gaps** between them.
- The words *overlap*, *merge*, *covered*, *free time*, *booking*, or *union of
  ranges* appear in the statement.
- You need the **total covered length**, the **number of disjoint groups**, or the
  **complement** (free slots) of a set of intervals.

## Typical complexity

| Step        | Cost                          |
|-------------|-------------------------------|
| Sorting     | `O(n log n)`                  |
| Linear sweep| `O(n)`                        |
| **Total**   | **`O(n log n)`** time         |
| Space       | `O(n)` for the output (or `O(log n)` / `O(n)` for the sort itself) |

When the intervals are **already sorted** (e.g. Insert Interval), the sort is
skipped and the sweep alone runs in `O(n)`.

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Teemo Attacking](problem-01-teemo-attacking/PROBLEM.md) | Easy | Merge overlapping poison windows to get total poisoned duration. |
| 2 | [Merge Intervals](problem-02-merge-intervals/PROBLEM.md) | Medium | Combine all overlapping intervals into disjoint ones (the canonical problem). |
| 3 | [Insert Interval](problem-03-insert-interval/PROBLEM.md) | Medium | Insert a new interval into a sorted list and merge any overlaps. |
| 4 | [Remove Covered Intervals](problem-04-remove-covered-intervals/PROBLEM.md) | Medium | Count intervals left after removing those fully covered by another. |
| 5 | [Employee Free Time](problem-05-employee-free-time/PROBLEM.md) | Hard | Merge everyone's busy intervals, then return the gaps common to all. |
