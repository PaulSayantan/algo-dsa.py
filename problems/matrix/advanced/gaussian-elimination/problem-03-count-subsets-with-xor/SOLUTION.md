# Solution — Count Subsets with a Given XOR

## Brute Force

Enumerate all `2^n` subsets, XOR each, and count matches with `k`.

- **Time:** `O(2^n * n)` — impossible for `n` up to `10^5`.
- **Space:** `O(1)`.

A DP over "number of elements considered" × "current XOR" runs in
`O(n * 2^B)` (where `B` is the bit width) and works for small `B`, but the linear-algebra
view below is faster and reveals the structure.

## Optimal Approach (Gaussian Elimination over GF(2))

The set of subset-XORs is the **linear span** of `nums` over `GF(2)`. Let `r` be the
**rank** of that span (the number of pivots you get from Gaussian elimination). The key
counting fact:

> If `k` is in the span, **exactly `2^(n - r)` subsets** XOR to `k`.
> If `k` is not in the span, **no** subset does (answer `0`).

### Why `2^(n - r)`

Consider a maximal independent set of `r` elements (the pivots). Any of the remaining
`n - r` elements is a linear combination of pivots, i.e. it adds a *dependency*. Formally,
the map `subset -> XOR` is a linear map from `GF(2)^n` onto the span (dimension `r`). By the
rank–nullity theorem its kernel has size `2^(n - r)`: there are `2^(n-r)` subsets that XOR
to `0`. Since the map is linear, every value it *does* hit is hit by a coset of the kernel,
which has the same size `2^(n - r)`. Hence every reachable target — including `k` — is
produced by exactly `2^(n-r)` subsets. This is why Examples 1 and 2 both give `2`
(`n = 3`, `r = 2`, so `2^(3-2) = 2`).

### Algorithm

1. Insert each `nums[i]` into a GF(2) basis (same reduction as the max-XOR problem):
   ```
   for bit high..low:
       if bit not set in x: continue
       if basis[bit] == 0: basis[bit] = x; break
       x ^= basis[bit]
   ```
   The number of non-zero `basis[bit]` entries is the rank `r`.
2. **Membership test:** reduce `k` by the basis exactly the same way. If it reduces to `0`,
   `k` is in the span; otherwise it is not.
3. Return `pow(2, n - r, MOD)` if `k` is reachable, else `0`.

### Reference implementation

```python
from typing import List
MOD = 10**9 + 7

def count_subsets_with_xor(nums: List[int], k: int) -> int:
    BITS = 20
    basis = [0] * (BITS + 1)
    rank = 0
    for x in nums:
        cur = x
        for bit in range(BITS, -1, -1):
            if not (cur >> bit) & 1:
                continue
            if basis[bit] == 0:
                basis[bit] = cur
                rank += 1
                break
            cur ^= basis[bit]
    # Is k in the span?
    cur = k
    for bit in range(BITS, -1, -1):
        if (cur >> bit) & 1 and basis[bit]:
            cur ^= basis[bit]
    if cur != 0:
        return 0
    return pow(2, len(nums) - rank, MOD)
```

### Complexity

- **Time:** `O(n * B)` to build the basis plus `O(B)` for the membership test.
- **Space:** `O(B)`.

## Key Insights & Edge Cases

- **`k = 0` always has an answer of at least 1** (the empty subset). With `n = r` (all
  elements independent) the answer is `2^0 = 1`.
- **Every reachable target has the same count.** The count depends only on the *rank*, not
  on `k`, so long as `k` is in the span.
- **Duplicates matter for counting but not for the basis.** A duplicate reduces to `0`
  during insertion (adding no pivot), which increases `n - r` by one and hence *doubles*
  the count — exactly right, since the duplicate can be freely included or excluded.
- **Watch the exponent modulus:** use fast modular exponentiation (`pow(2, n-r, MOD)`);
  `n - r` can be up to `10^5`.
- **Membership order:** always reduce from the highest bit down using the pivot stored at
  that bit — this mirrors the forward-elimination order.
