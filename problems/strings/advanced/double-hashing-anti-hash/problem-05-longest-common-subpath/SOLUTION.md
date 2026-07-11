# Solution — Longest Common Subpath

## Brute Force

For every length `L` (from the shortest path's length down to 1), collect the
set of all length-`L` contiguous blocks (as tuples of ints) from every path and
intersect the sets. Return the first `L` whose intersection is non-empty.

- **Time:** `O(L_max * S * L)` where `S` is the total number of elements — each
  window is materialized as a tuple of length `L`, so with many paths this is
  roughly `O(S * L_max^2)`. For `S` up to `10^5` and `L_max` up to `10^5` this
  is astronomically slow.
- **Space:** enormous — every window stored as a full tuple.

## Optimal Approach (Binary Search on Length + Double Hashing)

### Monotonicity -> binary search

If a subpath of length `L` is common to all paths, its length-`(L-1)` prefix is
also common. So `common(L)` is **monotone**, and we binary search the largest
`L` in `[1, minLen]` (where `minLen = min(len(p) for p in paths)`).

### Testing common(L) with hashing

Treat each path as a string over the alphabet of city ids and use a polynomial
hash with a **base `> n`** so each city id is a valid digit. For a fixed `L`:

- For each path, roll a length-`L` window across it, producing the set of hash
  pairs `(v1, v2)` for that path.
- Intersect the sets across all paths. `common(L)` is true iff the final
  intersection is non-empty.

Rolling one window to the next is `O(1)`:

```
h_new = ( (h_old - path[i]*B^(L-1)) * B + path[i+L] ) mod M
```

so each path costs `O(len)` and one `common(L)` evaluation costs
`O(S)` where `S = sum of path lengths`. With `O(log minLen)` evaluations the
total is `O(S log minLen)`.

### Why double hashing is essential here

We are intersecting hash sets built from **many different arrays** whose total
size is up to `10^5`, across `O(log n)` binary-search levels. A single-modulus
collision between a window in path A and an unrelated window in path B would
make them look identical, and the intersection would wrongly report a common
subpath that does not exist — a wrong answer. Two independent `~10^9` moduli
push the cross-array false-match probability to `~1/10^18`. LeetCode 1923 is
notorious for failing single-hash submissions; double hashing is the intended,
robust fix.

### Steps

1. `minLen = min(len(p) for p in paths)`; if `minLen == 0` return `0`.
2. Binary search `lo = 1`, `hi = minLen`:
   - `mid = (lo + hi + 1) // 2`,
   - if `common(mid)`: `best = mid`, `lo = mid + 1`; else `hi = mid - 1`.
3. Return `best` (initialized to `0`).

### Reference implementation

```python
from typing import List


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        MODS = (1_000_000_007, 998_244_353)
        BASES = (100_003, 100_019)   # both > n (n <= 1e5)

        def window_hashes(path, L):
            hs = set()
            for k in range(2):
                mod, base = MODS[k], BASES[k]
                top = pow(base, L - 1, mod)
                h = 0
                for i in range(L):
                    h = (h * base + path[i]) % mod
                per_k = [h]
                for i in range(L, len(path)):
                    h = ((h - path[i - L] * top) * base + path[i]) % mod
                    per_k.append(h)
                if k == 0:
                    first = per_k
                else:
                    second = per_k
            return set(zip(first, second))

        def common(L):
            acc = None
            for path in paths:
                if len(path) < L:
                    return False
                cur = window_hashes(path, L)
                acc = cur if acc is None else (acc & cur)
                if not acc:
                    return False
            return bool(acc)

        minLen = min(len(p) for p in paths)
        lo, hi, best = 1, minLen, 0
        while lo <= hi:
            mid = (lo + hi + 1) // 2
            if common(mid):
                best = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return best
```

- **Time:** `O(S log minLen)` where `S` is the sum of path lengths.
- **Space:** `O(S)` for the per-level hash sets.

## Key Insights & Edge Cases

- **Base must exceed `n`** so distinct city ids never alias to the same digit;
  using ordinary character bases (like 131) would be unsafe for large ids.
- **Intersect against the running accumulator** and bail out the moment it
  becomes empty — this prunes work when paths diverge early.
- **A path shorter than `L`** immediately makes `common(L)` false; guard with a
  length check.
- **No shared city** (e.g. `[[0],[1],[2]]`): `common(1)` already fails, so
  `best` stays `0`.
- **Reverse paths** (`[0,1,2,3,4]` vs `[4,3,2,1,0]`) share only single cities,
  giving `1` — the algorithm handles this because a length-1 window is still a
  valid subpath.
- Recomputing `B^(L-1)` per level via `pow(base, L-1, mod)` is fine; you can
  also precompute a global power table once and index into it.
- This is the archetypal multi-sequence anti-hash problem: the whole correctness
  argument rests on collisions across arrays being negligible, which only two
  moduli deliver.
