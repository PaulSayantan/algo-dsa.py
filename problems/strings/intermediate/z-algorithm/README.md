# Z-Algorithm

The Z-Algorithm computes, for a string `s` of length `n`, the **Z-array**: an
array where `z[i]` is the length of the longest substring starting at position
`i` that is **also a prefix of `s`**. It builds this entire array in
**O(n)** time and **O(n)** space in a single left-to-right pass.

## The core idea

For each `i >= 1`, `z[i] = ` the length of the longest common prefix (LCP)
between `s` and the suffix `s[i:]`. A naive computation compares from scratch at
every `i`, which is O(n^2). The Z-Algorithm reuses work by maintaining a
**Z-box** `[l, r]` — the interval with the largest right endpoint `r` that is
known to match a prefix of `s` (i.e. `s[l..r]` equals `s[0..r-l]`).

When we reach a new index `i`:

- **Inside the box** (`i <= r`): the character at `i` mirrors the character at
  `i - l` inside the prefix. So we can *reuse* the already-computed value
  `z[i - l]`, capped so it does not run past the box: `z[i] = min(r - i + 1, z[i - l])`.
- **Then extend**: try to grow `z[i]` by comparing `s[z[i]]` with `s[i + z[i]]`
  character by character.
- **Update the box**: if `i + z[i] - 1 > r`, slide the box to `l = i`,
  `r = i + z[i] - 1`.

The `while` loop that extends matches only ever pushes `r` forward, and `r`
never moves backward, so across the whole run the extension work is bounded by
`n` — giving the linear bound.

`z[0]` has no single convention. For prefix-matching answers it is convenient to
set `z[0] = n` (the whole string trivially matches itself). Many
substring-search uses leave it as `0` and simply ignore index 0.

## When to reach for the Z-Algorithm

- **Pattern matching** — search for `pattern` in `text` by running Z on
  `pattern + sep + text`; every position with `z[i] == len(pattern)` is a match.
- **Prefix = suffix / borders** — a suffix starting at `i` equals a prefix
  exactly when `z[i] == n - i`; this exposes all borders (e.g. "longest happy
  prefix").
- **LCP of the string with each of its suffixes** — this is *literally* the
  Z-array, so problems phrased as "sum of common-prefix lengths" become a sum
  over `z`.
- **Palindrome tricks** — run Z on `s + sep + reverse(s)` to find the longest
  palindromic prefix (shortest palindrome).
- **Periodicity / distinct-substring counting** — Z-values reveal repeated
  structure, similar to KMP's failure function but often easier to reason about.

Compared to KMP: the Z-array and the KMP prefix (LPS) array carry equivalent
information and are interconvertible. Z is frequently the more intuitive tool
when the question is naturally about "how far does a prefix reappear here?".

## Complexity

| Quantity                       | Cost      |
|--------------------------------|-----------|
| Build Z-array                  | O(n) time |
| Extra space (the array itself) | O(n)      |
| Pattern search (`p` + sep + `t`)| O(n + m) time |

The amortized argument: the box's right endpoint `r` is non-decreasing and can
advance at most `n` times total; every explicit character comparison in the
extend loop advances `r`, so the total comparison count is O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Find First Occurrence (strStr)](problem-01-find-first-occurrence/PROBLEM.md) | Canonical Z pattern search via `pattern + sep + text` | Easy |
| 2 | [String Matching in an Array](problem-02-string-matching-in-an-array/PROBLEM.md) | Repeated substring tests with Z | Easy |
| 3 | [Longest Happy Prefix](problem-03-longest-happy-prefix/PROBLEM.md) | Borders via `z[i] == n - i` | Medium |
| 4 | [Sum of Scores of Built Strings](problem-04-sum-of-scores-of-built-strings/PROBLEM.md) | Answer is the sum of the Z-array | Hard |
| 5 | [Shortest Palindrome](problem-05-shortest-palindrome/PROBLEM.md) | Longest palindromic prefix via `s + sep + reverse(s)` | Hard |

Work through them top to bottom. The first two drill the raw matching pattern;
the last three each reinterpret the Z-array in a different way (borders, LCP
sums, palindromes), which is exactly how the technique surfaces in interviews
and contests.
