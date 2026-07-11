# Squares of a Sorted Array — Solution

## Brute Force

Square every element, then sort.

```python
def sortedSquares(nums):
    return sorted(x * x for x in nums)
```

- **Time:** `O(n log n)` — the sort dominates.
- **Space:** `O(n)` for the output.

Correct, but it ignores the structure: the input is already sorted, so we should be able
to produce the answer in linear time.

## Optimal Approach (Two-Pointer Merge)

Key observation: a non-decreasing array splits into a **descending-magnitude** run of
negatives followed by an **ascending-magnitude** run of non-negatives. Equivalently,
scanning from both ends inward, the element with the **larger absolute value** is always
at one of the two ends. Squaring is monotonic in absolute value, so the largest square is
at an end.

This is exactly a merge of two sorted sequences (negatives read right-to-left, positives
read left-to-right) — we just fill the output from the **largest** square down to the
smallest.

```python
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for pos in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
    return result
```

**Why it is correct.** At any moment the untouched window is `nums[left..right]`. Because
the array is sorted, the maximum absolute value in that window is either `nums[left]`
(most negative) or `nums[right]` (most positive). We place its square at the current
highest unfilled position `pos` and shrink the window. By induction the suffix
`result[pos..]` always holds the largest squares in sorted order.

**Step-by-step** on `nums = [-4,-1,0,3,10]` (`|.|` = absolute value):

| left / right | `|nums[left]|` vs `|nums[right]|` | Place at pos | result |
| --- | --- | --- | --- |
| l=0(-4), r=4(10) | 4 vs 10 -> right | pos4 = 100 | `[_,_,_,_,100]` |
| l=0(-4), r=3(3)  | 4 vs 3  -> left  | pos3 = 16  | `[_,_,_,16,100]` |
| l=1(-1), r=3(3)  | 1 vs 3  -> right | pos2 = 9   | `[_,_,9,16,100]` |
| l=1(-1), r=2(0)  | 1 vs 0  -> left  | pos1 = 1   | `[_,1,9,16,100]` |
| l=2(0),  r=2(0)  | 0 vs 0  -> right | pos0 = 0   | `[0,1,9,16,100]` |

- **Time:** `O(n)` — each index handled once.
- **Space:** `O(n)` for the output (`O(1)` auxiliary beyond it).

## Key Insights & Edge Cases

- The largest square is always at one of the two ends — that is what lets you fill the
  output back-to-front, mirroring the in-place merge of Problem 1.
- Compare **absolute values**, not raw values, when deciding which end to take.
- All-negative or all-positive inputs still work: one pointer simply advances the whole
  way while the other stays put (see Example 3, which effectively reverses the array).
- Single-element array: the loop runs once and returns `[nums[0] ** 2]`.
- Using `>` vs `>=` in the comparison only changes which equal-magnitude end is taken
  first; the sorted result is identical.
