# Reverse Words in a String — Solution

## Brute Force

Lean on the language's tokenizer. Python's `str.split()` with no argument
splits on runs of whitespace and drops empty tokens, which handles all the
leading/trailing/multiple-space cases for free:

```python
def reverseWords(self, s: str) -> str:
    return " ".join(reversed(s.split()))
```

- **Time:** `O(n)` — `split`, `reversed`, and `join` each scan the data.
- **Space:** `O(n)` — the token list and the output string.

This is idiomatic and usually accepted. The interesting version is the
`O(1)`-auxiliary-space in-place approach on a mutable character buffer.

## Optimal Approach (Reverse Words / String)

The **reverse-whole-then-per-word** trick. On a mutable char array:

1. **Reverse the entire buffer.** Now the words are in the desired order but
   each word's letters are backwards, and spacing is still messy.
2. **Reverse each word back** using the two-pointer primitive, so its letters
   read correctly again.
3. **Normalize spaces** — either done in the same pass by compacting, or as a
   separate cleanup step.

Because Python strings are immutable, a clean way to show the idea while still
handling spaces is a manual two-pass build:

```python
def reverseWords(self, s: str) -> str:
    chars = []
    i, n = len(s) - 1, len(s)
    while i >= 0:
        # skip trailing/extra spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        if i < 0:
            break
        # mark end of the word, walk back to its start
        end = i
        while i >= 0 and s[i] != " ":
            i -= 1
        # s[i+1 .. end] is a word; append it, then a single space
        if chars:
            chars.append(" ")
        chars.append(s[i + 1:end + 1])
    return "".join(chars)
```

Or the pure double-reversal form on a buffer where spaces are pre-normalized:

```python
def reverseWords(self, s: str) -> str:
    words = s.split()          # normalizes spaces
    chars = list(" ".join(words))
    reverse(chars, 0, len(chars) - 1)      # step 1: reverse whole
    start = 0                              # step 2: reverse each word back
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == " ":
            reverse(chars, start, i - 1)
            start = i + 1
    return "".join(chars)
```

**Why the double-reversal works.** Reversing the whole buffer maps the word at
positions `[a, b]` to positions `[n-1-b, n-1-a]` and flips it. So the last word
becomes first (correct order) but spelled backwards. Reversing each word segment
in its new location un-flips the letters, leaving the words in reversed order and
spelled correctly.

**Step-by-step on `"the sky is blue"`:**

1. Reverse whole: `"eulb si yks eht"`.
2. Reverse each word segment back:
   - `"eulb"` → `"blue"`
   - `"si"` → `"is"`
   - `"yks"` → `"sky"`
   - `"eht"` → `"the"`
3. Result: `"blue is sky the"`.

- **Time:** `O(n)` — a constant number of linear passes.
- **Space:** `O(n)` in Python (immutable strings force a buffer); `O(1)`
  auxiliary in a language with mutable strings once spaces are normalized.

## Key Insights & Edge Cases

- **Space normalization is the trap.** Leading, trailing, and doubled spaces
  must all collapse to single separators with none on the ends. `str.split()`
  with no argument does this automatically; a manual scan must skip space runs.
- **Single word:** `"hello"` → `"hello"`. Reversing the order of one word is a
  no-op; the double reversal (reverse whole then reverse the one word back)
  returns the original.
- **All spaces trimmed to nothing?** The constraints guarantee at least one
  word, so the output is never empty here — but a robust manual version should
  still handle an all-space buffer by returning `""`.
- **Contrast with Problem 2 (III):** there we kept word order and reversed
  letters; here we reverse word order and keep letters. The double-reversal
  trick elegantly does both by composing the two reversals.
