# Solution — Running Sum of 1d Array

## Brute Force

For every index `i`, loop from `0` to `i` and add up the elements to compute
`out[i]`.

```python
def runningSum(nums):
    n = len(nums)
    out = [0] * n
    for i in range(n):
        total = 0
        for j in range(i + 1):      # re-sum the whole prefix each time
            total += nums[j]
        out[i] = total
    return out
```

- **Time:** O(n^2) — index `i` costs `i+1` additions, and `0+1+...+(n-1)` is
  quadratic.
- **Space:** O(n) for the output (O(1) auxiliary).

## Optimal Approach (Prefix Precomputation)

The running sum at index `i` is just the running sum at index `i-1` plus the new
element:

```
out[i] = out[i-1] + nums[i]      (out[0] = nums[0])
```

So we never need to re-add earlier elements — we carry a single running total.

```python
def runningSum(nums):
    out = []
    total = 0
    for x in nums:
        total += x          # extend the prefix by one element
        out.append(total)   # store the cumulative value
    return out
```

**Why it is correct.** By induction: `out[0] = nums[0]` is the sum of the length-1
prefix. Assuming `out[i-1]` correctly equals `nums[0] + ... + nums[i-1]`, then
`out[i-1] + nums[i]` equals `nums[0] + ... + nums[i]`, which is exactly the running
sum at `i`. Each element contributes to every later cumulative value exactly once.

**Step by step** on `[3, 1, 2, 10, 1]`:

| i | nums[i] | running total | out |
|---|---------|---------------|-----|
| 0 | 3       | 3             | [3] |
| 1 | 1       | 4             | [3, 4] |
| 2 | 2       | 6             | [3, 4, 6] |
| 3 | 10      | 16            | [3, 4, 6, 16] |
| 4 | 1       | 17            | [3, 4, 6, 16, 17] |

- **Time:** O(n) — one pass, one addition per element.
- **Space:** O(n) output, O(1) auxiliary. You can even overwrite `nums` in place
  (`nums[i] += nums[i-1]`) for O(1) extra space.

## Key Insights & Edge Cases

- This is the **inclusive** prefix sum. Many range-query problems use an
  **exclusive** variant with an extra leading zero (`prefix[0] = 0`,
  `prefix[i] = prefix[i-1] + nums[i-1]`) so that `sum(l..r) = prefix[r+1] - prefix[l]`.
  Know both conventions.
- A length-1 array returns a copy of itself — the loop handles it naturally.
- Negative numbers are fine; the running total can decrease.
- With values up to `10^6` and length up to `1000`, the total fits comfortably in a
  64-bit integer (Python ints are unbounded, so no overflow concern here).
