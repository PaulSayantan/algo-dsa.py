# Solution — Find the First Occurrence (strStr)

## Brute Force

Slide the needle across every start position of the haystack and compare
character by character.

```python
def strStr(haystack, needle):
    n, m = len(haystack), len(needle)
    for start in range(n - m + 1):
        if haystack[start:start + m] == needle:
            return start
    return -1
```

- **Time:** `O(n * m)` in the worst case (e.g. `haystack = "aaaa...a"`,
  `needle = "aaa...ab"`), because each of the `~n` start positions can require
  up to `m` comparisons.
- **Space:** `O(1)` extra (ignoring the slice, which is `O(m)`).

## Optimal Approach (Z-Algorithm)

**Construction.** Build a combined string

```
combined = needle + sep + haystack
```

where `sep` is any character guaranteed to appear in **neither** string (here
the inputs are lowercase letters, so `'#'` is safe). The separator prevents a
match from "spilling across" the boundary and over-counting.

Now compute the Z-array of `combined`. Let `m = len(needle)`. For every index
`i` that lies in the haystack region (`i > m`), `z[i]` is the length of the
longest prefix of `combined` — i.e. of `needle` — that matches starting at `i`.
Because the separator can never be part of a prefix match, `z[i]` can be at most
`m`. So:

```
z[i] == m  <=>  the needle occurs in the haystack starting at position (i - (m + 1))
```

Scan left to right and return the first such position; if none exists, return
`-1`.

### Why it is correct

`z[i]` by definition equals the length of the longest common prefix of
`combined` and `combined[i:]`. The prefix of `combined` starts with the entire
needle followed by `sep`. If `z[i] == m`, then `combined[i .. i+m-1]` equals the
needle exactly, and since `i` is past the separator, that region lies wholly
inside the haystack. The offset conversion is `haystack_index = i - (m + 1)`
because `needle` occupies indices `0..m-1` and `sep` occupies index `m`.

### Step-by-step

1. If `len(needle) > len(haystack)`, return `-1` early (optional).
2. Form `combined = needle + '#' + haystack`.
3. Compute `z = z_array(combined)` in one linear pass.
4. For each `i` from `m + 1` to `len(combined) - 1`, if `z[i] == m` return
   `i - (m + 1)`.
5. If the loop ends, return `-1`.

### Reference implementation

```python
from typing import List


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    z[0] = n              # whole string is a prefix of itself
    l = r = 0             # current Z-box [l, r]
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])   # reuse mirror value, capped by box
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1                     # extend past the box
        if i + z[i] > r:                  # box moved right -> update it
            l, r = i, i + z[i]
    return z


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        combined = needle + "#" + haystack
        z = z_array(combined)
        for i in range(m + 1, len(combined)):
            if z[i] == m:
                return i - (m + 1)
        return -1
```

- **Time:** `O(n + m)` — building the Z-array is linear in `len(combined)`.
- **Space:** `O(n + m)` for the combined string and its Z-array.

(Note: the box bounds above use the half-open convention `z[i] = min(r - i, ...)`
with `r = i + z[i]`. An equivalent closed-interval formulation uses
`min(r - i + 1, ...)` with `r = i + z[i] - 1`. Pick one and stay consistent.)

## Key Insights & Edge Cases

- **Separator must be foreign** to both strings, otherwise a Z-value could
  exceed `m` illegitimately or match across the boundary. With arbitrary input
  alphabets, sentinel-free variants exist, but a foreign separator is simplest.
- **First vs. all occurrences:** returning at the first `z[i] == m` gives the
  first occurrence; collecting all such `i` yields every occurrence in `O(n)`.
- **Overlapping matches** are handled naturally — Z checks each start position
  independently.
- **Needle longer than haystack** simply yields no `z[i] == m`, returning `-1`.
- Python's built-in `haystack.find(needle)` also works, but the point here is to
  practice the linear Z construction that generalizes to the harder problems.
