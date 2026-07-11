# Next Greater Element II — Solution

## Brute Force

For each index `i`, walk forward up to `n - 1` steps using modular arithmetic
`(i + k) % n`, stopping at the first strictly greater value.

```python
def brute(nums):
    n = len(nums)
    res = [-1] * n
    for i in range(n):
        for k in range(1, n):
            j = (i + k) % n
            if nums[j] > nums[i]:
                res[i] = nums[j]
                break
    return res
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)` beyond the output.

## Optimal Approach (Monotonic Stack)

The only twist over the linear "next greater element" is the wrap-around. We
handle it by pretending the array is doubled: iterate `i` from `0` to `2n - 1`
and use `nums[i % n]` as the current value. One pass over `2n` "virtual" indices
is enough because after visiting every element once more, any element that has a
greater element somewhere in the circle will have been resolved.

Maintain a stack of **real indices** (`0 .. n-1`) whose values are decreasing.
Only **push** during the first pass (`i < n`); in the second pass we merely use
the incoming values to resolve leftover indices — pushing again would be
redundant.

```python
def optimal(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # real indices, values decreasing bottom -> top
    for i in range(2 * n):
        cur = nums[i % n]
        while stack and nums[stack[-1]] < cur:
            res[stack.pop()] = cur
        if i < n:
            stack.append(i)
    return res
```

### Why it is correct

Going around the circle twice guarantees every element gets a chance to be
compared against all `n - 1` other elements that follow it circularly. The stack
holds indices still waiting for a greater value; when `cur` exceeds a stacked
value it is the nearest greater in forward (wrapping) order, exactly as in the
linear case. Indices never resolved after `2n` steps genuinely have no greater
element anywhere in the circle, so they keep `-1`.

Restricting pushes to the first `n` steps prevents duplicate work: every real
index is placed on the stack exactly once.

### Step-by-step on `[1, 2, 1]` (n = 3, loop i = 0..5)

| i | i%n | cur | stack before (idx) | pops -> res set | push? | stack after |
|---|-----|-----|--------------------|-----------------|-------|-------------|
| 0 | 0   | 1   | []                 | —               | yes   | [0]         |
| 1 | 1   | 2   | [0]                | res[0]=2        | yes   | [1]         |
| 2 | 2   | 1   | [1]                | —               | yes   | [1,2]       |
| 3 | 0   | 1   | [1,2]              | —               | no    | [1,2]       |
| 4 | 1   | 2   | [1,2]              | res[2]=2        | no    | [1]         |
| 5 | 2   | 1   | [1]                | —               | no    | [1]         |

Index `1` is never resolved, so `res[1] = -1`. Result: `[2, -1, 2]`.

- **Time:** `O(n)` — `2n` iterations, each index pushed once and popped at most
  once.
- **Space:** `O(n)` for the stack and result.

## Key Insights & Edge Cases

- The doubling trick (`i % n`, loop to `2n`) is the standard way to make a linear
  monotonic-stack technique work on a circular array.
- Use **strict** `<` when popping since we want a strictly greater number; equal
  values do not resolve each other (the global-max element returns `-1`).
- Guard pushes with `if i < n` so each index enters the stack only once.
- If the array is a single element, the answer is `[-1]`.
- Duplicates of the maximum all resolve to `-1` (nothing is strictly greater).
