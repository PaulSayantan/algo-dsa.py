# Reverse Vowels of a String — Solution

## Brute Force

Collect all vowels into a list, reverse that list, then walk the string again
and pop vowels off the reversed list as you encounter vowel positions:

```python
def reverseVowels(self, s: str) -> str:
    vowels = set("aeiouAEIOU")
    collected = [c for c in s if c in vowels]
    out = list(s)
    j = len(collected) - 1
    for i, c in enumerate(out):
        if c in vowels:
            out[i] = collected[j]
            j -= 1
    return "".join(out)
```

- **Time:** `O(n)` — two passes over the string.
- **Space:** `O(n)` — the `collected` list and the output buffer.

Correct, but it uses an extra list just to hold the vowels.

## Optimal Approach (Reverse Words / String)

This is the two-pointer reversal skeleton with a filter: only act when *both*
ends point at a vowel. `left` scans forward until it finds a vowel; `right`
scans backward until it finds a vowel; then we swap them and step both inward.

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
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)
```

**Why it is correct.** The relative order of the vowels is what gets reversed.
The `left` pointer always stops on the leftmost not-yet-processed vowel and
`right` on the rightmost. Swapping them puts the last unprocessed vowel where
the first should go and vice versa — exactly the reversal permutation restricted
to vowel positions. Consonants are skipped by advancing a single pointer, so
they never move. The window `[left, right]` shrinks every iteration, guaranteeing
termination.

**Step-by-step on `"leetcode"`** (indices: 0=l 1=e 2=e 3=t 4=c 5=o 6=d 7=e,
so vowels sit at 1, 2, 5, 7):

| left | right | action | buffer |
|------|-------|--------|--------|
| 0 | 7 | `s[0]='l'` not vowel → left++ | `leetcode` |
| 1 | 7 | both vowels (e,e) → swap, left++, right-- | `leetcode` |
| 2 | 6 | `s[6]='d'` not vowel → right-- | `leetcode` |
| 2 | 5 | both vowels (e,o) → swap, left++, right-- | `leotcede` |
| 3 | 4 | `s[3]='t'` not vowel → left++ | `leotcede` |
| 4 | 4 | `left == right` → stop | `leotcede` |

Result: `"leotcede"`. (The e↔e swap in the second row is a no-op on the visible
string, but it correctly consumes the outermost vowel pair.)

- **Time:** `O(n)` — each pointer moves monotonically; total moves bounded by `n`.
- **Space:** `O(n)` for the Python buffer; `O(1)` auxiliary in a language with
  mutable strings.

## Key Insights & Edge Cases

- **Case matters.** Include both lowercase and uppercase vowels in the set, or
  you will miss `A`, `E`, etc. Using a `set` gives `O(1)` membership tests.
- **Skip logic uses `if/elif/else`.** Only the `else` branch (both are vowels)
  performs a swap and moves both pointers. Advancing just one pointer at a time
  keeps consonants fixed.
- **No vowels / one vowel:** the loop either never swaps or the single vowel maps
  to itself — both return `s` unchanged, which is correct.
- **Equal vowels swapped:** swapping two identical vowels is harmless; you can
  optionally skip it, but it does not affect correctness.
- This generalizes the pure reversal: "reverse only the elements that satisfy a
  predicate" reuses the same converging-pointer shape.
