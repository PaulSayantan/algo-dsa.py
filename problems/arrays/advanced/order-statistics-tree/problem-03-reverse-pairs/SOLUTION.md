# Solution — Reverse Pairs

## Brute Force

Check every pair `(i, j)` with `i < j` and test `nums[i] > 2 * nums[j]`.

- Time: `O(n^2)`.
- Space: `O(1)`.

With `n` up to `5 * 10^4`, that is `~2.5 * 10^9` comparisons — too slow.

## Optimal Approach (Order-Statistics Tree)

Scan **left to right**, maintaining an order-statistics multiset of the elements seen
so far (all with index `< j`). For each new element `nums[j]`:

1. **Count** stored keys that are strictly greater than `2 * nums[j]`. Every such
   stored key sits at some index `i < j` with `nums[i] > 2 * nums[j]`, i.e. a reverse
   pair ending at `j`. Add this to the running total.
2. **Insert** `nums[j]` so it can pair with future elements.

Both operations are `O(log n)`, for `O(n log n)` total.

**The "greater than threshold" count.** With subtree `size` at each node, count keys
`> t` as `n - (keys <= t)`. It is cleanest to compute `count_le(t)` (keys `<= t`) and
subtract from the current tree size:

```
count_le(node, t):
    if node is None:      return 0
    if t < node.key:      return count_le(node.left, t)     # t below this key
    # node.key <= t: left subtree and this node's copies are all <= t
    return size(node.left) + node.count + count_le(node.right, t)

greater_than(root, t) = size(root) - count_le(root, t)
```

For a new element `x = nums[j]`, the threshold is `t = 2 * x` and we want keys
strictly greater than `t`, so `answer_j = size(root) - count_le(root, 2*x)`.

**Correctness.** When we process index `j`, the tree holds exactly
`{nums[0], ..., nums[j-1]}`. `count_le(root, 2*nums[j])` returns the number of those
earlier elements that are `<= 2*nums[j]`; subtracting from the total count of earlier
elements yields those strictly `> 2*nums[j]`, which is precisely the number of `i<j`
forming a reverse pair with `j`. Summing over all `j` counts every reverse pair
exactly once (each pair is counted when its larger-indexed member `j` is processed).
The BST invariant guarantees a node's left subtree holds only smaller keys, so the
size sums along the search path are exact.

**Watch the overflow / comparison boundary.** `2 * nums[j]` can exceed 32-bit range
(`nums[j]` up to `2^31 - 1`), so use 64-bit / arbitrary-precision arithmetic (Python
handles this natively; in C++/Java cast to `long`). Also note the strict `>`: an
element equal to `2 * nums[j]` is **not** a reverse pair, which is why `count_le`
uses `<=` (inclusive) and we subtract it.

Reference (treap core from Problem 1):

```python
def count_le(n, t):
    if n is None: return 0
    if t < n.key: return count_le(n.left, t)
    return _sz(n.left) + n.count + count_le(n.right, t)

class Solution:
    def reversePairs(self, nums):
        root = None
        total = 0
        for x in nums:
            if root is not None:
                total += root.size - count_le(root, 2 * x)  # keys strictly > 2x
            root = insert(root, x)
        return total
```

- Time: `O(n log n)`.
- Space: `O(n)`.

**Alternatives:** the standard editorial uses a modified merge sort that counts,
during the merge of two sorted halves, pairs with `left[i] > 2*right[j]`; a Fenwick
tree over coordinate-compressed values also works. The OST version needs no
compression and reads directly as "count elements above a scaled threshold."

## Key Insights & Edge Cases

- **Threshold scaling.** The query is not "greater than `nums[j]`" but "greater than
  `2 * nums[j]`." Keep the tree keyed on raw values and only scale the *query*
  threshold; do not store doubled values.
- **64-bit arithmetic.** `2 * nums[j]` overflows 32-bit ints for large positive
  `nums[j]`, and negative values double downward too — compute the threshold in a
  wide type.
- **Strict inequality.** `nums[i] > 2*nums[j]` is strict, so use `count_le` (keys
  `<=` threshold) and subtract; equality must not count.
- **Direction.** Left-to-right keeps "stored keys have smaller index," so a match is
  always a valid `(i, j)` with `i < j`. Querying before inserting avoids pairing an
  element with itself.
- **Length 0 or 1.** No pair exists; the loop naturally returns `0` (guard the query
  when the tree is empty, as shown).
- **Duplicates and negatives** are handled by `count` per key and ordinary signed
  comparisons; e.g. `[1,3,2,3,1]` correctly yields `2`.
