# Solution — Sliding Window Median

## Brute Force

For each of the `n - k + 1` windows, copy the `k` elements, sort them, and read the
middle one (or the average of the two middle ones for even `k`).

- Time: `O((n - k + 1) * k log k)` = `O(n k log k)`.
- Space: `O(k)` per window.

For `n, k` up to `10^5` this is far too slow.

## Optimal Approach (Order-Statistics Tree)

Maintain the current window as a **dynamic multiset** in an order-statistics tree
(balanced BST augmented with subtree `size`). The window supports exactly the three
operations an OST provides in `O(log k)`:

- **insert(x)** — the element entering on the right.
- **delete(x)** — the element leaving on the left (`nums[i - k]`).
- **select(t)** — the t-th smallest key, used to read the median.

**Median via select.** With `k` elements currently in the tree:
- If `k` is odd, the median is `select((k + 1) / 2)` (1-indexed middle).
- If `k` is even, the median is the average of `select(k/2)` and `select(k/2 + 1)`.

Use a wide type for the even-`k` average to avoid overflow when adding two large
values (in Python this is automatic; in C++/Java cast to `long`/`double`).

**Sliding.** Insert the first `k` elements, then repeat: record the median, delete
the element that falls out of the window (`nums[i - k]`), insert the element that
enters (`nums[i]`), until the array is exhausted.

**Delete with duplicates.** Windows frequently contain repeated values (see example
2). Store a per-key `count`: deleting a key with `count > 1` just decrements the
count and the subtree sizes; only when the last copy is removed is the node unlinked
(replaced by merging / rotating its children). This keeps `delete(nums[i-k])`
removing exactly one occurrence, matching the single copy that left the window.

```
delete(node, key):
    if node is None:            return None            # not found (shouldn't happen)
    if key < node.key:          node.left  = delete(node.left,  key)
    elif key > node.key:        node.right = delete(node.right, key)
    else:                       # found the key
        if node.count > 1:      node.count -= 1; node.size -= 1; return node
        if node.left is None:   return node.right
        if node.right is None:  return node.left
        # two children: rotate the higher-priority child up, then delete below
        if node.left.pr > node.right.pr:  node = rot_r(node); node.right = delete(node.right, key)
        else:                             node = rot_l(node); node.left  = delete(node.left,  key)
    update_size(node);          return node
```

**Correctness.** After the initial fill and each slide, the tree contains exactly the
`k` values of the current window (one insert balances one delete). `select` uses the
subtree sizes to locate the exact order statistic, and the BST invariant makes those
size counts correct. Hence each recorded value is the true median of its window.

Reference (treap core; `insert`, `select`, rotations, `_upd` as in Problem 1):

```python
class Solution:
    def medianSlidingWindow(self, nums, k):
        root = None
        for i in range(k):
            root = insert(root, nums[i])
        res = []
        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(select(root, k // 2 + 1)))
            else:
                lo = select(root, k // 2)
                hi = select(root, k // 2 + 1)
                res.append((lo + hi) / 2.0)
            if i == len(nums):
                break
            root = delete(root, nums[i - k])   # element leaving on the left
            root = insert(root, nums[i])        # element entering on the right
        return res
```

- Time: `O(n log k)` — one insert + one delete + O(1) selects per window.
- Space: `O(k)` — the tree holds only the current window.

**Alternative:** the popular two-heaps approach (a max-heap of the lower half and a
min-heap of the upper half) with lazy deletion also runs in `O(n log k)`. The OST is
arguably cleaner because a single structure handles both the "which element leaves"
delete and the median select without lazy-deletion bookkeeping.

## Key Insights & Edge Cases

- **Even vs. odd `k`.** Odd -> one `select`; even -> average two adjacent order
  statistics. Return floats so `[1, 3, -1] -> 1.0` and even windows average cleanly.
- **Overflow in the even case.** `select(k/2) + select(k/2+1)` can overflow 32-bit
  ints (values up to `2^31 - 1`); average in 64-bit / floating point.
- **Duplicates.** Maintain a `count` per key so `delete` removes exactly one copy;
  otherwise repeated values (example 2) break the window contents.
- **k == 1.** Every window is a single element and the median is that element itself.
- **k == len(nums).** There is exactly one window covering the whole array.
- **Deleting the correct element.** The element leaving is `nums[i - k]` (its value),
  not an index; on the OST you delete by value, so identical values are
  interchangeable and any one copy may be removed.
