# Solution — Knight Dialer

## Brute Force

A linear DP over the length. Let `dp[d]` be the number of valid numbers of the current length
that **end** on digit `d`. Start with `dp[d] = 1` for all digits (length-1 numbers), then
apply the knight moves `n-1` times:

```python
MOVES = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9],
         5:[],    6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}

def knightDialer(n):
    dp = [1] * 10
    for _ in range(n - 1):
        nxt = [0] * 10
        for d in range(10):
            for e in MOVES[d]:
                nxt[e] = (nxt[e] + dp[d]) % MOD
        dp = nxt
    return sum(dp) % MOD
```

- **Time:** `O(n)` (constant work per step, since the number of moves is bounded).
- **Space:** `O(1)`.

Accepted on the original LeetCode 935 (`n <= 5000`). For the large-`n` variant here it is
too slow.

## Optimal Approach — Matrix Exponentiation

### The transition matrix

Define a 10×10 matrix `M` where `M[e][d] = 1` if digit `d` can jump to digit `e` (i.e. `e` is
in `MOVES[d]`), else `0`. With the state vector `v = [dp[0], dp[1], ..., dp[9]]^T`, one appended
digit is `v' = M · v`, because

```
dp_new[e] = sum over all d that can reach e of dp_old[d].
```

Concretely, column `d` of `M` marks the digits reachable from `d`; equivalently row `e` marks
the digits that can reach `e`. (The knight-move graph is symmetric, so `M` is symmetric and it
does not matter which convention you pick — but be consistent.)

### Putting it together

- Length-1 state: `v_1 = [1,1,1,1,1,1,1,1,1,1]^T`.
- After `n-1` jumps: `v_n = M^(n-1) · v_1`.
- Answer: sum of the entries of `v_n`.

Compute `M^(n-1)` by fast exponentiation — `O(log n)` products of 10×10 matrices.

### Why it is correct

`M` linearly maps the count-by-ending-digit distribution at length `L` to the distribution at
length `L+1`, since every valid length-`(L+1)` number is a valid length-`L` number plus one
appended digit reachable by a knight move. Associativity gives `M^(n-1)` for `n-1` appended
digits. Digit `5` naturally drops out: it has no outgoing moves, so once you must append after
it, its contribution disappears — the matrix encodes this automatically (`M`'s column for `5`
is all zeros).

### Sanity check

`n = 1`: `M^0 = I`, sum of `I·v_1 = v_1` is `10`. `n = 2`: `M·v_1` sums the out-degrees of all
digits: `2+2+2+2+3+0+3+2+2+2 = 20`. `n = 3` gives `46`. All match the examples.

### Reference implementation

```python
MOD = 10**9 + 7

MOVES = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9],
         5:[],    6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}

def build_matrix():
    M = [[0] * 10 for _ in range(10)]
    for d in range(10):
        for e in MOVES[d]:
            M[e][d] = 1        # from d we can reach e
    return M

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
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        P = mat_pow(build_matrix(), n - 1)
        return sum(sum(row) for row in P) % MOD
```

- **Time:** `O(k^3 log n)` with `k = 10`, i.e. `O(1000 log n) = O(log n)`.
- **Space:** `O(k^2) = O(1)`.

## Key Insights & Edge Cases

- **`n = 1` returns `10`:** all ten digits are valid length-1 numbers. `M^0 = I` handles this
  automatically, but an explicit guard is clear.
- **Digit 5 is a dead end:** it has no knight moves out, so for `n >= 2` no valid number can
  have `5` anywhere except potentially as the final digit — and since nothing jumps *into* 5
  either (5 is not in any `MOVES` list), 5 only ever appears in length-1 numbers. The matrix
  captures this with an all-zero row and column for index 5.
- **Symmetric graph:** knight moves are reversible, so `M` is symmetric; summing all entries of
  `M^(n-1)` equals `sum(M^(n-1) · v_1)` because `v_1` is all-ones.
- **Modulus:** reduce after each multiply-add; with `k = 10`, each entry sums at most 10
  products of values `< 10^9`, safe in 64-bit.
- **Same template as Count Vowel Permutation:** only the adjacency (the automaton) changes; the
  matrix-power machinery is identical.
