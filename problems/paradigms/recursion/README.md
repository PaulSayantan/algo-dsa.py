# Recursion

**Category:** paradigms / paradigm

**One-line:** Solve by reducing to smaller self-similar subproblems.

## What is it?

**Recursion** is a problem-solving technique where a function solves a problem by
calling *itself* on a **smaller instance of the same problem**, then combining that
smaller answer into the answer for the original. Every recursive solution has two
essential parts:

1. **Base case(s)** — the smallest inputs whose answer is known outright and requires
   no further recursion. This is what *stops* the recursion.
2. **Recursive case** — express the answer for input of size `n` in terms of the
   answer for one or more strictly smaller inputs, and make progress toward a base
   case on every call.

The mental model is *trust*: assume the recursive call already returns the correct
answer for the smaller problem (the "recursive leap of faith"), and focus only on how
to (a) shrink the problem and (b) stitch the smaller answer back together. Under the
hood, each call gets its own **stack frame** holding its local state; frames pile up on
the way *down* to the base case and unwind on the way *back up*.

Recursion is the backbone of divide and conquer, backtracking, tree/graph traversal
(DFS), and dynamic programming — but at its core it is just: *shrink, delegate,
combine*.

## When to reach for it

Look for these signals:

- The problem is **self-similar** — a problem of size `n` contains a subproblem of the
  same shape at size `n-1` (or `n/2`). Factorials, Fibonacci, and linked-list walks
  fit this exactly.
- The data structure is **recursively defined** — linked lists (a node + a smaller
  list), trees (a root + subtrees), and nested/grammar structures are naturally
  traversed with recursion.
- You can identify a clean **base case** and a way to **strictly shrink** the input on
  every step (fewer elements, half the range, a smaller exponent).
- An iterative solution would need you to *manually manage a stack* — recursion lets
  the call stack do that bookkeeping for you.

## The three-question checklist

Before writing a recursive function, answer:

1. **What is the base case?** (When do I stop and return directly?)
2. **How do I make the problem smaller?** (What smaller input do I recurse on, and does
   it always move toward the base case?)
3. **How do I combine the sub-answer into my answer?** (What do I do with the value the
   recursive call returns?)

If every recursive call moves strictly toward a base case, the recursion terminates.

## How to analyze the running time

Recursion running time is captured by a **recurrence relation** `T(n)` for the work at
size `n` in terms of smaller sizes:

- **Linear recursion** (one call, size `n-1`): `T(n) = T(n-1) + O(1)` → `O(n)` time,
  `O(n)` stack. Examples: factorial, sum of a list, reverse a linked list.
- **Halving recursion** (one call, size `n/2`): `T(n) = T(n/2) + O(1)` → `O(log n)`.
  Example: fast exponentiation `Pow(x, n)`.
- **Binary/tree recursion** (two calls): naive Fibonacci `T(n) = T(n-1) + T(n-2) + O(1)`
  → `O(φ^n)` (exponential, because subproblems overlap and are recomputed). Tower of
  Hanoi `T(n) = 2T(n-1) + O(1)` → `O(2^n)`.

When two recursive branches **overlap** (recompute the same subproblem), plain
recursion is exponential — that is the cue to add **memoization** (top-down DP) or
switch to **tabulation**.

## Typical complexity

- **Time:** whatever the recurrence resolves to — `O(n)` for linear recursion,
  `O(log n)` for halving, `O(2^n)`/`O(φ^n)` for branching recursion with overlap.
- **Space:** at minimum `O(depth of recursion)` for the call stack — `O(n)` for linear
  recursion, `O(log n)` for balanced halving. This stack space is *implicit* and can
  cause a `RecursionError`/stack overflow on deep inputs.

> Watch out: deep linear recursion (millions of frames) can overflow the stack —
> Python's default limit is ~1000 frames. **Tail-call-shaped** linear recursion often
> converts cleanly to a loop, and overlapping branches call for **memoization**.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Fibonacci Number](problem-01-fibonacci-number/PROBLEM.md) | Base cases + a two-branch recurrence | Easy |
| 2 | [Reverse Linked List](problem-02-reverse-linked-list/PROBLEM.md) | Recurse to the tail, relink while unwinding | Easy |
| 3 | [Merge Two Sorted Lists](problem-03-merge-two-sorted-lists/PROBLEM.md) | Pick the smaller head, recurse on the rest | Easy |
| 4 | [Pow(x, n)](problem-04-pow-x-n/PROBLEM.md) | Halve the exponent — `O(log n)` fast power | Medium |
| 5 | [Swap Nodes in Pairs](problem-05-swap-nodes-in-pairs/PROBLEM.md) | Swap the first pair, recurse on the rest | Medium |
| 6 | [Tower of Hanoi](problem-06-tower-of-hanoi/PROBLEM.md) | Two subcalls of size `n-1` around one move | Medium |
