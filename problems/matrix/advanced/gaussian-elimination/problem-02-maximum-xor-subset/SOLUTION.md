# Solution — Maximum XOR of a Subset

## Brute Force

Enumerate all `2^n` subsets, XOR each, and track the maximum.

- **Time:** `O(2^n * n)` — infeasible past `n ~ 20`.
- **Space:** `O(1)` (or `O(n)` for recursion).

## Optimal Approach (Gaussian Elimination over GF(2))

Think of each integer as a vector over the field `GF(2)` (bit `k` is coordinate `k`). The
set of all achievable subset-XORs is exactly the **linear span** of `nums` over `GF(2)`.
Gaussian elimination lets us compute a **basis** of that span, and from a basis the maximum
element is found greedily.

### Building the basis (row reduction)

Keep an array `basis` indexed by bit position. To insert a value `x`:

```
for bit from high to low:
    if bit not set in x: continue
    if basis[bit] == 0:      # new pivot at this bit
        basis[bit] = x
        break
    x ^= basis[bit]          # eliminate this bit, keep reducing
# if x becomes 0 it was already representable -> add nothing
```

This is precisely Gaussian elimination: `basis[bit]` is the pivot row whose leading
(highest) set bit is `bit`, and `x ^= basis[bit]` is the row operation "add pivot row to
current row" (addition = XOR over GF(2)). The number of non-zero pivots is the **rank**.

### Maximizing

Once the basis is built, start with `answer = 0` and walk bits high to low. If XOR-ing in
`basis[bit]` would *increase* `answer`, do it:

```
answer = 0
for bit from high to low:
    if basis[bit] and (answer ^ basis[bit]) > answer:
        answer ^= basis[bit]
return answer
```

Because each basis vector's leading bit is unique, taking a vector when it flips a
currently-`0` high bit to `1` can only increase the value — the classic greedy on a
reduced basis is optimal.

### Reference implementation

```python
from typing import List

def max_subset_xor(nums: List[int]) -> int:
    BITS = 60
    basis = [0] * (BITS + 1)
    for x in nums:
        for bit in range(BITS, -1, -1):
            if not (x >> bit) & 1:
                continue
            if basis[bit] == 0:
                basis[bit] = x
                break
            x ^= basis[bit]
    ans = 0
    for bit in range(BITS, -1, -1):
        if basis[bit] and (ans ^ basis[bit]) > ans:
            ans ^= basis[bit]
    return ans
```

### Complexity

- **Time:** `O(n * B)` where `B` is the bit width (~60). Each insert does at most `B` XOR
  steps.
- **Space:** `O(B)` for the basis.

## Key Insights & Edge Cases

- **The basis is the compressed form of Gaussian elimination.** `basis[bit]` plays the role
  of a pivot row; each entry has a distinct leading bit, so the basis is already in
  echelon form.
- **Empty subset:** the answer is never negative; if all numbers are `0` the basis is empty
  and the greedy returns `0` (Example 3).
- **Reduced basis variant:** you can additionally XOR each new pivot into existing basis
  vectors to fully reduce (Gauss–Jordan), which makes some queries simpler, but is not
  required just to maximize.
- **Duplicates and zeros** insert nothing new — they reduce to `0` against the existing
  basis, which is correct because they add no new span.
- **Bit width:** size the basis to cover the largest possible input bit (here 60 for
  `nums[i] < 2^60`).
