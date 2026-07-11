# Solution — Minimum XOR Sum of Two Arrays

## Brute Force

Every rearrangement of `nums2` is a permutation. Try all `n!` of them, computing
the XOR sum, and keep the minimum.

```python
from itertools import permutations

def minimumXORSum_brute(nums1, nums2):
    n = len(nums1)
    return min(sum(nums1[i] ^ perm[i] for i in range(n))
               for perm in permutations(nums2))
```

- **Time:** `O(n! * n)` — infeasible beyond `n ~ 11`.
- **Space:** `O(n)`.

### Bitmask DP (the standard LeetCode-accepted answer)

Assign `nums1[i]` one at a time; `dp[mask]` = min XOR sum after matching the
first `popcount(mask)` elements of `nums1` to the `nums2` indices in `mask`.

```python
def minimumXORSum_dp(nums1, nums2):
    n = len(nums1)
    INF = float("inf")
    dp = [INF] * (1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        i = bin(mask).count("1")          # next nums1 index to place
        if i >= n:
            continue
        for j in range(n):
            if not (mask & (1 << j)):
                nm = mask | (1 << j)
                dp[nm] = min(dp[nm], dp[mask] + (nums1[i] ^ nums2[j]))
    return dp[(1 << n) - 1]
```

- **Time:** `O(n * 2^n)`; **Space:** `O(2^n)`. Fine for `n <= 14`
  (`14 * 2^14 ~ 2.3e5`) but exponential.

## Optimal Approach — Hungarian Algorithm

This is a **minimum-cost perfect matching** between `nums1` and `nums2`:

1. Build the `n x n` cost matrix `cost[i][j] = nums1[i] XOR nums2[j]`.
2. Run the `O(n^3)` Hungarian Algorithm; the returned minimum total cost is the
   answer.

### Why it is correct

A rearrangement of `nums2` is exactly a bijection between indices of `nums1` and
`nums2`, i.e. a perfect matching in a complete bipartite graph whose edge weight
is `nums1[i] XOR nums2[j]`. Minimizing the XOR sum is therefore minimum-weight
perfect matching, which the Hungarian Algorithm solves optimally. XOR is used
only to *fill* the cost matrix; once the matrix exists, the algorithm is oblivious
to how the numbers were produced.

```python
from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cost = [[nums1[i] ^ nums2[j] for j in range(n)] for i in range(n)]
        INF = float("inf")
        u = [0] * (n + 1); v = [0] * (n + 1)
        p = [0] * (n + 1); way = [0] * (n + 1)
        for i in range(1, n + 1):
            p[0] = i; j0 = 0
            minv = [INF] * (n + 1); used = [False] * (n + 1)
            while True:
                used[j0] = True; i0 = p[j0]; delta = INF; j1 = -1
                for j in range(1, n + 1):
                    if not used[j]:
                        cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur; way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]; j1 = j
                for j in range(n + 1):
                    if used[j]:
                        u[p[j]] += delta; v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while j0:
                j1 = way[j0]; p[j0] = p[j1]; j0 = j1
        return sum(cost[p[j] - 1][j - 1] for j in range(1, n + 1) if p[j] != 0)
```

- **Time:** `O(n^2)` to build the matrix + `O(n^3)` for Hungarian.
- **Space:** `O(n^2)` for the matrix, `O(n)` for the working arrays.

### Which to use?

For LeetCode's `n <= 14`, bitmask DP is simpler and usually preferred. The value
of the Hungarian framing is scalability: it stays polynomial (`O(n^3)`) while the
DP's `O(n * 2^n)` becomes hopeless around `n = 20-25`. Recognizing the assignment
structure is the transferable skill.

## Key Insights & Edge Cases

- **XOR is just the edge weight:** don't be distracted by the bitwise operation —
  the moment you write `cost[i][j] = nums1[i] ^ nums2[j]`, it is a plain
  assignment problem.
- **`n == 1`:** the answer is `nums1[0] XOR nums2[0]` (only one pairing).
- **Non-negative costs:** XOR of non-negative ints is non-negative, so no
  offsetting is required before running Hungarian.
- **Greedy fails:** matching each `nums1[i]` to its individually-closest
  `nums2[j]` can create conflicts and is not optimal — the global matching is
  what matters, which is exactly why Hungarian (or DP) is needed.
- **Value range:** with values up to `10^7` and `n <= 14`, the total fits in a
  64-bit integer.
