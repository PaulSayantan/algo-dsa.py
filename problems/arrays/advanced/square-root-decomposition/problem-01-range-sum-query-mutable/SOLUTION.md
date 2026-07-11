# Range Sum Query - Mutable — Solution

## Brute Force

Store the array as-is.

- `update(index, val)` overwrites `nums[index]` in `O(1)`.
- `sumRange(left, right)` loops from `left` to `right` and adds, in `O(n)`.

```python
class NumArray:
    def __init__(self, nums):
        self.nums = nums[:]
    def update(self, index, val):
        self.nums[index] = val
    def sumRange(self, left, right):
        return sum(self.nums[left:right + 1])
```

With up to `3 * 10^4` queries over an array of `3 * 10^4` elements, the query
cost is `O(q * n) ≈ 9 * 10^8` in the worst case — too slow.

A prefix-sum array gives `O(1)` queries but makes every `update` cost `O(n)` to
rebuild the affected suffix, so it just moves the bottleneck. We want something
that balances **both** operations.

## Optimal Approach (Square Root Decomposition)

Partition the array into contiguous **blocks** of size
`b = ceil(sqrt(n))` (any value near `sqrt(n)` works). There are about
`n / b ≈ sqrt(n)` blocks. Maintain an auxiliary array `block_sum[k]` holding the
sum of every element in block `k`, where element `i` belongs to block
`i // b`.

**Build** — walk the array once, accumulating each element into its block's
sum: `O(n)`.

**update(index, val)** — the value at `index` changes by
`delta = val - nums[index]`. Update the element and add `delta` to the single
block that contains it:

```python
def update(self, index, val):
    delta = val - self.nums[index]
    self.nums[index] = val
    self.block_sum[index // self.b] += delta
```

Only one block sum changes, so this is `O(1)`.

**sumRange(left, right)** — split the range into three parts:

1. A possibly-partial **left block**: add elements one by one from `left` up to
   the end of its block (or `right`, whichever comes first).
2. Zero or more **whole blocks** strictly inside the range: add their
   `block_sum` values directly instead of iterating their elements.
3. A possibly-partial **right block**: add elements one by one.

```python
def sumRange(self, left, right):
    b = self.b
    lb, rb = left // b, right // b
    total = 0
    if lb == rb:                        # range fits in one block
        for i in range(left, right + 1):
            total += self.nums[i]
        return total
    for i in range(left, (lb + 1) * b):  # partial left block
        total += self.nums[i]
    for k in range(lb + 1, rb):          # whole interior blocks
        total += self.block_sum[k]
    for i in range(rb * b, right + 1):   # partial right block
        total += self.nums[i]
    return total
```

**Why it is correct.** Every index in `[left, right]` is counted exactly once:
the two partial loops cover the indices in the boundary blocks that fall inside
the range, and the middle loop covers every index of each fully-contained block
via its precomputed sum. `block_sum[k]` is kept in sync with `nums` by `update`,
so the precomputed values always equal the true block totals.

**Complexity.** The two partial loops touch fewer than `b` elements each, and
the interior loop touches fewer than `n / b` blocks. Choosing `b ≈ sqrt(n)`
balances these to `O(sqrt(n))` per query and `O(1)` per update. Total for `q`
mixed operations: `O(n + q * sqrt(n))`. Space is `O(n + sqrt(n)) = O(n)`.

## Key Insights & Edge Cases

- **Block size choice.** `sqrt(n)` minimizes `b + n/b`. Any nearby value keeps
  the asymptotics; `int(math.sqrt(n)) + 1` is a safe integer choice that avoids
  a zero block size.
- **Single-block ranges.** When `left` and `right` land in the same block there
  are no whole interior blocks, so handle that case with one direct loop to
  avoid double counting the boundary.
- **update must use a delta,** not overwrite the block sum: recomputing the
  whole block would cost `O(sqrt(n))` per update instead of `O(1)`.
- **Negative values** need no special handling — sums are ordinary integers.
- **Off-by-one:** the interior block range is `[lb + 1, rb)` (exclusive on both
  the boundary blocks) precisely because those two blocks are handled
  element-by-element.
- A Binary Indexed Tree / Segment Tree solves this in `O(log n)` per operation,
  which is asymptotically better; sqrt decomposition is chosen here for its
  simplicity and because it generalizes to operations that trees cannot batch.
