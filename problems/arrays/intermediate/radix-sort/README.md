# Radix Sort

**Radix Sort** is a *non-comparison* sorting algorithm. Instead of comparing whole
keys against one another, it sorts data one "digit" at a time, from the least
significant digit (LSD) to the most significant digit (MSD), delegating each
single-digit pass to a **stable** counting sort. Because each pass is stable, the
relative order established by the earlier (less significant) passes is preserved,
and after processing every digit the whole array ends up fully sorted.

A "digit" is whatever fixed-size symbol you choose: a base-10 digit, a byte
(base 256), a character in a string, or an entire key in a tuple of keys. The
number of distinct symbol values is the *radix* `k`.

## When to reach for it

- You are sorting **integers**, **fixed-length strings**, or **fixed-length
  tuples/records** where keys are drawn from a small, bounded alphabet.
- The number of digits `d` is small and the radix `k` is `O(n)` or smaller, so
  the `O(d · (n + k))` bound beats `O(n log n)` comparison sorts.
- You need a **stable** sort (radix sort is naturally stable when built on a
  stable subsort).

Avoid it when keys are unbounded-precision, when `d` is large relative to
`log n`, or when the data is not easily decomposed into fixed digits.

## Complexity

| Metric | Cost |
|--------|------|
| Time | `O(d · (n + k))` where `d` = number of digits, `k` = radix (values per digit) |
| Space | `O(n + k)` auxiliary (output buffer + counting array) |
| Stable | Yes (when the per-digit subsort is stable) |
| In-place | No (needs an output buffer) |

For 32-bit integers processed one byte at a time, `d = 4` and `k = 256`, so the
work is `O(4 · (n + 256)) = O(n)` in practice.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort an Array](problem-01-sort-an-array/PROBLEM.md) | Sort integers (including negatives) with LSD radix sort | Medium |
| 2 | [Sort Fixed-Length Strings](problem-02-sort-fixed-length-strings/PROBLEM.md) | LSD radix sort over equal-length strings | Medium |
| 3 | [Sort Records by Date](problem-03-sort-records-by-date/PROBLEM.md) | Multi-key stable radix sort by day, month, year | Medium |
| 4 | [Maximum Gap](problem-04-maximum-gap/PROBLEM.md) | Sort in linear time, then scan for the largest adjacent gap | Hard |
| 5 | [Build a Suffix Array](problem-05-suffix-array/PROBLEM.md) | Prefix-doubling suffix array via radix sort of rank pairs | Hard |
