# Solution — Find Rotation Count in a Rotated Sorted Array

## Brute Force

Walk the array and return the index of the first element that is smaller than
its predecessor (the pivot). If no such drop exists, the array is unrotated and
the answer is `0`.

```python
def count_rotations(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return i
    return 0
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

Correct, but linear.

## Optimal Approach (Search in Rotated Sorted Array)

The number of clockwise rotations equals the **index of the minimum element**:
after `k` rotations the original first element has been pushed `k` slots to the
right, and the element that lands at index 0..k-1 are the old tail; the smallest
value ends up at index `k`. So this is exactly the pivot search from Problem 1 —
but we return the *index*, not the value.

Binary search over window `[lo, hi]`, comparing `nums[mid]` with `nums[hi]`:

- If `nums[mid] > nums[hi]`, the minimum is strictly to the right: `lo = mid + 1`.
- Otherwise the minimum is at `mid` or to its left: `hi = mid`.

When `lo == hi`, that index is both the minimum's position and the rotation
count.

```python
def count_rotations(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

**Why the index equals the rotation count.** Let the original sorted array be
`a`. After `k` clockwise rotations the array is
`[a[n-k], ..., a[n-1], a[0], ..., a[n-k-1]]`. The global minimum is `a[0]`,
which now occupies index `k`. Locating the minimum therefore recovers `k`
directly.

- **Time:** `O(log n)`.
- **Space:** `O(1)`.

### Step-by-step on `nums = [15,18,2,3,6,12]`

| lo | hi | mid | nums[mid] | nums[hi] | action |
|----|----|-----|-----------|----------|--------|
| 0  | 5  | 2   | 2         | 12       | `2 <= 12` -> hi = 2 |
| 0  | 2  | 1   | 18        | 2        | `18 > 2`  -> lo = 2 |

Now `lo == hi == 2`; the minimum `2` sits at index `2`, so the array was rotated
`2` times.

## Key Insights & Edge Cases

- **Return the index, not the value** — that is the only difference from
  "find minimum". A common mistake is returning `nums[lo]`.
- **Unrotated array (`k = 0`):** every `nums[mid] <= nums[hi]`, so `hi` slides to
  0 and the function returns `0` (Example 3).
- **Single element:** loop never runs, returns `0`.
- **Maximum rotation:** rotating an `n`-element array `n` times returns it to the
  original, so valid answers stay in `[0, n-1]`; the algorithm never returns `n`.
- **Distinctness** keeps the `nums[mid]` vs `nums[hi]` comparison unambiguous;
  with duplicates you would need the linear fallback (see Problem 5).
