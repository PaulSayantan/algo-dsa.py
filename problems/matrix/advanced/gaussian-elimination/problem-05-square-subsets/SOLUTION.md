# Solution — Square Subsets

## Brute Force

Enumerate all `2^n` subsets, multiply the chosen elements, and test whether the product is
a perfect square (e.g. `isqrt(P)**2 == P`).

- **Time:** `O(2^n * n)` plus big-integer multiplication — impossible for `n` up to `10^5`,
  and products overflow into huge integers.
- **Space:** `O(1)`.

## Optimal Approach (Gaussian Elimination over GF(2))

**Key number-theory fact:** an integer product is a perfect square **iff the exponent of
every prime in its factorization is even.** Only the *parity* of each prime's exponent
matters. Since `nums[i] <= 70`, the relevant primes are those `<= 70`:

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67   (19 primes)
```

Map each value `v` to a **parity vector** `x` over `GF(2)^19`: bit `p` is `1` if prime `p`
divides `v` an odd number of times. Multiplying numbers **adds** exponents, so parities
**XOR**. Therefore:

> A subset has a square product **iff the XOR of its parity vectors is `0`.**

Now it is the same counting problem as "Count Subsets with XOR = 0":

1. Build a **GF(2) linear basis** of the `n` parity vectors via Gaussian elimination; let
   `r` be its rank.
2. The number of subsets (including empty) whose vectors XOR to `0` is `2^(n - r)` by
   rank–nullity (the kernel of the linear map `subset -> XOR`).
3. **Subtract 1** to exclude the empty subset (the problem asks for non-empty subsets).

Answer: `(2^(n - r) - 1) mod (10^9 + 7)`.

### Worked check against the examples

- `[1,1,1,1]`: `1` has the all-zero parity vector, so every vector is `0`; rank `r = 0`.
  Count `= 2^4 - 1 = 15`. ✓
- `[2,2,2,2]`: every vector is the single bit for prime `2`; rank `r = 1`.
  Count `= 2^(4-1) - 1 = 8 - 1 = 7`. ✓
- `[2,3,6]`: vectors are `{2}`, `{3}`, `{2,3}`. Since `{2} XOR {3} = {2,3}`, they are
  dependent; rank `r = 2`. Count `= 2^(3-2) - 1 = 2 - 1 = 1`. ✓

### Reference implementation

```python
from typing import List
MOD = 10**9 + 7
PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]

def parity_vector(v: int) -> int:
    mask = 0
    for i, p in enumerate(PRIMES):
        cnt = 0
        while v % p == 0:
            v //= p
            cnt += 1
        if cnt & 1:
            mask |= 1 << i
    return mask

def count_square_subsets(nums: List[int]) -> int:
    B = len(PRIMES)
    basis = [0] * B
    rank = 0
    for v in nums:
        x = parity_vector(v)
        for bit in range(B - 1, -1, -1):
            if not (x >> bit) & 1:
                continue
            if basis[bit] == 0:
                basis[bit] = x
                rank += 1
                break
            x ^= basis[bit]
        # if x reduces to 0 it adds no pivot (a dependency / free variable)
    return (pow(2, len(nums) - rank, MOD) - 1) % MOD
```

### Complexity

- **Time:** `O(n * P)` to factor each of the `n` values against `P = 19` primes, plus
  `O(n * B)` for basis insertion with `B = 19`. Overall `O(n * P)`.
- **Space:** `O(B)` for the basis (`B = 19` primes).

## Key Insights & Edge Cases

- **Perfect square ⟺ all prime exponents even** — this is the whole reduction; once you see
  "even exponents," GF(2) and XOR follow immediately.
- **Value `1` (and any perfect square like 4, 9, 16, 36, 49, 64)** maps to the all-zero
  vector; each such element can be freely included/excluded and *doubles* the count. This is
  captured automatically: they add no pivot, so they increase `n - r`.
- **Subtract exactly 1**, not more — the empty product is `1` (a square), and it is the only
  subset we must exclude.
- **Modular arithmetic:** compute `pow(2, n - r, MOD)` first, then subtract `1` and take
  `% MOD` again to avoid a negative result when `n - r = 0` (though `r <= n` always, and
  `r <= 19`, so `n - r >= 0`).
- **This is the same engine as Problem 3** (count subsets with a target XOR, here target
  `0`); only the vector-construction step (prime parities) is new.
