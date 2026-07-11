# Solution — Substring Equality Queries

## Brute Force

For each query `(a, b, length)`, slice out both substrings and compare them
directly.

```python
def substring_equality_queries(s, queries):
    return [s[a:a + L] == s[b:b + L] for (a, b, L) in queries]
```

- **Time:** `O(q · n)` in the worst case — a single comparison of two length-`L`
  substrings is `O(L)`, and `L` can be as large as `n`. With `q` and `n` both up
  to `2·10^5`, that is up to `4·10^10` character operations. Too slow.
- **Space:** `O(n)` for the transient slices.

## Optimal Approach (Polynomial Prefix Hashing)

Assign each character a value (e.g. `ord(c) - ord('a') + 1`; adding 1 avoids the
"leading `a` = leading zero" ambiguity where `"a"`, `"aa"`, `"aaa"` would all
hash to 0). Define the prefix hash

```
H[0] = 0
H[i] = ( H[i-1] * B + val(s[i-1]) ) mod M      for i = 1..n
```

so `H[i]` is the hash of the prefix `s[0..i-1]`. Precompute powers `pw[k] = B^k
mod M`. Then the hash of the substring `s[l..r]` (inclusive, `0`-based) is

```
sub(l, r) = ( H[r+1] - H[l] * pw[r - l + 1] ) mod M
```

### Why it is correct

`H[r+1]` encodes `s[0..r]` as a base-`B` number. `H[l] * pw[r-l+1]` is exactly the
contribution of the leading part `s[0..l-1]` **shifted left** by the length of
`s[l..r]`, i.e. it lines up digit-for-digit with the high part of `H[r+1]`.
Subtracting cancels the prefix and leaves the polynomial value of `s[l..r]`
alone. Equal substrings therefore always produce equal `sub(...)` values.

The converse (equal hash ⇒ equal substring) can fail via a **collision**. Two
defenses:

- **Double hashing** — maintain two independent `(B, M)` pairs and treat the
  *pair* of hashes as the key. Collision probability drops to roughly
  `1/(M1·M2)`, negligible for `M ≈ 10^9`.
- **Verify on a hit** — if a query reports equal, confirm with a direct slice
  comparison. This makes the answer exact; verification is rare and cheap when a
  good prime is used.

### Step by step

1. Choose `B` (e.g. a random value in `[256, M)` or a fixed `131`) and a large
   prime `M` (e.g. `1_000_000_007`). For safety use two pairs.
2. Build `H[0..n]` and `pw[0..n]` in a single `O(n)` pass.
3. For each query `(a, b, length)`, compute `sub(a, a+length-1)` and
   `sub(b, b+length-1)` and compare — `O(1)`.

```python
from typing import List, Tuple


def substring_equality_queries(
    s: str, queries: List[Tuple[int, int, int]]
) -> List[bool]:
    n = len(s)
    # Two independent hash channels to avoid collisions.
    MODS = (1_000_000_007, 998_244_353)
    BASES = (131, 137)

    H = [[0] * (n + 1) for _ in MODS]
    PW = [[1] * (n + 1) for _ in MODS]
    for c in range(len(MODS)):
        M, B = MODS[c], BASES[c]
        for i in range(1, n + 1):
            H[c][i] = (H[c][i - 1] * B + (ord(s[i - 1]) - 96)) % M
            PW[c][i] = (PW[c][i - 1] * B) % M

    def sub(c: int, l: int, r: int) -> int:  # hash of s[l..r] on channel c
        M = MODS[c]
        return (H[c][r + 1] - H[c][l] * PW[c][r - l + 1]) % M

    out = []
    for a, b, L in queries:
        eq = all(sub(c, a, a + L - 1) == sub(c, b, b + L - 1)
                 for c in range(len(MODS)))
        out.append(eq)
    return out
```

- **Time:** `O(n)` preprocessing + `O(1)` per query = `O(n + q)`.
- **Space:** `O(n)` for prefix-hash and power arrays.

## Key Insights & Edge Cases

- **Map characters to nonzero values.** Using `ord(c) - 'a' + 1` (never `0`)
  prevents leading-character collisions where different-length all-`a` strings
  hash identically.
- **The subtraction can go negative before `% M`.** In Python `%` returns a
  non-negative result for positive `M`, so `(H[r+1] - H[l]*pw[len]) % M` is safe;
  in languages with truncating modulo, add `M` before taking the remainder.
- **`a == b` or `length == 0`** (if allowed) are trivially equal; the formula
  still returns them correctly.
- **Single vs. double hashing.** One 32-bit-ish prime is fine for a homework
  demo but risks a rare wrong answer on adversarial input; double hashing (or
  verify-on-hit) is the safe production choice.
- **Powers array is essential.** Recomputing `B^(r-l+1)` per query with `pow`
  would add a `log` factor; precompute `pw[]` once.
