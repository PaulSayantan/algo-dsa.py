# Solution — Implement strStr()

## Brute Force

Try every possible start index `i` in `haystack` and compare `needle` character by
character.

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1
```

- **Time:** `O(n * m)` in the worst case (e.g. `haystack = "aaaa...a"`, `needle = "aa...ab"`).
- **Space:** `O(1)` (ignoring the slice; `O(m)` if you count it).

## Optimal Approach — Shift-And bitmask automaton

The idea is to run a tiny nondeterministic automaton for the pattern using
**bit-parallelism**. Represent its state in the bits of one integer `D`:

> **Invariant:** after processing `haystack[0..i]`, bit `j` of `D` is set **iff**
> `needle[0..j]` (the first `j+1` pattern characters) matches
> `haystack[i-j .. i]`.

### Preprocessing — character masks

For every character `c`, precompute `B[c]` where bit `j` is set iff `needle[j] == c`:

```python
B = {}
for j, c in enumerate(needle):
    B[c] = B.get(c, 0) | (1 << j)
```

Characters not in the pattern implicitly map to `0`.

### Scanning

For each text character `c`, update the state:

```
D = ((D << 1) | 1) & B[c]
```

- `D << 1` advances every matched prefix by one character.
- `| 1` seeds bit 0 — "a fresh match can always start here".
- `& B[c]` keeps only prefixes whose next expected character equals `c`.

A full match ends at index `i` exactly when bit `m-1` is set, i.e.
`D & (1 << (m-1)) != 0`; the start index is `i - m + 1`.

### Reference implementation

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0
        B = {}
        for j, c in enumerate(needle):
            B[c] = B.get(c, 0) | (1 << j)
        D = 0
        match_bit = 1 << (m - 1)
        for i, c in enumerate(haystack):
            D = ((D << 1) | 1) & B.get(c, 0)
            if D & match_bit:
                return i - m + 1
        return -1
```

### Why it is correct

The recurrence maintains the invariant by induction. Initially `D = 0` (no prefix
matched). After reading `c` at position `i`: prefix `needle[0..j]` matches ending at
`i` iff prefix `needle[0..j-1]` matched ending at `i-1` (bit `j-1` was set, captured
by `D << 1`) **and** `needle[j] == c` (captured by `& B[c]`); the base prefix of
length 1 matches iff `needle[0] == c`, which the `| 1` seed combined with `& B[c]`
handles. Thus bit `m-1` set ⇔ a complete occurrence ends here.

### Complexity

Let `w` be the machine word size. With `m <= w`, every update is `O(1)`:

- **Time:** `O(n + m + sigma)` — `O(m + sigma)` preprocessing, `O(n)` scan.
- **Space:** `O(sigma)` for the mask table.

For `m > w`, use `ceil(m/w)` words and each step costs `O(ceil(m/w))`, giving
`O(n * ceil(m/w))`. Python integers are arbitrary precision, so a single `D` works
for any `m` (the shifts silently span multiple words).

## Key Insights & Edge Cases

- **Empty needle** returns `0` by convention — handle before the loop.
- **`needle` longer than `haystack`**: the match bit can never be reached, so the
  loop naturally returns `-1`.
- **First vs. all occurrences:** returning on the first set match bit gives the
  first occurrence (Problem 2 collects all of them).
- **Shift-Or dual:** if you invert the bit convention (0 = active) you avoid the
  `| 1` seed each step: `D = (D << 1) | B[c]`, and a match is when bit `m-1` is `0`.
  It saves one OR per character but is otherwise identical.
- **Alphabet handling:** using a dict `B` with default `0` cleanly handles any
  character (including ones absent from the pattern) without a fixed-size table.
