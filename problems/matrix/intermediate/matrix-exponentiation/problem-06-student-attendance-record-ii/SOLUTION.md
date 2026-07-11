# Solution — Student Attendance Record II

## Brute Force

A linear DP over the length with a small state. The state captures everything about a prefix
that constrains the next character:

- `a` = number of `'A'` used so far, in `{0, 1}` (2 must never be reached),
- `l` = length of the current trailing run of `'L'`, in `{0, 1, 2}` (3 must never be reached).

That is `2 × 3 = 6` states. Index them `s = a * 3 + l`. From each prefix we may append:

- `'P'` → resets the L-run: `(a, l) -> (a, 0)`,
- `'A'` → only allowed if `a == 0`; adds an absence and resets the L-run: `(0, l) -> (1, 0)`,
- `'L'` → only allowed if `l < 2`: `(a, l) -> (a, l + 1)`.

```python
def checkRecord(n):
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, a, l):
        if i == n:
            return 1
        total = dp(i + 1, a, 0)            # append 'P'
        if a == 0:
            total += dp(i + 1, 1, 0)       # append 'A'
        if l < 2:
            total += dp(i + 1, a, l + 1)   # append 'L'
        return total % MOD
    return dp(0, 0, 0)
```

- **Time:** `O(n)` (6 states, constant transitions each).
- **Space:** `O(n)` for recursion (or `O(1)` iterative).

Accepted on the original LeetCode 552 (`n <= 10^5`), but too slow for `n` up to `10^18`.

## Optimal Approach — Matrix Exponentiation

### The 6-state transition matrix

Order the states as `[ (0,0), (0,1), (0,2), (1,0), (1,1), (1,2) ]` (indices 0..5, with
`s = a*3 + l`). We want a matrix `M` such that if `v_t` is the column vector of counts of
prefixes of length `t` in each state, then `v_{t+1} = M · v_t`. Entry `M[new][old]` is the
number of characters that move a prefix from state `old` to state `new` (0 or 1 here).

Working out every transition (rows = new state, columns = old state):

```
             from:  (0,0)(0,1)(0,2)(1,0)(1,1)(1,2)
   to (0,0)  [       1    1    1    0    0    0  ]   P from any a=0 state
   to (0,1)  [       1    0    0    0    0    0  ]   L from (0,0)
   to (0,2)  [       0    1    0    0    0    0  ]   L from (0,1)
   to (1,0)  [       1    1    1    1    1    1  ]   A from any a=0 state, P from any a=1 state
   to (1,1)  [       0    0    0    1    0    0  ]   L from (1,0)
   to (1,2)  [       0    0    0    0    1    0  ]   L from (1,1)
```

Reading the rows:

- **`(0,0)`** (still 0 absences, no trailing L) is reached by appending `'P'` to any of the
  three `a = 0` states → ones in columns `(0,0),(0,1),(0,2)`.
- **`(0,1)`** is reached by appending `'L'` to `(0,0)`.
- **`(0,2)`** is reached by appending `'L'` to `(0,1)`.
- **`(1,0)`** (exactly 1 absence, no trailing L) is reached by appending `'A'` to an `a = 0`
  state (columns `(0,0),(0,1),(0,2)`) **or** appending `'P'` to an `a = 1` state (columns
  `(1,0),(1,1),(1,2)`) → all six columns are 1.
- **`(1,1)`** is reached by appending `'L'` to `(1,0)`.
- **`(1,2)`** is reached by appending `'L'` to `(1,1)`.

Transitions that would reach a forbidden state (a second `'A'`, or a third consecutive `'L'`)
are simply omitted — the corresponding count is dropped.

### Putting it together

- Start state (empty prefix): `v_0 = [1, 0, 0, 0, 0, 0]^T` (0 absences, 0 trailing L).
- After `n` appended characters: `v_n = M^n · v_0`.
- Answer: the sum of all entries of `v_n` (every non-forbidden ending state is valid).

Because `v_0` is the first unit vector, `v_n` is exactly **column 0 of `M^n`**, so the answer
is the sum of the entries in column 0 of `M^n`.

Compute `M^n` with fast exponentiation: `O(log n)` products of 6×6 matrices.

### Why it is correct

The six states form a complete, minimal description of every constraint-relevant fact about a
prefix. Each legal append is a deterministic state change, so `M` linearly maps the length-`t`
count distribution to the length-`(t+1)` distribution. Any string that would violate a rule
leads to a state we never include, so it is never counted. Associativity gives `M^n` for `n`
characters.

### Sanity check

- `n = 1`: `v_1 = M · v_0 = [1, 1, 0, 1, 0, 0]^T`, summing to `3` — the records `P`, `L`, `A`.
- `n = 2`: sums to `8`. `n = 3`: sums to `19`. All match the examples.

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
    def checkRecord(self, n: int) -> int:
        M = [
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        P = mat_pow(M, n)
        # v0 = [1,0,0,0,0,0]^T  =>  v_n = column 0 of P
        return sum(P[i][0] for i in range(6)) % MOD
```

- **Time:** `O(k^3 log n)` with `k = 6`, i.e. `O(216 log n) = O(log n)`.
- **Space:** `O(k^2) = O(1)`.

## Key Insights & Edge Cases

- **Choosing the state is the whole problem.** Once you realize only "A-count (capped at 1)"
  and "trailing L-run (capped at 2)" matter, the automaton has just 6 states and the matrix
  writes itself. Forbidden transitions (2nd `A`, 3rd `L`) are dropped, which is exactly how the
  constraints are enforced.
- **Direction of the matrix.** `M[new][old]` counts characters taking `old -> new`. If you
  instead think in terms of `old -> new` as rows, you will build the transpose; verify against
  `n = 1` (answer must be 3) to catch this.
- **Reading the result.** Since the start is a single unit vector, the answer is the sum of one
  column of `M^n`; alternatively multiply `M^n` by `v_0` explicitly and sum. Both are correct.
- **`n = 1`** must give 3, and `M^1 = M`; make sure your fast-power loop handles a single set
  bit correctly.
- **Modulus.** Reduce after each multiply-add. With `k = 6`, each entry sums at most 6 products
  of values `< 10^9`, which is safe in 64-bit integers.
- **Relation to the `O(n)` DP.** The 6-variable rolling DP and this matrix are the same
  recurrence; matrix exponentiation just applies `n` steps of it in `O(log n)` instead of
  `O(n)`.
