# Run-Length Decoding

**Difficulty:** Easy

Source: Classic introductory string/compression exercise (inverse of Problem 1).

## Description

You are given a string `encoded` produced by **Run-Length Encoding**, where each
run is stored as a single character followed by its count written in decimal.
For example `"a3b2c1"` decodes to `"aaabbc"`.

Reconstruct and return the original, decompressed string. Counts may span
multiple digits (e.g. `"w12"` means twelve `w`s), and a count of at least `1`
always follows each character.

## Constraints

- `0 <= len(encoded) <= 2 * 10^5`
- `encoded` is a valid RLE string: it is a concatenation of blocks, each block
  being exactly one non-digit character followed by one or more digits that form
  an integer `>= 1`.
- The decoded output fits comfortably in memory (total decoded length `<= 10^6`).
- The empty string decodes to the empty string.

## Examples

### Example 1
```
Input:  encoded = "a3b2c1"
Output: "aaabbc"
Explanation: a*3 = "aaa", b*2 = "bb", c*1 = "c", concatenated to "aaabbc".
```

### Example 2
```
Input:  encoded = "w12"
Output: "wwwwwwwwwwww"
Explanation: The count "12" is two digits, so 'w' is repeated twelve times.
```

### Example 3
```
Input:  encoded = "x1y1z1"
Output: "xyz"
Explanation: Each character has a count of 1, so it appears once.
```

## Hint

This is the inverse of **Run-Length Encoding**: scan the encoding, read one
character, then read the run of digits that follows to get the repeat count, and
append the character that many times.
