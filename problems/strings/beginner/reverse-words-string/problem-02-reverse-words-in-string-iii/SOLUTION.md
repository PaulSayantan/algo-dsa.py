# Reverse Words in a String III — Solution

## Brute Force

Split on spaces, reverse each token with slicing, and join back:

```python
def reverseWords(self, s: str) -> str:
    return " ".join(word[::-1] for word in s.split(" "))
```

- **Time:** `O(n)` — `split`, per-word reverse, and `join` each scan the input.
- **Space:** `O(n)` — the list of tokens plus the reversed output string.

This is perfectly acceptable and often the expected answer. It is called
"brute force" here only because it allocates helper collections rather than
working on a single buffer.

## Optimal Approach (Reverse Words / String)

Because the guarantee is exactly one space between words and no edge spaces, the
answer has the **same length and the same space positions** as the input. So we
can work on a mutable character buffer and reverse each word segment in place
using the two-pointer primitive.

```python
def reverseWords(self, s: str) -> str:
    chars = list(s)
    n = len(chars)
    start = 0
    for i in range(n + 1):
        if i == n or chars[i] == " ":
            # reverse the word occupying [start, i - 1]
            left, right = start, i - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            start = i + 1
    return "".join(chars)
```

**Why it is correct.** We scan left to right and treat every space (and the
virtual boundary at index `n`) as the end of the current word. The current word
occupies `[start, i - 1]`; reversing just that span flips its letters without
disturbing the spaces or any other word. Setting `start = i + 1` positions us at
the first character of the next word. Because word order and space positions
never change, only the intra-word letters are affected.

**Step-by-step on `"Mr Ding"`:**

1. `i = 2` hits the space. Word span `[0, 1]` = `"Mr"` → reverse to `"rM"`.
   Buffer: `rM Ding`. Set `start = 3`.
2. `i = 7` is the virtual end. Word span `[3, 6]` = `"Ding"` → reverse to
   `"gniD"`. Buffer: `rM gniD`. Done.

Result: `"rM gniD"`.

- **Time:** `O(n)` — every character is read once and swapped at most once.
- **Space:** `O(n)` for the buffer in Python (strings are immutable). In a
  language with mutable strings/char arrays this is `O(1)` auxiliary space.

## Key Insights & Edge Cases

- **Boundary sentinel.** Looping `i` up to and including `n` lets the final word
  (which has no trailing space) be flushed by the same code path. Without the
  `i == n` check you would forget to reverse the last word.
- **Single-character words** (e.g. `"a"`) reverse to themselves; the inner
  `left < right` guard makes this a no-op.
- **Word order is untouched** — this is the key difference from
  "Reverse Words in a String" (I/II), which reverse the order of the words.
- The problem statement forbids leading/trailing spaces and double spaces, which
  is exactly what lets us keep the layout identical and reverse in place. If
  those guarantees were relaxed, prefer the split-reverse-join version or a
  normalization pass first.
