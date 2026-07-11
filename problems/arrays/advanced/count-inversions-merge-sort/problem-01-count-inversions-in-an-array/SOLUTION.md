# Solution — Count Inversions in an Array

## Brute Force

Check every pair `(i, j)` with `i < j` and increment a counter whenever
`a[i] > a[j]`.

```python
def count_inversions_brute(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                count += 1
    return count
```

- **Time:** `O(n^2)` — quadratic number of pairs.
- **Space:** `O(1)`.

Fine for `n` up to a few thousand, but far too slow at `n = 10^5`
(≈ 10^10 comparisons).

## Optimal Approach — Count Inversions (Merge Sort)

Modify merge sort so that it returns both the sorted subarray **and** the number
of inversions inside it.

Split the array into a left half `L` and a right half `R`. Every inversion
`(i, j)` falls into exactly one of three buckets:

1. Both `i` and `j` are in the left half → counted by the recursive call on `L`.
2. Both are in the right half → counted by the recursive call on `R`.
3. `i` is in the left half and `j` is in the right half → these are the
   **cross inversions**, counted during the merge.

The magic is in step 3. When we merge, both halves are already sorted. We walk a
pointer `p` over `L` and `q` over `R`. At each step we take the smaller front
element:

- If `L[p] <= R[q]`, take `L[p]`. It is `<=` everything remaining in `R`, so it
  creates no inversion with the right half. Advance `p`.
- If `L[p] > R[q]`, take `R[q]`. Because `L` is sorted, **every** remaining
  element `L[p], L[p+1], ..., L[end]` is also `> R[q]` and each sits at an index
  less than `R[q]`'s original index. So this contributes `len(L) - p` inversions
  at once. Advance `q`.

Using `<=` (not `<`) in the first branch is what makes equal elements *not*
count as inversions.

### Why it is correct

- The three buckets are mutually exclusive and exhaustive, so summing the three
  contributions counts each inversion exactly once.
- Within the merge, the "add `len(L) - p` at once" shortcut is valid precisely
  because `L` is sorted: if the front of `L` exceeds `R[q]`, so does the entire
  tail of `L`. Sorting the halves as we recurse is what enables the batch count
  on the next level up — the sort and the count reinforce each other.

### Step-by-step on `a = [2, 4, 1, 3, 5]`

- Split into `L = [2, 4, 1]` and `R = [3, 5]`.
- Recurse on `L`:
  - Split into `[2]` and `[4, 1]`.
  - `[4, 1]` → merging `[4]` and `[1]`: `1 < 4`, take `1` while `4` remains →
    `+1` inversion. Sorted `[1, 4]`.
  - Merge `[2]` with `[1, 4]`: take `1` (`2 > 1`) → `+1` (the element `2`
    remains). Then take `2`, then `4`. Sorted `[1, 2, 4]`. Left total = `2`.
- Recurse on `R = [3, 5]`: already sorted, `0` inversions.
- Merge `[1, 2, 4]` with `[3, 5]`:
  - `1 <= 3` take 1; `2 <= 3` take 2; `4 > 3` take 3 → `+1` (`4` still in L);
    `4 <= 5` take 4; take 5. Cross inversions = `1`.
- Total = `2 (left) + 0 (right) + 1 (cross) = 3`. ✓

### Reference implementation

```python
from typing import List


def count_inversions(a: List[int]) -> int:
    def sort_count(arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        mid = n // 2
        left, right = arr[:mid], arr[mid:]
        inv = sort_count(left) + sort_count(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                inv += len(left) - i   # remaining left elements > right[j]
            k += 1
        while i < len(left):
            arr[k] = left[i]; i += 1; k += 1
        while j < len(right):
            arr[k] = right[j]; j += 1; k += 1
        return inv

    return sort_count(a[:])   # copy so the caller's array is not mutated
```

- **Time:** `O(n log n)` — recurrence `T(n) = 2 T(n/2) + O(n)`.
- **Space:** `O(n)` for the temporary halves plus `O(log n)` recursion stack.

## Key Insights & Edge Cases

- **Batch counting** `len(left) - i` is the whole trick; do not count one at a
  time or you regress toward `O(n^2)` in spirit.
- **Duplicates:** use `<=` when taking from the left so equal values are not
  counted. Using `<` would incorrectly count equal pairs.
- **Overflow:** the count can reach `n*(n-1)/2 ≈ 5*10^9` for `n = 10^5`, beyond
  32-bit range. Python handles big ints natively; in C++/Java use `long long`.
- **Empty / single-element array:** `0` inversions; the recursion base case
  `n <= 1` handles both.
- **Do not mutate the caller's array** unless the contract allows it — sort a
  copy (or accept that the input is reordered and document it).
