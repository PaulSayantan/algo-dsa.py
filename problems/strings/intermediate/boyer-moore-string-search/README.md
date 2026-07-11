# Boyer–Moore (String Search)

Boyer–Moore is a single-pattern string-matching algorithm that aligns the
pattern `P` (length `m`) against the text `T` (length `n`) and **compares
characters right-to-left**. On a mismatch (or a full match) it uses two
precomputed shift heuristics to slide the pattern forward by more than one
position, often skipping large chunks of text without ever looking at them —
which is why it can be **sublinear on average**.

## The two shift rules

1. **Bad-character rule.** When text character `c` causes a mismatch, shift the
   pattern so its *last* occurrence of `c` lines up under that text position
   (or shift past it entirely if `c` does not occur in the pattern). Precomputed
   as a "last occurrence" table over the alphabet.
2. **Good-suffix rule.** When a suffix of the pattern already matched before the
   mismatch, shift so that the next occurrence of that matched suffix (or a
   prefix of the pattern that is also a suffix of it) lines up. Precomputed with
   a border/failure-style table in `O(m)`.

On each step take the **larger** of the two proposed shifts (and never shift by
less than 1). Preprocessing is `O(m + |Σ|)`; matching is `O(n·m)` worst case but
`O(n/m)` best case and `O(n)`-ish on typical text. Space is `O(m + |Σ|)`.

## When to reach for it

- You are searching for **one** fixed pattern in a (possibly long) text and want
  the fast average case, especially with a **large alphabet** where the
  bad-character rule skips aggressively (this is what `grep`, editors, and many
  `strstr`/`memmem` implementations use).
- Many "does substring exist / where" problems, and clever reductions like
  *"is `goal` a rotation of `s`?"* → search `goal` inside `s + s`, or
  *"is `s` a repetition of a block?"* → search `s` inside `(s+s)[1:-1]`.

If you need every occurrence of *many* patterns at once, prefer Aho–Corasick; if
you need guaranteed worst-case linear time, KMP is the simpler choice. Boyer–
Moore shines on the common single-pattern case.

## Complexity summary

| Phase | Time | Space |
|---|---|---|
| Preprocess pattern | `O(m + |Σ|)` | `O(m + |Σ|)` |
| Search (worst case) | `O(n·m)` | — |
| Search (average / best) | sublinear, ~`O(n/m)` best | — |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Implement strStr()](problem-01-implement-strstr/PROBLEM.md) | Return the index of the first occurrence of `needle` in `haystack`. | Easy |
| 2 | [Rotate String](problem-02-rotate-string/PROBLEM.md) | Decide whether `goal` is some rotation of `s` via a search in `s + s`. | Easy |
| 3 | [Repeated Substring Pattern](problem-03-repeated-substring-pattern/PROBLEM.md) | Decide whether `s` is built by repeating one substring, via a search in `(s+s)[1:-1]`. | Easy |
| 4 | [Find All Occurrences](problem-04-find-all-occurrences/PROBLEM.md) | Return every start index where `pattern` appears in `text` (overlaps included). | Medium |
| 5 | [Repeated String Match](problem-05-repeated-string-match/PROBLEM.md) | Fewest copies of `a` so that `b` becomes a substring. | Medium |
| 6 | [Find Beautiful Indices](problem-06-beautiful-indices/PROBLEM.md) | Indices of `a` in `s` that sit within distance `k` of some occurrence of `b`. | Medium |
