# Naive Pattern Matching

**Naive Pattern Matching** (also called the *brute-force* or *sliding-window comparison*
string search) is the most direct way to find every place a **pattern** `P` (length `m`)
occurs inside a **text** `T` (length `n`).

## The Idea

Line the pattern up under the text at position `0`. Compare the pattern against the
text character by character. If every character matches, you have found an occurrence
at that position. Whether it matched fully or not, slide the pattern **one position to
the right** and repeat, until the pattern would run past the end of the text.

```
for start in range(0, n - m + 1):        # every valid alignment
    j = 0
    while j < m and T[start + j] == P[j]: # compare char-by-char
        j += 1
    if j == m:                            # full match found
        report start
```

There is no preprocessing and no auxiliary data structure — just two nested loops.

## When to Reach for It

- The text and/or pattern are **short**, or you only run the search a few times.
- You want something **simple and obviously correct** with no bug-prone preprocessing
  (unlike KMP, Rabin-Karp, or Boyer-Moore).
- Many "does string A contain string B", "is B a rotation of A", or
  "how many times does B occur in A" problems reduce to sliding one string over another.

For very large inputs or many repeated searches, prefer KMP / Z-algorithm / Rabin-Karp,
which achieve `O(n + m)` by avoiding redundant re-comparisons. Naive matching is the
mental model those algorithms optimize.

## Complexity

| Measure | Value | Notes |
|---|---|---|
| Time (worst case) | `O(n · m)` | e.g. `T = "aaaa...a"`, `P = "aaa...ab"` forces `m` comparisons at nearly every alignment |
| Time (typical/random text) | `O(n)` | mismatches usually happen after 1-2 comparisons |
| Space | `O(1)` | only index variables; no extra tables |

Here `n = len(text)` and `m = len(pattern)`, with `m <= n`.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Implement strStr()](problem-01-implement-strstr/PROBLEM.md) | Return the index of the first occurrence of `needle` in `haystack`. | Easy |
| 2 | [Rotate String](problem-02-rotate-string/PROBLEM.md) | Decide whether `goal` is a rotation of `s` by searching `s + s`. | Easy |
| 3 | [Count Pattern Occurrences](problem-03-count-pattern-occurrences/PROBLEM.md) | Count all (overlapping) occurrences of a pattern in a text. | Easy |
| 4 | [Repeated Substring Pattern](problem-04-repeated-substring-pattern/PROBLEM.md) | Decide whether a string is built by repeating one of its substrings. | Medium |
| 5 | [Repeated String Match](problem-05-repeated-string-match/PROBLEM.md) | Fewest repeats of `a` so that `b` becomes a substring. | Medium |

Work them top to bottom — they progress from the textbook search to problems that
*reduce* to a substring search once you spot the trick.
