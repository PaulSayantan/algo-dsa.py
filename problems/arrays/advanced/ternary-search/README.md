# Ternary Search

**Ternary Search** finds the **extremum** (minimum or maximum) of a **unimodal**
function by repeatedly discarding one third of the search interval. It is the
optimization cousin of binary search: binary search locates a **boundary** in a
**monotone** predicate, while ternary search locates the single **peak or valley** of
a function that first rises then falls (or first falls then rises).

## The core idea

A function `f` on `[lo, hi]` is **unimodal** (for a maximum) if it is strictly
increasing up to some point `x*` and strictly decreasing after it. Pick two interior
probes that split the interval into thirds:

```
m1 = lo + (hi - lo) / 3
m2 = hi - (hi - lo) / 3          # so lo < m1 < m2 < hi
```

Compare `f(m1)` and `f(m2)`:

- If `f(m1) < f(m2)`, the maximum cannot lie in `[lo, m1]` — discard it: `lo = m1`.
- If `f(m1) > f(m2)`, the maximum cannot lie in `[m2, hi]` — discard it: `hi = m2`.
- If equal (continuous case), either third can be dropped.

Each step shrinks the interval by a factor of `2/3`, so after `k` steps the interval
length is `(2/3)^k` of the original. To reach absolute precision `eps` you need
`O(log_{3/2}((hi - lo) / eps))` iterations. (For a **minimum**, flip the comparison.)

## When to reach for it

Reach for ternary search when **all** of these hold:

- You are **optimizing a value** (find the best `x`, or the best `f(x)`), not searching
  for a target or a boundary. If you want "the first index where a predicate turns
  true," that is **binary search**.
- The objective is **unimodal** on the search interval: exactly one local extremum,
  which is therefore the global extremum. Convex functions (min) and concave functions
  (max) are always unimodal. The pointwise **max of convex functions** is convex; the
  **sum of convex functions** is convex — both very common ways unimodality appears.
- You can **evaluate `f(x)` cheaply** at an arbitrary point. If one evaluation costs
  `E`, the total cost is `E · O(log(range / eps))`.

> Ternary search does **not** work on a merely monotone function (there is no interior
> extremum) and gives **garbage on multimodal functions** (multiple humps) — it may
> converge to the wrong local extremum. Verify unimodality before using it.

## Complexity

| Domain | Time | Space |
|---|---|---|
| Real interval to precision `eps` | `O(E · log_{3/2}((hi - lo) / eps))` | `O(1)` |
| Integer interval of length `n` | `O(E · log_{3/2} n)` | `O(1)` |
| Nested 2D (ternary inside ternary) | `O(E · log^2(range / eps))` | `O(1)` |

`E` is the cost of one function evaluation.

## Integer vs. continuous

- **Continuous:** loop for a fixed number of iterations (e.g. 200) or until
  `hi - lo < eps`. Two fresh evaluations per step (or reuse one).
- **Integer:** shrink until `hi - lo <= 2` (a tiny window), then scan the few
  remaining points directly. Update with `lo = m1 + 1` / `hi = m2 - 1` to guarantee
  progress and avoid an infinite loop.

## Problems

| # | Problem | Technique flavor | Difficulty |
|---|---|---|---|
| 1 | [Peak Index in a Mountain Array](problem-01-peak-index-mountain-array/PROBLEM.md) | Integer ternary — argmax of a unimodal array | Easy |
| 2 | [Minimum of the Upper Envelope of Parabolas](problem-02-minimum-of-upper-envelope-of-parabolas/PROBLEM.md) | Continuous ternary on a real interval | Medium |
| 3 | [Closest Approach of Two Moving Points](problem-03-closest-approach-of-two-moving-points/PROBLEM.md) | Continuous ternary over a time window | Medium |
| 4 | [Best Position for a Service Centre](problem-04-best-position-for-a-service-centre/PROBLEM.md) | Nested (2D) ternary search | Hard |
| 5 | [Weakness and Poorness](problem-05-weakness-and-poorness/PROBLEM.md) | Ternary on a real parameter with an `O(n)` evaluator | Hard |
