# Solution — Number of Segments in a String

## Brute Force

Scan the string character by character. Maintain a boolean `in_segment`. Every
time you transition from a space (or the start of the string) into a non-space
character, you have started a new segment, so increment a counter.

```python
def countSegments(s: str) -> int:
    count = 0
    in_segment = False
    for ch in s:
        if ch != " ":
            if not in_segment:
                count += 1
                in_segment = True
        else:
            in_segment = False
    return count
```

- **Time:** `O(n)` — one pass over the string.
- **Space:** `O(1)` — only two scalar variables.

This is perfectly correct, but it re-implements exactly what the language's split
routine already does.

## Optimal Approach (String Tokenization / Split)

Tokenize on whitespace and count the tokens:

```python
def countSegments(s: str) -> int:
    return len(s.split())
```

**Why it is correct.** `str.split()` with **no argument** splits on *runs* of
whitespace and automatically discards leading/trailing empty pieces. So
`"  a   b  ".split()` returns `["a", "b"]`. Each returned element is exactly one
maximal run of non-space characters — the problem's definition of a segment. The
length of that list is therefore the number of segments.

**Step by step** for `s = "Hello, my name is John"`:

1. `split()` scans left to right, collapsing every whitespace run into a boundary.
2. It yields `["Hello,", "my", "name", "is", "John"]`.
3. `len(...)` is `5`. Done.

For `s = "   "`, `split()` returns `[]` (all whitespace collapses to nothing), so
the answer is `0`.

- **Time:** `O(n)` — split makes a single linear scan.
- **Space:** `O(n)` — the token list. If you truly need `O(1)` auxiliary space,
  fall back to the brute-force scan; both are `O(n)` time.

## Key Insights & Edge Cases

- **Use no-argument `split()`, not `split(" ")`.** `"a  b".split(" ")` returns
  `["a", "", "b"]` — the empty string between the two spaces would be miscounted.
  The parameterless form is the one that collapses whitespace runs.
- **Empty string** `""` → `split()` returns `[]` → `0`. Correct.
- **All spaces** `"   "` → `[]` → `0`. Correct.
- **No spaces** `"Hello"` → `["Hello"]` → `1`. Correct.
- The constraint list allows punctuation inside tokens (e.g. `"Hello,"`); that is
  irrelevant to splitting since only the space character is a delimiter here.
