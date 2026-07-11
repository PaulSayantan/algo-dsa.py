# Solution — Valid Palindrome

## Brute Force

Build a cleaned string by keeping only alphanumeric characters (lowercased),
then compare it to its reverse.

```python
def isPalindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```

- **Time:** O(n) — one pass to filter, one pass to reverse and compare.
- **Space:** O(n) — a new list/string is allocated for the cleaned copy and
  its reverse.

This is perfectly correct and readable, but it allocates extra memory
proportional to the input.

## Optimal Approach (Two Pointers)

Avoid the extra string. Keep two indices, `left` at the start and `right` at
the end, and walk them toward each other.

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters from the left.
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right.
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare the two ends, case-insensitively.
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### Why it is correct

A string is a palindrome iff the k-th significant character from the front
equals the k-th significant character from the back, for every k. The two
pointers enumerate exactly these paired positions (skipping characters that
do not count). If any pair mismatches, the string is not a palindrome and we
return early. If the pointers meet or cross with no mismatch, every pair
matched, so it is a palindrome.

### Step-by-step on `"A man, a plan, a canal: Panama"`

1. `left` -> `'A'`, `right` -> `'a'`; equal (case-insensitive). Move inward.
2. Skip the space/comma as needed; compare `'m'` vs `'m'`, `'a'` vs `'a'`, ...
3. Every significant pair matches until the pointers cross -> return `True`.

- **Time:** O(n) — each pointer advances monotonically, so each character is
  visited at most once.
- **Space:** O(1) — only two integer indices are used.

## Key Insights & Edge Cases

- **Empty / all-punctuation input** (e.g. `" "`, `",."`): after skipping, the
  pointers immediately meet or cross, so we return `True` (an empty sequence
  is a palindrome).
- **Bounds inside the skip loops matter:** the inner `while` loops must keep
  the `left < right` guard, otherwise a string of only non-alphanumeric
  characters could push a pointer out of range.
- **Case folding:** compare with `.lower()` (or `.upper()`), not raw
  characters, since `'A'` should equal `'a'`.
- **Digits count:** `isalnum()` keeps digits, so `"0P0"` is a palindrome.
- Using `str.isalnum()` handles letters and digits in one check; if you
  only wanted ASCII letters you would test membership explicitly.
