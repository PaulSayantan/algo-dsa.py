# Solution — Running Sum of 1d Array

## Brute Force

For each index `i`, loop from `0` to `i` and add up `nums[0..i]`.

```python
def runningSum(nums):
    result = []
    for i in range(len(nums)):
        total = 0
        for j in range(i + 1):
            total += nums[j]
        result.append(total)
    return result
```

- **Time:** O(n^2) — index `i` costs `i + 1` additions, so the total is
  `1 + 2 + ... + n = n(n+1)/2`.
- **Space:** O(n) for the output (O(1) auxiliary).

The wasted work is obvious: the sum for index `i` recomputes everything that the
sum for index `i-1` already computed.

## Optimal Approach (Prefix Sum, 1D)

Carry a single running total. The running sum at index `i` is just the running
sum at index `i-1` plus `nums[i]`:

```
runningSum[i] = runningSum[i-1] + nums[i]
```

Reference implementation (in place, reusing the input array):

```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
```

Or without mutating the input:

```python
def runningSum(nums):
    result = []
    total = 0
    for x in nums:
        total += x
        result.append(total)
    return result
```

**Why it is correct:** by induction. `result[0] = nums[0]` is the sum of the
single-element prefix. Assuming `result[i-1]` correctly holds
`nums[0] + ... + nums[i-1]`, adding `nums[i]` yields `nums[0] + ... + nums[i]`,
which is exactly `result[i]`.

**Step by step** on `[3, 1, 2, 10, 1]`:

| i | nums[i] | running total | output so far |
|---|---------|---------------|----------------|
| 0 | 3       | 3             | [3]            |
| 1 | 1       | 4             | [3, 4]         |
| 2 | 2       | 6             | [3, 4, 6]      |
| 3 | 10      | 16            | [3, 4, 6, 16]  |
| 4 | 1       | 17            | [3, 4, 6, 16, 17] |

- **Time:** O(n) — one pass.
- **Space:** O(1) auxiliary if you write in place; O(n) if you allocate a new list.

## Key Insights & Edge Cases

- This problem *is* the prefix-sum construction. Master it and the rest of the
  folder reduces to "build a prefix array, then subtract."
- **Single element:** `[5] -> [5]`. The loop starting at index 1 simply never
  runs, which is correct.
- **Negative numbers:** the running total can decrease or go negative; nothing
  special is required because addition handles signs naturally.
- **In-place vs. new array:** mutating the input is fine here and saves memory,
  but if the caller still needs the original values, allocate a fresh list.
- Many libraries expose this directly (e.g. `itertools.accumulate` in Python),
  but implementing it by hand cements the pattern.
