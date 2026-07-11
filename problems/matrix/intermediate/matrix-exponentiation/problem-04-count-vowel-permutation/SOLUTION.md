# Solution — Count Vowel Permutation

## Brute Force

A linear DP over the length. Let `dp[v]` be the number of valid strings of the current length
that **end** in vowel `v` (order `[a, e, i, o, u]`). Initialize all to `1` (length-1 strings),
then extend `n-1` times using the "who can precede whom" rule:

```python
def countVowelPermutation(n):
    a = e = i = o = u = 1
    for _ in range(n - 1):
        a, e, i, o, u = (
            (e + i + u) % MOD,   # a can be preceded by e, i, u
            (a + i) % MOD,       # e   "        "     "  a, i
            (e + o) % MOD,       # i   "        "     "  e, o
            (i) % MOD,           # o   "        "     "  i
            (i + o) % MOD,       # u   "        "     "  i, o
        )
    return (a + e + i + o + u) % MOD
```

- **Time:** `O(n)`.
- **Space:** `O(1)`.

This is the accepted LeetCode-1220 solution (where `n <= 2·10^4`). For the large-`n` variant
here (`n` up to `10^18`) it is far too slow.

## Optimal Approach — Matrix Exponentiation

### Deriving the transition matrix

Each rule says which vowel may **follow** another. To grow the counts we need, for each target
vowel `x`, the set of vowels that may *precede* it (i.e. that can be followed by `x`):

- `a` follows `e`, `i`, `u`  →  `new_a = e + i + u`
- `e` follows `a`, `i`       →  `new_e = a + i`
- `i` follows `e`, `o`       →  `new_i = e + o`
- `o` follows `i`            →  `new_o = i`
- `u` follows `i`, `o`       →  `new_u = i + o`

With the state vector `v = [a, e, i, o, u]^T`, one extension step is `v' = M · v` where

```
      a  e  i  o  u
a  [  0  1  1  0  1 ]
e  [  1  0  1  0  0 ]
M = i  [  0  1  0  1  0 ]
o  [  0  0  1  0  0 ]
u  [  0  0  1  1  0 ]
```

Row `x` of `M` has a `1` in column `y` exactly when vowel `y` may be followed by vowel `x`.

### Putting it together

- The length-1 state is `v_1 = [1, 1, 1, 1, 1]^T`.
- After `n-1` extensions, `v_n = M^(n-1) · v_1`.
- The answer is the sum of the entries of `v_n`.

Compute `M^(n-1)` with fast exponentiation: `O(log n)` multiplications of 5×5 matrices.

### Why it is correct

`M` linearly maps "counts by ending vowel at length `L`" to the same counts at length `L+1`,
because every valid length-`(L+1)` string is a valid length-`L` string plus one appended vowel
allowed by the adjacency rule, and the mapping counts exactly those extensions. Associativity
of matrix multiplication then gives `M^(n-1)` for `n-1` steps.

### Sanity check (n = 2)

`M · [1,1,1,1,1]^T = [3, 2, 2, 1, 2]^T`, summing to `3+2+2+1+2 = 10` — matching Example 2.

### Reference implementation

```python
MOD = 10**9 + 7

def mat_mult(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if A[i][k]:
                a = A[i][k]
                for j in range(m):
                    C[i][j] = (C[i][j] + a * B[k][j]) % MOD
    return C

def mat_pow(M, p):
    n = len(M)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while p:
        if p & 1:
            R = mat_mult(R, M)
        M = mat_mult(M, M)
        p >>= 1
    return R

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = [
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0],
        ]
        P = mat_pow(M, n - 1)
        # multiply P by the all-ones vector = sum of every entry of P
        return sum(sum(row) for row in P) % MOD
```

Because the initial vector is all-ones, `sum(v_n) = sum of all entries of M^(n-1)`, which is
why the code just sums the whole powered matrix.

- **Time:** `O(k^3 log n)` with `k = 5`, i.e. `O(125 log n) = O(log n)`.
- **Space:** `O(k^2) = O(1)`.

## Key Insights & Edge Cases

- **Direction matters:** the matrix uses "who may *precede* `x`", the transpose of the raw
  "who may follow" rules. Getting this backwards is the most common bug; verify against `n = 2`.
- **`n = 1`:** `M^0 = I`, and `sum(I) = 5`, giving the correct answer `5` with no special case.
- **Two equivalent readouts:** either sum all entries of `M^(n-1)` (because `v_1` is all-ones),
  or explicitly compute `M^(n-1) · v_1` and sum that vector — both give the same result.
- **Modulus:** reduce every product/sum; in 64-bit languages the intermediate products stay
  safe since `k = 5` means at most 5 added products of values `< 10^9`.
- **Same template, different automaton:** this is the general "count length-`n` sequences under
  fixed adjacency constraints" pattern — see also Knight Dialer and Student Attendance Record II.
