# Solution — Wildcard `?` Pattern Search

## Brute Force

Slide a window of length `m` across the text and compare position by position,
treating `?` as an automatic match.

```python
def wildcard_search(text, pattern):
    n, m = len(text), len(pattern)
    res = []
    for i in range(n - m + 1):
        if all(pattern[j] == '?' or pattern[j] == text[i + j] for j in range(m)):
            res.append(i)
    return res
```

- **Time:** `O(n * m)` worst case.
- **Space:** `O(1)` extra.

## Optimal Approach — Shift-And with a wildcard mask

The single-character wildcard `?` fits the bitmask model perfectly. In Shift-And,
`& B[c]` keeps a partial match alive only if the pattern character at that position
equals the text character `c`. A `?` should keep the match alive **regardless** of
`c` — that is, position `j` should behave as though it matches every character.

We achieve this by adding a **wildcard mask** `Q` with a bit set at each `?`
position, and OR-ing it into the character mask during the update:

```
D = ((D << 1) | 1) & (B[c] | Q)
```

Because bit `j` of `Q` is always present, position `j` matches any text character,
which is exactly the semantics of `?`. Everything else is ordinary Shift-And.

### Preprocessing

```python
Q = 0
B = {}
for j, c in enumerate(pattern):
    if c == '?':
        Q |= (1 << j)
    else:
        B[c] = B.get(c, 0) | (1 << j)
```

### Reference implementation

```python
from typing import List

def wildcard_search(text: str, pattern: str) -> List[int]:
    m = len(pattern)
    res: List[int] = []
    if m == 0:
        return res
    Q = 0
    B = {}
    for j, c in enumerate(pattern):
        if c == '?':
            Q |= (1 << j)
        else:
            B[c] = B.get(c, 0) | (1 << j)
    D = 0
    match_bit = 1 << (m - 1)
    for i, c in enumerate(text):
        D = ((D << 1) | 1) & (B.get(c, 0) | Q)
        if D & match_bit:
            res.append(i - m + 1)
    return res
```

### Why it is correct

The Shift-And invariant becomes: bit `j` of `D` is set iff pattern positions
`0..j` each *either* equal the corresponding text character *or* are `?`. The
`(B[c] | Q)` term encodes "position matches `c` OR position is a wildcard", so the
`& (B[c] | Q)` step preserves precisely the partial matches that remain consistent
with a `?`-aware comparison. The top bit therefore lights up exactly at the end of a
valid wildcard match.

### Walkthrough — `text = "xyzxyz"`, `pattern = "?y?"` (`m = 3`)

`Q = 0b101` (positions 0 and 2 are `?`), `B = {'y': 0b010}`.

| i | c | `B[c]|Q`      | `(D<<1)|1` | new D | bit2 set? | start |
|---|---|---------------|-----------|-------|-----------|-------|
| 0 | x | 101           | 001       | 001   | no        |       |
| 1 | y | 111           | 011       | 011   | no        |       |
| 2 | z | 101           | 111       | 101   | yes       | 0     |
| 3 | x | 101           | 011       | 001   | no        |       |
| 4 | y | 111           | 011       | 011   | no        |       |
| 5 | z | 101           | 111       | 101   | yes       | 3     |

Result: `[0, 3]`.

### Complexity

- **Time:** `O(n * ceil(m/w) + m + sigma)`; `O(n)` when `m <= w`.
- **Space:** `O(sigma * ceil(m/w))` for masks plus one extra word for `Q`.

The wildcard costs nothing asymptotically — it is a single extra OR per character.

## Key Insights & Edge Cases

- **`?` is "free":** one precomputed mask `Q` and one OR per step handles any number
  of wildcards anywhere in the pattern.
- **Character classes** (`[abc]`, ranges) generalize the same trick: set the class's
  bit in `B[a]`, `B[b]`, `B[c]`. A negated class sets the bit in every char *except*
  the excluded ones. `?` is just the class "any character".
- **No `*` wildcard here:** `*` (match zero or more) needs a different, richer
  automaton (an epsilon transition / `D |= (D adjustments)` loop) because it changes
  the match length. This problem is fixed-length and thus pure Shift-And.
- **All-wildcard pattern** `"???"` matches every window of length 3 — the code
  returns every start index, which is correct.
- **Overlaps** are reported just like exact matching (see Problem 2): the state word
  keeps shorter live prefixes around.
