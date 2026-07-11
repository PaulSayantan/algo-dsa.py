# Solution — Palindromic Substrings

## Brute Force

Enumerate all `O(n^2)` substrings and test each with a two-pointer palindrome
check, counting the ones that pass.

```python
def countSubstrings(s: str) -> int:
    def is_pal(lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_pal(i, j):
                count += 1
    return count
```

- **Time:** O(n^3) — O(n^2) substrings, each check O(n).
- **Space:** O(1).

Correct but does redundant work: checking `s[i..j]` repeats the interior
comparisons already done for `s[i+1..j-1]`.

## Optimal Approach (Expand Around Center)

Instead of validating each substring from scratch, generate palindromes
directly from their centers. There are `2n - 1` centers (`n` single-character
centers for odd lengths and `n - 1` between-character centers for even
lengths). From each center, push two pointers outward; **every** time the
outer characters match, the current `[left, right]` window is a distinct
palindromic substring, so increment the count and keep going.

```python
def countSubstrings(s: str) -> int:
    n = len(s)

    def count_from(left: int, right: int) -> int:
        cnt = 0
        while left >= 0 and right < n and s[left] == s[right]:
            cnt += 1          # s[left..right] is a palindrome
            left -= 1
            right += 1
        return cnt

    total = 0
    for center in range(n):
        total += count_from(center, center)       # odd-length centers
        total += count_from(center, center + 1)   # even-length centers
    return total
```

### Why it is correct

A palindromic substring is uniquely determined by its center and its radius.
Each center produces palindromes of increasing radius, and expansion stops at
the first mismatch or the string boundary — exactly the point where no larger
palindrome shares that center. Because every palindromic substring has a
well-defined center that we visit, and each successful expansion corresponds
to one distinct `(left, right)` index pair, the running total counts each
palindromic substring exactly once. Different index ranges naturally count
separately, matching the problem's definition.

### Step-by-step on `"aaa"`

- Center 0 odd: `"a"` (1). Even `(0,1)`: `"aa"` (1), then `(-1,2)` out of
  bounds. Subtotal 2.
- Center 1 odd: `"a"`, then `(0,2)` `s[0]='a'==s[2]='a'` -> `"aaa"` (2 total).
  Even `(1,2)`: `"aa"` (1). Subtotal 3.
- Center 2 odd: `"a"` (1). Even `(2,3)` out of bounds (0). Subtotal 1.
- Total = 2 + 3 + 1 = **6**, matching "a","a","a","aa","aa","aaa".

- **Time:** O(n^2) — `2n - 1` centers, each expansion up to O(n).
- **Space:** O(1) — only counters and indices.

## Key Insights & Edge Cases

- **Count during expansion, not after.** Each matched pair *is* a new
  palindrome; add one on every successful step rather than only counting the
  maximal one.
- **Both center types.** Odd centers (`center, center`) and even centers
  (`center, center + 1`) together cover all `2n - 1` axes; skipping the even
  ones undercounts (you would miss the `"aa"` substrings).
- **Every single character counts**, so the answer is always at least `n`
  (see `"abc"` -> 3).
- **Duplicates by position:** identical-looking substrings at different
  indices are counted separately, which expand-around-center handles for free
  because each center is independent.
- **Relation to LeetCode 5:** the same expansion machinery that *counts*
  palindromes here can instead track the *longest* one — the two problems are
  two readouts of the identical two-pointer expansion.
