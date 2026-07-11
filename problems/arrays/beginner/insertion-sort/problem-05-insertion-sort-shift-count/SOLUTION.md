# Solution — Insertion Sort Shift Count (Inversions)

## Brute Force

Directly count inversions by checking every pair: for each `i < j`, increment a counter when
`nums[i] > nums[j]`.

```python
count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            count += 1
return count
```

- Time: `O(n^2)`.
- Space: `O(1)`.

Correct, but it does not explain the connection to sorting and is slow for large `n`.

## Optimal Approach (Insertion Sort simulation)

Run insertion sort and **count each shift** the inner loop makes. Every time we execute
`nums[j+1] = nums[j]` we move one element one slot right, so we add 1 to the counter.

```python
def countShifts(self, nums):
    a = list(nums)          # copy so we don't mutate the caller's array
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shifts += 1     # one element moved right
        a[j + 1] = key      # placing the key is NOT a shift
    return shifts
```

**Why the shift count equals the inversion count.** When insertion sort inserts `key = a[i]`
into the sorted prefix `a[0..i-1]`, the inner loop shifts *exactly* those prefix elements that
are greater than `key`. Each such element `x` sits at an index less than `i` but has `x > key`,
i.e. the pair `(index of x, i)` is an inversion. Conversely, every inversion `(p, i)` with
`p < i` and `a[p] > a[i]` (in the original array) causes exactly one shift when `a[i]` is
inserted. So the shifts done while inserting element `i` count precisely the inversions whose
right endpoint is `i`; summed over all `i`, total shifts = total inversions.

- Time: `O(n^2)` worst case (reverse-sorted), `O(n)` best case (already sorted, no shifts).
- Space: `O(1)` beyond the optional defensive copy.

## Faster: Merge Sort Inversion Counter (`O(n log n)`)

Because the answer is just the inversion count, we can compute it in `O(n log n)` with a
modified merge sort. During the merge step, when an element from the right half is placed
before remaining elements of the left half, every remaining left element forms an inversion
with it, so add `len(left) - i` to the counter.

```python
def countShifts(self, nums):
    def sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, cl = sort_count(arr[:mid])
        right, cr = sort_count(arr[mid:])
        merged, i, j, split = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:      # <= keeps it stable, no inversion
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                split += len(left) - i   # all remaining lefts > right[j]
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, cl + cr + split
    return sort_count(list(nums))[1]
```

- Time: `O(n log n)`. Space: `O(n)`.

Use the insertion-sort version to *understand* why shifts = inversions; use the merge-sort
version when `n` is large.

## Key Insights & Edge Cases

- **Placing the key is not a shift.** Only the `while`-loop moves count. Off-by-one here is
  the classic mistake — do not add 1 for the final `a[j+1] = key` assignment.
- **Sorted input → 0**, reverse-sorted length `n` → `n*(n-1)/2` (the maximum).
- **Use `<=` in the merge**, not `<`, so equal elements are not counted as inversions (an
  inversion requires a strict `>`), which also keeps the merge stable.
- **Overflow.** In languages with fixed-width ints, the count can reach ~`5*10^7` for
  `n = 10^4` and up to ~`5*10^9` for `n = 10^5`; use 64-bit. Python ints are unbounded.
- **Don't mutate the input** unless allowed — copy first if the caller still needs the
  original order.
