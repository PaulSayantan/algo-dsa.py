# Solution — Reverse Words in a String

## Brute Force

Manually parse words while skipping over arbitrary runs of spaces, push each word
onto a list, then emit the list in reverse joined by single spaces. The tricky
part is correctly skipping leading, trailing, and repeated interior spaces so you
never emit an empty word.

```python
def reverseWords(s: str) -> str:
    words = []
    i, n = 0, len(s)
    while i < n:
        while i < n and s[i] == " ":   # skip spaces
            i += 1
        if i >= n:
            break
        j = i
        while j < n and s[j] != " ":   # read one word
            j += 1
        words.append(s[i:j])
        i = j
    return " ".join(reversed(words))
```

- **Time:** `O(n)`.
- **Space:** `O(n)`.

Correct, but the double-`while` whitespace skipping is precisely the boilerplate
that tokenization eliminates.

## Optimal Approach (String Tokenization / Split)

Split on whitespace runs (which also strips the ends), reverse the token list,
and join:

```python
def reverseWords(s: str) -> str:
    return " ".join(reversed(s.split()))
```

**Why it is correct.** Parameterless `s.split()` splits on *any run* of
whitespace and drops leading/trailing empties, so it returns exactly the clean
list of words regardless of how many spaces separate them —
`"  a good   example ".split()` → `["a", "good", "example"]`. `reversed(...)`
flips their order, and `" ".join(...)` reinserts exactly one space between each,
guaranteeing no extra spaces in the result.

**Step by step** for `s = "a good   example"`:

1. `s.split()` → `["a", "good", "example"]` (the triple space collapses).
2. `reversed(...)` → iterator yielding `"example", "good", "a"`.
3. `" ".join(...)` → `"example good a"`. Done.

For `s = "  hello world  "`: split → `["hello", "world"]`, reversed →
`["world", "hello"]`, join → `"world hello"` — no leading/trailing spaces.

- **Time:** `O(n)`.
- **Space:** `O(n)` for the token list and output.

## Key Insights & Edge Cases

- **Must use `split()` not `split(" ")`.** With multiple spaces, `split(" ")`
  produces empty strings (`"a  b".split(" ")` → `["a", "", "b"]`) which would
  create stray spaces after joining. The no-argument form is what makes this a
  clean one-liner.
- **Leading/trailing spaces** are handled for free by `split()`.
- `reversed(list)` returns an iterator; `join` consumes it directly, so you don't
  need `list(...)` around it. `s.split()[::-1]` also works.
- **Single word input** (`"hello"`) → `["hello"]` → `"hello"`. Correct.
- If asked to do it **in place with O(1) extra space** (a common follow-up), the
  classic trick is: reverse the entire character array, then reverse each word
  back — but Python strings are immutable, so the split-based approach is the
  natural fit here.
