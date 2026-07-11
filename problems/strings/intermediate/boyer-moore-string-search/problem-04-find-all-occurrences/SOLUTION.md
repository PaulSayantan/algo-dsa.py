# Solution — Find All Occurrences of a Pattern

## Brute Force

Slide the pattern one position at a time and compare fully at each alignment,
recording every match.

```python
def find_all_occurrences(text, pattern):
    n, m = len(text), len(pattern)
    res = []
    for s in range(n - m + 1):
        if text[s:s + m] == pattern:
            res.append(s)
    return res
```

- **Time:** `O(n · m)` worst case (many partial matches, e.g. `text = "aaaa"`,
  `pattern = "aa"`).
- **Space:** `O(1)` extra beyond the output.

## Optimal Approach — Boyer–Moore (string search)

The single-match matcher (Problem 1) turns into an all-matches matcher with one
change: when the entire pattern matches, **record the index** and then shift
using `gs[0]` (the good-suffix shift for a *complete* match) instead of
returning. `gs[0]` equals `m - border[0]`, i.e. `m` minus the length of the
longest proper border of the pattern — exactly the shift that lines up the next
possible overlapping occurrence, so overlaps are not missed.

```python
def find_all_occurrences(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    last = {c: i for i, c in enumerate(pattern)}   # bad-character table

    # good-suffix table via borders (O(m))
    gs = [0] * (m + 1)
    border = [0] * (m + 1)
    i, j = m, m + 1
    border[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
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

    res = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            res.append(s)
            s += gs[0]                          # shift after a full match
        else:
            bad = j - last.get(text[s + j], -1)
            s += max(gs[j + 1], bad, 1)
    return res
```

### Why it is correct

- For mismatches, the shift is `max(good-suffix, bad-character, 1)`, each of
  which is a proven lower bound on the safe shift (see Problem 1), so no matching
  alignment between `s` and the new `s` is skipped.
- For a full match, `gs[0] = m - len(longest proper border)` is precisely the
  smallest shift that keeps the pattern consistent with itself; using it means
  the **next overlapping** occurrence is not jumped over. For a pattern with no
  self-overlap (like `"ab"`... actually `"ab"` has border length 0) `gs[0] = m`;
  for `"aa"` the border length is 1 so `gs[0] = 1`, correctly catching the
  overlap.

### Step-by-step on Example 1 (`text = "ababab"`, `pattern = "ab"`)

`m = 2`, `last = {a:0, b:1}`. Longest proper border of `"ab"` is `""` (length 0),
so `gs[0] = 2`... but note the matches at 0, 2, 4 don't overlap, so a shift of 2
after each match is exactly right.

- `s=0`: `'b'`=`text[1]`✓, `'a'`=`text[0]`✓ → match at 0; `s += 2` → `s=2`.
- `s=2`: `'b'`=`text[3]`✓, `'a'`=`text[2]`✓ → match at 2; `s += 2` → `s=4`.
- `s=4`: `'b'`=`text[5]`✓, `'a'`=`text[4]`✓ → match at 4; `s += 2` → `s=6 > 4`,
  stop. Result `[0, 2, 4]`.

(For an overlapping case like `pattern = "aa"`, `border[0] = 1`, so `gs[0] = 1`
and the scan advances by 1 after each match, catching `[0, 1, 2, ...]`.)

### Complexity

- **Preprocess:** `O(m + |Σ|)` time and space.
- **Search:** `O(n · m)` worst case, sublinear on average, best case `O(n / m)`.
  Output size is `O(number of matches)`.

## Key Insights & Edge Cases

- **Overlapping matches** are handled by shifting `gs[0]` (which can be as small
  as 1) after a full match — never hard-code a shift of `m`, or you would miss
  overlaps like `"aa"` in `"aaaa"`.
- **`m > n`** → no occurrences, return `[]` early.
- **Empty pattern** — this problem defines `pattern` as non-empty; if you choose
  to support it, the mathematically consistent answer is every index
  `0..n` (`n+1` positions), but keep the guard explicit.
- Reporting the mismatch shift as `max(gs[j+1], bad, 1)` (never below 1)
  guarantees forward progress even when the bad-character shift is negative.
- This is the general workhorse: Problems 2, 3, 5, and 6 all reduce to some form
  of "find (all) occurrences," so a correct all-matches Boyer–Moore is a reusable
  building block.
