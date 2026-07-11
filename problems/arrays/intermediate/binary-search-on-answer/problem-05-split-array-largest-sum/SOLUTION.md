# Split Array Largest Sum — Solution

## Brute Force

The classic exact method is **dynamic programming**. Let `dp[i][j]` be the minimized largest sum when splitting the first `i` elements into `j` subarrays. Transition: try every position `p` for the last cut, `dp[i][j] = min over p of max(dp[p][j-1], sum(p..i))`.

```python
def splitArray(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x

    INF = float("inf")
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for p in range(j - 1, i):
                seg = prefix[i] - prefix[p]
                dp[i][j] = min(dp[i][j], max(dp[p][j - 1], seg))
    return dp[n][k]
```

- **Time:** O(n^2 · k).
- **Space:** O(n · k).

Correct and fine for `n <= 1000`, but heavier to reason about and slower than the binary-search approach.

## Optimal Approach (Binary Search on Answer)

Reframe the problem: instead of "what is the minimized largest sum?", ask "for a candidate cap `X`, can we split `nums` into **at most** `k` contiguous subarrays each with sum `<= X`?" If yes, `X` is achievable; we then look for a smaller cap.

**Answer range.** Any subarray must hold at least one element, so the cap can be no smaller than `max(nums)`. Putting everything in one subarray gives a cap of `sum(nums)`, which is always feasible for `k >= 1`. So the answer lives in `[max(nums), sum(nums)]`.

**Feasibility predicate.** Greedily walk left to right, extending the current subarray until adding the next element would exceed `X`; then start a new subarray. Count the subarrays used.

```python
def parts_needed(nums, cap):
    parts, cur = 1, 0
    for x in nums:
        if cur + x > cap:      # would overflow → open a new subarray
            parts += 1
            cur = 0
        cur += x
    return parts

feasible(X) = parts_needed(nums, X) <= k
```

Because `cap >= max(nums)`, every single element fits, so the greedy never gets stuck. Using **at most** `k` parts is equivalent to exactly `k` here: if you can do it in fewer parts, you can always split one part further (elements are non-negative) to reach exactly `k` without increasing the maximum.

**Monotonicity.** A larger cap `X` needs at most as many parts, so `parts_needed` is non-increasing in `X`. The predicate flips once from `False` to `True`: `F F ... F T T ... T`. We want the **first** `True` — the smallest achievable largest sum.

```python
def splitArray(nums, k):
    def parts_needed(cap):
        parts, cur = 1, 0
        for x in nums:
            if cur + x > cap:
                parts += 1
                cur = 0
            cur += x
        return parts

    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if parts_needed(mid) <= k:   # feasible → try a smaller cap
            hi = mid
        else:                        # needs too many parts → raise the cap
            lo = mid + 1
    return lo
```

**Why it is correct.** The invariant is that the optimal cap always lies in `[lo, hi]`. When `mid` is feasible, `mid` may be optimal, so `hi = mid`. When `mid` is infeasible, the answer must be larger, so `lo = mid + 1`. The window strictly shrinks; at `lo == hi` the single value is the minimized largest sum. The greedy `parts_needed` is optimal for a fixed cap because packing each part as full as possible minimizes the number of parts (any less-full packing can only need more parts).

**Step-by-step for `nums = [7, 2, 5, 10, 8], k = 2`** (range `[10, 32]`):

| lo | hi | mid | greedy split at cap mid | parts | <= 2? | action |
|----|----|-----|-------------------------|-------|-------|--------|
| 10 | 32 | 21  | [7,2,5],[10,8]          | 2     | yes   | hi = 21 |
| 10 | 21 | 15  | [7,2,5],[10],[8]        | 3     | no    | lo = 16 |
| 16 | 21 | 18  | [7,2,5],[10,8]          | 2     | yes   | hi = 18 |
| 16 | 18 | 17  | [7,2,5],[10],[8]        | 3     | no    | lo = 18 |

`lo == hi == 18` → return `18`. Correct.

- **Time:** O(n · log(sum(nums))).
- **Space:** O(1).

## Key Insights & Edge Cases

- **Lower bound `max(nums)` is mandatory:** a cap below the largest element can never fit that element, so any feasible cap is at least `max(nums)`.
- **"At most k" vs "exactly k":** with non-negative integers these coincide, because any split using fewer than `k` parts can be refined into exactly `k` parts without raising the maximum. This is why the predicate uses `<= k`.
- **`k == 1`:** the answer is `sum(nums)` (one subarray).
- **`k == len(nums)`:** the answer is `max(nums)` (each element alone); the search converges there.
- **Zeros in the array:** allowed (`nums[i]` can be `0`) and handled naturally — a zero element never forces a new part.
- **Same template as Capacity To Ship Packages** (Problem 3): "minimize the maximum contiguous-group sum using at most `k` groups." The binary-search-on-answer solution is asymptotically faster and simpler than the O(n^2·k) DP.
