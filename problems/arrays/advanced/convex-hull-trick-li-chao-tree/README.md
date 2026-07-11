# Convex Hull Trick / Li Chao Tree

## What it is

Many dynamic-programming recurrences have the shape

```
dp[i] = min ( dp[j] + cost(j, i) )        (or max)
        j < i
```

where, after algebraic rearrangement, the term contributed by each candidate `j`
becomes a **linear function of some query value `x_i`**:

```
dp[i] = min ( m_j * x_i + b_j ) + (something depending only on i)
        j
```

Here `m_j` (the *slope*) and `b_j` (the *intercept*) depend only on `j`, and `x_i`
is a query point that depends only on `i`. A naive evaluation checks every `j` for
every `i`, giving `O(n^2)`.

The **Convex Hull Trick (CHT)** and the **Li Chao Tree** both answer
"what is the minimum (or maximum) of a set of lines at a given `x`?" much faster.
Only the lines on the **lower hull** (for minimization) or **upper hull** (for
maximization) can ever be optimal, so we maintain that hull and query it.

- **Monotonic CHT** — when new lines are inserted in monotonic slope order *and*
  queries arrive in monotonic `x` order, a deque + moving pointer gives amortized
  `O(1)` per operation, so the whole DP runs in `O(n)`.
- **Sorted / binary-search CHT** — lines still inserted in monotonic slope order,
  but queries are arbitrary: binary search the hull in `O(log n)` per query.
- **Li Chao Tree** — no monotonicity assumptions at all. Insert arbitrary lines
  and query arbitrary points in `O(log C)` each, where `C` is the coordinate range
  (or number of distinct query points after compression). This is the most general
  tool and is what you reach for when slopes are *not* monotonic.

## When to reach for it

Reach for CHT / Li Chao Tree when your `O(n^2)` DP transition can be written as a
minimum/maximum over lines `m_j * x_i + b_j`. Telltale signs:

- The cost term contains a product like `h_j * h_i`, `S_j * S_i`, or `(S_i - S_j)^2`
  that, once expanded, splits cleanly into an `i`-only part and a `j`-dependent line.
- `N` is large (say `>= 10^4`) so `O(n^2)` is too slow, and you need `O(n log n)`
  or `O(n)`.

## Typical complexity

| Variant | Insert | Query | Total DP |
|---|---|---|---|
| Monotonic CHT (deque + pointer) | amortized O(1) | amortized O(1) | O(n) |
| CHT with binary search | amortized O(1) | O(log n) | O(n log n) |
| Li Chao Tree | O(log C) | O(log C) | O(n log C) |

Space is `O(n)` for CHT and `O(n)` (with coordinate compression) or `O(C)` for the
Li Chao Tree.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Frog Jump III](problem-01-frog-jump-iii/PROBLEM.md) | Monotonic CHT (min); slopes & queries both monotone | Easy |
| 2 | [Print Article](problem-02-print-article/PROBLEM.md) | Monotonic CHT (min) on prefix sums; `(S_i - S_j)^2` split | Medium |
| 3 | [Kalila and Dimna in the Forest](problem-03-kalila-and-dimna/PROBLEM.md) | Monotonic CHT (min); direct `b_j * a_i` product | Medium |
| 4 | [Commando](problem-04-commando/PROBLEM.md) | Monotonic CHT (max); quadratic segment value, maximization | Medium-Hard |
| 5 | [Building Bridges](problem-05-building-bridges/PROBLEM.md) | Li Chao Tree (min); non-monotonic slopes force the general tool | Hard |
