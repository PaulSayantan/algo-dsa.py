# Solution - Two Sum II - Input Array Is Sorted

## Brute Force

Try every pair `(i, j)` with `i < j` and check whether `numbers[i] + numbers[j] == target`.

```python
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
```

- **Time:** O(n^2) — every pair is examined.
- **Space:** O(1).

This ignores the fact that the array is already sorted, which is the key gift here.

## Optimal Approach (Two-Pointer on Sorted Sums)

Because the array is **sorted in non-decreasing order**, we can find the pair in a
single linear scan with two pointers.

### The invariant

Keep `lo` at the start and `hi` at the end. At all times the true answer pair (if
it still exists) lies within the window `[lo, hi]`. Consider `s = numbers[lo] + numbers[hi]`:

- If `s == target` we found it — return the 1-based indices `[lo + 1, hi + 1]`.
- If `s < target` the sum is too small. `numbers[hi]` is the largest value we could
  pair with `numbers[lo]`; since even that is not enough, `numbers[lo]` can never be
  part of the answer. Safely discard it: `lo += 1`.
- If `s > target` the sum is too large. `numbers[lo]` is the smallest value we could
  pair with `numbers[hi]`; since even that overshoots, `numbers[hi]` can never be
  part of the answer. Discard it: `hi -= 1`.

Each step eliminates one element while never discarding a member of the unique
solution, so the window shrinks by one per iteration and the answer is guaranteed
to be found before the pointers cross.

### Reference implementation

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo + 1, hi + 1]
            elif s < target:
                lo += 1
            else:
                hi -= 1
        return []  # unreachable: a solution is guaranteed
```

### Why it is correct

The "discard" argument above is the loop invariant. When `s < target`, no pair
using `numbers[lo]` can reach `target` (its best partner `numbers[hi]` already
falls short), so removing `lo` from consideration preserves the answer. The
symmetric argument holds for `s > target`. Since exactly one solution exists, the
pointers must meet it before crossing.

- **Time:** O(n) — each pointer moves inward at most `n` times total.
- **Space:** O(1) — two integer pointers, meeting the constant-space requirement.

## Key Insights & Edge Cases

- **Return 1-based indices.** Add 1 to each pointer; forgetting this is the most
  common bug on this problem.
- **`lo < hi`, never `<=`** — the two numbers must be at distinct positions; you may
  not use the same element twice.
- **Negative numbers are fine.** The monotonic-move argument only relies on the
  array being sorted, not on the sign of values.
- **No hash map needed.** The sorted input is precisely what lets us drop the O(n)
  extra space that classic Two Sum requires — this is the base case of the whole
  k-Sum two-pointer family.
