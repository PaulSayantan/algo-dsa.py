# Solution — Count of Range Sum

## Brute Force

Enumerate every subarray, sum it, and test membership in `[lower, upper]`. Using
prefix sums to get each subarray sum in `O(1)` still leaves `O(n^2)` pairs.

- Time: `O(n^2)`.
- Space: `O(n)` for prefix sums (or `O(1)` if summed on the fly).

With `n` up to `10^5`, `n^2 = 10^10` — too slow.

## Optimal Approach (Order-Statistics Tree)

**Reduce to prefix sums.** Define `P[0] = 0` and `P[t] = nums[0] + ... + nums[t-1]`.
Then the subarray sum `S(i, j) = P[j+1] - P[i]` for `0 <= i <= j < n`. Renaming
`r = j+1` and `l = i`, a valid range sum corresponds to a pair `l < r` with:

```
lower <= P[r] - P[l] <= upper
  <=>  P[r] - upper <= P[l] <= P[r] - lower
```

So for each right endpoint `P[r]`, we must count how many **earlier** prefix sums
`P[l]` (`l < r`) lie in the interval `[P[r] - upper, P[r] - lower]`.

**Maintain the prefix sums in an OST.** Keep an order-statistics multiset of the
prefix sums seen so far, augmented with subtree `size`. A range-count over
`[lo, hi]` is two rank queries:

```
count_in_range(lo, hi) = count_le(hi) - count_lt(lo)
```

where
- `count_le(x)` = number of stored keys `<= x`, and
- `count_lt(x)` = number of stored keys `< x` (called `rank_less` in Problem 2).

```
count_le(node, x):                 # keys <= x
    if node is None:      return 0
    if x < node.key:      return count_le(node.left, x)
    return size(node.left) + node.count + count_le(node.right, x)

count_lt(node, x):                 # keys strictly < x
    if node is None:      return 0
    if x <= node.key:     return count_lt(node.left, x)
    return size(node.left) + node.count + count_lt(node.right, x)
```

**Algorithm.**
1. Insert `P[0] = 0` into the tree (the empty prefix, a valid left endpoint).
2. For `r = 1 .. n`: let `hi = P[r] - lower`, `lo = P[r] - upper`. Add
   `count_le(hi) - count_lt(lo)` to the answer, then insert `P[r]`.

**Correctness.** When processing `P[r]`, the tree holds exactly
`{P[0], ..., P[r-1]}` — all earlier prefix sums. `count_le(hi) - count_lt(lo)` counts
stored keys in `[lo, hi] = [P[r]-upper, P[r]-lower]`, i.e. earlier `P[l]` with
`lower <= P[r]-P[l] <= upper`. Each such `l < r` corresponds to a unique subarray
`nums[l .. r-1]` with sum in range, and every qualifying subarray is counted once at
its right endpoint. Inserting `P[r]` *after* querying prevents pairing `r` with
itself. The subtree-size augmentation makes both rank queries exact under the BST
invariant.

Reference (treap core from Problem 1; `count_le` / `count_lt` as above):

```python
class Solution:
    def countRangeSum(self, nums, lower, upper):
        root = insert(None, 0)     # P[0] = 0
        prefix = 0
        ans = 0
        for x in nums:
            prefix += x            # prefix == P[r]
            hi = prefix - lower
            lo = prefix - upper
            ans += count_le(root, hi) - count_lt(root, lo)
            root = insert(root, prefix)
        return ans
```

- Time: `O(n log n)` — one range-count (two `O(log n)` rank queries) and one insert
  per element.
- Space: `O(n)` — the tree holds `n + 1` prefix sums.

**Alternatives:** merge sort that counts qualifying pairs while merging prefix sums,
or a Fenwick / segment tree over the coordinate-compressed set of all prefix sums and
query bounds. The OST avoids the offline coordinate-compression step and reads
directly as "count earlier prefix sums in a window."

## Key Insights & Edge Cases

- **Seed with `P[0] = 0`.** Subarrays that start at index 0 correspond to `l = 0`;
  forgetting to insert the empty-prefix `0` undercounts them. In example 2,
  `nums = [0]`: after inserting `P[0]=0`, `P[1]=0`, query window `[0-0, 0-0]=[0,0]`
  contains the stored `0`, giving the single valid range sum `S(0,0)=0`.
- **64-bit prefix sums.** With `n` up to `10^5` and `|nums[i]|` up to `2^31 - 1`,
  prefix sums can reach `~2^46`, overflowing 32-bit ints. Python is safe natively; in
  C++/Java use `long long`/`long`. The bounds `P[r]-lower` and `P[r]-upper` must use
  the same wide type.
- **Inclusive interval.** The window `[P[r]-upper, P[r]-lower]` is inclusive at both
  ends; that is why the count is `count_le(hi) - count_lt(lo)` (include `hi`, exclude
  everything below `lo`).
- **Query before insert.** Insert `P[r]` only after counting, so a prefix sum is
  never matched against itself (which would fabricate an empty/zero-length range).
- **Duplicate prefix sums.** Repeated prefix-sum values are common (e.g. runs summing
  to 0); a `count` per key ensures they are all counted, not collapsed.
- **All valid / none valid.** If every range sum lies in `[lower, upper]` the answer
  is `n(n+1)/2`; if none do, it is `0`. The method handles both without special
  casing.
