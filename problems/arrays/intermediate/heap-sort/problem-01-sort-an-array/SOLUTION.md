# Solution — Sort an Array

## Brute Force

Selection sort is heap sort's naive cousin: scan the unsorted prefix to find the
maximum, swap it to the end, repeat. Finding each maximum is a linear scan.

- **Time:** `O(n^2)` — `n` scans of up to `n` elements. Too slow for
  `n = 5 * 10^4`.
- **Space:** `O(1)`.

Heap sort keeps the same "extract the max, put it at the end" skeleton but makes
finding the max cheap by maintaining a **heap** instead of rescanning.

## Optimal Approach (Heap Sort)

A **max-heap** stored in an array satisfies: for every index `i`,
`arr[i] >= arr[2i+1]` and `arr[i] >= arr[2i+2]` (when those children exist). The
maximum therefore always lives at index `0`.

**Phase 1 — Build the heap (`O(n)`).** Call `sift_down` on every internal node,
from the last parent `n//2 - 1` back to index `0`. Processing bottom-up
guarantees both children subtrees are already valid heaps when a node is
sifted.

**Phase 2 — Sort by repeated extraction (`O(n log n)`).** For `i` from `n-1`
down to `1`: swap `arr[0]` (the current max) with `arr[i]`, which locks the max
into its final sorted slot. Then treat `arr[0:i]` as the heap and `sift_down`
the new root to repair it. The sorted region grows from the right.

```python
def sortArray(self, nums):
    n = len(nums)

    def sift_down(start, end):        # heapify arr[start] within arr[:end]
        root = start
        while True:
            child = 2 * root + 1      # left child
            if child >= end:
                break
            if child + 1 < end and nums[child + 1] > nums[child]:
                child += 1            # pick the larger child
            if nums[root] >= nums[child]:
                break                 # heap property already holds
            nums[root], nums[child] = nums[child], nums[root]
            root = child

    # Phase 1: build max-heap
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)

    # Phase 2: repeatedly move the max to the end
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0, end)

    return nums
```

**Why it is correct.** After Phase 1 the whole array is a max-heap, so `arr[0]`
is the global maximum. Each iteration of Phase 2 moves the current maximum to
position `end`, then restores the heap on the strictly smaller prefix `arr[:end]`.
By induction the suffix `arr[end:]` is always the sorted largest elements, so
when the loop finishes the entire array is sorted ascending.

**Complexity.**

- **Time:** `O(n)` to build + `O(n log n)` for `n` extractions each costing
  `O(log n)` = `O(n log n)` overall, in the best, average, and worst case.
- **Space:** `O(1)` auxiliary — everything happens inside `nums`. (The iterative
  `sift_down` uses no recursion stack.)

### Worked trace on `[5,2,3,1]`

```
build-heap (sift_down from index 1, then 0):
  [5,2,3,1]  sift_down(1): 2 >= 1  -> unchanged
             sift_down(0): 5 >= max(2,3)=3 -> unchanged
  max-heap = [5,2,3,1]

extract:
  swap 0,3 -> [1,2,3,5]  sift_down(0,3): 1<3 swap -> [3,2,1 | 5]
  swap 0,2 -> [1,2,3,5]  sift_down(0,2): 1<2 swap -> [2,1 | 3,5]
  swap 0,1 -> [1,2,3,5]  done
  sorted   = [1,2,3,5]
```

## Key Insights & Edge Cases

- **Build is `O(n)`, not `O(n log n)`.** Summing the work of `sift_down` over all
  nodes gives a convergent series `n * sum(h / 2^h) = O(n)`; most nodes are near
  the leaves and barely move.
- **Max-heap sorts ascending.** Because you park each extracted max at the *end*
  of the array, a max-heap yields ascending order. A min-heap would produce
  descending order with the same scheme.
- **`sift_down` beats `sift_up` for building.** Building by repeated insertion
  (`sift_up`) is `O(n log n)`; the bottom-up `sift_down` build is `O(n)`.
- **Not stable.** Equal elements can be reordered by the swaps, so heap sort is
  not a stable sort. That is fine here since only values matter.
- **Edge cases:** length 0 or 1 arrays skip both loops and are already sorted.
  Duplicates and negatives (Examples 2 and 3) need no special handling — only
  comparisons are used.
- **Off-by-one:** pass the current heap boundary `end` explicitly so the sorted
  suffix is never touched; comparing `child + 1 < end` avoids reading into it.
