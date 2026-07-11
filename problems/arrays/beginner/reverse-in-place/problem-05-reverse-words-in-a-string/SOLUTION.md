# Reverse Words in a String — Solution

## Brute Force

Lean on the language's built-ins: split on whitespace (which discards empty tokens from
runs of spaces), reverse the list of words, and join with a single space.

```python
return " ".join(reversed(s.split()))
```

- **Time:** O(n) — splitting, reversing, and joining are each linear.
- **Space:** O(n) — the list of word tokens and the output string. Clean and idiomatic,
  but it hides the underlying reversal mechanics.

## Optimal Approach (Reverse In-Place)

The instructive, low-level version works on a mutable character buffer using two kinds
of reversal — the classic technique interviewers look for (and the intended solution
when the buffer is given as a `char[]`, as in the follow-up):

1. Clean the buffer: trim leading/trailing spaces and collapse interior runs of spaces
   to a single space (can be done in place with a slow/fast pointer).
2. Reverse the **entire** buffer.
3. Reverse **each individual word** back, so its characters read forward again.

```python
def reverseWords(self, s: str) -> str:
    # Step 1: collapse spaces into a mutable list of chars.
    chars = []
    i, n = 0, len(s)
    while i < n:
        if s[i] != " ":
            if chars:
                chars.append(" ")          # single separator between words
            while i < n and s[i] != " ":
                chars.append(s[i])
                i += 1
        else:
            i += 1

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            chars[lo], chars[hi] = chars[hi], chars[lo]
            lo += 1
            hi -= 1

    # Step 2: reverse the whole buffer.
    reverse(0, len(chars) - 1)

    # Step 3: reverse each word back to normal.
    start = 0
    for end in range(len(chars) + 1):
        if end == len(chars) or chars[end] == " ":
            reverse(start, end - 1)
            start = end + 1

    return "".join(chars)
```

**Why it is correct:** Reversing the whole buffer flips both the order of the words
*and* the letters inside each word. The words are now in the desired final order, but
each is spelled backward. Reversing every word individually undoes the letter flip
while preserving the new word order — leaving the words reversed but each spelled
correctly.

Worked example on `"the sky is blue"`:
- Reverse all -> `"eulb si yks eht"`
- Reverse each word -> `"blue is sky the"`  ✓

- **Time:** O(n) — cleaning is one pass; the whole-buffer reverse is O(n); the sum of
  the per-word reverses is also O(n).
- **Space:** O(n) only because Python strings are immutable (a `char[]` input could be
  handled with O(1) extra space).

## Key Insights & Edge Cases

- **Two-level reversal** is the heart of the trick: global reverse for word order, local
  reverse for spelling.
- **Space handling** is the fiddly part: strip leading/trailing spaces and collapse
  interior runs to exactly one space before (or during) the reversals.
- **Single word:** global reverse then word reverse cancel out — the word is returned
  unchanged (aside from trimming), which is correct.
- **All-of-word boundary:** the loop uses `end == len(chars)` as a sentinel so the final
  word is also reversed even though it is not followed by a space.
