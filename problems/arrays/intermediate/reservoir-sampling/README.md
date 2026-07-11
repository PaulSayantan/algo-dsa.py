# Reservoir Sampling

**Reservoir Sampling** is a family of randomized algorithms for choosing a simple
random sample of **k** items from a stream of **unknown or unbounded** length `n`,
using only `O(k)` memory and a **single pass** over the data. You never need to know
`n` in advance, and you never need to store the whole stream — which is exactly why it
shines on data that is too large to fit in memory (log files, network streams, database
cursors) or that arrives one element at a time.

## The core idea (k = 1)

Keep one "chosen" element. Process the stream one item at a time. When the **i-th**
item arrives (1-indexed), replace the currently chosen element with the new one with
probability **1/i**.

```
chosen = None
for i, item in enumerate(stream, start=1):
    if randint(1, i) == 1:      # happens with probability 1/i
        chosen = item
return chosen
```

At the end, **every** item has probability exactly `1/n` of being the one chosen —
even though we never learned `n` and stored only a single element.

### Why it is uniform

Item `j` is the final choice iff it was picked at step `j` **and** never replaced
afterwards:

```
P(j chosen) = (1/j) · (1 - 1/(j+1)) · (1 - 1/(j+2)) · ... · (1 - 1/n)
            = (1/j) · (j/(j+1)) · ((j+1)/(j+2)) · ... · ((n-1)/n)
            = (1/j) · (j/n)                # telescoping product
            = 1/n
```

## The general algorithm (Algorithm R, k ≥ 1)

1. Put the **first k** items into a `reservoir` array (indices `0..k-1`).
2. For each later item at 1-indexed position `i > k`:
   - Pick a random integer `j` in `[0, i-1]`.
   - If `j < k`, overwrite `reservoir[j]` with the new item; otherwise discard it.
3. When the stream ends, the reservoir holds a uniform random sample of size `k`.

Each item survives in the reservoir with probability exactly `k/n`.

## When to reach for it

- The input is a **stream / iterator** and its length `n` is **unknown, huge, or
  infinite** — you cannot afford (or are not able) to buffer it or make two passes.
- You want a **uniform** sample (`k = 1`, or `k > 1` without replacement) drawn online.
- Memory is the constraint: you can hold `O(k)` items but not `O(n)`.

If you already have the full array in memory and know `n`, a plain
`random.sample` / Fisher–Yates partial shuffle is simpler and just as correct.
Use **weighted** reservoir sampling (A-Res, Efraimidis–Spirakis) when items carry
weights and you want selection probability proportional to weight.

## Complexity

| Metric | Value |
|--------|-------|
| Time | `O(n)` — one pass, `O(1)` work per item |
| Extra space | `O(k)` — the reservoir only (`O(1)` when `k = 1`) |
| Passes over data | 1 |
| Requires knowing `n`? | No |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Linked List Random Node](problem-01-linked-list-random-node/PROBLEM.md) | Return a uniformly random node value from a list of unknown length. | Medium |
| 2 | [Random Pick Index](problem-02-random-pick-index/PROBLEM.md) | Return a uniformly random index whose value equals a target. | Medium |
| 3 | [Sample K Items From a Stream](problem-03-sample-k-from-stream/PROBLEM.md) | Draw a uniform sample of size k from a one-pass stream. | Medium |
| 4 | [Random Node in a Binary Tree](problem-04-random-node-in-binary-tree/PROBLEM.md) | Pick a uniformly random tree node in one traversal without precounting. | Medium |
| 5 | [Weighted Reservoir Sampling](problem-05-weighted-reservoir-sampling/PROBLEM.md) | Sample k items with probability proportional to weight in one pass. | Hard |
