# Solution — Longest Palindromic Substring

## Brute Force

Enumerate every substring and check each with the two-pointer palindrome
test, keeping the longest that passes.

```python
def longestPalindrome(s: str) -> str:
    def is_pal(t: str) -> bool:
        return t == t[::-1]

    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j - i + 1 > len(best) and is_pal(s[i:j + 1]):
                best = s[i:j + 1]
    return best
```

- **Time:** O(n^3) — O(n^2) substrings, each checked in O(n).
- **Space:** O(n) for the substring slices (O(1) if you check by index).

Correct, but too slow for the upper end of the constraints and wasteful.

## Optimal Approach (Expand Around Center)

Every palindrome is symmetric about a center. A length-`n` string has
`2n - 1` possible centers: `n` single-character centers (odd-length
palindromes) and `n - 1` between-character centers (even-length
palindromes). For each center place two pointers and push them **outward**
as long as the characters match; the widest match at that center is the
longest palindrome centered there. Take the best over all centers.

```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    def expand(left: int, right: int) -> tuple:
        # Grow outward while in bounds and characters match.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Loop overshoots by one on each side; the palindrome is (left+1, right-1).
        return left + 1, right - 1

    start, end = 0, 0
    for center in range(len(s)):
        l1, r1 = expand(center, center)        # odd length
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(center, center + 1)    # even length
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]
```

### Why it is correct

A substring `s[l..r]` is a palindrome iff `s[l] == s[r]` and the inner
substring `s[l+1..r-1]` is a palindrome. Expanding outward from a center
enforces exactly this recurrence: starting from a trivially palindromic core
(a single character, or an empty gap between two positions) and stepping out
one matched pair at a time. Because we start every possible center, the
global maximum over all centers is the longest palindromic substring in the
whole string. When the `while` finally fails, the pointers have moved one
step past the valid range, so the palindrome is `[left+1, right-1]`.

### Step-by-step on `"cbbd"`

- Center at index 0 `'c'`: odd expand -> `"c"`; even expand `('c','b')`
  fails -> length 1.
- Center at index 1 `'b'`: odd -> `"b"`; even `('b','b')` matches, expand to
  `(0,3)`? `s[0]='c'` vs `s[3]='d'` mismatch -> stays `"bb"` (length 2). New
  best.
- Remaining centers yield nothing longer -> answer `"bb"`.

- **Time:** O(n^2) — `2n - 1` centers, each expansion O(n) worst case.
- **Space:** O(1) — only indices are tracked; the result is one final slice.

## Key Insights & Edge Cases

- **Two center types.** Missing the even-length centers (`center, center+1`)
  is the classic bug — you would never find `"bb"` or `"abba"`.
- **Off-by-one after expansion.** The `while` loop always steps one beyond
  the palindrome, so the valid bounds are `left+1` and `right-1`.
- **Empty / single char:** guard the empty string; a single character is its
  own answer.
- **Ties:** any longest palindrome is acceptable; comparing strictly with
  `>` keeps the first maximal one found.
- **Manacher's algorithm** solves this in O(n), but expand-around-center is
  the intuitive two-pointer approach and is fast enough for `n <= 1000`.
