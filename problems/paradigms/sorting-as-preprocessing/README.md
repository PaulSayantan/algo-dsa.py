# Sorting as Preprocessing

**Category:** paradigms / paradigm

## What it is

"Sorting as Preprocessing" is a problem-solving paradigm: before attacking a problem,
you **sort the input**, which reorders the data into a monotone structure. That monotone
structure then unlocks a fast follow-up technique that would be impossible (or much
slower) on unsorted data:

- **Two pointers** — once values are ordered, a left/right pointer pair can converge in
  linear time (e.g. find a pair summing to a target, or greedily pair the lightest with
  the heaviest element).
- **Greedy** — sorting by the right key (start time, end time, deadline, size) makes the
  locally optimal choice provably globally optimal (interval scheduling, activity
  selection, matching).
- **Binary search** — a sorted array lets you locate or count elements in `O(log n)`,
  and enables patience-sorting style `O(n log n)` LIS.

## When to reach for it

Reach for sorting-as-preprocessing when any of these are true:

- The problem talks about **pairs / triples that satisfy a numeric relation** (sums,
  differences, capacities). Sorting + two pointers usually beats hashing on space and
  handles duplicates cleanly.
- The problem involves **intervals, meetings, or ranges**, and you must merge, count,
  or remove overlaps. Sorting by start or end almost always exposes a one-pass greedy.
- You need the **k-th smallest / largest**, a **median**, or **ordered output**.
- You suspect a greedy works but can't justify it on the raw order — sorting often
  supplies the exchange-argument ordering that makes greedy correct.
- Absolute positions/indices do **not** matter (or you can carry original indices
  alongside the values before sorting).

**When NOT to use it:** if the original order carries meaning you can't recover
(and you can't stash indices), or if an `O(n)` hash/counting solution already exists and
the extra `O(n log n)` sort is pure overhead.

## Typical complexity

- **Time:** dominated by the sort, `O(n log n)`. The follow-up pass (two pointers,
  greedy sweep) is usually `O(n)`; a binary-search follow-up is `O(n log n)` overall.
- **Space:** `O(1)` to `O(n)` depending on whether the sort is in place and whether you
  build output/index arrays.

The recurring win: you trade a naive `O(n^2)` (all pairs) or `O(n^3)` (all triples)
brute force for an `O(n log n)` sort plus a linear scan.

## Problems

| # | Problem | Technique unlocked | Difficulty |
|---|---------|--------------------|------------|
| 1 | [Assign Cookies](problem-01-assign-cookies/PROBLEM.md) | Greedy two-pointer over two sorted arrays | Easy |
| 2 | [Merge Intervals](problem-02-merge-intervals/PROBLEM.md) | Greedy one-pass merge after sorting by start | Medium |
| 3 | [3Sum](problem-03-3sum/PROBLEM.md) | Two pointers per fixed element, with dedup | Medium |
| 4 | [Boats to Save People](problem-04-boats-to-save-people/PROBLEM.md) | Greedy lightest-with-heaviest two-pointer | Medium |
| 5 | [Non-overlapping Intervals](problem-05-non-overlapping-intervals/PROBLEM.md) | Activity-selection greedy after sorting by end | Medium |
| 6 | [Russian Doll Envelopes](problem-06-russian-doll-envelopes/PROBLEM.md) | Sort + binary-search LIS | Hard |
