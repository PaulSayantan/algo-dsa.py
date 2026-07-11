# Meeting Rooms / Interval Scheduling

**Interval scheduling** is a family of problems where you are given a collection of
intervals `[start, end]` and must reason about how they overlap. Almost every problem
in this family is solved by the same two-step recipe:

1. **Sort** the intervals — by *start* time when you want to sweep left-to-right and
   detect/merge overlaps, or by *end* time when you are greedily picking the maximum
   number of compatible (non-overlapping) intervals.
2. **Sweep** through the sorted list keeping a small amount of state (the current
   merged interval, the last chosen end, a running count, or a min-heap of active
   end times) and update it in one linear pass.

## When to reach for it

Reach for interval scheduling whenever the input is a list of ranges and the question
asks you to:

- decide whether any two ranges collide (can a person attend all meetings?),
- **merge** overlapping ranges into consolidated blocks,
- keep the **maximum number of non-overlapping** ranges / remove the fewest ranges
  (the classic *activity selection* greedy),
- find the **maximum number of ranges overlapping at once** (minimum resources /
  meeting rooms needed), or
- attend/cover as many ranges as possible under a per-unit constraint.

## Typical complexity

- **Time:** `O(n log n)`, dominated by the sort. The sweep itself is `O(n)`, and any
  heap operations add another `O(n log n)` at worst.
- **Space:** `O(n)` for the sort / output, or `O(n)` for a heap; `O(1)` extra beyond
  the sort for the simplest counting variants.

## Two greedy templates to memorize

| Goal | Sort key | Sweep state |
|---|---|---|
| Merge / detect overlap | **start** | last merged interval's end |
| Max non-overlapping / min removals / min arrows | **end** | last kept interval's end |
| Min simultaneous resources | **start** (+ min-heap of ends) | heap of active end times |

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Meeting Rooms](problem-01-meeting-rooms/PROBLEM.md) | Easy | Sort by start; check if any adjacent meetings overlap. |
| 2 | [Merge Intervals](problem-02-merge-intervals/PROBLEM.md) | Medium | Sort by start; fold overlapping intervals into one. |
| 3 | [Non-overlapping Intervals](problem-03-non-overlapping-intervals/PROBLEM.md) | Medium | Sort by end; greedily keep intervals, count removals. |
| 4 | [Minimum Arrows to Burst Balloons](problem-04-minimum-arrows-burst-balloons/PROBLEM.md) | Medium | Sort by end; shoot one arrow per group of overlapping balloons. |
| 5 | [Meeting Rooms II](problem-05-meeting-rooms-ii/PROBLEM.md) | Medium | Sort by start; use a min-heap of end times to count peak overlap. |
| 6 | [Maximum Number of Events That Can Be Attended](problem-06-maximum-events-attended/PROBLEM.md) | Hard | Sweep by day; greedily attend the event that ends soonest via a heap. |
