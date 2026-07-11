# Solution - Remove Duplicates from Sorted Array

## Brute Force

Collect the distinct values into a separate structure, then copy them back.

```python
seen = []
for x in nums:
    if not seen or seen[-1] != x:
        seen.append(x)
for i, x in enumerate(seen):
    nums[i] = x
return len(seen)
```

- **Time:** `O(n)`.
- **Space:** `O(n)` for the auxiliary list — this violates the `O(1)` extra
  memory requirement.

## Optimal Approach (Two Pointers, same direction)

Because the array is sorted, equal elements are contiguous. Maintain:

- `write` — the index just past the last unique value we have committed. The
  region `nums[0 .. write - 1]` always holds the unique prefix.
- `read` — the scanning index that visits every element once.

Initialize `write = 1` (the first element is always unique). For each `read`
from `1` to `n - 1`:

- If `nums[read] != nums[write - 1]`, we have found a new distinct value. Store
  it at `nums[write]` and increment `write`.
- Otherwise `nums[read]` duplicates the last committed value, so skip it.

Return `write`.

### Why it is correct

**Invariant:** at the start of each iteration, `nums[0 .. write - 1]` is exactly
the sorted set of distinct values seen among `nums[0 .. read - 1]`.

- *Initialization:* before the loop, `write = 1`, `read = 1`, and `nums[0]` is
  trivially the unique set of `nums[0 .. 0]`.
- *Maintenance:* `nums[write - 1]` is the largest committed value. Since the
  array is sorted, `nums[read]` is either equal to it (a duplicate we correctly
  skip) or strictly greater (a brand-new value we correctly append). Either way
  the invariant holds for `read + 1`.
- *Termination:* when `read == n`, the invariant says `nums[0 .. write - 1]`
  contains all distinct values, so `write` is the answer `k`.

### Step-by-step (nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

| read | nums[read] | nums[write-1] | new? | write after | prefix              |
|------|-----------|---------------|------|-------------|---------------------|
| 1    | 0         | 0             | no   | 1           | [0]                 |
| 2    | 1         | 0             | yes  | 2           | [0,1]               |
| 3    | 1         | 1             | no   | 2           | [0,1]               |
| 4    | 1         | 1             | no   | 2           | [0,1]               |
| 5    | 2         | 1             | yes  | 3           | [0,1,2]             |
| 6    | 2         | 2             | no   | 3           | [0,1,2]             |
| 7    | 3         | 2             | yes  | 4           | [0,1,2,3]           |
| 8    | 3         | 3             | no   | 4           | [0,1,2,3]           |
| 9    | 4         | 3             | yes  | 5           | [0,1,2,3,4]         |

Return `k = 5`.

### Reference implementation

```python
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

- **Time:** `O(n)` — one pass; `read` never revisits an index.
- **Space:** `O(1)` — only two integer indices.

## Key Insights & Edge Cases

- **Sorted-ness makes duplicates adjacent**, which is why comparing against just
  `nums[write - 1]` suffices instead of tracking a full set.
- **Compare against `nums[write - 1]`, not `nums[read - 1]`.** Comparing to the
  last *committed* value is what makes it robust across runs of duplicates.
- **Single element** (`[5]`): the loop body never runs, `write` stays `1`
  (Example 3).
- **All identical** (`[7, 7, 7]`): no comparison ever triggers a write, so
  `write` remains `1`.
- The values beyond index `k` are intentionally left as-is; the grader only
  checks `nums[:k]`.
