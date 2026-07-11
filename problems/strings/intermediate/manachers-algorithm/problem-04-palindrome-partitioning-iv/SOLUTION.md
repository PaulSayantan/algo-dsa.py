# Palindrome Partitioning IV — Solution

## Brute Force

Try every pair of cut positions `(i, j)` (there are O(n^2) of them) and, for each,
verify all three parts are palindromes with an O(n) two-pointer check.

- **Time:** O(n^3). **Space:** O(1).

With `n` up to 2000 this is ~8 * 10^9 operations in the worst case — too slow.

## Optimal Approach (Manacher's Algorithm)

The bottleneck is the repeated O(n) palindrome verification. If we could answer
"is `s[l..r]` a palindrome?" in O(1), the two-cut scan would be O(n^2), which is
fine for n = 2000. Manacher gives us exactly that after O(n) preprocessing.

### O(1) palindrome query from Manacher radii

Build `t = "#" + "#".join(s) + "#"` and compute the radius array `p` where `p[i]`
is the palindrome length in `s` centered at transformed index `i`. For an original
range `[l, r]` (inclusive), its center in `t` is `l + r + 1` (because original
index `x` maps to transformed index `2x + 1`, and the midpoint of `2l+1` and
`2r+1` is `l + r + 1`). The range is a palindrome iff the radius there covers the
whole span:

```
is_pal(l, r)  ==  p[l + r + 1] >= (r - l + 1)
```

### Search the two cuts

With O(1) queries, iterate the first cut `i` (first part `s[0..i-1]`) and, when
`s[0..i-1]` is a palindrome, iterate the second cut `j` and check the middle part
`s[i..j]` and the tail `s[j+1..n-1]`.

### Reference implementation

```python
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        t = "#" + "#".join(s) + "#"
        m = len(t)
        p = [0] * m
        c = r = 0
        for i in range(m):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < m
                   and t[i - p[i] - 1] == t[i + p[i] + 1]):
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]

        def is_pal(l: int, rr: int) -> bool:
            return p[l + rr + 1] >= (rr - l + 1)

        n = len(s)
        for i in range(1, n - 1):          # first part = s[0..i-1]
            if not is_pal(0, i - 1):
                continue
            for j in range(i, n - 1):      # middle = s[i..j], tail = s[j+1..n-1]
                if is_pal(i, j) and is_pal(j + 1, n - 1):
                    return True
        return False
```

- **Preprocessing:** O(n). **Search:** O(n^2). **Total time:** O(n^2).
- **Space:** O(n).

### Why the center formula is correct

Original index `x` sits at transformed index `2x + 1` (odd positions hold real
characters; `#` occupies even positions). The palindrome covering original `[l, r]`
is centered at the midpoint of transformed indices `2l + 1` and `2r + 1`, namely
`(2l + 1 + 2r + 1) / 2 = l + r + 1`. Its length in `s` equals `p[l + r + 1]`; it
contains `[l, r]` iff that length is at least `r - l + 1`.

## Key Insights & Edge Cases

- **O(1) queries are the whole trick:** Manacher's real value here is not finding a
  single palindrome but enabling constant-time membership so an outer O(n^2) scan
  becomes feasible.
- **Center index parity:** a range `[l, r]` of even length has its center on a `#`
  (even transformed index), and odd length on a letter — the single formula
  `l + r + 1` handles both automatically.
- **Cut bounds:** the loops keep all three parts non-empty (`1 <= i`, `i <= j`,
  `j + 1 <= n - 1`).
- **All identical, e.g. "aaa":** trivially true via three singletons.
- **Early continue:** skipping `j` when the first part is not a palindrome prunes a
  large fraction of pairs in practice.
- **Alternative DP:** a boolean `dp[i][j]` palindrome table (O(n^2) space) also
  gives O(1) queries; Manacher achieves the same with only O(n) space.
