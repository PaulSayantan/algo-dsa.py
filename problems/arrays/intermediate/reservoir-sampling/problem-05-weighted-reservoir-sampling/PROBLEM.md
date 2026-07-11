# Weighted Reservoir Sampling

**Difficulty:** Hard

**Source:** Classic — Efraimidis & Spirakis, *"Weighted random sampling with a
reservoir"* (2006), algorithm **A-Res**.

## Description

You are given a **stream** of `(item, weight)` pairs whose total length `n` is **not
known in advance**, and an integer `k`. Each `weight` is a positive real number.

Return `k` items sampled **without replacement** using **weighted random sampling**: the
probability of drawing an item is proportional to its weight. Concretely, using the
Efraimidis–Spirakis scheme, the sample is generated as if you repeatedly draw items one
at a time, where at each draw an as-yet-unchosen item `i` is picked with probability

```
weight_i / (sum of weights of all items not yet chosen)
```

until `k` items have been drawn. For the special case `k = 1`, this means item `i` is
returned with probability exactly `weight_i / (sum of all weights)`.

You must do this in a **single pass** using only `O(k)` extra memory — you may not buffer
the whole stream. If the stream has fewer than `k` items, return all of them.

## Constraints

- `1 <= k`
- `0 <= n` (stream length unknown until fully consumed).
- Every `weight > 0` (weights are positive; they need not sum to 1).
- The stream is read exactly once, front to back.

## Examples

### Example 1

```
Input:  stream = [("a", 1.0), ("b", 1.0), ("c", 2.0)], k = 1
Output: "c"        # one possible run
```

**Explanation:** Total weight is `1 + 1 + 2 = 4`. With `k = 1`, the selection
probabilities are `P(a) = 1/4`, `P(b) = 1/4`, `P(c) = 2/4 = 1/2`. `"c"` is the most
likely single outcome (it is twice as likely as `"a"` or `"b"`), but any of the three can
be returned. Over many runs, `"c"` appears about half the time.

### Example 2

```
Input:  stream = [("x", 5.0), ("y", 3.0)], k = 5
Output: ["x", "y"]
```

**Explanation:** The stream has only `2 < 5 = k` items, so the whole stream is returned
regardless of weights — there is nothing to sample away.

## Hint

Give each streamed item a random **key** `u^(1/weight)` where `u` is uniform in `(0, 1)`,
and keep the `k` items with the **largest** keys using a size-`k` **min-heap**. Higher
weight biases the key toward 1, so heavier items are more likely to survive. This is
weighted **Reservoir Sampling** (algorithm A-Res).
