# KMP (Knuth–Morris–Pratt)

KMP is a linear-time string-matching algorithm. Given a text of length `n` and a
pattern of length `m`, it finds all occurrences of the pattern in **O(n + m)**
time and **O(m)** extra space — never re-examining a text character it has
already passed.

## The core idea

A naive matcher, on a mismatch, throws away all the progress it made and slides
the pattern forward by one, re-comparing characters it already looked at. KMP
avoids this by precomputing, for the *pattern only*, a **failure / prefix
function** — usually called the **LPS array** (Longest Proper Prefix that is
also a Suffix).

`lps[i]` = the length of the longest proper prefix of `pattern[0..i]` that is
also a suffix of `pattern[0..i]`. When a mismatch happens after matching `k`
characters, instead of restarting we jump to `lps[k-1]`: the pattern's own
structure already guarantees that the first `lps[k-1]` characters still match,
so no text pointer ever moves backward.

## When to reach for KMP

- **Substring search** — find a pattern inside a text (the classic use).
- **Prefix = suffix questions** — "longest border", "longest happy prefix".
- **Periodicity / repetition** — detect whether a string is a repeated block
  (uses the fact that `n - lps[n-1]` is the smallest period when it divides `n`).
- **Palindrome / concatenation tricks** — build a combined string like
  `s + '#' + reverse(s)` and read off its LPS.
- Any problem where you need `O(n)` matching and hashing feels risky
  (collision-sensitive) or where you specifically need the border structure.

## Complexity

| Quantity                | Cost      |
|-------------------------|-----------|
| Build LPS array         | O(m) time |
| Search text             | O(n) time |
| Total                   | O(n + m) time |
| Extra space             | O(m)      |

The amortized argument: the "match" pointer increases at most `n` times total,
and each `lps` fallback strictly decreases it, so the total number of
comparisons is bounded by `2n`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Implement strStr()](problem-01-implement-strstr/PROBLEM.md) | Canonical KMP substring search | Easy |
| 2 | [Repeated Substring Pattern](problem-02-repeated-substring-pattern/PROBLEM.md) | LPS period property of a whole string | Easy |
| 3 | [Repeated String Match](problem-03-repeated-string-match/PROBLEM.md) | KMP search over a bounded concatenation | Medium |
| 4 | [Longest Happy Prefix](problem-04-longest-happy-prefix/PROBLEM.md) | Reading the final LPS value directly | Hard |
| 5 | [Shortest Palindrome](problem-05-shortest-palindrome/PROBLEM.md) | LPS of `s + '#' + reverse(s)` | Hard |

Work through them top to bottom — each one reuses the LPS array in a slightly
different way, so by the end you will have seen the four main ways KMP shows up
in interviews and contests.
