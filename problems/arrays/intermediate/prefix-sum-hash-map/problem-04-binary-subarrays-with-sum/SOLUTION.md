# Solution — Binary Subarrays With Sum

## Brute Force

Enumerate every start `i` and end `j`, accumulate the sum, and count matches
with `goal`.

```python
count = 0
for i in range(len(nums)):
    running = 0
    for j in range(i, len(nums)):
        running += nums[j]
        if running == goal:
            count += 1
return count
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Prefix Sum + Hash Map

This is LeetCode 560 restricted to a binary array. With `running = prefix[j]`,
the number of subarrays ending at `j` with sum `goal` is the number of earlier
prefix sums equal to `running - goal`. Keep a hash map of prefix-sum **counts**,
seeded with `{0: 1}`.

```python
from collections import defaultdict

def numSubarraysWithSum(nums, goal):
    seen = defaultdict(int)
    seen[0] = 1
    running = 0
    count = 0
    for x in nums:
        running += x
        count += seen[running - goal]
        seen[running] += 1
    return count
```

### Why it is correct

Identical reasoning to counting subarrays with sum `k`: each earlier index with
prefix sum `running - goal` marks the start of a distinct subarray ending here
whose sum is `goal`. Reading `seen[running - goal]` before inserting `running`
keeps subarrays non-empty.

### Step by step on `nums = [1, 0, 1], goal = 1`

| x | running | need = running-1 | seen[need] | count | seen after |
|---|---------|------------------|------------|-------|------------|
| — | 0       | —                | —          | 0     | {0:1}      |
| 1 | 1       | 0                | 1          | 1     | {0:1, 1:1} |
| 0 | 1       | 0                | 1          | 2     | {0:1, 1:2} |
| 1 | 2       | 1                | 2          | 4     | {0:1,1:2,2:1} |

Result: **4** ✓.

- **Time:** O(n).
- **Space:** O(n) (bounded by O(n) distinct prefix sums; at most `len(nums)+1`
  values here).

### Alternative: two sliding windows

Because the array is binary and prefix sums are monotonic, you can also compute
`atMost(goal) - atMost(goal - 1)` with two sliding-window passes in O(n) time
and O(1) space. The hash-map form is shown here because it generalizes to
arbitrary integers.

## Key Insights & Edge Cases

- **`goal = 0` is the classic trap.** You need the `{0: 1}` seed and you count
  runs of consecutive zeros. For `[0,0,0,0,0]` the answer is
  `1+2+3+4+5 = 15`.
- **Counts, not indices** — this is a counting problem, so store how many times
  each prefix sum appeared.
- Since values are only 0/1, prefix sums range from `0` to `len(nums)`, so the
  map stays small.
