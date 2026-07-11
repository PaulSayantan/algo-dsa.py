# Monotonic Stack / Queue

A **monotonic stack** (or **monotonic queue/deque**) is an ordinary stack/deque with one
extra rule: the elements inside it always stay sorted (strictly or non-strictly increasing
or decreasing). Before pushing a new element, you *pop* every element that would break the
ordering. That single pop-loop is what makes the whole family of problems run in linear time.

## What it is

- **Monotonic stack** — used for "next / previous greater or smaller element" style
  problems. You scan the array once; each element is pushed once and popped at most once,
  so the total work is `O(n)`. The moment you pop an element `x` because the current
  element `c` violates the ordering, you have just discovered the answer for `x` (its
  next-greater or next-smaller neighbor is `c`).
- **Monotonic queue (deque)** — used for **sliding-window extremum** problems (window max
  or min). The deque stores indices whose values are monotonic; the front always holds the
  index of the current window's extremum. Elements enter from the back and leave from
  either end, again `O(n)` total.

## When to reach for it

Look for these signals:

- "Find the next / previous element that is greater / smaller than each element."
- "For every element, how far until a larger value?" (span / warmer-day problems)
- "Sum or count over all subarrays of the min / max element."
- "Maximum area / largest rectangle bounded by heights."
- "Maximum or minimum of every window of size `k`."

If a brute-force solution is `O(n^2)` because each element re-scans its neighbors, a
monotonic structure usually collapses it to `O(n)`.

## Typical complexity

| Structure | Time | Space |
|-----------|------|-------|
| Monotonic stack | `O(n)` amortized (each index pushed/popped once) | `O(n)` |
| Monotonic queue (deque) | `O(n)` amortized | `O(k)` for the window |

## The core invariant

> While the incoming element breaks the stack/deque's ordering, pop. Whatever you pop is
> "resolved" by the incoming element. What remains after the loop is the incoming element's
> own answer (the top of the stack is its nearest surviving neighbor).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Next Greater Element I](problem-01-next-greater-element-i/PROBLEM.md) | Monotonic stack, next-greater map | Easy |
| 2 | [Daily Temperatures](problem-02-daily-temperatures/PROBLEM.md) | Monotonic stack storing indices (distance) | Medium |
| 3 | [Sum of Subarray Minimums](problem-03-sum-of-subarray-minimums/PROBLEM.md) | Monotonic stack, contribution counting | Medium |
| 4 | [Sliding Window Maximum](problem-04-sliding-window-maximum/PROBLEM.md) | Monotonic **deque** (window extremum) | Hard |
| 5 | [Largest Rectangle in Histogram](problem-05-largest-rectangle-in-histogram/PROBLEM.md) | Monotonic stack, previous/next-smaller spans | Hard |
