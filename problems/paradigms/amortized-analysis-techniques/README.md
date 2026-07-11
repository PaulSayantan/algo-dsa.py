# Amortized Analysis Techniques

**Amortized analysis** is a way of reasoning about the *average* cost of an operation
over a *worst-case sequence* of operations, rather than the worst-case cost of a
single operation in isolation. The key idea when *designing* algorithms with it:
structure your work so that any single expensive step is "paid for" by many cheap
steps that came before it. An operation may occasionally cost O(n), yet the total
cost of *m* operations is still O(m), giving O(1) **amortized** per operation.

## The Three Classic Methods

1. **Aggregate method** — bound the total cost of *n* operations by some T(n), then
   declare the amortized cost T(n)/n. (Used to analyze the dynamic array / "table
   doubling" where n pushes cost O(n) total, so O(1) each.)
2. **Accounting (banker's) method** — overcharge cheap operations and store the
   surplus as "credit" on data-structure elements; expensive operations spend that
   stored credit so they never go into debt.
3. **Potential method** — define a potential function Φ (stored energy) over the data
   structure. Amortized cost = actual cost + ΔΦ. Choose Φ so the drop in potential
   during an expensive op cancels its actual cost.

## When To Reach For It

- A structure has operations whose *individual* worst case is scary (O(n)) but where
  that worst case cannot happen every time — e.g. each element is pushed and popped
  from a stack **at most once**, so total stack work is O(n) across the whole run.
- Classic homes for the technique: **monotonic stack/queue** problems, the **sliding
  window** with a moving left pointer, **two-stack queues**, dynamic-array resizing,
  and union-find with path compression.
- Heuristic to spot it: if you're tempted to say "this inner `while` loop is O(n) so
  the whole thing is O(n^2)", check whether the inner loop's *total* iterations across
  the outer loop are bounded by n. If so, it's really O(n) amortized.

## Typical Complexity

- **Time:** many of these structures/algorithms achieve **O(1) amortized** per
  operation, i.e. **O(n) total** for n operations, even though a single operation may
  spike to O(n).
- **Space:** usually O(n) for the auxiliary stack/window/array.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Implement Queue using Stacks](problem-01-implement-queue-using-stacks/PROBLEM.md) | Two-stack queue; each element moved at most once → O(1) amortized `pop`/`peek` | Easy |
| 2 | [Daily Temperatures](problem-02-daily-temperatures/PROBLEM.md) | Monotonic stack; each index pushed/popped once → O(n) total | Medium |
| 3 | [Longest Substring Without Repeating Characters](problem-03-longest-substring-without-repeating-characters/PROBLEM.md) | Sliding window; left pointer only advances → O(n) total | Medium |
| 4 | [Online Stock Span](problem-04-online-stock-span/PROBLEM.md) | Monotonic stack with span accumulation → O(1) amortized `next` | Medium |
| 5 | [Largest Rectangle in Histogram](problem-05-largest-rectangle-in-histogram/PROBLEM.md) | Monotonic stack; every bar pushed/popped once → O(n) total | Hard |
| 6 | [Trapping Rain Water](problem-06-trapping-rain-water/PROBLEM.md) | Monotonic decreasing stack; each bar entering/leaving once → O(n) total | Hard |
