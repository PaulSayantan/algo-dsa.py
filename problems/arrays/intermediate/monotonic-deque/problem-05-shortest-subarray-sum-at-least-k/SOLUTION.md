# Shortest Subarray with Sum at Least K — Solution

## Brute Force

Fix a start `i`, extend `j` to the right accumulating the sum, and record the
first (shortest) `j` where the running sum reaches `k`.

```python
def brute(nums, k):
    n, best = len(nums), float("inf")
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s >= k:
                best = min(best, j - i + 1)
                break
    return best if best != float("inf") else -1
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

Note the ordinary two-pointer sliding window (shrink from the left while the sum
is `>= k`) does **not** work here because negative numbers mean a longer window
can have a *smaller* sum, so there is no monotone shrink invariant.

## Optimal Approach (Monotonic Deque over Prefix Sums)

Build prefix sums `P` with `P[0] = 0` and `P[j] = nums[0] + ... + nums[j-1]`, so
the subarray covering original indices `i .. j-1` has sum `P[j] - P[i]` and
length `j - i`. For each right endpoint `j` we want the **largest** `i < j` with
`P[i] <= P[j] - k`, minimizing `j - i`.

Maintain a deque of prefix-sum indices whose `P` values are **increasing** front
to back. For each `j` (from `0` to `n`):

1. **Answer extraction (pop front).** While the deque is non-empty and
   `P[j] - P[dq[0]] >= k`, index `dq[0]` gives a valid subarray ending at `j`;
   record `j - dq[0]` and `popleft`. We can discard `dq[0]` permanently: any
   later `j' > j` paired with it would only be longer.
2. **Maintain monotonicity (pop back).** While the deque is non-empty and
   `P[dq[-1]] >= P[j]`, pop the back. A later index with a smaller-or-equal
   prefix sum dominates `dq[-1]`: it is both closer to future `j'` and easier to
   satisfy `P[i] <= P[j'] - k`.
3. Append `j`.

```python
from collections import deque

def optimal(nums, k):
    n = len(nums)
    P = [0] * (n + 1)
    for i in range(n):
        P[i + 1] = P[i] + nums[i]

    dq = deque()            # indices into P, P[...] increasing front -> back
    best = n + 1
    for j in range(n + 1):
        while dq and P[j] - P[dq[0]] >= k:
            best = min(best, j - dq.popleft())
        while dq and P[dq[-1]] >= P[j]:
            dq.pop()
        dq.append(j)
    return best if best <= n else -1
```

### Why it is correct

- The deque stays increasing in `P`, so when we test the front we are testing the
  *smallest* prefix sum still in play — the one most likely to satisfy
  `P[j] - P[i] >= k`. If even the front fails, no other stored `i` can succeed.
- **Front pop is safe** because once `P[j] - P[dq[0]] >= k`, index `dq[0]` has
  found its shortest possible partner (this `j`); pairing it with any larger `j'`
  yields a longer subarray, so it is never needed again.
- **Back pop is safe** because if `P[dq[-1]] >= P[j]` with `dq[-1] < j`, then `j`
  is a strictly better left endpoint for every future query — nearer and with a
  no-larger prefix sum — so `dq[-1]` is dominated.

### Step-by-step on `nums = [2, -1, 2], k = 3`

Prefix sums `P = [0, 2, 1, 3]`.

| j | P[j] | front-pop check                 | best | back-pop           | dq after |
|---|------|---------------------------------|------|--------------------|----------|
| 0 | 0    | deque empty                     | inf  | —                  | [0]      |
| 1 | 2    | 2 - P[0]=2 >= 3? no             | inf  | P[0]=0 >= 2? no    | [0,1]    |
| 2 | 1    | 1 - P[0]=1 >= 3? no             | inf  | P[1]=2 >= 1? yes   | [0,2]    |
| 3 | 3    | 3 - P[0]=3 >= 3? yes -> len 3   | 3    | P[2]=1 >= 3? no    | [2,3]    |

After the front pop at `j = 3`, the deque front becomes index `2`, and
`3 - P[2] = 3 - 1 = 2 >= 3` is false, so we stop. Best length `3`, matching
Example 3.

- **Time:** `O(n)` — each index is appended once and removed at most once (from
  either end).
- **Space:** `O(n)` for the prefix-sum array and the deque.

## Key Insights & Edge Cases

- Use `P[0] = 0` and iterate `j` over `0 .. n` so single-element and full-array
  subarrays are both representable as `P[j] - P[i]`.
- A **plain two-pointer window fails** with negatives; the prefix-sum deque is
  what handles them.
- `k` can be as large as `10^9`, larger than any achievable sum — then no front
  pop ever fires and the function returns `-1` (Example 2).
- Because sums can reach `~10^{10}`, use 64-bit integers in languages other than
  Python.
- Front pops use `>=` (sum "at least" `k`); back pops use `>=` to also discard
  equal prefix sums, keeping the deque as short as possible.
