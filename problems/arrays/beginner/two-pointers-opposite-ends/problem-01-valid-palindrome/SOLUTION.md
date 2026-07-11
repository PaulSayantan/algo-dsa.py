# Valid Palindrome — Solution

## Brute Force

Build a cleaned string by keeping only alphanumeric characters and lowercasing
them, then compare it to its reverse.

```python
cleaned = [c.lower() for c in s if c.isalnum()]
return cleaned == cleaned[::-1]
```

- **Time:** `O(n)` to filter and `O(n)` to reverse/compare → `O(n)`.
- **Space:** `O(n)` for the cleaned copy and its reversal.

This is perfectly acceptable, but it allocates extra memory proportional to the
input. The two-pointer approach removes that overhead.

## Optimal Approach (Two Pointers, opposite ends)

Keep two indices, `left = 0` and `right = len(s) - 1`, and walk them toward each
other.

1. While `left < right`:
   - Advance `left` rightward while `s[left]` is **not** alphanumeric.
   - Retreat `right` leftward while `s[right]` is **not** alphanumeric.
   - If now `left < right` and `s[left].lower() != s[right].lower()`, the string
     is **not** a palindrome → return `False`.
   - Otherwise step inward: `left += 1`, `right -= 1`.
2. If the loop finishes without a mismatch, return `True`.

**Why it is correct.** A string is a palindrome iff the *k*-th significant
character from the front equals the *k*-th significant character from the back
for every *k*. The two pointers visit exactly those significant (alphanumeric)
characters in matching front/back order, skipping the ignorable ones. Any
mismatch immediately disproves the palindrome property; if none is found, all
mirrored pairs matched.

```python
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

- **Time:** `O(n)` — each index is moved inward at most `n` times total.
- **Space:** `O(1)` — only two integer indices, no extra copy of the string.

## Key Insights & Edge Cases

- **Guard the inner skip loops** with `left < right` so you never run the
  pointers past each other while skipping a run of punctuation.
- **Empty / all-punctuation strings** (e.g. `" "`, `",.;"`) collapse to an empty
  significant sequence, which is a palindrome → `True`.
- **Case-insensitivity**: lowercase both characters before comparing.
- **Digits count** as alphanumeric — `"0P"` is `False` (`'0'` vs `'p'`), while
  `"aba"` and `"1a2a1"` are palindromes.
- Comparing at a single center character is naturally handled: when `left` and
  `right` land on the same index the `while left < right` guard stops the loop.
