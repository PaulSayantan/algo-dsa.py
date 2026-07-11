# Solution — Sort an Array

## Brute Force

The most naive "correct" approach is **selection by repeated scanning**: repeatedly scan the
unsorted portion, find the minimum, and append it to an output list (removing it from the
input). Removing from a Python list is `O(n)`, and we do it `n` times, so this is `O(n^2)`
time and `O(n)` extra space for the output list. It works but wastes memory and is clumsy.

- Time: `O(n^2)`
- Space: `O(n)`

## Optimal Approach (Insertion Sort)

Insertion sort sorts **in place** with only `O(1)` extra space. The idea:

1. Treat `nums[0..i-1]` as an already-sorted prefix. Initially `i = 1`, so the prefix is just
   the single element `nums[0]`, which is trivially sorted.
2. Take `key = nums[i]`, the first element of the unsorted region.
3. Walk left from index `i-1`. While the element there is **greater** than `key`, copy it one
   slot to the right (opening a gap). Stop when you reach the start or an element `<= key`.
4. Drop `key` into the gap. The sorted prefix has now grown to `nums[0..i]`.
5. Repeat for `i = 1, 2, ..., n-1`.

**Why it is correct.** Loop invariant: *before processing index `i`, the subarray
`nums[0..i-1]` contains the original first `i` elements, rearranged into sorted order.* The
inner loop shifts exactly those elements larger than `key` to its right and places `key` after
the last element that is `<= key`, so `nums[0..i]` is sorted afterward. When the outer loop
finishes with `i = n-1`, the whole array is sorted.

**Stability.** We shift only while `nums[j] > key` (strict). An element equal to `key` stops
the loop, so `key` is placed *after* equal elements that came before it — relative order of
equals is preserved.

```python
def sortArray(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]   # shift larger element right
            j -= 1
        nums[j + 1] = key           # insert key into the opened gap
    return nums
```

- Time: `O(n^2)` average and worst case (reverse-sorted input shifts every element all the
  way left); `O(n)` best case (already sorted — the inner `while` never executes).
- Space: `O(1)` — in place.

## Key Insights & Edge Cases

- **Shift, don't swap.** Copying the larger element rightward and dropping `key` once at the
  end does one write per shifted element plus one final write, versus three writes per swap.
  Both are `O(n^2)` but shifting is a constant factor cheaper.
- **Best case is genuinely linear.** On sorted input the `while` condition fails immediately
  for every `i`, so the total work is one comparison per element.
- **Negatives and duplicates** need no special handling — comparisons work the same.
- **Single element / empty.** With `n <= 1` the outer loop never runs and the array is
  returned unchanged.
- **In place vs. copy.** If the caller must keep the original untouched, operate on
  `nums = list(nums)` first.
