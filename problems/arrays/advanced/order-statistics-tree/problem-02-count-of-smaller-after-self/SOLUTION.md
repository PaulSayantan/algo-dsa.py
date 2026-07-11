# Solution — Count of Smaller Numbers After Self

## Brute Force

For every index `i`, scan all indices `j > i` and count how many satisfy
`nums[j] < nums[i]`.

- Time: `O(n^2)`.
- Space: `O(1)` extra (besides the output).

With `n` up to `10^5`, `n^2 = 10^10` — far too slow.

## Optimal Approach (Order-Statistics Tree)

Process the array **from right to left**, maintaining an order-statistics multiset
of all elements already visited (which are exactly the elements to the *right* of
the current index). For each `nums[i]`:

1. **Query** `rank(nums[i])` = number of stored keys **strictly less than**
   `nums[i]`. This is the answer for index `i`, because every stored key sits to the
   right of `i`.
2. **Insert** `nums[i]` into the multiset so it is available for indices further
   left.

Both steps are `O(log n)` on a balanced OST, giving `O(n log n)` total.

**The rank query.** Store subtree `size` at each node (`size = count + size(left) +
size(right)`, duplicates counted). To count keys strictly less than `x`:

```
rank_less(node, x):
    if node is None:        return 0
    if x <= node.key:       return rank_less(node.left, x)      # x is small: go left only
    # node.key < x: the whole left subtree AND this node's copies are < x
    return size(node.left) + node.count + rank_less(node.right, x)
```

The `x <= node.key` test (rather than `<`) is what makes the count **strict**: equal
keys are *not* counted as smaller, which is exactly why example 2 (`[-1, -1]`) yields
`[0, 0]`.

**Correctness.** When we reach index `i`, the multiset contains precisely
`{nums[i+1], ..., nums[n-1]}` (everything to the right, and nothing else, because we
insert only after querying). `rank_less` sums, along the search path for `x`, the
subtree sizes plus node counts of every key that is `< x`, using the BST invariant
that a node's left subtree holds only smaller keys. Hence it returns the exact number
of already-inserted (right-side) elements smaller than `nums[i]`.

Reference (treap core; `insert`/`_upd`/rotations as in Problem 1):

```python
def rank_less(n, x):
    if n is None: return 0
    if x <= n.key: return rank_less(n.left, x)
    return _sz(n.left) + n.count + rank_less(n.right, x)

class Solution:
    def countSmaller(self, nums):
        root = None
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            res[i] = rank_less(root, nums[i])
            root = insert(root, nums[i])
        return res
```

- Time: `O(n log n)` expected (treap) or worst case (AVL / red-black).
- Space: `O(n)` for the tree.

**Alternatives:** a merge-sort that counts inversions while merging, or a Fenwick
tree over coordinate-compressed values, both achieve `O(n log n)`. The OST is the
natural "online" framing and is what generalizes to the harder problems in this
folder.

## Key Insights & Edge Cases

- **Direction matters.** Scanning right to left makes the invariant "the multiset =
  elements to the right" hold automatically. Query *before* inserting the current
  element so it never counts itself.
- **Strictly smaller.** Use `x <= node.key -> go left` so equal keys are excluded;
  `[-1, -1] -> [0, 0]` is the guard test.
- **Negative values.** Keys can be negative; the BST comparisons work unchanged (no
  need to shift into non-negative range as a Fenwick approach would).
- **Single element / all equal.** A length-1 array returns `[0]`; an all-equal array
  returns all zeros since no element to the right is strictly smaller.
- **Large range, sparse values.** Because the OST keys on actual values, the value
  range (`-10^4..10^4`) does not need compression; memory is `O(n)` in the number of
  elements, not the value span.
