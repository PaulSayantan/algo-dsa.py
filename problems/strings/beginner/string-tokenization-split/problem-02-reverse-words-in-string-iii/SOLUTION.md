# Solution — Reverse Words in a String III

## Brute Force

Walk the string, accumulate characters of the current word into a buffer, and
when you hit a space (or the end), append the reversed buffer to the output plus
the space. This works but forces you to track word boundaries by hand.

```python
def reverseWords(s: str) -> str:
    out = []
    word = []
    for ch in s:
        if ch == " ":
            out.append("".join(reversed(word)))
            out.append(" ")
            word = []
        else:
            word.append(ch)
    out.append("".join(reversed(word)))  # flush final word
    return "".join(out)
```

- **Time:** `O(n)`.
- **Space:** `O(n)` for the buffers.

The manual boundary bookkeeping (and the "flush the last word" trap) is exactly
what tokenization removes.

## Optimal Approach (String Tokenization / Split)

Split into words, reverse each token with a slice, and re-join with a single
space:

```python
def reverseWords(s: str) -> str:
    return " ".join(word[::-1] for word in s.split(" "))
```

**Why it is correct.** The problem guarantees words are separated by exactly one
space with no leading/trailing spaces, so `s.split(" ")` yields exactly the list
of words with no empty tokens. `word[::-1]` reverses each word's characters.
`" ".join(...)` places exactly one space back between every pair of words,
reproducing the required spacing.

**Step by step** for `s = "Mr Ding"`:

1. `s.split(" ")` → `["Mr", "Ding"]`.
2. Reverse each: `"Mr"[::-1]` → `"rM"`, `"Ding"[::-1]` → `"gniD"`.
3. `" ".join(["rM", "gniD"])` → `"rM gniD"`. Done.

- **Time:** `O(n)` — split, per-character reversal, and join are each linear.
- **Space:** `O(n)` — token list plus output string.

## Key Insights & Edge Cases

- **Single word** (`"hello"`) → `split(" ")` returns `["hello"]` → reversed →
  `"olleh"`. Correct.
- **`split(" ")` vs `split()`:** here the guarantee of *exactly one* space means
  either would work, but `split(" ")` is the literal match for the spec. If the
  input could contain double spaces, you would need to preserve them, so you must
  match the delimiter model to the guarantees.
- **Reverse with a slice** (`word[::-1]`) is idiomatic and `O(len(word))`; no need
  for an explicit two-pointer swap.
- Because there are no leading/trailing spaces, you never produce a stray empty
  token, so no filtering is required.
