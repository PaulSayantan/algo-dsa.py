# Solution — Reverse Pairs

## Brute Force

Check every pair `(i, j)` with `i < j` and count those with
`nums[i] > 2 * nums[j]`.

```python
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] > 2 * nums[j]:
            count += 1
```

- **Time:** `O(n^2)` — too slow for `n = 5 * 10^4` (`~1.25 * 10^9` comparisons).
- **Space:** `O(1)`.

## Optimal Approach (Merge Sort with a separate counting pass)

As with inversions, a reverse pair `(i, j)` is either within the left half, within
the right half, or **split** (`i` in left, `j` in right). Recursion handles the
first two; we count split pairs during the merge.

The subtlety versus inversion counting: the counting comparison is
`left[i] > 2 * right[j]`, but the *merge ordering* comparison is
`left[i] <= right[j]`. Because `x > 2y` is not the same predicate as `x > y`, you
**cannot** count while you merge with a single pointer. Do it in **two passes**:

1. **Count pass.** With both halves sorted, use two pointers. For each left
   element `left[i]`, advance `j` over the right half while
   `left[i] > 2 * right[j]`. Every such `right[j]` forms a reverse pair with
   `left[i]` — and, crucially, with every later left element too, since the left
   half is sorted ascending. So `j` only ever moves forward across the whole left
   scan, giving a linear pass.
2. **Merge pass.** Merge `left` and `right` normally into sorted order.

```python
def reversePairs(self, nums):
    def sort(lo, hi):                 # sorts nums[lo:hi], returns reverse-pair count
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        count = sort(lo, mid) + sort(mid, hi)

        # --- count pass ---
        j = mid
        for i in range(lo, mid):
            while j < hi and nums[i] > 2 * nums[j]:
                j += 1
            count += j - mid

        # --- merge pass ---
        nums[lo:hi] = sorted(nums[lo:hi])   # or a manual two-pointer merge
        return count

    return sort(0, len(nums))
```

(For a from-scratch merge, replace the `sorted(...)` line with an explicit
two-pointer merge of `nums[lo:mid]` and `nums[mid:hi]`.)

**Why it is correct.** In the count pass both halves are sorted. Fix `i`; the set
of right-half elements with `nums[i] > 2 * nums[j]` is a **prefix** of the right
half (since it is sorted ascending, if `nums[i] > 2*nums[j]` fails for some `j` it
fails for all larger `j`). Because the left half is also sorted ascending, that
prefix only grows as `i` increases, so the pointer `j` never resets — total work
is `O(size)`. Adding `j - mid` for each `i` counts exactly the split reverse pairs.
Recursion adds the within-half counts, and every reverse pair is counted once at
the level where `i` and `j` first separate into different halves. The subsequent
merge restores the sorted order that the parent call relies on.

**Complexity.**

- **Time:** `O(n log n)` — two linear passes per merge, `log n` levels.
- **Space:** `O(n)` for merging plus `O(log n)` recursion.

### Worked trace on `[2,4,3,5,1]`

The decisive split compares a sorted left group against a sorted right group that
contains `1`. Left values `4`, `3`, and `5` each satisfy `x > 2 * 1 = 2`, so the
count pass credits `3` split pairs (`(1,4)`, `(2,4)`, `(3,4)` in original
indices); value `2` does not (`2 > 2` is false). Within-half counts contribute
`0`, giving the final answer `3`.

## Key Insights & Edge Cases

- **Two passes, not one.** Counting uses `nums[i] > 2 * nums[j]`; merging uses the
  natural order. Trying to fuse them (as in inversion counting) gives wrong
  answers because the two predicates differ.
- **Pointer `j` does not reset** across the left scan — that is what keeps the
  count pass `O(n)` per merge rather than `O(n^2)`.
- **Overflow:** `2 * nums[j]` can exceed 32-bit range; in Java/C++ cast to `long`
  (compare `nums[i] > 2L * nums[j]`). Python is safe.
- **Strict inequality** (`>`, not `>=`): equal boundary values like `nums[i] == 2 *
  nums[j]` are **not** reverse pairs.
- **Sorted ascending, positive input:** answer is `0` (Example 3), a good check.
- Negative numbers work without special handling, but keep the arithmetic in a
  wide integer type in non-Python languages.
