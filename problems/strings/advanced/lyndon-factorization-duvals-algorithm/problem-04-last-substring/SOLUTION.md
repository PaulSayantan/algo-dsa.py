# Solution — Last Substring in Lexicographical Order (LeetCode 1163)

## Brute Force

The lexicographically largest substring is always a suffix, so compare all suffixes.

```python
def lastSubstring_brute(s):
    return max(s[i:] for i in range(len(s)))
```

- **Time:** `O(n^2)` (building/comparing up to `n` suffixes of length up to `n`).
- **Space:** `O(n)` for the slices.

TLEs for `n = 4 * 10^5`.

## Optimal Approach (Duval-style Maximum-Suffix Scan)

Duval's algorithm, in its "smallest suffix" reading, tracks the **minimum** suffix (the
last Lyndon factor). The exact same two-pointer skeleton, with the comparison flipped,
finds the **maximum** suffix in one linear pass.

### Two pointers plus an offset

- `i`: start of the best (largest) candidate suffix found so far.
- `j`: start of the challenger suffix (`j > i`).
- `k`: how many characters `s[i..]` and `s[j..]` have matched so far.

Compare `s[i + k]` with `s[j + k]`:

1. **Equal** (`s[i+k] == s[j+k]`): extend the match, `k += 1`.
2. **Challenger smaller** (`s[i+k] < s[j+k]`): the challenger `j` is actually larger.
   The old best `i` and everything between `i` and `j` cannot start the max suffix, so
   jump `i` forward: `i = max(i + k + 1, j)`, then `j = i + 1`, `k = 0`.
3. **Champion larger** (`s[i+k] > s[j+k]`): the challenger loses; every start in
   `[j, j+k]` is dominated, so `j = j + k + 1`, `k = 0`.

```python
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            else:  # s[i + k] > s[j + k]
                j = j + k + 1
                k = 0
        return s[i:]
```

### Why it's correct

At all times `i` is the start of the best suffix among starts `< j`, and no start in
`(i, j)` can beat it. When the challenger wins (case 2), the new best must start at `j`
(or just after the diverging matched block, whichever is further right, hence
`max(i+k+1, j)`), because any start strictly between the old `i` and `j` shares the
matched prefix and diverged unfavourably. When the champion wins (case 3), all starts in
`[j, j+k]` are provably not the maximum, so we skip past them. Each character advances
either `k`, `i`, or `j` monotonically, so the total work is linear.

- **Time:** `O(n)` — `i + k`, `j`, and `j + k` never decrease across iterations.
- **Space:** `O(1)` extra (the final `s[i:]` slice is the output).

### Relationship to Lyndon / Duval

Finding the **minimum** suffix is exactly the last factor of Duval's Lyndon
factorization. Finding the **maximum** suffix is the dual: reverse the alphabet order (or
flip the comparisons, as above) and the identical amortized-linear argument applies. This
is why the technique lives in the same family as Duval's algorithm.

## Key Insights & Edge Cases

- **Single character** `"z"`: loop never runs, returns `"z"`.
- **All identical** `"aaaa"`: case 1 keeps extending `k` until `j + k` reaches `n`;
  answer is the whole string `"aaaa"` (`i` stays 0).
- **Strictly increasing** `"abc"`: the last char starts the max suffix -> `"c"`.
- **The `max(i + k + 1, j)` guard is essential.** Using plain `i = j` can revisit
  positions and break the linear-time bound (and correctness for overlapping runs like
  `"cacacb"`). Always jump past the matched block.
- The largest *substring* equals the largest *suffix* because extending any substring to
  the end of the string can only make it lexicographically larger or keep it a prefix that
  is then beaten by the longer extension.
