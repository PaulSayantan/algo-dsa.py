# Solution — Implement strStr()

## Brute Force

Try to match the pattern starting at every index of the haystack.

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    for start in range(n - m + 1):
        if haystack[start:start + m] == needle:
            return start
    return -1
```

- **Time:** `O(n * m)`. The killer case is `haystack = "aaaa...aab"` and
  `needle = "aaaa...b"`: at each of the `~n` start positions we compare `~m`
  characters before failing on the last one.
- **Space:** `O(1)` extra (ignoring the slice), `O(m)` if the slice is counted.

## Optimal Approach — KMP

The waste in brute force is that after a partial match fails, we throw away
everything we learned and slide the pattern by exactly one. KMP eliminates that.

### Step 1 — Build the LPS array

`lps[i]` = length of the longest **proper** prefix of `needle[0..i]` that is
also a suffix of `needle[0..i]`. "Proper" means it cannot be the whole
substring.

```python
def build_lps(p):
    m = len(p)
    lps = [0] * m
    k = 0                       # length of current longest prefix-suffix
    for i in range(1, m):
        while k > 0 and p[i] != p[k]:
            k = lps[k - 1]      # fall back to the next-best border
        if p[i] == p[k]:
            k += 1
        lps[i] = k
    return lps
```

For `needle = "aabaa"` the LPS is `[0, 1, 0, 1, 2]`.

### Step 2 — Scan the haystack

Keep a pointer `j` into the pattern. Walk `i` across the haystack once. On a
mismatch, instead of resetting `j` to 0, jump to `lps[j-1]` — the pattern's own
border guarantees those characters already match, so `i` never moves backward.

```python
def strStr(haystack, needle):
    if needle == "":
        return 0
    lps = build_lps(needle)
    j = 0                                   # matched length so far
    for i, c in enumerate(haystack):
        while j > 0 and c != needle[j]:
            j = lps[j - 1]
        if c == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1                # full match ends at i
    return -1
```

### Why it is correct

`lps[j-1]` is by definition the longest suffix of the already-matched prefix
that is itself a prefix of the pattern. Every shorter alignment KMP skips would
require matching a border shorter than `lps[j-1]` at a position we already know
cannot start a full match, so no occurrence is ever missed.

### Complexity

- **Time:** `O(m)` to build LPS + `O(n)` to scan = **O(n + m)**. The `while`
  loop only ever *decreases* `j`, and `j` increases at most `n` times, so the
  total work across all iterations is amortized linear.
- **Space:** `O(m)` for the LPS array.

## Key Insights & Edge Cases

- **Empty needle → return 0** by convention. Handle it before building LPS.
- **The `while` (not `if`) on fallback is essential.** After one fallback the
  characters may still mismatch, so you keep falling back until either they
  match or `j == 0`.
- **Never move `i` backward.** That single invariant is what makes KMP linear;
  the LPS array is the machinery that lets you honor it.
- **Reusable primitive.** The `build_lps` function alone answers "longest
  border", periodicity, and several other problems in this folder.
