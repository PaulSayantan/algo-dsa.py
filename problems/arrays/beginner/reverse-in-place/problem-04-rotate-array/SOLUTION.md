# Rotate Array — Solution

## Brute Force

Rotate one step at a time, `k` times. Each step pops the last element and inserts it at
the front.

```python
k %= len(nums)
for _ in range(k):
    last = nums.pop()          # O(1)
    nums.insert(0, last)       # O(n) shift
```

- **Time:** O(n * k) — each of the `k` rotations shifts up to `n` elements.
- **Space:** O(1). Correct, but far too slow for `n, k` up to 10^5.

An alternative brute force uses an extra array: `result[(i + k) % n] = nums[i]`, which
is O(n) time but O(n) space.

## Optimal Approach (Reverse In-Place)

Rotating right by `k` is equivalent to three reversals:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining `n - k` elements.

```python
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n                       # normalize; rotating by n is a no-op
    if k == 0:
        return

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)            # whole array
    reverse(0, k - 1)            # first k
    reverse(k, n - 1)            # last n - k
```

**Why it is correct:** After a full reverse, the last `k` elements (which belong at the
front) now occupy the front slots but in reversed order; the first `n - k` elements
occupy the back in reversed order. Reversing each of those two segments restores their
internal order, leaving exactly the right-rotated arrangement.

Worked example, `nums = [1,2,3,4,5,6,7]`, `k = 3`:
- Reverse all -> `[7,6,5,4,3,2,1]`
- Reverse first 3 -> `[5,6,7,4,3,2,1]`
- Reverse last 4 -> `[5,6,7,1,2,3,4]`  ✓

- **Time:** O(n) — three reversals, each linear; every element is swapped a constant
  number of times.
- **Space:** O(1) — only index variables.

## Key Insights & Edge Cases

- **Take `k %= n` first.** If `k >= n`, rotating by `k` is the same as rotating by
  `k mod n`; skipping this can index out of bounds or waste work.
- **`k == 0` (after mod):** the array is unchanged — returning early avoids redundant
  reversals.
- **The three-reversal identity** generalizes: reversing the whole then the pieces is
  the standard O(1)-space way to "swap two adjacent blocks" of an array.
- **In place:** every swap is done directly on `nums`, so no auxiliary array is needed.
