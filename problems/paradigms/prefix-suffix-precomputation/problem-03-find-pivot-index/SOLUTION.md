# Solution — Find Pivot Index

## Brute Force

For each candidate index `i`, sum everything to its left and everything to its
right, then compare.

```python
def pivotIndex(nums):
    n = len(nums)
    for i in range(n):
        left = sum(nums[:i])
        right = sum(nums[i + 1:])
        if left == right:
            return i
    return -1
```

- **Time:** O(n^2) — each of the `n` indices recomputes the two partial sums from
  scratch.
- **Space:** O(1) extra.

## Optimal Approach (Prefix + Total)

Compute the **total** of the array once. As you scan left to right, keep a running
**left sum** (the prefix sum of everything strictly before `i`). The right sum at
index `i` is then whatever remains after removing the left part and `nums[i]` itself:

```
right(i) = total - left(i) - nums[i]
```

Index `i` is a pivot exactly when `left(i) == right(i)`, i.e.

```
left == total - left - nums[i]
```

```python
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        # right sum = total - left - x
        if left == total - left - x:
            return i
        left += x          # extend the prefix to include index i
    return -1
```

**Why it is correct.** By construction `left` always holds the sum of
`nums[0..i-1]` when we test index `i` (it is updated *after* the check). The
remaining elements are the array total minus that left prefix minus the current
element, which is precisely the right sum. Scanning left to right and returning on
the first match guarantees the **leftmost** pivot.

**Step by step** on `[1, 7, 3, 6, 5, 6]`, `total = 28`:

| i | nums[i] | left (before) | right = 28 - left - nums[i] | pivot? |
|---|---------|---------------|-----------------------------|--------|
| 0 | 1       | 0             | 27                          | no |
| 1 | 7       | 1             | 20                          | no |
| 2 | 3       | 8             | 17                          | no |
| 3 | 6       | 11            | 11                          | **yes → return 3** |

- **Time:** O(n) — one pass for the total, one pass to scan.
- **Space:** O(1) — just two integers (`total`, `left`).

## Key Insights & Edge Cases

- The trick `right = total - prefix - nums[i]` is the invertible-operation shortcut:
  instead of maintaining an explicit suffix-sum array, derive the suffix value from
  the total and the prefix. This drops space from O(n) to O(1).
- **Update `left` after the comparison**, not before — otherwise `left` would already
  include `nums[i]` and the equation breaks.
- Edge indices work automatically: at `i = 0`, `left = 0` (empty left side); at the
  last index, `right = total - left - nums[i] = 0` (empty right side).
- Negative numbers are allowed, so an early index can be a pivot even when later
  elements are large — always return the first match.
- A single-element array returns `0`: left and right are both empty sums (`0 == 0`).
