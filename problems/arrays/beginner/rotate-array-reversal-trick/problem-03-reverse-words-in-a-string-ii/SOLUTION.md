# Reverse Words in a String II — Solution

## Brute Force

Join the character array into a string, split on spaces, reverse the resulting
list of words, and join them back with spaces:

```python
words = "".join(s).split(" ")
s[:] = list(" ".join(reversed(words)))
```

- **Time:** O(n).
- **Space:** O(n) — the intermediate string and word list violate the O(1)
  extra-space requirement.

## Optimal Approach — The Reversal Trick

Do it in two phases, both using an in-place two-pointer reverse:

1. **Reverse the entire array.** This reverses the word order, but every word is
   now spelled backwards.
2. **Reverse each word in place.** Scan for word boundaries (spaces) and reverse
   each `[start, end]` span, which fixes the internal letter order.

```python
def reverseWords(self, s: List[str]) -> None:
    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

    n = len(s)
    reverse(0, n - 1)               # phase 1: reverse everything

    start = 0                       # phase 2: reverse each word
    for i in range(n + 1):
        if i == n or s[i] == " ":
            reverse(start, i - 1)
            start = i + 1
```

### Why it is correct

Model the sentence as blocks `w1 · sp · w2 · sp · ... · wm`. Reversing the whole
array gives `reverse(wm) · sp · ... · sp · reverse(w1)` — the words are now in
reverse order (correct!) but each word's letters are reversed. Phase 2 reverses
each word block back to its original spelling, leaving the words in reversed
order with correct spelling. This is the same "reverse all, then un-reverse each
block" structure as Rotate Array, applied at word granularity.

Worked example, `"the sky is blue"`:

```
phase 1 (reverse all):    "eulb si yks eht"
reverse "eulb" -> "blue":  "blue si yks eht"
reverse "si"   -> "is":    "blue is yks eht"
reverse "yks"  -> "sky":   "blue is sky eht"
reverse "eht"  -> "the":   "blue is sky the"
```

### Complexity

- **Time:** O(n) — one full reversal plus one pass that reverses disjoint word
  spans; every character is swapped at most twice.
- **Space:** O(1) — only index variables.

## Key Insights & Edge Cases

- **Boundary sentinel:** looping `i` up to `n` (inclusive) and treating `i == n`
  like a space cleanly flushes the final word without duplicating the reverse
  call after the loop.
- **Single word:** phase 1 reverses it, then phase 2 reverses it back —
  net unchanged, which is correct (`"hello"` stays `"hello"`).
- **Order of phases is interchangeable:** reversing each word first and then the
  whole array produces the same result. Choose whichever reads more clearly.
- **Single-space guarantee** matters: this variant assumes exactly one space
  between words and no padding, so no whitespace normalization is needed (unlike
  LeetCode 151).
