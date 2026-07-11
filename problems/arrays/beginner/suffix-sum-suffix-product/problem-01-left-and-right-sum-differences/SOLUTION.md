# Solution — Left and Right Sum Differences

## Brute Force

For each index `i`, loop over the whole array a second time: add everything with
index `< i` into `leftSum` and everything with index `> i` into `rightSum`, then
record `abs(leftSum - rightSum)`.

```python
def leftRightDifference(nums):
    n = len(nums)
    answer = []
    for i in range(n):
        left = sum(nums[:i])
        right = sum(nums[i + 1:])
        answer.append(abs(left - right))
    return answer
```

- **Time:** O(n^2) — each of the `n` indices rescans up to `n` elements.
- **Space:** O(1) extra (ignoring the output).

## Optimal Approach (Suffix Sum + Prefix Sum)

Every `rightSum[i]` is a **suffix sum**: the total of all elements from index
`i + 1` to the end. Every `leftSum[i]` is a **prefix sum**: the total of all
elements before `i`. Compute both in linear time.

One clean two-variable version: start with `right = sum(nums)` conceptually and
maintain a running `left`. As you visit index `i`, first subtract `nums[i]` out
of the "right" total (since `rightSum[i]` excludes `i` itself), then compute the
answer, then fold `nums[i]` into `left` for the next index.

Reference implementation:

```python
def leftRightDifference(nums):
    n = len(nums)

    # suffix[i] = sum of nums[i:] ; suffix[n] = 0
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + nums[i]

    answer = [0] * n
    left = 0
    for i in range(n):
        right = suffix[i + 1]          # elements strictly to the right of i
        answer[i] = abs(left - right)
        left += nums[i]                # extend prefix for the next index
    return answer
```

**Why it is correct:** `suffix[i + 1]` sums exactly `nums[i+1..n-1]`, which is
`rightSum[i]`. The running `left` holds `nums[0..i-1]` when index `i` is
processed, which is `leftSum[i]`. Neither includes `nums[i]`, matching the
definition, and `abs` gives the required non-negative difference.

**Step by step** for `nums = [10, 4, 8, 3]`:

```
suffix = [25, 15, 11, 3, 0]      (built right-to-left)
          i=0  i=1 i=2 i=3 i=4

i=0: left=0,  right=suffix[1]=15 -> |0 - 15|  = 15, then left=10
i=1: left=10, right=suffix[2]=11 -> |10 - 11| = 1,  then left=14
i=2: left=14, right=suffix[3]=3  -> |14 - 3|  = 11, then left=22
i=3: left=22, right=suffix[4]=0  -> |22 - 0|  = 22, then left=25

answer = [15, 1, 11, 22]
```

- **Time:** O(n) — one pass to build the suffix, one pass to fill the answer.
- **Space:** O(n) for the suffix array (reducible to O(1) extra with the
  two-variable rolling technique).

## Key Insights & Edge Cases

- The pairing "prefix on the left, suffix on the right" is the reusable idea:
  anything of the form "aggregate everything except this index" is naturally a
  prefix aggregate combined with a suffix aggregate.
- **Single element** (`n == 1`): `leftSum = rightSum = 0`, so the answer is `[0]`.
  The trailing `suffix[n] = 0` handles this without a special case.
- The endpoints are the "extreme" cases: index `0` has `leftSum = 0` and index
  `n-1` has `rightSum = 0`; the trailing-zero convention makes both fall out
  automatically.
- You do not even need the full suffix array — a single `right` variable that you
  decrement as you sweep left to right gives O(1) extra space.
