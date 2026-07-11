# Solution — Maximum Length of Repeated Subarray

## Brute Force

Try every pair of start positions and extend the match as far as it goes.

```python
def findLength(nums1, nums2):
    n, m = len(nums1), len(nums2)
    best = 0
    for i in range(n):
        for j in range(m):
            k = 0
            while i + k < n and j + k < m and nums1[i + k] == nums2[j + k]:
                k += 1
            best = max(best, k)
    return best
```

- **Time:** `O(n · m · min(n, m))` — a pair of starts, each extended up to
  `min(n, m)`.
- **Space:** `O(1)`.

The standard DP solution improves this to `O(n·m)` time / `O(m)` space:
`dp[i][j] = dp[i+1][j+1] + 1` when `nums1[i] == nums2[j]`. That is the usual
answer — but the hashing route below is the one that scales when the "match"
predicate is more expensive, and it teaches the binary-search-on-length pattern.

## Optimal Approach (Binary Search on Length + Rolling Hash)

**Monotonicity.** If a common subarray of length `L` exists, then any length
`L' < L` also has a common subarray (take a prefix). So the set of achievable
lengths is `{0, 1, ..., ans}` — a monotone predicate `has_common(L)`. Binary
search for the largest `L` with `has_common(L) == True`.

**Checking `has_common(L)` with hashing.** Treat each array as a "string" of
integers. Roll a length-`L` hash across `nums1`, storing every window hash in a
set. Then roll across `nums2`; if any window's hash is in the set (and, to be
safe, the actual windows match), a common length-`L` subarray exists. Each check
is `O(n + m)`.

Rolling update for a window of width `L` with base `B`, modulus `M`:

```
h = (h - out * B^(L-1)) * B + in      (mod M)
```

### Why it is correct

Rolling hash gives every window a fingerprint such that equal windows share a
fingerprint. A set hit therefore flags a *candidate* common block; verifying the
candidate (or using double hashing) removes false positives, so `has_common(L)`
is exact. Binary search over a correct monotone predicate returns the exact
maximum length.

### Step by step

1. `lo, hi = 0, min(len(nums1), len(nums2))`.
2. While `lo < hi`: `mid = (lo + hi + 1) // 2`; if `has_common(mid)` set
   `lo = mid`, else `hi = mid - 1`.
3. Return `lo`.

```python
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, B = (1 << 61) - 1, 131          # big prime + base
        n, m = len(nums1), len(nums2)

        def has_common(L: int) -> bool:
            if L == 0:
                return True
            power = pow(B, L - 1, M)
            # hash all length-L windows of `arr`, yielding (hash, start)
            def windows(arr):
                h = 0
                for i in range(L):
                    h = (h * B + arr[i] + 1) % M      # +1: keep values nonzero
                yield h, 0
                for i in range(L, len(arr)):
                    h = ((h - (arr[i - L] + 1) * power) * B + arr[i] + 1) % M
                    yield h, i - L + 1

            seen = {}
            for h, start in windows(nums1):
                seen.setdefault(h, []).append(start)
            for h, start in windows(nums2):
                for s1 in seen.get(h, ()):            # verify to kill collisions
                    if nums1[s1:s1 + L] == nums2[start:start + L]:
                        return True
            return False

        lo, hi = 0, min(n, m)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if has_common(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
```

- **Time:** `O((n + m) · log(min(n, m)))` for the binary search; verification is
  rare with a good modulus. (Using a Mersenne prime like `2^61 - 1` with a single
  channel is already very safe.)
- **Space:** `O(n)` for the hash map of `nums1`'s windows.

## Key Insights & Edge Cases

- **Predicate must be monotone** for binary search to be valid — it is, because a
  common block of length `L` contains a common block of every smaller length.
- **`L = 0` is trivially common**; keep it as the lower bound so "no common
  element" correctly returns `0`.
- **Values can be 0.** Offset by `+1` when hashing so a leading `0` does not make
  the fingerprint indistinguishable from a shorter window.
- **Verify on a hash hit** (or use a 61-bit / double hash). Without verification
  a collision could report a length that is not actually achievable, corrupting
  the binary search and *overshooting* the answer.
- **DP is simpler here** at `n, m <= 1000`; reach for binary-search + hashing
  when the array/string is long or when you specifically want the
  longest-common-substring generalization.
