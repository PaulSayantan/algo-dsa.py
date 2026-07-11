# Move Zeroes — Solution

## Brute Force

Create a new list of all the non-zero elements, pad it with the right number of
zeros, and copy it back.

```python
def moveZeroes(nums):
    non_zero = [x for x in nums if x != 0]
    zeros = len(nums) - len(non_zero)
    nums[:] = non_zero + [0] * zeros
```

- **Time:** O(n).
- **Space:** O(n) for `non_zero` — violates the "no copy of the array" rule.

## Optimal Approach (Two Pointers, same direction)

This is a **stable partition**: keep the non-zeros in order at the front and let
the zeros fall to the back. Use a writer pointer to place non-zeros.

- `write` — the index where the next non-zero element belongs. Everything in
  `nums[0 .. write-1]` is a non-zero in original order.
- `read` — scans every index.

**Pass 1** copies each non-zero forward:

```python
def moveZeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    # Pass 2: fill the remainder with zeros.
    for i in range(write, len(nums)):
        nums[i] = 0
```

After pass 1, `nums[0 .. write-1]` holds every non-zero in order. The tail
`nums[write .. n-1]` is then set to `0`.

### One-pass swap variant

You can merge both passes by swapping the reader's non-zero into the writer slot,
which places zeros at the back automatically:

```python
def moveZeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
```

Because `write <= read`, when they differ the writer always points at a zero, so
the swap moves a non-zero forward and carries a zero back — order preserved.

### Why it is correct

**Invariant:** after processing index `read`, `nums[0 .. write-1]` contains, in
order, all non-zero elements from `nums[0 .. read-1]`. Each non-zero extends this
prefix by one; zeros are skipped (copy version) or exchanged out to the reader's
old spot (swap version). Since `write <= read`, we never overwrite an unread
value.

### Complexity

- **Time:** O(n) — one or two linear passes.
- **Space:** O(1) — index variables only.

## Key Insights & Edge Cases

- **Stability matters:** the problem demands non-zero order be preserved, which
  is exactly what the forward-copy / swap partition guarantees. A "swap zero with
  the last element" trick would be O(n) too but would scramble order.
- **All zeros** (`[0, 0, 0]`): `write` stays `0`, pass 2 rewrites zeros — result
  unchanged, correct.
- **No zeros:** every element copies/swaps onto itself; array unchanged.
- **Single element:** trivially correct for both `[0]` and `[5]`.
- **Swap variant minimizes writes** when zeros are rare, but performs a
  self-swap on leading non-zeros unless you add a `read != write` guard.
