# Squares of a Sorted Array — Solution

## Brute Force

Square every element, then sort the result.

```python
return sorted(x * x for x in nums)
```

- **Time:** `O(n log n)` dominated by the sort.
- **Space:** `O(n)` for the output (plus sort overhead).

Correct and short, but it throws away the input's existing order. We can do
better by exploiting that order.

## Optimal Approach (Two Pointers, opposite ends)

Key observation: in a sorted array the **largest absolute values sit at the two
ends** — the most-negative number is on the left, the most-positive on the
right. Therefore the largest square is always produced by one of the two ends.
We can fill the output array **from the largest slot down to the smallest**.

1. Allocate `result` of length `n`. Set `left = 0`, `right = n - 1`, and a write
   position `pos = n - 1`.
2. While `left <= right`:
   - Let `lsq = nums[left] ** 2` and `rsq = nums[right] ** 2`.
   - If `lsq > rsq`: write `lsq` at `result[pos]`, then `left += 1`.
   - Else: write `rsq` at `result[pos]`, then `right -= 1`.
   - Decrement `pos` after writing.
3. Return `result`.

**Why it is correct.** At each step the remaining unprocessed elements are the
contiguous slice `nums[left..right]`. Because the array is sorted, the maximum
square among *those* elements is at one of the two ends (`left` or `right`). We
place that maximum in the current highest empty slot `pos` and shrink the window
by one. By induction, `result` is filled from largest to smallest, i.e. in
non-decreasing order once complete.

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        lsq = nums[left] * nums[left]
        rsq = nums[right] * nums[right]
        if lsq > rsq:
            result[pos] = lsq
            left += 1
        else:
            result[pos] = rsq
            right -= 1
        pos -= 1
    return result
```

- **Time:** `O(n)` — each element is squared and placed exactly once.
- **Space:** `O(n)` for the output array; `O(1)` auxiliary beyond that.

## Key Insights & Edge Cases

- **Fill from the back.** Because you know the *largest* value first, writing
  right-to-left avoids any later shifting or reversal.
- Use `left <= right` (inclusive) so the final middle element is written.
- **All-negative input** (`[-5, -3, -2]`): the left pointer supplies the biggest
  squares first — the two-pointer logic still holds.
- **All-non-negative input** (`[1, 2, 3]`): the right pointer always wins, which
  effectively copies the squares in place — still `O(n)`.
- **Single element** (`n == 1`): the loop runs once and returns `[nums[0] ** 2]`.
- Ties (`lsq == rsq`, e.g. from `-3` and `3`) can take either branch; the `else`
  branch handling equality keeps it correct and stable.
