# Order-Statistics Tree

An **Order-Statistics Tree (OST)** is a balanced binary search tree (BST) in which
every node stores the **size of its subtree** (the number of stored keys in the
subtree rooted at that node, counting duplicates). This single augmentation turns
an ordinary BST into a structure that answers two extra queries in `O(log n)`:

- **`select(k)`** — return the k-th smallest key (the key of *order statistic* k).
- **`rank(x)`** — return how many stored keys are `< x` (equivalently, the position
  x would occupy in sorted order).

Because the subtree-size field can be recomputed from a node's children in `O(1)`
(`size = count + size(left) + size(right)`), it is maintained for free during the
normal rotations / rebalancing of any balanced BST (AVL, red-black, treap, or a
Fenwick/order-indexed variant). The classic presentation is the red-black
augmentation in CLRS chapter 14; in practice a **treap** or **AVL** is easiest to
code from scratch, and that is what the answer keys here use.

## When to reach for it

Reach for an OST when you need a **dynamic** multiset that supports, all at once:

- insert / delete of arbitrary keys, and
- "what is the k-th smallest?" (select), and/or
- "how many elements are `< x` / `<= x` / in `[lo, hi]`?" (rank / range-count).

If the value universe is small or can be coordinate-compressed offline, a **Fenwick
tree (BIT)** or **segment tree over value indices** gives the same asymptotics with
a smaller constant and is often preferred in contests — an OST is the tool when you
want a self-contained pointer structure, cannot compress values up front (truly
online insertions), or need the actual key back from a `select`.

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| insert / delete | `O(log n)` expected (treap) or worst-case (AVL/red-black) | `O(1)` extra |
| select(k) | `O(log n)` | `O(1)` |
| rank(x) / count in range | `O(log n)` | `O(1)` |
| build from n items | `O(n log n)` | `O(n)` |

Total space for the structure is `O(n)`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Kth Largest Element in a Stream](problem-01-kth-largest-in-a-stream/PROBLEM.md) | `select` on a growing multiset | Easy |
| 2 | [Count of Smaller Numbers After Self](problem-02-count-of-smaller-after-self/PROBLEM.md) | insert + `rank` (scan right-to-left) | Hard |
| 3 | [Reverse Pairs](problem-03-reverse-pairs/PROBLEM.md) | order-count with a `2*x` threshold | Hard |
| 4 | [Sliding Window Median](problem-04-sliding-window-median/PROBLEM.md) | insert + delete + `select` in a window | Hard |
| 5 | [Count of Range Sum](problem-05-count-of-range-sum/PROBLEM.md) | prefix sums + range `rank` query | Hard |
