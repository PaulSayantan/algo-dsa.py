# String Tokenization / Split

**Category:** Strings / Beginner

## What It Is

*Tokenization* (also called *splitting*) is the act of breaking a string into a
list of smaller pieces — **tokens** — using one or more **delimiter** characters
(spaces, commas, slashes, dots, punctuation, ...). It is the single most common
first step in text processing: once a raw string has been chopped into a clean
list of tokens, the rest of the problem usually reduces to iterating over that
list.

In Python the workhorses are:

- `str.split(sep=None)` — split on a delimiter. With **no argument** it splits on
  *runs* of whitespace **and** discards leading/trailing empties (great for messy
  input like `"  a   b  "` → `["a", "b"]`). With an explicit `sep` it splits on
  every single occurrence and **keeps** empty tokens (`"a,,b".split(",")` →
  `["a", "", "b"]`).
- `str.rsplit`, `str.splitlines`, and `str.partition` for specialized cases.
- `re.split(pattern, s)` when the delimiter is a *character class* or regex
  (e.g. "split on any non-letter").
- `str.join` — the inverse operation that stitches tokens back together.

## When To Reach For It

Reach for tokenization whenever the input is a **sentence, path, version string,
CSV row, or any delimiter-separated record** and the logic naturally operates on
whole tokens rather than individual characters. Typical tells: "words separated
by spaces", "components separated by `/`", "revisions separated by `.`".

If you find yourself manually scanning character-by-character to carve out
substrings, a single `split` call usually replaces that entire loop.

## Complexity

- **Time:** `O(n)` to scan and split a string of length `n`.
- **Space:** `O(n)` to hold the resulting tokens (plus any joined output).

Splitting is linear and cheap; the "algorithm" is really about *choosing the
right delimiter* and *handling edge cases* (empty tokens, extra delimiters,
leading/trailing separators).

## Problems

| # | Problem | Technique Focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Number of Segments in a String](problem-01-number-of-segments/PROBLEM.md) | Split on whitespace, count tokens | Easy |
| 2 | [Reverse Words in a String III](problem-02-reverse-words-in-string-iii/PROBLEM.md) | Split, reverse each token, rejoin | Easy |
| 3 | [Reverse Words in a String](problem-03-reverse-words-in-a-string/PROBLEM.md) | Split on whitespace runs, reverse token order | Medium |
| 4 | [Compare Version Numbers](problem-04-compare-version-numbers/PROBLEM.md) | Split on `.`, compare numeric tokens | Medium |
| 5 | [Simplify Path](problem-05-simplify-path/PROBLEM.md) | Split on `/`, process tokens with a stack | Medium |
