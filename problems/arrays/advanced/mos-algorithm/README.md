# Mo's Algorithm

**Mo's Algorithm** is an *offline* technique for answering many range queries
`[l, r]` on a static array. Instead of answering the queries in the order given, it
**reorders** them cleverly so that the answer to one query can be transformed into
the answer to the next by moving two pointers `curL` / `curR` only a small total
distance. The reordering splits the array into blocks of size `~√n` and sorts the
queries by `(block of l, then r)`. With that order the pointers travel `O((n+q)√n)`
steps in total, and each single step is a cheap `add`/`remove` of one element.

The only requirement is that you can maintain the query's answer *incrementally*:
given the answer for `[l, r]`, you must be able to update it in `O(1)` (or some small
cost) when you **add** or **remove** one element at either end.

## When to reach for it

Reach for Mo's when **all** of the following hold:

- The array is **static** (no updates between queries) — this is the classic form.
  (A harder variant, "Mo's with updates", relaxes this at cost `O(n^{2/3})` per op.)
- You have **many** range queries and can process them **offline** (you are allowed
  to read all queries first and answer in any order).
- The per-query answer supports cheap **incremental add/remove** of a boundary
  element, but has **no easy `merge` of two sub-ranges** — which is exactly when a
  segment tree does *not* apply. Canonical examples: *number of distinct values in a
  range*, *`Σ x·cnt[x]²`*, *count of values whose frequency equals themselves*.

Typical signals:
- "count distinct / mode / k-th frequency in a range" with no obvious associative merge
- an answer that is a function of the **frequency histogram** of the sub-range
- offline queries, static data, `n, q` up to `~10^5`–`2·10^5`

If the operation *is* associative and mergeable (sum, min, gcd), prefer a segment
tree / sparse table — they are online and often faster in practice.

## Complexity

| Aspect                                   | Cost                          |
|------------------------------------------|-------------------------------|
| Sorting queries                          | `O(q log q)`                  |
| Pointer movement (add/remove calls)      | `O((n + q)·√n)`               |
| Total (with `O(1)` add/remove)           | `O((n + q)·√n)`               |
| Block size (optimal)                     | `√n`, or `n/√q` if `q ≪ n`    |
| Space                                    | `O(n + q)` (+ frequency array)|

If `add`/`remove` each cost `f`, multiply the movement term by `f`. For Mo's on a
tree, flatten with an Euler tour (length `2n`) and the same bounds hold.

## The core template

```
B = max(1, int(n / sqrt(q)))          # block size
sort queries by (l // B, r)           # (even blocks asc r, odd blocks desc r → faster)
curL, curR = 0, -1                    # current window is empty
for (l, r) in sorted_queries:
    while curR < r: curR += 1; add(curR)
    while curL > l: curL -= 1; add(curL)
    while curR > r: remove(curR); curR -= 1
    while curL < l: remove(curL); curL += 1
    answer[query.id] = current_answer
```

**Ordering matters:** move the pointers in the "grow first, shrink last" order above
(or any order that never lets the window become invalid, e.g. `curL > curR`). The
[even/odd `r` sorting trick](problem-01-distinct-values-in-range/SOLUTION.md) roughly
halves the constant.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Distinct Values in a Range](problem-01-distinct-values-in-range/PROBLEM.md) | The canonical intro: maintain a distinct-count with a frequency array | Medium |
| 2 | [Little Elephant and Array](problem-02-little-elephant-and-array/PROBLEM.md) | Answer counts values whose frequency equals the value itself | Medium |
| 3 | [Powerful Array](problem-03-powerful-array/PROBLEM.md) | Maintain `Σ x·cnt[x]²` via an incremental **delta** on add/remove | Hard |
| 4 | [XOR and Favorite Number](problem-04-xor-and-favorite-number/PROBLEM.md) | Reduce subarray-XOR to **prefix-XOR pairs**, then run Mo's | Hard |
| 5 | [Count Distinct Values on Tree Paths](problem-05-tree-path-distinct-values/PROBLEM.md) | **Mo's on a tree**: Euler flatten + LCA + toggle add/remove | Hard |
