# Next Greater Element I — Solution

## Brute Force

For each value in `nums1`, scan `nums2` to find its position, then keep scanning
to the right until you find a strictly larger value.

```python
def brute(nums1, nums2):
    ans = []
    for x in nums1:
        j = nums2.index(x)          # O(n) locate
        nxt = -1
        for k in range(j + 1, len(nums2)):  # O(n) scan right
            if nums2[k] > x:
                nxt = nums2[k]
                break
        ans.append(nxt)
    return ans
```

- **Time:** `O(m * n)` where `m = len(nums1)`, `n = len(nums2)` (locate + scan
  for each query). Worst case `O(n^2)`.
- **Space:** `O(1)` beyond the output.

## Optimal Approach (Monotonic Stack)

Precompute, in a single pass over `nums2`, the next greater element of **every**
value. Then each `nums1` query is an `O(1)` hash-map lookup.

Maintain a stack of values kept **strictly decreasing** from bottom to top. Walk
`nums2` left to right. For the current value `x`:

- While the stack is non-empty and its top is **less than** `x`, `x` is the next
  greater element of that top. Pop it and record `next_greater[top] = x`.
- Push `x`.

Any value still on the stack at the end has no greater element to its right, so
its answer is `-1`.

```python
def optimal(nums1, nums2):
    next_greater = {}
    stack = []
    for x in nums2:
        while stack and stack[-1] < x:
            next_greater[stack.pop()] = x
        stack.append(x)
    return [next_greater.get(x, -1) for x in nums1]
```

### Why it is correct

The stack always holds values that are still "waiting" for a greater element to
their right, in decreasing order. When `x` arrives, it is the *first* value to
the right of every stack element that it exceeds — precisely because those
elements were never resolved by anything in between (otherwise they'd have been
popped). Elements smaller than or equal to nothing that follows stay on the
stack forever and correctly resolve to `-1`.

### Step-by-step on `nums2 = [1, 3, 4, 2]`

| x | stack before | pops (resolved) | stack after |
|---|--------------|-----------------|-------------|
| 1 | []           | —               | [1]         |
| 3 | [1]          | 1 -> 3          | [3]         |
| 4 | [3]          | 3 -> 4          | [4]         |
| 2 | [4]          | —               | [4, 2]      |

Leftover `4` and `2` map to `-1`. So `next_greater = {1: 3, 3: 4, 4: -1, 2: -1}`.
Querying `[4, 1, 2]` gives `[-1, 3, -1]`.

- **Time:** `O(m + n)` — each `nums2` value is pushed and popped at most once;
  each `nums1` value is one dictionary lookup.
- **Space:** `O(n)` for the stack and hash map.

## Key Insights & Edge Cases

- Because all values are **distinct**, using values (not indices) as map keys is
  safe. With duplicates you would store indices instead.
- The comparison is `stack[-1] < x` (strictly greater desired). If the problem
  asked for "next greater-or-equal," you would pop on `<=`.
- A value with no greater element to the right remains on the stack; default the
  lookup to `-1`.
- Single-element `nums2` (`[5]`) yields all `-1`.
