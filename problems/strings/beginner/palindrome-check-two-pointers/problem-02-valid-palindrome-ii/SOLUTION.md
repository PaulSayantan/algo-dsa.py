# Solution — Valid Palindrome II

## Brute Force

Try deleting each character one at a time and test whether the resulting
string is a palindrome; also test the original with no deletion.

```python
def validPalindrome(s: str) -> bool:
    def is_pal(t: str) -> bool:
        return t == t[::-1]

    if is_pal(s):
        return True
    for i in range(len(s)):
        if is_pal(s[:i] + s[i + 1:]):
            return True
    return False
```

- **Time:** O(n^2) — up to `n` deletions, each costing O(n) to build and
  compare.
- **Space:** O(n) — each candidate substring is materialized.

For `n` up to 10^5 this is far too slow.

## Optimal Approach (Two Pointers)

Scan inward with two pointers. As long as the ends match, keep closing in —
that portion is guaranteed palindromic. The **first** mismatch is the only
place a deletion could help, and there are only two ways to spend the single
allowed deletion: drop the left character or drop the right character. After
that deletion no further deletions are allowed, so each candidate reduces to
a plain palindrome check.

```python
def validPalindrome(s: str) -> bool:
    def is_pal(lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Spend the one deletion: skip left OR skip right.
            return is_pal(left + 1, right) or is_pal(left, right - 1)
        left += 1
        right -= 1
    return True  # already a palindrome, zero deletions used
```

### Why it is correct

While `s[left] == s[right]`, those two characters are a valid matching pair
and cannot benefit from a deletion, so we advance safely. At the first
mismatch, a palindrome with one deletion is possible **iff** removing one of
the two offending characters leaves the interior `[left+1, right]` or
`[left, right-1]` as a palindrome. The outer characters already matched
symmetrically, so only this inner window needs to be a plain palindrome.
Testing both candidates covers every legal single deletion. If we finish the
outer loop with no mismatch, the string was already a palindrome.

### Step-by-step on `"abca"`

1. `left=0 ('a')`, `right=3 ('a')` -> match, move inward.
2. `left=1 ('b')`, `right=2 ('c')` -> mismatch.
3. Try `is_pal(2, 2)` (skip left 'b'): single char `"c"` window -> palindrome
   -> return `True`. (`is_pal(1, 1)` skipping right would also succeed.)

- **Time:** O(n) — the outer scan is O(n) and at most one inner O(n) check
  runs (only after the first mismatch).
- **Space:** O(1) — indices only; `is_pal` works on the original string.

## Key Insights & Edge Cases

- **Only the first mismatch matters.** Everything before it already paired
  up correctly, so there is no reason to consider deletions there.
- **Exactly two candidates.** A common bug is to test only one side; you must
  try skipping both the left and the right character.
- **Already a palindrome:** the loop completes without a mismatch and returns
  `True` using zero deletions.
- **Length 1 or 2 with equal chars** (e.g. `"a"`, `"aa"`): trivially `True`.
- **Reuse the index-based helper** `is_pal(lo, hi)` instead of slicing so the
  check stays O(1) space and does not re-copy the string.
