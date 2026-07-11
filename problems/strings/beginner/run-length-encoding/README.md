# Run-Length Encoding (RLE)

**Run-Length Encoding** is a simple lossless compression technique: instead of
storing every character of a string, you store each *run* (a maximal sequence of
identical consecutive characters) as a `(count, character)` pair. The string
`"aaabbc"` becomes the encoding `"a3b2c1"` (or `"3a2b1c"` depending on the chosen
format).

## When to reach for it

- The data contains long stretches of repeated symbols (bitmaps, sparse matrices,
  DNA/protein sequences, fax/scanner images, simple game boards).
- You need a cheap, streaming-friendly compression whose encode/decode logic is
  trivial and has no lookup tables.
- A problem hands you data already in RLE form (a list of `(count, value)` pairs)
  and asks you to expand it, iterate it, or answer queries without fully
  materializing it.

The core loop is always the same: **scan left to right, group equal adjacent
elements, and emit `(runLength, element)`**. Decoding is the mirror image: read a
count, then repeat the element that many times.

## Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Encode a string of length `n` | `O(n)` | `O(1)` extra beyond the output (output can be up to `~2n`) |
| Decode an encoding into a string of length `m` | `O(m)` | `O(1)` extra beyond the output |

RLE is a *single linear pass*. It only helps size-wise when runs are long; on data
with few repeats the "compressed" form can be larger than the original, which is a
recurring theme in the edge cases below.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Basic Run-Length Encoding](problem-01-basic-run-length-encoding/PROBLEM.md) | Encode a string into `char + count` pairs | Easy |
| 2 | [Run-Length Decoding](problem-02-run-length-decoding/PROBLEM.md) | Expand a `char + count` encoding back to the original string | Easy |
| 3 | [Decompress Run-Length Encoded List](problem-03-decompress-rle-list/PROBLEM.md) | Expand `(freq, val)` pairs from a flat array (LeetCode 1313) | Easy |
| 4 | [String Compression](problem-04-string-compression/PROBLEM.md) | In-place RLE where runs of length 1 drop the count (LeetCode 443) | Medium |
| 5 | [Count and Say](problem-05-count-and-say/PROBLEM.md) | Build a sequence where each term is the RLE description of the previous (LeetCode 38) | Medium |
| 6 | [RLE Iterator](problem-06-rle-iterator/PROBLEM.md) | Design an iterator that walks an RLE stream and exhausts `n` elements per call (LeetCode 900) | Medium |
