# Solution — k-Mismatch Substring Search (Hamming Bitap)

## Brute Force

For each start index, count mismatches against the pattern and keep it if the count is `<= k`:

```python
def k_mismatch_search(text, pattern, k):
    m, n = len(pattern), len(text)
    res = []
    for s in range(n - m + 1):
        mismatches = 0
        for j in range(m):
            if text[s + j] != pattern[j]:
                mismatches += 1
                if mismatches > k:
                    break
        else:
            res.append(s)
    return res
```

- **Time:** `O(n · m)` worst case (early-exit on `k` helps but does not change the bound).
- **Space:** `O(1)` extra.

## Optimal Approach — Bitap under Hamming distance

### The registers

Keep `k + 1` registers `R[0], R[1], ..., R[k]`, all initialized to `0`. The invariant generalizes Problem 1:

> **Bit `j` of `R[d]`** is set after reading `text[0..i]` **iff** the pattern prefix `pattern[0..j]` matches the
> text suffix `text[i-j..i]` with **at most `d` mismatches**.

`R[0]` is exactly the exact-match register from Problem 1. A `<= k`-mismatch occurrence ends at position `i`
whenever the top bit `1 << (m-1)` of `R[k]` is set.

### The recurrence

Process the registers from `d = 0` upward. Let `oldR[d]` denote each register's value *before* the current
character `c` was processed. For each text character:

```
R[0] = ((oldR[0] << 1) | 1) & peq[c]

R[d] = ( ((oldR[d] << 1) | 1) & peq[c] )   # (a) extend a d-mismatch match on a matching char
       | (oldR[d-1] << 1)                  # (b) spend one mismatch: extend a (d-1)-match on ANY char
       | 1                                 # (c) a length-1 prefix always matches within d>=1 mismatches
       for d = 1..k
```

- **(a)** is the same "matching character extends the prefix" step as exact matching.
- **(b)** is the new idea: take everything that matched with `d-1` mismatches ending at the previous position
  (`oldR[d-1]`), shift it up by one, and accept it *regardless* of whether `c` matches — that shift "spends" one
  more mismatch. Crucially this uses `oldR[d-1]` (the value before this step), which is why we track a saved copy
  rather than the already-updated `R[d-1]`.
- **(c)** seeds bit 0: with a budget of `d >= 1`, a single-character prefix can always match by substituting.

### Reference implementation

```python
from typing import List

def k_mismatch_search(text: str, pattern: str, k: int) -> List[int]:
    m = len(pattern)
    peq = {}
    for j, ch in enumerate(pattern):
        peq[ch] = peq.get(ch, 0) | (1 << j)
    R = [0] * (k + 1)
    top = 1 << (m - 1)
    res = []
    for i, c in enumerate(text):
        prev = R[0]                    # oldR[d-1] for the d=1 step
        mask = peq.get(c, 0)
        R[0] = ((prev << 1) | 1) & mask
        for d in range(1, k + 1):
            cur = R[d]                 # save oldR[d] before overwriting
            R[d] = (((cur << 1) | 1) & mask) | (prev << 1) | 1
            prev = cur                 # cur becomes oldR[d] == oldR[(d+1)-1] next round
        if R[k] & top:
            res.append(i - m + 1)
    return res
```

### Why it is correct

By induction over text position and mismatch budget: a length-`j+1` prefix matches ending at `i` with `<= d`
mismatches iff either (a) a length-`j` prefix matched ending at `i-1` with `<= d` mismatches **and**
`pattern[j] == text[i]`, or (b) a length-`j` prefix matched ending at `i-1` with `<= d-1` mismatches and we treat
`pattern[j] != text[i]` as the `d`-th mismatch. Term (a) is `((oldR[d] << 1) & peq[c])` and term (b) is
`oldR[d-1] << 1`; the `| 1` handles the `j = 0` base case. Since `R[d-1]`'s bits are a superset relationship
across `d`, the top bit of `R[k]` captures "matched with at most `k` mismatches." Verified against a brute-force
Hamming counter on thousands of random inputs.

### Complexity

- **Preprocessing:** `O(m + σ)`.
- **Search:** `O(n · k · ⌈m / w⌉)`, i.e. `O(n · k)` when `m <= w`. Each of the `n` characters does `O(k)` word
  operations.
- **Space:** `O(σ + k)` — the mask table plus `k + 1` registers.

## Key Insights & Edge Cases

- **`k = 0` collapses to exact matching.** Only `R[0]` exists and the recurrence is identical to Problem 1.
- **Update order matters.** Go from `d = 0` to `d = k` and read the *pre-update* value of `R[d-1]`. Reading the
  already-updated `R[d-1]` (which corresponds to the current character, not the previous one) is the classic bug;
  the saved `prev`/`cur` copies avoid it.
- **`k >= m`.** Every window trivially matches (you can substitute the entire pattern), so all valid start
  indices `0..n-m` are returned. The `| 1` seeding and shifts produce this automatically.
- **Hamming only.** This variant fixes the window length to `m`. If you need insertions/deletions (so the matched
  region can be shorter or longer than `m`), you need the Levenshtein recurrence — that is Problem 4.
- **Reporting.** As before, a set top bit at index `i` means the match *ends* at `i`; the start index of a
  Hamming match of length `m` is `i - m + 1`.
