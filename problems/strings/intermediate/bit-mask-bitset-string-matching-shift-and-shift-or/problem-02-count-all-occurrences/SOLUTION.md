# Solution — Count All Occurrences

## Brute Force

For each candidate start index, compare the pattern against the corresponding slice.

```python
def find_all_occurrences(text, pattern):
    n, m = len(text), len(pattern)
    res = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            res.append(i)
    return res
```

- **Time:** `O((n - m + 1) * m)` = `O(n * m)` worst case.
- **Space:** `O(1)` extra (plus the output list).

## Optimal Approach — Shift-And, collect every match bit

This is the same Shift-And automaton as Problem 1, but instead of returning at the
first match we **append the start index and keep scanning**. Because the state word
`D` tracks *all* partial matches at once, it already knows about matches that overlap
one another — no reset, no restart.

### Invariant

After reading `text[0..i]`, bit `j` of `D` is set iff `pattern[0..j]` matches
`text[i-j..i]`. A full occurrence ends at `i` exactly when bit `m-1` is set, so its
start index is `i - m + 1`.

Crucially, the update `D = ((D << 1) | 1) & B[c]` does **not** clear the lower bits
when a full match is found: a shorter prefix match that started later is still alive
in `D`. That is precisely what lets overlapping matches (like `"aa"` in `"aaaaa"`)
all be discovered.

### Reference implementation

```python
from typing import List

def find_all_occurrences(text: str, pattern: str) -> List[int]:
    m = len(pattern)
    res: List[int] = []
    if m == 0:
        return res
    B = {}
    for j, c in enumerate(pattern):
        B[c] = B.get(c, 0) | (1 << j)
    D = 0
    match_bit = 1 << (m - 1)
    for i, c in enumerate(text):
        D = ((D << 1) | 1) & B.get(c, 0)
        if D & match_bit:
            res.append(i - m + 1)
    return res
```

### Walkthrough — `text = "aaaaa"`, `pattern = "aa"` (`m = 2`, `match_bit = 0b10`)

| i | char | D before | `(D<<1)|1` | `& B['a']=0b11` | match? | start |
|---|------|----------|-----------|-----------------|--------|-------|
| 0 | a | 000 | 001 | 01 | no | |
| 1 | a | 01  | 011 | 11 | yes (bit1) | 0 |
| 2 | a | 11  | 111 | 11 | yes | 1 |
| 3 | a | 11  | 111 | 11 | yes | 2 |
| 4 | a | 11  | 111 | 11 | yes | 3 |

Result: `[0, 1, 2, 3]`, as expected.

### Complexity

- **Time:** `O(n * ceil(m/w) + m + sigma)`; `O(n)` when `m` fits one word.
- **Space:** `O(sigma * ceil(m/w))` for masks, plus `O(#occurrences)` output.

The scan is output-sensitive in the good sense: it visits each text character once
regardless of how many matches occur.

## Key Insights & Edge Cases

- **Overlapping matches** are reported automatically — this is the key difference
  from naive "find, then jump past the match" strategies.
- **Counting only:** if you just need the count, keep a counter instead of a list.
- **`pattern` longer than `text`:** the match bit is never reached; returns `[]`.
- **Non-lowercase / large alphabet:** the dict-based `B` handles arbitrary
  characters; positions of characters absent from the pattern default to mask `0`,
  which correctly kills any partial match.
- **Multi-word patterns (`m > 64`):** replace the single int with a fixed array of
  words (a "bitset") and carry the shift across word boundaries; complexity gains a
  `ceil(m/w)` factor. In Python the built-in big-int already does this for you.
