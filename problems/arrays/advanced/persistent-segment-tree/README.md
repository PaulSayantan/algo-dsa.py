# Persistent Segment Tree

A **persistent segment tree** is a segment tree that keeps every historical
version of itself alive after each update. Instead of mutating nodes in place,
an update creates copies of only the `O(log n)` nodes that lie on the path from
the root to the changed leaf; all other nodes are shared with the previous
version. Each update therefore returns a brand-new root, and any past root can
still be queried exactly as it looked at that moment in time.

## Why it works

A normal segment tree has `2n` nodes. A point update touches exactly one
root-to-leaf path (`~log n` nodes). If, instead of overwriting those nodes, we
allocate fresh copies and re-point the copies at the *shared* untouched
children, we get a new tree that differs from the old one in only `O(log n)`
nodes while reusing everything else. Keeping the list of roots gives us `O(1)`
access to any version.

```
version k-1 root ──┐        version k root ──┐
                   ▼                          ▼
              [ node ]                    [ node' ]   (new copy)
              /      \                    /       \
        [shared]  [shared]          [node']     [shared]  <- one child shared,
                                    (new copy)              one child rebuilt
```

## When to reach for it

- **k-th smallest / order statistics in a subarray `[l, r]`** — build one
  version per prefix; the range answer is `version[r] − version[l−1]`.
- **Count of values `≤ x` (or in a value range) inside `[l, r]`** — same prefix
  trick, merged at query time.
- **Historical / time-travel queries** — "what did the array look like after the
  17th update?"
- **Distinct-element counting online**, k-th smallest on a **tree path**, and
  binary-search-on-versions problems (e.g. maximum-height contiguous block).

The unifying trick is the **prefix-sum-of-trees**: two versions subtracted
node-for-node behave like a segment tree over just the elements between them.

## Complexity

| Operation                | Time         | Space (total)      |
|--------------------------|--------------|--------------------|
| Build initial version    | `O(n)`       | `O(n)`             |
| One point update / insert| `O(log n)`   | `O(log n)` extra   |
| One range query          | `O(log n)`   | —                  |
| k-th smallest on `[l,r]`  | `O(log n)`   | —                  |
| `m` updates, total memory | —            | `O(n + m log n)`   |

`n` here is the size of the coordinate domain (often the number of distinct
values after coordinate compression).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Versioned Range Sum](problem-01-versioned-range-sum/PROBLEM.md) | Point updates that fork new versions; range-sum any past version | Medium |
| 2 | [Count Elements ≤ X in a Subarray](problem-02-count-at-most-x-in-range/PROBLEM.md) | How many `A[i] ≤ x` for `l ≤ i ≤ r`, using prefix versions | Medium |
| 3 | [K-th Smallest Number in Range](problem-03-kth-smallest-in-range/PROBLEM.md) | Order statistic of `A[l..r]` (SPOJ MKTHNUM) — the flagship | Hard |
| 4 | [Distinct Elements in Range](problem-04-distinct-elements-in-range/PROBLEM.md) | Online count of distinct values in `A[l..r]` (SPOJ DQUERY) | Hard |
| 5 | [Sign on Fence](problem-05-sign-on-fence/PROBLEM.md) | Max height with a width-`w` contiguous block inside `[l,r]` (Codeforces 484E) | Very Hard |
