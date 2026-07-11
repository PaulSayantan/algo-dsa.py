# Reverse Vowels of a String — Solution

## Brute Force

Scan the string once, collect all vowels into a list, then scan again and pop vowels
off the end of that list to refill the vowel positions.

```python
vowels = set("aeiouAEIOU")
collected = [c for c in s if c in vowels]
result = list(s)
for i, c in enumerate(result):
    if c in vowels:
        result[i] = collected.pop()   # pop() takes from the end -> reversed order
return "".join(result)
```

- **Time:** O(n) — two passes.
- **Space:** O(n) — the `collected` list plus the `result` list. Works, but uses extra
  storage proportional to the number of vowels.

## Optimal Approach (Reverse In-Place)

Convert the string to a mutable list of characters (Python strings are immutable, so
some copy is unavoidable, but the *reversal itself* is done in place with O(1) extra
work). Then run two pointers from both ends:

```python
def reverseVowels(self, s: str) -> str:
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] not in vowels:
            left += 1
        elif chars[right] not in vowels:
            right -= 1
        else:                       # both are vowels -> swap them
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)
```

**Why it is correct:** The two pointers only ever swap when both point at vowels, so
consonants are never moved. Every vowel encountered from the left is paired with the
symmetric vowel from the right, exactly mirroring the pure reverse-in-place pattern
but restricted to the sub-sequence of vowels. That produces the reversed vowel order
in their original slots.

- **Time:** O(n) — each pointer moves inward at most n times total.
- **Space:** O(1) extra beyond the character-list copy that Python's immutable strings
  force (the swap logic allocates nothing).

## Key Insights & Edge Cases

- **Advance-on-consonant** is the key twist: unlike a plain reverse, a pointer that
  lands on a non-vowel must move without swapping.
- **Case sensitivity:** uppercase vowels count too, so the vowel set must include
  `AEIOU`. The swap preserves case exactly (an `I` can land where an `A` was).
- **No vowels / one vowel:** with fewer than two vowels no swap ever fires, and the
  string is returned unchanged — correct, since a length-<=1 vowel subsequence is its
  own reverse.
- **Both-vowel branch must move both pointers**; forgetting to advance one after a swap
  causes an infinite loop.
