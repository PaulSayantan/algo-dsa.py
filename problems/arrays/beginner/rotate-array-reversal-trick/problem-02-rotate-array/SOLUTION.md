# Rotate Array — Solution

## Brute Force

Rotate one step at a time, `k` times. Each single rotation saves the last
element, shifts everything right by one, and places the saved element at index
0.

```python
for _ in range(k % n):
    last = nums[-1]
    for i in range(n - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = last
```

- **Time:** O(n · k) — up to `n` shifts per rotation, `k` rotations. TLE for
  large inputs.
- **Space:** O(1).

An alternative brute force uses an auxiliary array: place each element at
`(i + k) % n` in a copy, then copy back — that is O(n) time but **O(n) space**,
which violates the follow-up.

## Optimal Approach — The Reversal Trick

Think of the array as two blocks: `A = nums[0 .. n-k-1]` and
`B = nums[n-k .. n-1]`. A right rotation by `k` transforms `A · B` into `B · A`.
Three in-place reversals accomplish exactly that.

```python
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n                      # normalize; rotating by n is a no-op

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)           # reverse everything
    reverse(0, k - 1)           # reverse the first k
    reverse(k, n - 1)           # reverse the remaining n - k
```

### Why it is correct

Let the array be `A · B` where `B` is the last `k` elements. Using the identity
`reverse(A · B) = reverse(B) · reverse(A)`:

1. `reverse(0, n-1)` turns `A · B` into `reverse(B) · reverse(A)`.
2. `reverse(0, k-1)` reverses the first block `reverse(B)` back into `B`.
3. `reverse(k, n-1)` reverses the second block `reverse(A)` back into `A`.

The result is `B · A` — precisely the array rotated right by `k`.

Worked example, `nums = [1,2,3,4,5,6,7]`, `k = 3`:

```
start:            1 2 3 4 5 6 7
reverse all:      7 6 5 4 3 2 1
reverse first 3:  5 6 7 4 3 2 1
reverse last 4:   5 6 7 1 2 3 4   <-- rotated right by 3
```

### Complexity

- **Time:** O(n) — three passes, each element swapped at most twice total.
- **Space:** O(1) — all work is done in place with a two-pointer reverse.

## Key Insights & Edge Cases

- **Always take `k %= n` first.** Without it, `reverse(0, k-1)` can run out of
  bounds or do redundant work when `k >= n`. Example 3 (`k = 3, n = 2`) relies
  on this: `k` becomes `1`.
- **`k % n == 0`:** the array is unchanged. The three reversals still run
  (`reverse(0, n-1)` then `reverse(0, -1)` which is a no-op, then
  `reverse(0, n-1)` again), netting the original array — correct, though you may
  early-return for clarity.
- **Single element:** `n == 1` ⇒ `k %= 1 == 0`, no change.
- **Left rotation variant:** to rotate *left* by `k`, either rotate right by
  `n - k`, or swap the split point: reverse first `k`, reverse last `n - k`,
  then reverse the whole array.
- The trick generalizes the "swap two adjacent blocks" operation — rotation is
  just the special case where the blocks are `A` and `B`.
