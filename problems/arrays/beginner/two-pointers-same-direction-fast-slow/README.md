# Two Pointers (Same Direction / Fast-Slow)

## What it is

The **same-direction two-pointer** technique walks two indices through a sequence
that both move from left to right (they never cross, and neither ever moves
backward). The classic form uses a **reader** (also called *fast*) pointer that
scans every element, and a **writer** (also called *slow*) pointer that marks the
boundary of the "result" region built up so far. Whenever the reader finds an
element that belongs in the output, we copy it to the writer's position and
advance the writer. Because the writer never gets ahead of the reader, we can
overwrite the input array safely and produce the answer **in place** with O(1)
extra memory.

A related member of the family is the **fast-slow** (Floyd's tortoise & hare)
variant, where one pointer advances twice as fast as the other. On an array that
encodes a functional graph (each value points to an index), the two speeds are
guaranteed to meet inside a cycle, which lets us detect duplicates or loops
without extra space.

## When to reach for it

- You must transform an array/list **in place** (interview constraint: O(1) extra
  space, or "modify the input").
- The task is **filtering** (drop elements matching a predicate), **dedup**
  (collapse runs of equal values), or **partitioning** (push a class of elements
  to one side while preserving order).
- The data is **sorted**, so equal elements are adjacent and a single backward
  glance (`nums[writer-1]`) is enough to decide keep/skip.
- You need **cycle detection** on a sequence that behaves like `i -> nums[i]`
  (fast-slow variant).

## Typical complexity

- **Time:** O(n) — each pointer sweeps the array at most once.
- **Space:** O(1) — everything happens in the original array with a couple of
  index variables.

## Core invariant

At every step, elements in `nums[0 .. writer-1]` are exactly the finished result,
and the reader is inspecting a candidate at or ahead of the writer. Keeping this
invariant true through each iteration is what makes the in-place overwrite safe.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Remove Element](problem-01-remove-element/PROBLEM.md) | In-place filtering with a write pointer | Easy |
| 2 | [Remove Duplicates from Sorted Array](problem-02-remove-duplicates-sorted-array/PROBLEM.md) | Dedup a sorted array, keep 1 of each | Easy |
| 3 | [Move Zeroes](problem-03-move-zeroes/PROBLEM.md) | Stable partition non-zeros to the front | Easy |
| 4 | [Remove Duplicates from Sorted Array II](problem-04-remove-duplicates-sorted-array-ii/PROBLEM.md) | Dedup keeping at most 2 of each value | Medium |
| 5 | [Find the Duplicate Number](problem-05-find-the-duplicate-number/PROBLEM.md) | Fast-slow (Floyd) cycle detection on an array | Medium |
