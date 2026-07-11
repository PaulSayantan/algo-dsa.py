# Floyd's Cycle Detection (Tortoise & Hare)

Floyd's Cycle Detection algorithm — nicknamed **Tortoise & Hare** — uses two
pointers that traverse a sequence at different speeds to detect whether the
sequence eventually repeats (forms a cycle). The **slow** pointer advances one
step at a time; the **fast** pointer advances two steps at a time. If the
sequence is cyclic, the fast pointer eventually laps the slow pointer and they
meet at the same node/value. If the fast pointer reaches the end (a null/no
successor), there is no cycle.

The trick works on **any deterministic "next" function** — not just linked
lists. If each element `x` has exactly one successor `f(x)`, then the sequence
`x, f(x), f(f(x)), ...` is eventually periodic (it must revisit a value in a
finite state space), and Floyd's algorithm finds that period. This is why the
same idea solves array problems like *Find the Duplicate Number* (where
`f(x) = nums[x]`) and *Happy Number* (where `f(x)` is the sum of squared
digits).

## When to reach for it

- You need to detect a cycle in a linked list or a functional graph.
- You must do it in **O(1) extra space** (a hash set would work but costs O(n)
  memory).
- You have an implicit sequence defined by "keep applying the same function"
  and want to find whether/where it repeats, or find the cycle's entry point.

## Complexity

- **Time:** O(n) — both pointers together traverse a linear number of steps
  before meeting (the fast pointer travels at most ~2n steps).
- **Space:** O(1) — only two pointers, regardless of input size.

## Two phases

1. **Detection:** move `slow` by 1 and `fast` by 2 until they meet (cycle) or
   `fast` falls off the end (no cycle).
2. **Finding the cycle entrance (optional):** reset one pointer to the start,
   then advance both by 1; they meet exactly at the cycle's entry node. This
   follows from the distance math `x + y = k*loop` (explained in the solutions).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Linked List Cycle](problem-01-linked-list-cycle/PROBLEM.md) | Detect whether a cycle exists (phase 1 only) | Easy |
| 2 | [Happy Number](problem-02-happy-number/PROBLEM.md) | Cycle detection on an implicit numeric sequence | Easy |
| 3 | [Find the Duplicate Number](problem-03-find-the-duplicate-number/PROBLEM.md) | Treat the array as a linked list; find cycle entrance | Medium |
| 4 | [Linked List Cycle II](problem-04-linked-list-cycle-ii/PROBLEM.md) | Return the node where the cycle begins (both phases) | Medium |
| 5 | [Circular Array Loop](problem-05-circular-array-loop/PROBLEM.md) | Cycle detection with directional/length constraints | Medium |
