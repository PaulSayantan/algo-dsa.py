# Sort an Array — Solution

## Brute Force

A simple quadratic sort — selection sort, insertion sort, or bubble sort — repeatedly
finds/settles the next element in place.

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

Correct but far too slow for `n = 5·10^4` on adversarial input; we want `O(n log n)`.

## Optimal Approach (Divide and Conquer — Merge Sort)

**Idea:** A one-element array is already sorted (base case). To sort a larger array,
split it into two halves, sort each half recursively, and then **merge** the two
sorted halves into a single sorted array.

1. **Divide:** `mid = len // 2`; the halves are `nums[:mid]` and `nums[mid:]`.
2. **Conquer:** recursively sort each half.
3. **Combine (merge):** walk two pointers `i, j` across the sorted halves, always
   copying the smaller front element into the output; append the leftover tail.

```python
def sortArray(nums):
    def merge(a, b):
        merged, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:          # <= keeps the sort stable
                merged.append(a[i]); i += 1
            else:
                merged.append(b[j]); j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    def sort(arr):
        if len(arr) <= 1:             # base case
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    return sort(nums)
```

**Why it is correct:** by induction the two recursive calls return fully sorted halves;
`merge` produces a sorted array from two sorted inputs because at every step the
smallest not-yet-placed element sits at the front of one of the two lists, and that is
exactly what we take.

**Recurrence:** `T(n) = 2T(n/2) + O(n)` — two subproblems of half size plus a linear
merge → `O(n log n)` by the Master Theorem (case `f(n) = Θ(n^{log_b a}) = Θ(n)`).

- **Time:** `O(n log n)` in the best, average, and worst case — the split is always
  balanced, so there is no `O(n^2)` degeneration.
- **Space:** `O(n)` for the merge scratch buffers plus `O(log n)` recursion stack.

## Key Insights & Edge Cases

- **Merge is the whole trick.** Splitting is trivial; the linear merge of two sorted
  runs is what actually creates order and what gives the guaranteed `O(n log n)`.
- **Stability:** using `a[i] <= b[j]` (take from the left half on ties) makes the sort
  stable — equal elements keep their original relative order.
- **Duplicates and negatives** need no special handling; comparisons order them
  correctly (see examples 2 and 3).
- **Base case** must catch length `0` and `1` (`len(arr) <= 1`) so recursion bottoms
  out.
- **Merge sort vs. quicksort:** merge sort guarantees `O(n log n)` and is stable but
  uses `O(n)` extra space; quicksort is in-place on average but has an `O(n^2)` worst
  case. Both are Divide and Conquer — the difference is *where* the work lives:
  quicksort does it in the *divide* (partition), merge sort in the *combine* (merge).
