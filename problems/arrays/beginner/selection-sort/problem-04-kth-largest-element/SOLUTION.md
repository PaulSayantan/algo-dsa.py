# Solution — Kth Largest Element in an Array

## Brute Force

Sort the whole array descending and index into it:

```python
def findKthLargest(self, nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]
```

- **Time:** `O(n log n)` for the full sort.
- **Space:** `O(1)` extra (or `O(n)` depending on the sort implementation).

Correct and simple, but it does more work than necessary: we only need the top `k` elements, yet we
sorted all `n`.

## Optimal Approach (Partial Selection Sort)

Selection Sort finalizes one element per pass. To find the k-th largest we only need the first `k`
elements of the descending order, so we run **exactly `k` passes** and stop. This is often called
"partial selection sort" or the *selection algorithm*.

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(k):                     # only k passes, not n - 1
            max_idx = i
            for j in range(i + 1, n):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            if max_idx != i:
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
        return nums[k - 1]
```

### Why it is correct

By the Selection Sort invariant (adapted to descending order), after pass `i` the positions
`0 .. i` hold the `i + 1` **largest** elements of the array, in non-increasing order. Running `k`
passes therefore places the `k` largest elements — with duplicates counted — into `nums[0 .. k-1]`
in sorted order. The element now at index `k - 1` is precisely the k-th largest. Duplicates are
handled correctly because each pass moves one physical element; two equal values simply become the
i-th and (i+1)-th largest on consecutive passes.

### Step-by-step on `nums=[3,2,1,5,6,4]`, `k=2`

| pass i | max in suffix | swap indices | array               |
|--------|---------------|--------------|---------------------|
| 0      | `6` @4        | swap 0,4     | `[6,2,1,5,3,4]`     |
| 1      | `5` @3        | swap 1,3     | `[6,5,1,2,3,4]`     |

Stop after 2 passes. `nums[k-1] = nums[1] = 5`. ✔

### Complexity

- **Time:** `O(n·k)` — `k` passes, each scanning up to `n` elements. When `k` is small this beats the
  `O(n log n)` full sort; when `k ≈ n` it degrades to `O(n²)`.
- **Space:** `O(1)` — in place.

For very large inputs with large `k`, a heap (`O(n log k)`) or Quickselect (`O(n)` average) is
preferable — but partial Selection Sort is the clearest illustration of "select the top `k`."

## Key Insights & Edge Cases

- **Stop early:** the whole point is running `range(k)` passes, not `range(n - 1)`. This turns the
  `O(n²)` sort into an `O(n·k)` selection.
- **1-based rank:** `k` is 1-based counting from the largest, so the answer sits at index `k - 1`
  after `k` passes — a frequent off-by-one trap.
- **Duplicates count as separate ranks:** in `[5,5,6]` with `k=2`, the answer is `5`, not the "2nd
  distinct" value. Selecting physical elements handles this automatically.
- **k == 1:** one pass finds the global maximum; `nums[0]` is returned.
- **k == n:** the last pass fixes the smallest element; the method still works but costs the full
  `O(n²)`.
- **Negatives:** plain integer comparison handles negative values with no special-casing.
- **Input mutation:** this approach reorders `nums` in place. If the caller must preserve the
  original order, operate on a copy (`nums = nums[:]`).
