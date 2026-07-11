# Solution — Wildcard Single-Character Match (Bitap + wildcard mask)

## Brute Force

For every start index `s`, compare the pattern against `text[s : s + m]`, letting `?` match anything:

```python
def wildcard_search(text, pattern):
    m, n = len(pattern), len(text)
    res = []
    for s in range(n - m + 1):
        if all(pattern[j] == '?' or pattern[j] == text[s + j] for j in range(m)):
            res.append(s)
    return res
```

- **Time:** `O(n · m)`.
- **Space:** `O(1)` extra (besides the output).

## Optimal Approach — Bitap with a wildcard mask

The only structural difference from exact matching (Problem 1) is that a `?` at pattern position `j` must count
as a match **no matter what** text character arrives. In Bitap terms: bit `j` should survive the `& mask` step
unconditionally.

### Preprocessing

Split the pattern into literal-position masks and a single wildcard mask:

```python
from collections import defaultdict

peq = defaultdict(int)   # peq[c] bit j set iff pattern[j] == c (literals only)
wildcard = 0             # bit j set iff pattern[j] == '?'
for j, ch in enumerate(pattern):
    if ch == '?':
        wildcard |= (1 << j)
    else:
        peq[ch] |= (1 << j)
```

### The update

For each text character `c`:

```
R = ((R << 1) | 1) & (peq[c] | wildcard)
```

`peq[c] | wildcard` says "a candidate at position `j` is allowed if the pattern's literal there equals `c`
**or** the pattern has a `?` there." Everything else is identical to exact matching, including the full-match
test on bit `m-1`.

### Reference implementation

```python
from collections import defaultdict
from typing import List

def wildcard_search(text: str, pattern: str) -> List[int]:
    m = len(pattern)
    peq = defaultdict(int)
    wildcard = 0
    for j, ch in enumerate(pattern):
        if ch == '?':
            wildcard |= (1 << j)
        else:
            peq[ch] |= (1 << j)
    R = 0
    top = 1 << (m - 1)
    res = []
    for i, c in enumerate(text):
        R = ((R << 1) | 1) & (peq[c] | wildcard)
        if R & top:
            res.append(i - m + 1)
    return res
```

### Why it is correct

The register invariant is unchanged from Problem 1 — bit `j` set means "the first `j+1` pattern positions match
the text suffix ending here." The wildcard mask simply relaxes the per-position matching predicate at `?`
positions from "equals a specific letter" to "always true." Since `?` still consumes exactly one text character,
the shift-by-one alignment logic is untouched, so the top bit lights up precisely when all `m` positions match.

### Complexity

- **Preprocessing:** `O(m + σ)`.
- **Search:** `O(n · ⌈m / w⌉)`, i.e. `O(n)` when `m <= w` (guaranteed here, `m <= 64`).
- **Space:** `O(σ)` for `peq` plus one word for `wildcard`.

## Key Insights & Edge Cases

- **The `| wildcard` trick generalizes.** Any pattern position with a *set* of allowed characters (a small
  character class like `[abc]`) can be encoded the same way: set bit `j` in `peq[c]` for every `c` in the class.
  `?` is just the class "all characters," so instead of touching every `peq[c]` you keep one shared `wildcard`
  mask and OR it in each step.
- **`*` is NOT handled here.** A multi-character `*` breaks the one-shift-per-character alignment that Bitap
  relies on and needs a different technique (DP or greedy). This problem is deliberately restricted to `?`.
- **Text character absent from `peq`.** `defaultdict(int)` (or `peq.get(c, 0)`) yields `0`, so only the wildcard
  bits can survive — exactly right.
- **All-wildcard pattern.** If every position is `?`, then `peq[c] | wildcard` has all `m` low bits set every
  step, so the pattern matches at every start index `i` with `i + m <= n`. The algorithm produces
  `[0, 1, ..., n - m]` naturally.
- **Match reporting.** As in Problem 1, a set top bit at text index `i` means the match *ends* at `i`, so the
  *start* index is `i - m + 1`.
