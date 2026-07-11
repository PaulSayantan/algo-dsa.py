# Solution - Valid Palindrome

## Brute Force

Build a cleaned string (lowercase, alphanumeric only), then compare it with its
reverse.

```python
cleaned = [c.lower() for c in s if c.isalnum()]
return cleaned == cleaned[::-1]
```

- **Time:** `O(n)` to filter and `O(n)` to reverse and compare.
- **Space:** `O(n)` for the cleaned copy and its reversal.

This is clean and correct, but it allocates two auxiliary strings. We can do it
in place with `O(1)` extra space.

## Optimal Approach (Two Pointers)

Keep `left` at the start and `right` at the end. Repeat while `left < right`:

1. Advance `left` rightward while it points at a non-alphanumeric character.
2. Advance `right` leftward while it points at a non-alphanumeric character.
3. Compare `s[left]` and `s[right]` case-insensitively. If they differ, the
   string is not a palindrome, so return `False`.
4. Otherwise step both pointers inward (`left += 1`, `right -= 1`).

If the pointers cross without a mismatch, return `True`.

### Why it is correct

A string is a palindrome iff the i-th significant character from the front
equals the i-th significant character from the back, for all i. The two pointers
enumerate exactly those significant character pairs from the outside in,
skipping characters that the problem says to ignore. Each comparison verifies
one required equality; a single failure disproves the palindrome, and exhausting
all pairs proves it. Because both pointers only move inward, the scan halts.

### Step-by-step (s = "race a car")

Cleaned view: `r a c e a c a r`.

| left char | right char | match? |
|-----------|------------|--------|
| r         | r          | yes    |
| a         | a          | yes    |
| c         | c          | yes    |
| e         | a          | **no** → return False |

### Reference implementation

```python
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

- **Time:** `O(n)` — each pointer moves through the string at most once.
- **Space:** `O(1)` — no auxiliary copy of the string.

## Key Insights & Edge Cases

- **Skip before compare.** The two `continue` guards must run before the
  comparison so pointers land on alphanumeric characters.
- **Empty / all-punctuation strings** (`" "`, `",.;"`) are palindromes: the
  loop's guards move the pointers past each other with no comparison, returning
  `True` (Example 3).
- **Case-insensitivity** requires `.lower()` (or `.upper()`) on both sides.
- **Digits count** as alphanumeric, so `"0P"` is `False` and `"aba"` is `True`.
- Using `left < right` (strict) means the exact middle character of an
  odd-length string is never compared to itself, which is correct.
