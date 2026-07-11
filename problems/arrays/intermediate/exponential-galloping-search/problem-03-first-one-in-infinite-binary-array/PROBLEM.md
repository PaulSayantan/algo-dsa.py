# First 1 in an Infinite Sorted Binary Array

**Difficulty:** Medium

**Source:** Classic interview problem ("index of first 1 in an infinite sorted
binary array"; a monotonic-predicate variant of exponential search)

## Description

You are given a **conceptually infinite** array `bits` that begins with a
(possibly empty) block of `0`s and is `1` from some index onward — that is, it
is sorted, and once a `1` appears every later element is also `1`. Concretely,
there is an unknown transition index `t >= 0` such that `bits[i] == 0` for
`i < t` and `bits[i] == 1` for `i >= t`. You do not know where the transition
is, and the array has no end.

You can read the array only through `reader.get(i)`, which returns the bit at
index `i`. Because the array is infinite and eventually all `1`s, **a first `1`
always exists**; your job is to return its index `t`.

Since the length is unbounded, you cannot bound a binary search up front. You
must first find *some* index that already holds a `1`, then pin down the exact
transition point.

## Constraints

- The array is infinite and sorted: all `0`s come first, then all `1`s.
- `reader.get(i)` returns `0` or `1` for any index `i >= 0`.
- The transition index `t` (the answer) fits in a 32-bit signed integer.
- `t` may be `0` (the array is `1` everywhere).

## Examples

**Example 1**

```
Input:  bits = 0, 0, 0, 0, 1, 1, 1, 1, ...   (transition at index 4)
Output: 4
Explanation: Probing index 1 (0), 2 (0), 4 (1) finds a 1 at index 4, bounding
the transition in [2, 4]. Binary search for the leftmost 1 returns index 4.
```

**Example 2**

```
Input:  bits = 1, 1, 1, 1, ...              (transition at index 0)
Output: 0
Explanation: get(0) == 1 already, so the very first element is a 1; the answer
is index 0.
```

**Example 3**

```
Input:  bits = 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, ...   (transition at index 9)
Output: 9
Explanation: Doubling probes 1, 2, 4, 8 (all 0), then 16 (1), bounding the
transition in [8, 16]. Binary search for the leftmost 1 returns index 9.
```

## Hint

Use Exponential (Galloping) Search on the monotonic predicate "is this bit a 1?":
double the probe index until `reader.get(bound) == 1`, then binary-search
`[bound // 2, bound]` for the leftmost index whose bit is `1`.
