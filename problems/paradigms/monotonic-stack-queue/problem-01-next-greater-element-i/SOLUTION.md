# Next Greater Element I — Solution

## Brute Force

For each value `x` in `nums1`, find its position in `nums2`, then walk to the right until
you find the first value greater than `x` (or fall off the end).

- Finding `x` in `nums2`: `O(n2)`.
- Walking right: `O(n2)`.
- Repeated for each of `n1` queries: **`O(n1 * n2)`** time, `O(1)` extra space.

For the given constraints (≤ 1000) this passes, but it does redundant re-scanning.

## Optimal Approach (Monotonic Stack / Queue)

**Key idea:** compute the next greater element for *every* value in `nums2` in a single
`O(n2)` pass, store it in a hash map, then answer each `nums1` query in `O(1)`.

Maintain a **monotonically decreasing stack** of values (top is the smallest). Scan
`nums2` left to right:

1. While the stack is non-empty **and** the current value `c` is greater than the value on
   top of the stack, pop that top value `t`. Because `c` is the first value to the right of
   `t` that exceeds it, record `next_greater[t] = c`.
2. Push `c` onto the stack.

After the pass, any values still on the stack never found a greater element to their right,
so their answer is `-1`. Finally, map each `nums1[i]` through `next_greater` (default `-1`).

### Why it is correct

The stack holds exactly the elements seen so far that are still "waiting" for a greater
element, and they are in decreasing order from bottom to top. When a new value `c` arrives,
every waiting element smaller than `c` has now met its next-greater (which is `c`, the very
first larger value encountered to its right). Elements larger than `c` remain waiting. This
guarantees each element's recorded answer is the *nearest* greater value on its right.

### Reference implementation

```python
def nextGreaterElement(self, nums1, nums2):
    next_greater = {}
    stack = []                      # decreasing stack of values
    for c in nums2:
        while stack and c > stack[-1]:
            next_greater[stack.pop()] = c
        stack.append(c)
    return [next_greater.get(x, -1) for x in nums1]
```

### Complexity

- **Time:** `O(n1 + n2)`. Each element of `nums2` is pushed and popped at most once.
- **Space:** `O(n2)` for the stack and hash map.

## Key Insights & Edge Cases

- **Store what you can look up:** because all values are distinct, keying the map by value
  (not index) is safe and makes `nums1` lookups trivial.
- **Leftovers = -1:** elements remaining on the stack at the end have no greater element to
  their right.
- **Strictly greater:** the comparison is `>`, not `>=`; with distinct values this
  distinction does not bite here, but it matters in variants with duplicates.
- **Single-element `nums2`:** the loop pushes once, pops nothing; every query maps to `-1`.
