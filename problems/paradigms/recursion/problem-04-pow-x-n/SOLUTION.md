# Pow(x, n) — Solution

## Brute Force

Multiply `x` by itself `|n|` times in a loop, then take the reciprocal if `n` was
negative.

```python
def myPow(x, n):
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    for _ in range(n):
        result *= x
    return result
```

- **Time:** `O(n)` — `n` multiplications, which for `n` up to `2^31` is far too slow.
- **Space:** `O(1)`.

The linear approach ignores the self-similarity in exponentiation. We can do
exponentially better.

## Optimal Approach (Recursion — Fast Exponentiation)

The key identity: `x^n = (x^(n/2))^2`. If `n` is even, `x^n = (x^(n/2))^2` exactly. If
`n` is odd, `x^n = (x^(n//2))^2 * x`. Computing the half power **once** and squaring it
means each recursive step *halves* the exponent, so the recursion depth is `O(log n)`.

Handle the sign of `n` up front: `x^(-n) = 1 / x^n`.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base, exp):
            if exp == 0:                 # base case: anything^0 = 1
                return 1.0
            half = fast_pow(base, exp // 2)   # compute x^(exp/2) ONCE
            if exp % 2 == 0:
                return half * half
            return half * half * base    # odd exponent: one extra factor

        if n < 0:
            return 1.0 / fast_pow(x, -n)
        return fast_pow(x, n)
```

**Why it is correct:** By induction on `exp`. Base case `exp == 0` returns `1.0`
correctly. For `exp > 0`, assume `fast_pow(base, exp // 2)` returns `base^(exp//2)`.
If `exp` is even, `exp = 2 * (exp//2)`, so `half * half = base^exp`. If `exp` is odd,
`exp = 2 * (exp//2) + 1`, so `half * half * base = base^exp`. Because we bind `half`
to a single recursive call and reuse it, we never recompute the subproblem.

**Step by step for `x = 2, n = 10`:**

1. `fast_pow(2, 10)` → `half = fast_pow(2, 5)`.
2. `fast_pow(2, 5)` → `half = fast_pow(2, 2)`; odd, so result = `half^2 * 2`.
3. `fast_pow(2, 2)` → `half = fast_pow(2, 1)`; even, so result = `half^2`.
4. `fast_pow(2, 1)` → `half = fast_pow(2, 0) = 1`; odd, so result = `1 * 1 * 2 = 2`.
5. Unwind: `fast_pow(2,2) = 2^2 = 4`; `fast_pow(2,5) = 4^2 * 2 = 32`;
   `fast_pow(2,10) = 32^2 = 1024`. ✓

- **Time:** `O(log n)` — the exponent halves each call.
- **Space:** `O(log n)` — recursion depth.

## Key Insights & Edge Cases

- **Compute the half power once.** Writing `fast_pow(base, exp//2) * fast_pow(base,
  exp//2)` instead of binding `half` recreates the `O(n)` blowup — the whole speedup
  depends on reusing the single subproblem result.
- **Negative exponents:** convert with the reciprocal *outside* the recursion so the
  recursive helper only ever sees non-negative exponents. Doing `x, n = 1/x, -n`
  in-line also works.
- **`n = 0`** is the base case → `1.0` (even `0^0` is returned as `1.0` here, matching
  the problem's expectations).
- **Overflow of `-n`:** in languages with fixed-width ints, negating `-2^31` overflows;
  Python's arbitrary-precision ints make `-n` safe. In C++/Java you would widen `n` to
  a `long` before negating.
- This "halve the exponent" pattern generalizes to **matrix exponentiation** (e.g.
  computing Fibonacci in `O(log n)`) and modular exponentiation in cryptography.
