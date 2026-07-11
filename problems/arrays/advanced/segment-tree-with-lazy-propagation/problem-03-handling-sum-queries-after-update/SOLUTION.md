# Solution — Handling Sum Queries After Update

## Brute Force

Simulate literally:

- Type 1 (`[1, l, r]`): loop `i` from `l` to `r`, `nums1[i] ^= 1`. `O(n)`.
- Type 2 (`[2, p, 0]`): loop over all `i`, `nums2[i] += nums1[i] * p`. `O(n)`.
- Type 3 (`[3, 0, 0]`): `sum(nums2)`. `O(n)` (or `O(1)` with a running total).

With `n, q ≤ 10^5`, each type-1/type-2 query is `O(n)`, giving `O(q * n) ≈ 10^10`
— too slow.

- **Time:** `O(n)` per query. **Space:** `O(n)`.

## Optimal Approach — Segment Tree with Lazy Propagation

### The key reduction

A type-2 query adds `p` to `nums2[i]` exactly where `nums1[i] == 1`. Therefore

```
sum(nums2) increases by p * (number of 1s currently in nums1).
```

So we never modify `nums2` element-by-element. Maintain a single running scalar
`total = sum(nums2)`. Then:

- Type 2: `total += p * ones`, where `ones` is the current count of 1s in `nums1`.
- Type 3: append `total`.

All that remains is to keep `ones` (and the count of 1s in any range) under range
*flips*. That is exactly a lazy segment tree over `nums1`.

### The flip (XOR) lazy tag

Each node covering `[lo, hi]` (length `k = hi - lo + 1`) stores:

- `ones` — the number of 1s in its range, reflecting its own pending flip;
- `flip` — a boolean tag: `True` means "this whole range still needs to be
  flipped in the children".

`apply(node)` flips the node: `ones = k - ones` and `flip ^= True`. Two flips
cancel (`flip ^= True` twice returns to `False`), which is why XOR composition is
correct — flipping is an *involution*.

`push_down(node)` applies the flip to both children (with their own lengths) and
clears the parent tag.

Range flip is the usual three-case recursion, combining children by `ones =
left.ones + right.ones`. The count of 1s in the whole array is just the root's
`ones`.

### Why it is correct

Invariant 1: a node's `ones` reflects its own pending flip, so a fully covered
node needs no descent. Invariant 2: the flip tag has not reached the children, so
`push_down` restores consistency before any partial descent. Because flip is
self-inverse and order-independent per element, deferring and later applying tags
yields the same per-element parity as immediate application.

Each type-1 query is `O(log n)`; type-2 and type-3 are `O(1)` given the root's
`ones` and the running `total`. Total: `O((n + q) log n)`.

### Reference implementation

```python
from typing import List


class Solution:
    def handleQuery(self, nums1, nums2, queries) -> List[int]:
        n = len(nums1)
        ones = [0] * (4 * n)
        flip = [False] * (4 * n)

        def build(node, lo, hi):
            if lo == hi:
                ones[node] = nums1[lo]
                return
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            ones[node] = ones[2 * node] + ones[2 * node + 1]

        def apply(node, lo, hi):
            ones[node] = (hi - lo + 1) - ones[node]
            flip[node] ^= True

        def push_down(node, lo, mid, hi):
            if flip[node]:
                apply(2 * node, lo, mid)
                apply(2 * node + 1, mid + 1, hi)
                flip[node] = False

        def update(node, lo, hi, l, r):
            if r < lo or hi < l:
                return
            if l <= lo and hi <= r:
                apply(node, lo, hi)
                return
            mid = (lo + hi) // 2
            push_down(node, lo, mid, hi)
            update(2 * node, lo, mid, l, r)
            update(2 * node + 1, mid + 1, hi, l, r)
            ones[node] = ones[2 * node] + ones[2 * node + 1]

        build(1, 0, n - 1)
        total = sum(nums2)
        ans = []
        for t, a, b in queries:
            if t == 1:
                update(1, 0, n - 1, a, b)
            elif t == 2:
                total += a * ones[1]     # a is p; ones[1] = #1s in nums1
            else:
                ans.append(total)
        return ans
```

- **Time:** `O(n)` build, `O(log n)` per flip, `O(1)` per type-2/3.
  Overall `O((n + q) log n)`. **Space:** `O(n)`.

## Key Insights & Edge Cases

- **Recognize the reduction first.** The hard part is *seeing* that you only need
  the count of 1s and a running total; the segment tree is then a standard flip
  tree. Without the reduction you'd be tempted to build a tree over `nums2`.
- **Flip is XOR, hence self-inverse.** Tag composition is `flip ^= True`; the count
  transform is `ones = length - ones`. Both a length factor *and* a boolean tag
  are needed.
- **`p` can be 0** (Example 2): `total += 0 * ones` is a no-op — fine.
- **`total` can be large:** up to `~10^5 * 10^9` from initial `nums2` plus
  `~10^5 * 10^6 * 10^5` from updates. Use 64-bit integers when porting (Python
  handles big ints natively).
- **Only type-3 queries produce output**; do not emit anything for types 1 and 2.
- **Read the root once per type-2 query** (`ones[1]`); do not re-traverse the tree.
