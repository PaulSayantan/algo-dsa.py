# Solution — Longest Happy Prefix

## Brute Force

Try every candidate border length `k` from `n - 1` down to `1` and check whether
`s[:k] == s[n-k:]`.

```python
def longestPrefix(s):
    n = len(s)
    for k in range(n - 1, 0, -1):
        if s[:k] == s[n - k:]:
            return s[:k]
    return ""
```

- **Time:** `O(n^2)` — up to `n` candidate lengths, each comparison up to `O(n)`.
- **Space:** `O(n)` for the slices (or `O(1)` if compared index by index).

This TLEs at `n = 10^5`.

## Optimal Approach (Z-Algorithm)

Compute the Z-array of `s` in `O(n)`. Recall `z[i]` = length of the longest
prefix of `s` that also starts at index `i`.

**Key equivalence.** The suffix of `s` beginning at index `i` has length
`n - i`. That suffix *equals a prefix of `s`* precisely when the prefix match at
`i` runs all the way to the end of the string, i.e.

```
z[i] == n - i
```

When this holds, `s[i:]` (length `n - i`) is simultaneously a suffix (it ends at
the last character) and a prefix (Z says so) — a border of length `n - i`.

To get the **longest** border, we want the **smallest** `i >= 1` with
`z[i] == n - i` (smaller `i` gives a longer suffix). Scan `i` from `1` upward and
return `s[i:]` at the first hit; if none, return `""`.

### Why it is correct

By definition `z[i]` cannot exceed `n - i` (there are only `n - i` characters
from `i` to the end). So `z[i] == n - i` means the entire tail `s[i:]` matches
the prefix `s[0 : n-i]` character for character. That is exactly the definition
of a proper prefix that is also a suffix (proper because `i >= 1`). Iterating `i`
in increasing order, the first success maximizes `n - i`.

### Step-by-step on `s = "ababab"` (n = 6)

Z-array:

| i | s[i:]    | z[i] | n - i | z[i] == n - i? |
|---|----------|------|-------|----------------|
| 0 | ababab   | 6    | 6     | (skip i = 0)   |
| 1 | babab    | 0    | 5     | no             |
| 2 | abab     | 4    | 4     | **yes**        |
| 3 | bab      | 0    | 3     | no             |
| 4 | ab       | 2    | 2     | yes            |
| 5 | b        | 0    | 1     | no             |

First hit is `i = 2` → border `s[2:] = "abab"`, length `4`. Correct.

### Reference implementation

```python
from typing import List


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        z = z_array(s)
        for i in range(1, n):
            if z[i] == n - i:
                return s[i:]
        return ""
```

- **Time:** `O(n)` to build Z plus `O(n)` to scan.
- **Space:** `O(n)` for the Z-array.

## Key Insights & Edge Cases

- **`z[i] == n - i` is the border test.** Memorize it — it is the Z-analog of
  reading `lps[n-1]` in KMP, and it generalizes to "all borders" if you collect
  every hit instead of the first.
- **Smallest index → longest border.** Do not scan from the end; scanning
  upward and returning immediately is both correct and fastest.
- **No border case** (`"abcdef"`): the loop finds nothing and returns `""`.
- **Single character** (`n == 1`): the loop range `range(1, 1)` is empty, so it
  returns `""` — correct, since a proper prefix must be shorter than `s`.
- **Whole-string exclusion** is automatic: starting the scan at `i = 1` (not
  `i = 0`) forbids the trivial border equal to `s` itself.
- **Equivalent KMP framing:** the LPS/failure function's last value `lps[n-1]`
  gives the same longest border length; the two methods are interchangeable.
