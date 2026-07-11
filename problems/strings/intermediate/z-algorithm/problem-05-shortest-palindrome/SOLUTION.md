# Solution — Shortest Palindrome

## Brute Force

The answer is `reverse(s[p:]) + s` where `p` is the length of the longest
**palindromic prefix** of `s`. Find `p` by testing each prefix length from
longest to shortest.

```python
def shortestPalindrome(s):
    n = len(s)
    for p in range(n, 0, -1):
        if s[:p] == s[:p][::-1]:      # is this prefix a palindrome?
            return s[p:][::-1] + s
    return s                          # empty string
```

- **Time:** `O(n^2)` — up to `n` prefix lengths, each palindrome check `O(n)`.
- **Space:** `O(n)` for slices.

At `n = 5 * 10^4` this is too slow.

## Optimal Approach (Z-Algorithm)

We need the longest prefix of `s` that is a palindrome. A prefix `s[:p]` is a
palindrome iff it equals its own reverse. Equivalently, a prefix of `s` is a
palindrome iff that same block appears as a **suffix of `reverse(s)`** (because
reversing a palindromic prefix leaves it unchanged and lands it at the tail of
`reverse(s)`).

**Construction.** Let `rev = reverse(s)` and build

```
combined = s + '#' + rev
```

with `'#'` foreign to the alphabet. Compute the Z-array of `combined`. Let
`total = len(combined)`. For an index `i` sitting in the `rev` region, `z[i]` is
the length of the longest prefix of `s` that matches starting at `i` in `rev`.

We care about matches that reach the **very end** of `combined`, because those
correspond to a suffix of `rev`. Concretely, if

```
z[i] == total - i
```

then a prefix of `s` of length `z[i]` equals the suffix of `rev` of the same
length — i.e. a palindromic prefix of `s` of length `z[i]`. The **largest** such
`z[i]` is the longest palindromic prefix length `p`.

Then the shortest palindrome is:

```
reverse(s[p:]) + s
```

### Why it is correct

- A prefix `W = s[:p]` is a palindrome ⟺ `W == reverse(W)`.
- `reverse(W)` is the length-`p` **suffix** of `rev = reverse(s)` (reversing the
  whole string sends the length-`p` prefix to the length-`p` suffix).
- So `W` is a palindrome ⟺ the length-`p` prefix of `s` equals the length-`p`
  suffix of `rev`. The Z-array over `s # rev` detects exactly "prefix of `s`
  matches here in `rev`", and requiring the match to run to the end of
  `combined` (`z[i] == total - i`) forces it to be a *suffix* of `rev`.
- Taking the maximum matched length gives the longest palindromic prefix `p`.
  The characters `s[p:]` are not part of any palindromic prefix, so they must be
  mirrored in front: prepend `reverse(s[p:])`. This is minimal because any
  shorter addition would leave a non-palindromic prefix uncovered.

### Step-by-step on `s = "aacecaaa"`

- `rev = "aaacecaa"`, `combined = "aacecaaa#aaacecaa"`, `total = 17`.
- Scanning the `rev` region, the match that reaches the end has length `7`,
  corresponding to the palindromic prefix `"aacecaa"`. So `p = 7`.
- Leftover suffix `s[7:] = "a"`; `reverse("a") = "a"`.
- Answer: `"a" + "aacecaaa" = "aaacecaaa"`. Correct.

### Reference implementation

```python
from typing import List


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    if n == 0:
        return z
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
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        rev = s[::-1]
        combined = s + "#" + rev
        z = z_array(combined)
        total = len(combined)
        p = 0                          # longest palindromic prefix length
        # indices of the rev region start at len(s) + 1
        for i in range(len(s) + 1, total):
            if z[i] == total - i:      # match runs to the end => suffix of rev
                p = max(p, z[i])
        return rev[:len(s) - p] + s    # rev[:n-p] == reverse(s[p:])
```

- **Time:** `O(n)` — one linear Z build over a string of length `2n + 1`.
- **Space:** `O(n)` for `combined` and its Z-array.

## Key Insights & Edge Cases

- **The reduction is the whole trick:** "shortest palindrome by prepending" ⟺
  "longest palindromic prefix." Everything after that is mechanical.
- **Why the `#` separator:** without a foreign separator, a match could run from
  the `s` region straight into the `rev` region and overcount; the separator can
  never be part of a prefix of `s`, so it caps every match at `len(s)` and blocks
  cross-boundary spill.
- **`z[i] == total - i` is the "reaches the end" test** — it is what turns a
  generic prefix match into a *suffix-of-rev* match (hence a palindromic prefix).
- **Empty string** `s = ""`: return `""` immediately.
- **Already a palindrome** (e.g. `"aba"`): `p == n`, leftover is empty, so the
  answer is `s` unchanged.
- **`rev[:len(s) - p]` equals `reverse(s[p:])`:** using `rev` directly avoids an
  extra reversal. If you prefer clarity, `s[p:][::-1] + s` is equivalent.
- **KMP alternative:** the same longest-palindromic-prefix length is the last
  LPS value of `s + '#' + reverse(s)`; Z and KMP are interchangeable here.
