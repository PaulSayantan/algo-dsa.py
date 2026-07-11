# Shortest Palindrome — Solution

## Key reduction

We may only prepend characters. If the longest palindromic **prefix** of `s` has
length `k`, then `s[0:k]` is already a palindrome and stays fixed at the center.
The suffix `s[k:]` is not part of any palindromic prefix, so its reverse must be
placed in front to mirror it. The answer is:

```
reverse(s[k:]) + s
```

and its length is `n + (n - k)`, minimized precisely by maximizing `k`. So the
whole problem collapses to: **find the longest palindromic prefix.**

## Brute Force

Check `s[0:len]` for being a palindrome for `len = n, n-1, ..., 1`, stop at the
first hit `k`, then return `reverse(s[k:]) + s`.

- Up to n prefix checks, each O(n).
- **Time:** O(n^2). **Space:** O(n).

A KMP-based O(n) solution also exists (build the failure function of
`s + "#" + reverse(s)`), but here we use Manacher.

## Optimal Approach (Manacher's Algorithm)

1. **Transform:** `t = "#" + "#".join(s) + "#"`.
2. **Run Manacher** to obtain `p[i]` = palindrome radius at center `i` in `t`
   (which equals the palindrome length in `s`).
3. **Find the longest palindromic prefix.** A palindrome centered at `i` in `s`
   starts at original index `(i - p[i]) // 2`. It is a *prefix* iff that start
   index is 0. Scan all centers, and among those with start index 0 take the
   maximum length `k`.
4. **Build the answer:** `return s[k:][::-1] + s`.

### Reference implementation

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        c = r = 0
        best = 0  # longest palindromic-prefix length
        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while (i - p[i] - 1 >= 0 and i + p[i] + 1 < n
                   and t[i - p[i] - 1] == t[i + p[i] + 1]):
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
            start = (i - p[i]) // 2
            if start == 0 and p[i] > best:
                best = p[i]
        return s[best:][::-1] + s
```

- **Time:** O(n). **Space:** O(n).

### Why it is correct

Manacher yields the exact maximal radius at each center, so the set of "palindromes
that start at index 0" is complete. Taking the longest one gives the true longest
palindromic prefix `k`. The suffix `s[k:]` cannot overlap any longer palindromic
prefix (else `k` would be larger), so its reversal is both necessary and sufficient
to make the concatenation a palindrome, and no shorter prepend can work.

## Key Insights & Edge Cases

- **Only the prefix matters:** because insertion is restricted to the front, the
  longest palindromic prefix fully determines the minimal answer.
- **Start-at-0 test:** the condition `(i - p[i]) // 2 == 0` selects palindromes
  anchored at the left end; among these the maximum `p[i]` is the answer length.
- **Already a palindrome:** e.g. `"aba"` -> best = 3, `s[3:]` is empty, so the
  output equals `s`.
- **No palindromic prefix beyond one char:** e.g. `"abcd"` -> best = 1, prepend
  `reverse("bcd") = "dcb"`.
- **Empty string:** return `""` immediately.
- **Large n (5*10^4):** the quadratic scan can be too slow in the worst case (e.g.
  `"a"*25000 + "b" + ...` style inputs); the O(n) Manacher pass stays comfortably
  fast.
