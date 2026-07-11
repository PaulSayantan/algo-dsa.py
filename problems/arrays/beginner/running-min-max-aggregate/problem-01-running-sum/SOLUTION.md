# Solution — Running Sum of 1d Array

## Brute Force

For each index `i`, loop from `0` to `i` and add up every element to compute
`runningSum[i]` independently.

```python
out = []
for i in range(len(nums)):
    total = 0
    for j in range(i + 1):
        total += nums[j]
    out.append(total)
```

- **Time:** O(n^2) — for index `i` we redo work proportional to `i`, and
  `0 + 1 + ... + (n-1) = n(n-1)/2` additions.
- **Space:** O(n) for the output (O(1) extra beyond the output).

The waste is obvious: to compute the sum up to index `i` we recompute the sum
up to index `i-1` from scratch, even though we just calculated it.

## Optimal Approach (Running Aggregate)

Maintain a single scalar `running` that always equals the sum of everything
seen so far. When we advance to index `i`, the answer is simply the previous
total plus the new element:

```
runningSum[i] = runningSum[i-1] + nums[i]
```

Reference implementation (in-place, reusing the input array as output):

```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
```

Or with an explicit accumulator:

```python
def runningSum(nums):
    out, running = [], 0
    for x in nums:
        running += x
        out.append(running)
    return out
```

**Why it is correct.** Addition is associative, so
`nums[0] + ... + nums[i] = (nums[0] + ... + nums[i-1]) + nums[i]`. The invariant
"`running` holds the sum of `nums[0..i]`" is established at `i = 0`
(`running == nums[0]`) and preserved at each step because we add exactly one new
term. By induction it holds for every index, so each emitted value is correct.

**Step-by-step** on `[3, 1, 2, 10, 1]`:

| i | nums[i] | running before | running after | output so far |
| - | ------- | -------------- | ------------- | ------------- |
| 0 | 3       | 0              | 3             | [3]           |
| 1 | 1       | 3              | 4             | [3, 4]        |
| 2 | 2       | 4              | 6             | [3, 4, 6]     |
| 3 | 10      | 6              | 16            | [3, 4, 6, 16] |
| 4 | 1       | 16             | 17            | [3, 4, 6, 16, 17] |

- **Time:** O(n) — one pass.
- **Space:** O(1) extra (in-place variant) or O(n) for a fresh output list.

## Key Insights & Edge Cases

- This is the canonical "prefix sum" and it underpies many harder problems:
  precompute running sums once, then answer range-sum queries in O(1).
- A single-element array returns itself (`[x] -> [x]`), which the loop handles
  naturally because it starts the running total at the first element.
- Values can be negative; the running total may go down as well as up. Nothing
  special is needed — addition handles signs automatically.
- Watch out only for languages with fixed-width integers where the cumulative
  sum could overflow. In Python integers are unbounded, so it is a non-issue
  here, but note it if porting to C/Java (use 64-bit).
