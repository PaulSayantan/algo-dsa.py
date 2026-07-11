# Solution — Sum of Scores of Built Strings

## Brute Force

For each built length `i` (from `1` to `n`), take the suffix `s[n - i:]` and
count how many leading characters it shares with `s`, then add that to the total.

```python
def sumScores(s):
    n = len(s)
    total = 0
    for i in range(1, n + 1):
        suffix = s[n - i:]
        k = 0
        while k < len(suffix) and suffix[k] == s[k]:
            k += 1
        total += k
    return total
```

- **Time:** `O(n^2)` — `n` suffixes, each LCP scan up to `O(n)`. On the worst
  case `s = "aaaa...a"` every score is large, so this is genuinely quadratic and
  TLEs at `n = 10^5`.
- **Space:** `O(1)` extra (or `O(n)` if you materialize slices).

## Optimal Approach (Z-Algorithm)

The score of the built string of length `i` is, by the problem's own wording,
the longest common prefix (LCP) of `s` and its suffix of length `i`, i.e. the
suffix that **starts at index `j = n - i`**.

But the LCP of `s` with the suffix starting at index `j` is *exactly the
definition of `z[j]`*. Therefore:

```
score(i) = z[n - i]
```

As `i` ranges over `1 .. n`, the index `j = n - i` ranges over `n-1 .. 0`, so we
touch every entry of the Z-array exactly once. The full string `s_n = s` has
score `n`, matching the convention `z[0] = n`. Hence:

```
answer = sum(z)          # with z[0] = n
```

That is: **build the Z-array and add up its entries.** No separator, no second
string — the problem *is* the Z-array.

### Why it is correct

`z[j]` is defined as the length of the longest prefix of `s` that also occurs
starting at position `j`, which equals the LCP of `s` with `s[j:]`. The built
string of length `i` is precisely the suffix `s[n - i:] = s[j:]` with `j = n-i`,
and the problem defines its score as that same LCP. So `score(i) = z[n-i]`, and
summing over all `i` sums all of `z`.

### Step-by-step on `s = "babab"` (n = 5)

Compute the Z-array:

| j | s[j:]  | z[j] |
|---|--------|------|
| 0 | babab  | 5    |
| 1 | abab   | 0    |
| 2 | bab    | 3    |
| 3 | ab     | 0    |
| 4 | b      | 1    |

`sum(z) = 5 + 0 + 3 + 0 + 1 = 9`. This matches the enumerated scores
`1 + 0 + 3 + 0 + 5 = 9` (the same multiset, just indexed from the other end).

### Reference implementation

```python
from typing import List


def z_array(s: str) -> List[int]:
    n = len(s)
    z = [0] * n
    z[0] = n                 # full string matches the full string
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
    def sumScores(self, s: str) -> int:
        return sum(z_array(s))
```

- **Time:** `O(n)` — one linear Z build plus a linear sum.
- **Space:** `O(n)` for the Z-array (or `O(1)` extra if you accumulate the sum
  inside the Z construction and never store the array).

## Key Insights & Edge Cases

- **Set `z[0] = n`.** The full built string contributes `n` to the total; if you
  leave `z[0] = 0` you must add `n` back manually. Getting this off-by-`n` wrong
  is the most common bug here.
- **Use a 64-bit accumulator.** With `s = "aaaa...a"` and `n = 10^5`, the sum is
  `n(n+1)/2 ≈ 5 * 10^9`, which overflows 32-bit integers. Python integers are
  unbounded, so this is only a concern when porting to C++/Java.
- **The direction of building** (prepend vs. append) does not change the answer:
  the built strings of each length are all suffixes of `s`, and every suffix's
  score is a Z-value, so the multiset of scores is the same as `sum(z)`.
- **`n == 1`:** `z = [1]`, sum `= 1` — the single built string equals `s` and
  scores `1`.
- This is a rare problem where the Z-array is not a *means* to the answer — it
  *is* the answer.
