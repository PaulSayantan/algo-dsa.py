# Solution — Operations to Make GCD Array Uniform

## Brute Force

Literally simulate the operation: each round replaces `a[i]` with
`gcd(a[i], a[(i+1) % n])` and you stop when all entries are equal.

- Each round is O(n · log M); the array can take up to `n - 1` rounds to stabilize.
- **Time:** O(n^2 · log M). **Space:** O(n).

For `n = 2 * 10^5` this is ~`4 * 10^10` gcd calls — far too slow.

## Optimal Approach (Sparse Table over gcd on the doubled array)

### The reformulation

The crucial observation: after `k` operations, the value at index `i` equals the gcd of
the cyclic window `a[i], a[i+1], ..., a[i+k]` (length `k + 1`). This is provable by
induction — one operation combines a window with the next neighbor, extending its
length by one. Since gcd is associative and commutative, `k` operations fold together a
window of `k + 1` consecutive elements.

The whole array becomes uniform exactly when every window of length `k + 1` collapses
to the global gcd `G = gcd(a[0..n-1])`. (Any window's gcd is a multiple of `G`, and it
can only reach `G`; once a window spans enough elements it equals `G`.) So:

```
answer = ( max over all starts i of  minLen(i) ) - 1
```

where `minLen(i)` is the shortest window length starting at `i` whose gcd equals `G`.
If the array is already uniform, every `minLen(i) = 1` and the answer is `0`.

### Handling the cyclic wrap

Cyclic windows are awkward. **Duplicate** the array: `doubled = a + a` (length `2n`).
A cyclic window of length `L <= n` starting at `i` is exactly the ordinary subarray
`doubled[i .. i + L - 1]`. We only need window lengths up to `n` (a length-`n` window
always equals `G`), so indices stay within `[0, 2n)`.

### The Sparse Table

gcd is **idempotent** and associative, so build a Sparse Table over `doubled`:

```
sp[j][i] = gcd( doubled[i .. i + 2^j - 1] )
```

Then `gcd(doubled[l..r])` is an O(1) query.

### Finding minLen(i)

For a fixed start `i`, `gcd(doubled[i .. i + L - 1])` is **non-increasing** in `L`
(adding elements can only shrink the gcd) and bottoms out at `G`. So the set of lengths
reaching `G` is a suffix `[minLen(i), n]`, and we **binary search** the smallest `L` in
`[1, n]` with `gcd(doubled[i .. i + L - 1]) == G`. Each candidate is one O(1) query, so
`minLen(i)` costs O(log n).

### Putting it together

```
answer = max_i minLen(i) - 1
```

- Build: O(n log n · log M).  Per start: O(log n) queries → O(n log n) total.
- **Overall time:** O(n log n).  **Space:** O(n log n).

### Why it is correct

- The reformulation (proved by induction) turns "operations" into "window lengths".
- gcd idempotency makes the overlapping-block query exact.
- Monotonicity of gcd in window length justifies the binary search.
- Taking the max over starts picks the slowest-converging position, which determines
  when the *entire* array is uniform; subtracting 1 converts window length to operation
  count.

### Reference implementation

```python
from math import gcd
from functools import reduce
from typing import List


class SparseTableGCD:
    def __init__(self, nums: List[int]) -> None:
        n = len(nums)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        K = self.log[n] + 1 if n else 1
        self.sp = [[0] * n for _ in range(K)]
        self.sp[0] = nums[:]
        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                self.sp[j][i] = gcd(self.sp[j - 1][i], self.sp[j - 1][i + half])
            j += 1

    def query(self, l: int, r: int) -> int:
        k = self.log[r - l + 1]
        return gcd(self.sp[k][l], self.sp[k][r - (1 << k) + 1])


class Solution:
    def min_operations_to_uniform_gcd(self, a: List[int]) -> int:
        n = len(a)
        G = reduce(gcd, a)
        doubled = a + a
        st = SparseTableGCD(doubled)

        best_len = 1
        for i in range(n):
            lo, hi, ans = 1, n, n
            while lo <= hi:
                mid = (lo + hi) // 2          # window length
                if st.query(i, i + mid - 1) == G:
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            best_len = max(best_len, ans)
        return best_len - 1
```

## Key Insights & Edge Cases

- **Doubling the array** is the standard trick to make cyclic ranges into linear ranges;
  it also caps the needed length at `n`.
- **Already-uniform input** (all equal) yields `best_len = 1`, so the answer is `0`.
- **gcd monotonicity + idempotency** are both essential: monotonicity for the binary
  search, idempotency for the O(1) overlapping-block query.
- **Values up to 10^6** keep each gcd cheap; the `log M` factor is small.
- **The final value is always `G`** — no window can go below the global gcd, and a full
  wrap-around window equals `G`, guaranteeing the search terminates within length `n`.
- **No updates** — the structure is rebuilt from scratch if the array changes.
