# Solution — Count of Smaller Numbers After Self

## Brute Force

For every `i`, scan all `j > i` and count `nums[j] < nums[i]`. This is a double
loop: `O(n^2)` time, `O(1)` extra space (besides output). For `n = 10^5` that is
`10^10` operations — too slow.

The textbook `O(n log n)` solutions are a modified **merge sort** (count
inversions while merging) or a **Fenwick/BIT over compressed values** processed
right-to-left. Both are standard. The Wavelet Tree gives an alternative
`O(n log sigma)` solution that also generalizes to arbitrary range windows, not
just suffixes.

## Optimal Approach (Wavelet Tree)

### Reduction

`counts[i]` asks: among the suffix `nums[i+1 .. n)`, how many values are
**strictly less** than `nums[i]`? That is exactly

```
counts[i] = rangeCountLeq(i + 1, n, nums[i] - 1)
```

a range "count of values `<= x`" query with `x = nums[i] - 1` (see Problem 2).

### Algorithm

1. **Build** a Wavelet Tree over the entire `nums` once: `O(n log sigma)`.
2. For each `i` from `0` to `n-1`, answer
   `rangeCountLeq(i + 1, n, nums[i] - 1)` in `O(log sigma)`.
3. Total: `O(n log sigma)` time, `O(n log sigma)` space.

```python
class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        wt = WaveletTree(nums)            # supports rangeCountLeq(l, r, x)
        return [wt.range_count_leq(i + 1, n, nums[i] - 1) for i in range(n)]
```

`range_count_leq` is the routine from Problem 2: route the window `[i+1, n)` down
the tree; at a node with `mid`, if the threshold `x >= mid` add the whole left
count and recurse right, else recurse left. `O(log sigma)` per call.

### Why it is correct

The suffix `[i+1, n)` contains exactly the elements "to the right" of index `i`.
"Strictly smaller than `nums[i]`" is equivalent to "value `<= nums[i] - 1`" for
integer data. The Wavelet Tree's `rangeCountLeq` counts precisely those, so each
`counts[i]` is computed directly. Because the query is by **position window** and
**value threshold** simultaneously, no ordering/processing tricks are needed —
one static build serves all indices.

**Complexity:** `O(n log sigma)` time, `O(n log sigma)` space (or `O(log n)` per
query after coordinate compression).

## Key Insights & Edge Cases

- **Strict `<` vs `<=`**: use `x = nums[i] - 1` for integer values so ties
  (`nums[j] == nums[i]`) are excluded. Duplicates like `[-1, -1]` then correctly
  yield `0`.
- **Last element** (`i = n - 1`): the window `[n, n)` is empty → `0`. Make sure
  `range_count_leq` returns `0` on an empty window.
- **Negative values**: coordinate-compress (or offset by `-min`) before building
  so the alphabet starts at `0`; the query value `nums[i] - 1` must be mapped on
  the *same* scale. Comparing on the raw value scale inside the tree (comparing
  `x` against raw `mid`) also works and avoids the "threshold between two present
  values" pitfall.
- **Single element** input → `[0]`.
- Because `-10^4 <= nums[i] <= 10^4`, even without compression `sigma <= 20001`,
  so `log sigma <= 15` — comfortably fast.
- The Fenwick-tree solution is simpler to code for this *specific* suffix
  variant; choose the Wavelet Tree when you also need arbitrary `[l, r)` windows
  or k-th-smallest on the same data.
