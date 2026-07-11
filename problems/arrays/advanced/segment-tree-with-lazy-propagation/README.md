# Segment Tree with Lazy Propagation

## What it is

A **segment tree** is a binary tree over an array in which every node stores an
aggregate (sum, min, max, …) of a contiguous sub-range. It answers a range query
and a *point* update in `O(log n)`.

A plain segment tree, however, struggles with **range updates** ("add 5 to every
element in `[l, r]`"): touching each covered leaf costs `O(n)` in the worst case.
**Lazy propagation** fixes this. When an update fully covers a node's range, we
apply the change to that node's aggregate and store a *pending* value (a "lazy
tag") on the node instead of recursing into its children. The tag is only
**pushed down** to children later, when a subsequent query or update actually
needs to descend through that node. This defers work until it is unavoidable, so
both range updates and range queries run in `O(log n)`.

## When to reach for it

Use a lazy segment tree when you need **both**:

1. Updates that affect a *whole range* of indices (add / assign / flip / multiply), and
2. Queries that aggregate over a *range* (sum / min / max / count).

If updates are point-only, a plain segment tree or a Fenwick (BIT) tree is
simpler. If you only need range updates but *point* queries, a difference array
or a BIT-with-difference trick is lighter. Reach for lazy propagation once *both*
sides of the workload are range-based.

## Complexity

| Operation        | Time       | Space  |
|------------------|------------|--------|
| Build            | `O(n)`     | `O(n)` |
| Range update     | `O(log n)` | —      |
| Range query      | `O(log n)` | —      |
| Overall storage  | —          | `O(n)` (≈ `4n` nodes for a recursive tree) |

The recursion depth (and the implicit push-down stack) is `O(log n)`.

## The two invariants that make it correct

1. **A node's aggregate is always fully up to date**, *including* any pending
   update stored in its own lazy tag.
2. **A node's lazy tag has not yet been applied to its children.** Before you
   recurse into either child, you must `push_down` the tag so the children become
   consistent again.

Getting the *combine order* of tags right (e.g. an `assign` must clear a pending
`add`, but an `add` composes on top of an `assign`) is the subtle part these
problems drill.

## Problems

| # | Problem | Technique variant | Difficulty |
|---|---------|-------------------|------------|
| 1 | [Range Add and Range Sum](problem-01-range-add-range-sum/PROBLEM.md) | Additive lazy tag, sum aggregate | Medium |
| 2 | [Range Assign and Range Minimum](problem-02-range-assign-range-min/PROBLEM.md) | Assignment lazy tag, min aggregate | Medium |
| 3 | [Handling Sum Queries After Update](problem-03-handling-sum-queries-after-update/PROBLEM.md) | Boolean flip (XOR) lazy tag, count/sum aggregate (LeetCode 2569) | Hard |
| 4 | [Falling Squares](problem-04-falling-squares/PROBLEM.md) | Range set-to-value lazy tag + range max, with coordinate compression (LeetCode 699) | Hard |
| 5 | [Range Updates and Sums](problem-05-range-updates-and-sums/PROBLEM.md) | Two interacting lazy tags (assign + add), sum aggregate (CSES 1735) | Hard |

Work them in order: problems 1–2 establish the two canonical tag types, problem 3
introduces an involutive (self-inverse) tag, problem 4 layers coordinate
compression on top, and problem 5 forces two tag types to coexist correctly.
