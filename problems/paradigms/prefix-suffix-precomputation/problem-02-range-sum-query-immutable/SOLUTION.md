# Solution — Range Sum Query - Immutable

## Brute Force

Store the array. For each `sumRange(left, right)`, loop from `left` to `right`
adding elements.

```python
class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right + 1])   # O(right - left + 1) per call
```

- **Construction:** O(1).
- **Each query:** O(n) in the worst case.
- **`q` queries:** O(n * q) — with `n` and `q` both up to `10^4`, that is up to
  `10^8` operations. Too slow when queries repeat.

## Optimal Approach (Prefix Precomputation)

Precompute an **exclusive** prefix-sum array once, in the constructor:

```
prefix[0] = 0
prefix[i] = nums[0] + nums[1] + ... + nums[i-1]     (i = 1 .. n)
```

`prefix` has length `n + 1`. The sum of the inclusive range `[left, right]` is then

```
sumRange(left, right) = prefix[right + 1] - prefix[left]
```

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

**Why it is correct.** `prefix[right + 1]` is the sum of `nums[0..right]` and
`prefix[left]` is the sum of `nums[0..left-1]`. Subtracting removes exactly the
elements before `left`, leaving `nums[left] + ... + nums[right]`. The extra leading
zero (`prefix[0] = 0`) makes `left == 0` work without a special case, since
`prefix[right+1] - prefix[0] = prefix[right+1]`.

**Step by step** for `nums = [-2, 0, 3, -5, 2, -1]`:

```
prefix = [0, -2, -2, 1, -4, -2, -3]
          ^  ^   ^   ^  ^   ^   ^
          |  -2  -2  1  -4  -2  -3   (cumulative)
index     0   1   2  3   4   5   6
```

- `sumRange(0, 2) = prefix[3] - prefix[0] = 1 - 0 = 1`
- `sumRange(2, 5) = prefix[6] - prefix[2] = -3 - (-2) = -1`
- `sumRange(0, 5) = prefix[6] - prefix[0] = -3 - 0 = -3`

- **Construction:** O(n) time, O(n) space.
- **Each query:** O(1) time.
- **Total for `q` queries:** O(n + q).

## Key Insights & Edge Cases

- The **exclusive** prefix array of length `n + 1` with a leading `0` is the cleanest
  convention: it eliminates the `left == 0` special case that an inclusive prefix
  array would need.
- Off-by-one is the classic bug. Memorize `prefix[right + 1] - prefix[left]`; note the
  `+1` sits on `right`, not on `left`.
- Because the subtraction relies on invertibility of addition, this exact trick works
  for sums, products (with care about zeros), and XOR — but **not** for `min`/`max`,
  which need a different structure (sparse table / segment tree).
- This is the "immutable" version. If the array could be *updated* between queries, a
  static prefix array would need O(n) rebuilds; you would switch to a Fenwick
  (Binary Indexed) tree or a segment tree.
