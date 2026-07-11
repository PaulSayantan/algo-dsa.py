# Solution — Implement strStr()

## Brute Force

Try every alignment `s` of the pattern over the text. For each `s`, compare the
`m` characters of `needle` against `haystack[s .. s+m-1]`. Return the first `s`
that matches fully.

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    for s in range(n - m + 1):
        if haystack[s:s + m] == needle:
            return s
    return -1
```

- **Time:** `O(n · m)` in the worst case (e.g. `haystack = "aaaa...a"`,
  `needle = "aaab"`), because a mismatch only advances the alignment by one and
  re-compares up to `m` characters each time.
- **Space:** `O(1)` extra.

## Optimal Approach — Boyer–Moore (string search)

The key idea: compare the pattern to the current window **from right to left**,
and when a mismatch occurs, use precomputed information about the pattern to
slide it forward by (usually) many positions instead of one.

### Preprocessing

**1. Bad-character table.** For each character `c`, store the index of its
**last** occurrence in the pattern. When a mismatch happens at pattern index `j`
against text character `c = text[s + j]`, the bad-character shift is
`j - last[c]` (and `last[c] = -1` if `c` is absent, which pushes the pattern past
the mismatch). This can be negative, so we always floor the final shift at 1.

**2. Good-suffix table.** When a suffix `text[s+j+1 .. s+m-1]` already matched
before the mismatch at `j`, we can shift so that the *next* occurrence of that
matched suffix (or a pattern prefix that equals a suffix of it) aligns. This is
built in `O(m)` with a border array, the same technique behind KMP's failure
function. `gs[j+1]` gives the shift when the mismatch is at index `j`; `gs[0]` is
the shift to use after a full match.

### Matching loop

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    if m > n:
        return -1

    last = {c: i for i, c in enumerate(needle)}   # bad-character table

    # good-suffix table (borders)
    gs = [0] * (m + 1)
    border = [0] * (m + 1)
    i, j = m, m + 1
    border[i] = j
    while i > 0:
        while j <= m and needle[i - 1] != needle[j - 1]:
            if gs[j] == 0:
                gs[j] = j - i
            j = border[j]
        i -= 1; j -= 1
        border[i] = j
    j = border[0]
    for i in range(m + 1):
        if gs[i] == 0:
            gs[i] = j
        if i == j:
            j = border[j]

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and needle[j] == haystack[s + j]:
            j -= 1
        if j < 0:
            return s                      # full match
        bad = j - last.get(haystack[s + j], -1)
        s += max(gs[j + 1], bad, 1)       # take the larger safe shift
    return -1
```

### Why it is correct

Both rules are **conservative**: they never skip an alignment that could match.

- The bad-character rule aligns the mismatching text character with its last
  possible matching position in the pattern; any smaller shift would still place
  a non-matching character there.
- The good-suffix rule only shifts by an amount that keeps the already-matched
  suffix consistent with the pattern; any smaller shift would contradict a
  character we already verified.

Taking the **maximum** of the two shifts is safe because each individually is a
lower bound on how far we can move without missing an occurrence. Flooring at 1
guarantees forward progress and termination.

### Step-by-step on Example 3 (`haystack = "GCAATGCC"`, `needle = "GCC"`)

`last = {G:0, C:2}`, `m = 3`.

- `s = 0`: compare `needle[2]='C'` vs `text[2]='A'` → mismatch at `j = 2`.
  bad = `2 - last['A'(-1)] = 3`. Shift by `max(gs[3], 3, 1) = 3` → `s = 3`.
- `s = 3`: compare `needle[2]='C'` vs `text[5]='G'` → mismatch at `j = 2`.
  bad = `2 - last['G'] = 2`. Shift by `max(gs[3], 2, 1) = 2` → `s = 5`.
- `s = 5`: compare `'C'`vs`text[7]='C'` ✓, `'C'`vs`text[6]='C'` ✓,
  `'G'`vs`text[5]='G'` ✓ → full match, return `5`.

### Complexity

- **Preprocess:** `O(m + |Σ|)` time, `O(m + |Σ|)` space.
- **Search:** `O(n · m)` worst case, but `O(n / m)` best case and typically
  sublinear on real text with a reasonably sized alphabet.

## Key Insights & Edge Cases

- **Empty needle** → return `0` by convention (handle before indexing).
- **`m > n`** → immediately return `-1`.
- **Negative bad-character shift.** When the mismatching character occurs to the
  *right* of `j` in the pattern, `j - last[c]` is negative — this is exactly why
  we take `max(..., 1)`; without the floor the loop could stall or go backward.
- **Only the bad-character rule** already beats brute force in practice and is
  easy to get right; the good-suffix rule is what removes the pathological
  `O(n·m)` blowup on inputs like `"aaaa...a"` vs `"baaa"`.
- Comparing **right-to-left** is what enables the big skips — a mismatch on the
  last character with a symbol absent from the pattern lets you jump a full `m`.
