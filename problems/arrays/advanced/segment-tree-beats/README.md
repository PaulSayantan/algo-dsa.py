# Segment Tree Beats

**Segment Tree Beats** (Ji Driver Segment Tree, introduced by Ruyi "Ji Driver"
Ji in 2016) is a segment-tree augmentation that supports range updates which are
**not uniform over a range** — most famously **range chmin** (`a[i] = min(a[i],
x)`) and **range chmax** (`a[i] = max(a[i], x)`) alongside range-add and
range-sum. A plain lazy segment tree cannot handle chmin/chmax because there is
no single tag that describes "lower only the elements above `x`."

## The core idea

Each node stores extra statistics about its value distribution:

- for **chmin**: the **maximum**, the **strict second maximum**, and the **count
  of the maximum**;
- for **chmax** (mirror): the **minimum**, the **strict second minimum**, and the
  **count of the minimum**;
- plus the **sum** (and, in the full version, an **add** lazy tag).

A `chmin(x)` on a node then has three cases:

1. `x >= max` — no element is affected; **stop** (a break condition).
2. `secondMax < x < max` — only the maximum elements are affected; drop them to
   `x` in `O(1)` and adjust the sum; **stop**.
3. `x <= secondMax` — the effect is not uniform; **recurse** into the children
   and re-merge. This forced recursion is where "the tree gets beaten," and a
   potential-function argument bounds how often it can happen.

More broadly, Beats is the family of "augment a node with an extremal statistic,
then **recurse only past a break condition**" tricks — the same skeleton powers
range-square-root, range-modulo, and countdown-style updates.

## When to reach for it

- Range `chmin` / `chmax` combined with range `sum` / `max` / `min`.
- Range operations that touch each element only a bounded number of "real" times:
  range `x -> floor(sqrt(x))`, range `x -> x % m`, or "tick a counter every `k`
  increments."
- Any time a normal lazy tag does not exist but each element can only change a
  limited number of times before stabilizing.

## Complexity

- **chmin-only or chmax-only + sum:** `O((n + q) log n)` amortized.
- **Full chmin + chmax + add + sum:** `O((n + q) log^2 n)` amortized.
- **Space:** `O(n)`.

The bounds are **amortized** and rest on a potential argument (each forced
recursion strictly reduces the number of distinct extremal values in a subtree).
Individual operations can be slow, but the total across a run is near-linear-log.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Range Square-Root and Range Sum](problem-01-sum-and-replace/PROBLEM.md) | Break condition on the range **max**; stop when `max <= 1` | Medium |
| 2 | [Range Modulo, Point Assignment, Range Sum](problem-02-range-mod-point-set/PROBLEM.md) | Break condition on the range **max**; stop when `max < x` | Hard |
| 3 | [Gorgeous Sequence — Range chmin / Max / Sum](problem-03-gorgeous-sequence/PROBLEM.md) | Classic Beats: **max + strict second max + count** for chmin | Hard |
| 4 | [Naive Operations — Increment and Floor-Division Sum](problem-04-naive-operations/PROBLEM.md) | Break condition on a **min countdown**; tick and reset | Hard |
| 5 | [Range chmin / chmax / add / Sum](problem-05-chmin-chmax-add-sum/PROBLEM.md) | Full Beats: both extremes + second extremes + add tag | Very Hard |

Work them in order: problems 1 and 2 build the "augment + break" intuition on a
single max, problem 3 introduces the second-max/count machinery that defines
Beats, problem 4 shows the mirrored countdown flavor, and problem 5 combines
everything into the general chmin/chmax/add tree.
