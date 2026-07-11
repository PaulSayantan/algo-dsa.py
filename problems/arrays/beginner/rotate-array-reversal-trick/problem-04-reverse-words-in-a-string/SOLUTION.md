# Reverse Words in a String — Solution

## Brute Force

Lean on library functions: `str.split()` with no argument already splits on
runs of whitespace and drops leading/trailing spaces, so:

```python
return " ".join(reversed(s.split()))
```

- **Time:** O(n).
- **Space:** O(n) — a list of words plus the output string.

This is perfectly acceptable in an interview if allowed, but it hides the
mechanics. The reversal-trick approach below is what you would use in a language
with mutable strings and an O(1)-extra-space requirement.

## Optimal Approach — The Reversal Trick

Work on a mutable character list. Two ideas combine:

1. **Whitespace normalization:** compact the array so there are no leading,
   trailing, or doubled spaces.
2. **Reversal trick:** reverse the whole array, then reverse each word — exactly
   like Reverse Words in a String II.

```python
def reverseWords(self, s: str) -> str:
    chars = list(s)

    # Phase A: compact spaces in place -> write index `w`.
    w = 0
    i, n = 0, len(chars)
    while i < n:
        if chars[i] != " ":
            if w != 0:                # add a separator before every word but the first
                chars[w] = " "
                w += 1
            while i < n and chars[i] != " ":   # copy the whole word
                chars[w] = chars[i]
                w += 1
                i += 1
        else:
            i += 1
    chars = chars[:w]                 # trim to the compacted length
    m = len(chars)

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            chars[lo], chars[hi] = chars[hi], chars[lo]
            lo += 1
            hi -= 1

    # Phase B: reverse everything, then reverse each word.
    reverse(0, m - 1)
    start = 0
    for j in range(m + 1):
        if j == m or chars[j] == " ":
            reverse(start, j - 1)
            start = j + 1

    return "".join(chars)
```

### Why it is correct

After Phase A the array is a clean `w1 · sp · w2 · sp · ... · wm` with single
separators and no padding. Phase B is the standard reversal trick: reversing the
whole array reverses word *order* while leaving each word spelled backwards, and
reversing each word span restores its spelling. The composition yields the words
in reversed order, correctly spelled — the desired output.

Worked example, `s = "a good   example"`:

```
compact:              "a good example"
reverse all:          "elpmaxe doog a"
reverse "elpmaxe":    "example doog a"
reverse "doog":       "example good a"
reverse "a":          "example good a"   (single char, unchanged)
result:               "example good a"
```

### Complexity

- **Time:** O(n) — compaction is one pass; the reversal phase touches each
  character a constant number of times.
- **Space:** O(n) in Python only because strings are immutable and we build a
  char list. In a language with mutable strings the same logic is O(1) extra
  space.

## Key Insights & Edge Cases

- **This differs from LC 186 only by the normalization step.** Once spaces are
  clean, it *is* Reverse Words in a String II.
- **Multiple / leading / trailing spaces** (`"  hello world  "`) are the crux:
  the `w != 0` guard emits a separator only *between* words, so no stray spaces
  survive.
- **Single word after trimming:** reversing all then reversing the one word
  cancels out — correct.
- **All-caps of the reversal identity:** the order of the two reversals in Phase
  B can be swapped (reverse each word first, then the whole array) for the same
  result.
