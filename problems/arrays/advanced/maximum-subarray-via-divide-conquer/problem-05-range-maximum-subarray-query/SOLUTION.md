# Range Maximum Subarray Query — Solution

## Brute Force

Answer each query independently by running Kadane (or the `O(n log n)` recursion)
on the sub-range `nums[l..r]`.

```python
def brute(nums, queries):
    def kadane(l, r):
        best = cur = nums[l]
        for i in range(l + 1, r + 1):
            cur = max(nums[i], cur + nums[i])
            best = max(best, cur)
        return best
    return [kadane(l, r) for (l, r) in queries]
```

- **Time:** `O(q · n)` — fine for a single query, too slow when `q` and `n` are
  both large (up to `5·10^9` operations at the constraint limits).
- **Space:** `O(1)` beyond the output.

## Optimal Approach (Divide & Conquer as a Segment Tree)

The one-shot divide & conquer algorithm already merges two halves with a crossing
rule. A **segment tree** freezes that recursion into a reusable data structure:
every node covering a range stores a summary, and the merge of two child summaries
is *exactly* the crossing-combine step. Answering a query = merging the `O(log n)`
canonical nodes that tile `[l, r]`.

**Node summary** for a range:

- `total`       — sum of the whole range,
- `best_prefix` — max sum of a prefix starting at the range's left end,
- `best_suffix` — max sum of a suffix ending at the range's right end,
- `best`        — max sum of any subarray inside the range (the answer for that
  range).

**Leaf** (single element `x`): `total = best_prefix = best_suffix = best = x`.

**Merge** left child `L` (lower indices) with right child `R`:

```python
def merge(L, R):
    total       = L.total + R.total
    best_prefix = max(L.best_prefix, L.total + R.best_prefix)
    best_suffix = max(R.best_suffix, R.total + L.best_suffix)
    best        = max(L.best, R.best, L.best_suffix + R.best_prefix)
    return Node(total, best_prefix, best_suffix, best)
```

The `L.best_suffix + R.best_prefix` term is the **crossing subarray** — the best
suffix of the left glued to the best prefix of the right — identical to the
combine step of problems 1 and 2. `best_prefix`/`best_suffix` let parents keep
merging: a prefix of the combined range is either a prefix of `L`, or all of `L`
plus a prefix of `R`.

Reference build + query:

```python
from collections import namedtuple
Node = namedtuple("Node", "total best_prefix best_suffix best")

class Solution:
    def rangeMaxSubarray(self, nums, queries):
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        NEG = float("-inf")
        IDENTITY = Node(0, NEG, NEG, NEG)     # neutral element for merge
        tree = [IDENTITY] * (2 * size)

        for i, x in enumerate(nums):          # leaves
            tree[size + i] = Node(x, x, x, x)
        for p in range(size - 1, 0, -1):      # internal nodes, O(n)
            tree[p] = merge(tree[2 * p], tree[2 * p + 1])

        def query(l, r):                      # inclusive [l, r], iterative
            left_acc, right_acc = IDENTITY, IDENTITY
            l += size
            r += size + 1
            while l < r:
                if l & 1:
                    left_acc = merge(left_acc, tree[l]); l += 1
                if r & 1:
                    r -= 1; right_acc = merge(tree[r], right_acc)
                l >>= 1; r >>= 1
            return merge(left_acc, right_acc).best

        return [query(l, r) for (l, r) in queries]
```

Note the query accumulates **left pieces in order and right pieces in reverse** so
the final `merge` respects index order — a subtle but essential detail, since
`merge` is not commutative.

**Why it is correct.** By induction each node's summary is correct: leaves are
trivially correct, and `merge` combines two correct child summaries using the
same three-case argument as the recursive algorithm (a subarray of the union is
inside the left, inside the right, or crosses the boundary). A query decomposes
`[l, r]` into `O(log n)` disjoint canonical nodes in left-to-right order; merging
them reconstructs the exact summary of `nums[l..r]`, whose `best` field is the
answer. The `IDENTITY` node (`best = -inf`, `total = 0`) is a neutral element:
merging it never introduces a spurious subarray and never adds to sums.

**Step by step on `nums = [-1, 2, 3, -5, 4]`, query `(0, 2)`:**

- Canonical nodes covering `[0, 2]` are `[0,1]` and `[2,2]`.
- `[0,1] = [-1, 2]`: `total = 1`, `best_prefix = max(-1, -1+2) = 1`,
  `best_suffix = max(2, 2+-1) = 2`, `best = max(-1, 2, (-1)+2) = 2`.
- `[2,2] = [3]`: all fields `3`.
- Merge: `best = max(2, 3, best_suffix(2) + best_prefix(3)) = max(2, 3, 5) = 5`. ✓

**Complexity.** Build `O(n)`, each query `O(log n)`, total `O(n + q log n)`. Space
`O(n)` for the tree. Point updates (change `nums[i]`) also cost `O(log n)`, which
is why this structure — not Kadane — is the standard answer when the array
changes between queries.

## Key Insights & Edge Cases

- **The merge IS the divide & conquer combine.** `L.best_suffix + R.best_prefix`
  is the crossing subarray; the whole segment tree is the recursion made
  persistent and query-able.
- **`merge` is not commutative** — the left range must sit to the left of the
  right range. In the iterative query, collect right-boundary nodes and merge them
  in reverse so order is preserved. Getting this wrong produces subtly wrong
  answers only on some ranges.
- **Non-empty subarray requirement** means the identity's `best` must be `-inf`
  (not `0`), so all-negative ranges like `[-3, -1]` correctly return `-1`, never
  an empty-subarray `0`.
- **`best_prefix`/`best_suffix` are what make composition work.** Storing only
  `best` would lose the information needed to compute crossing subarrays at higher
  levels.
- **Supports updates:** replace a leaf and re-`merge` up its `O(log n)` ancestors.
  This is the real reason to prefer the segment tree over repeated Kadane.
