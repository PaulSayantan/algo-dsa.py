# Solution — k-Mismatch Search (Hamming Distance)

## Brute Force

For every window, count mismatching positions and keep the window if the count is
`<= k`.

```python
def k_mismatch_search(text, pattern, k):
    n, m = len(text), len(pattern)
    res = []
    for i in range(n - m + 1):
        dist = sum(1 for j in range(m) if text[i + j] != pattern[j])
        if dist <= k:
            res.append(i)
    return res
```

- **Time:** `O(n * m)` — each of `~n` windows costs `O(m)`.
- **Space:** `O(1)` extra.

## Optimal Approach — Bit-parallel Shift-And ladder

We extend Shift-And to tolerate substitutions by running a **ladder of `k+1` state
words** `R[0], R[1], ..., R[k]`:

> **Invariant:** after reading `text[0..i]`, bit `j` of `R[d]` is set iff a prefix
> `pattern[0..j]` can be aligned to end at `i` using **at most `d` substitutions**.

`R[0]` is exactly the exact-match automaton. For `d >= 1`, a prefix of length `j+1`
matches with `<= d` errors ending at `i` if **either**:

1. it matched with `<= d` errors ending at `i-1` and `pattern[j] == text[i]`
   (a normal match) — the term `((R_old[d] << 1) | 1) & B[c]`, **or**
2. the prefix of length `j` matched with `<= d-1` errors ending at `i-1`, and we
   spend one more substitution to accept `text[i]` no matter what it is — the term
   `(R_old[d-1] << 1) | 1` (advance **without** the `& B[c]` filter).

Combine them:

```
R[d] = (((R_old[d] << 1) | 1) & B[c])   |   ((R_old[d-1] << 1) | 1)
```

The `| 1` seeds a fresh start at position 0 for each level. Use a snapshot
`R_old = R[:]` so level `d` reads the *previous* step's values of `d` and `d-1`.

A window ends at `i` (start `i - m + 1`) within `k` mismatches exactly when bit
`m-1` of `R[k]` is set.

### Reference implementation

```python
from typing import List

def k_mismatch_search(text: str, pattern: str, k: int) -> List[int]:
    m = len(pattern)
    res: List[int] = []
    if m == 0:
        return res
    B = {}
    for j, c in enumerate(pattern):
        B[c] = B.get(c, 0) | (1 << j)
    R = [0] * (k + 1)
    match_bit = 1 << (m - 1)
    for i, c in enumerate(text):
        bc = B.get(c, 0)
        old = R[:]                          # snapshot of the previous step
        R[0] = ((old[0] << 1) | 1) & bc
        for d in range(1, k + 1):
            R[d] = (((old[d] << 1) | 1) & bc) | ((old[d - 1] << 1) | 1)
        if R[k] & match_bit:
            res.append(i - m + 1)
    return res
```

### Why it is correct

By induction on `i` and `d`. Level 0 is the proven exact automaton. For level `d`,
the two OR-ed terms enumerate the only two ways a length-`(j+1)` prefix can end at
`i` with `<= d` substitutions: match the current char (case 1), or substitute it
(case 2, which consumes one of the `d` allowed errors and hence draws from level
`d-1`). Since Hamming distance only allows same-length substitutions, there is no
insert/delete term. Therefore `R[k]`'s top bit is set iff some length-`m` window
ending at `i` is within `k` mismatches.

### Complexity

- **Time:** `O(n * k * ceil(m/w))`; with `m <= w` this is `O(n * k)`.
- **Space:** `O(k)` state words plus `O(sigma)` masks.

## Key Insights & Edge Cases

- **`k = 0`** collapses the ladder to a single word — plain Shift-And exact match.
- **`k >= m`** makes every window trivially match (you can substitute all `m`
  characters); the code still returns all start indices correctly.
- **Fixed-length semantics:** because both terms shift by 1 each step, all levels
  track prefixes of the *same* length as the text consumed — no length drift. This
  is what distinguishes Hamming search from the edit-distance search in Problem 5.
- **Monotonicity:** `R[d]` always contains `R[d-1]`'s bits (fewer errors is a
  special case of more errors), so checking only `R[k]` suffices.
- **Snapshot matters:** updating `R` in place without the `old = R[:]` copy would
  let level `d` read the *already-updated* level `d-1`, corrupting the recurrence.
