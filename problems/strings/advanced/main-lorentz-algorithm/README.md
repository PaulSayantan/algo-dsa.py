# Main–Lorentz Algorithm

The **Main–Lorentz algorithm** (Main & Lorentz, 1979) finds **all tandem repeats
(a.k.a. squares / repetitions)** in a string of length `n` in **O(n log n)** time.
A *tandem repeat* (or *square*) is a substring of the form `XX` — some non-empty
block `X` immediately followed by an identical copy of `X`. For example, in
`abcabcabc` the substring `abcabc` (`X = abc`) is a square.

## The core idea

The algorithm is a **divide and conquer** on the string:

1. Split `s` into a left half `u` and a right half `v`.
2. Recurse on `u` and on `v` — this catches every square that lies entirely
   inside one half.
3. Find every square that **crosses the boundary** between `u` and `v`. This is
   the clever part, and it is done in linear time using the **Z-function**.

For crossing squares, we fix a "center" position and ask, for each candidate
half-length `l`, how far a match extends to the left and to the right of the
boundary. Those two extension lengths (`k1`, `k2`) come directly from Z-functions
computed on `u`, `v`, and their reverses. Whenever the left extension plus the
right extension is large enough to "cover" `l`, an entire **contiguous range of
squares** of length `2l` exists, and we record it as a range in O(1). Summing the
linear work over all `log n` levels of recursion gives **O(n log n)** total.

The output is naturally compressed: instead of listing squares one by one (there
can be Θ(n²) of them, e.g. in `aaaa...a`), the algorithm emits **O(n log n)
ranges**, each meaning "every start index in `[lo, hi]` begins a square of a fixed
length `2l`." From these ranges you can answer existence, counting, longest,
per-index, and distinctness queries.

## When to reach for it

- You must decide whether a string contains **any** square / tandem repeat.
- You must find the **longest** square, or **count** all square occurrences, when
  `n` is large enough (up to ~10⁵–10⁶) that the O(n²) brute force is too slow.
- You need every repetition in compressed form to feed into further string
  analysis (e.g. computing all *runs* / maximal repetitions).

## Complexity

| Quantity | Cost |
|---|---|
| Time | **O(n log n)** |
| Extra space | **O(n)** (Z-arrays are rebuilt per level) |
| Output size | **O(n log n)** ranges (even when there are Θ(n²) squares) |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Detect a Tandem Repeat](problem-01-detect-tandem-repeat/PROBLEM.md) | Decide whether the string contains any square `XX`. | Easy |
| 2 | [Longest Tandem Repeat](problem-02-longest-tandem-repeat/PROBLEM.md) | Return the leftmost longest square substring. | Medium |
| 3 | [Count Square Substrings](problem-03-count-square-substrings/PROBLEM.md) | Count all occurrences of squares (with multiplicity). | Medium |
| 4 | [Distinct Echo Substrings (LeetCode 1316)](problem-04-distinct-echo-substrings/PROBLEM.md) | Count *distinct* substrings of the form `XX`. | Hard |
| 5 | [Squares Starting at Each Index](problem-05-squares-per-start-index/PROBLEM.md) | For every index, how many squares start there. | Hard |

Work them top to bottom: they reuse the same `square_ranges` primitive, and each
one asks a slightly harder question about the ranges it produces.
