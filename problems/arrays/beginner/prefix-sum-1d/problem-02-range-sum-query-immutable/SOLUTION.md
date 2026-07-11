# Solution — Range Sum Query - Immutable

## Brute Force

Store `nums` as-is. For each `sumRange(left, right)`, loop and add the elements.

```python
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total
```

- **Time:** O(1) construction, but O(n) per query. With `q` queries that is
  O(n * q), which is too slow when both are ~10^4.
- **Space:** O(1) extra.

## Optimal Approach (Prefix Sum, 1D)

Build a prefix array **once** in the constructor using the length-`n+1`
convention with a leading zero:

```
prefix[0] = 0
prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
```

Then the inclusive sum of `[left, right]` is:

```
sumRange(left, right) = prefix[right + 1] - prefix[left]
```

Reference implementation:

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

**Why it is correct:** `prefix[right + 1]` is the sum of `nums[0..right]` and
`prefix[left]` is the sum of `nums[0..left-1]`. Subtracting removes exactly the
elements before `left`, leaving `nums[left] + ... + nums[right]`. The leading
`0` at `prefix[0]` makes `left = 0` work without a special case, since
`prefix[left] = prefix[0] = 0`.

**Step by step** for `nums = [-2, 0, 3, -5, 2, -1]`:

```
prefix = [0, -2, -2, 1, -4, -2, -3]
          |   |   |  |   |   |   |
index     0   1   2  3   4   5   6

sumRange(0, 2) = prefix[3] - prefix[0] = 1 - 0     = 1
sumRange(2, 5) = prefix[6] - prefix[2] = -3 - (-2) = -1
sumRange(0, 5) = prefix[6] - prefix[0] = -3 - 0    = -3
```

- **Time:** O(n) construction, O(1) per query, O(n + q) overall.
- **Space:** O(n) for the prefix array.

## Key Insights & Edge Cases

- The `n + 1` sized prefix array with `prefix[0] = 0` is the cleanest convention:
  it removes the "what if the range starts at 0?" branch entirely.
- If you instead use an inclusive prefix (`P[i] = nums[0..i]`), the query becomes
  `P[right] - P[left-1]` and you must special-case `left == 0`. Both work; the
  half-open version is less error-prone.
- **Single-element range** (`left == right`) returns `nums[left]`, since
  `prefix[left+1] - prefix[left] == nums[left]`.
- The array is immutable, so precomputation is a pure win. If updates were
  allowed (see LeetCode 307), a plain prefix array would need O(n) per update
  and you'd move to a Fenwick tree or segment tree instead.
