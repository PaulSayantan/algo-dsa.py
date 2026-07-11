# Basic Run-Length Encoding

**Difficulty:** Easy

Source: Classic introductory string/compression exercise (common in competitive
programming warmups and interview screens).

## Description

Given a string `s`, compress it using **Run-Length Encoding**. Scan the string
from left to right and replace every *run* — a maximal block of one or more
identical consecutive characters — with the character followed by the length of
the run written in decimal.

For example, the string `"aaabbc"` contains three runs: `"aaa"`, `"bb"`, and
`"c"`, so its encoding is `"a3b2c1"`.

Return the encoded string. Note that this simple format always emits the count,
even when a run has length `1`.

## Constraints

- `0 <= len(s) <= 10^5`
- `s` consists of lowercase and/or uppercase English letters and digits are **not**
  present in `s` (so counts in the output can never be confused with characters).
- The empty string encodes to the empty string.

## Examples

### Example 1
```
Input:  s = "aaabbc"
Output: "a3b2c1"
Explanation: The runs are "aaa" (a, 3), "bb" (b, 2), and "c" (c, 1),
             concatenated as "a3" + "b2" + "c1".
```

### Example 2
```
Input:  s = "abc"
Output: "a1b1c1"
Explanation: Every character is its own run of length 1, so each becomes
             char + "1".
```

### Example 3
```
Input:  s = "wwwwwwwwwwww"
Output: "w12"
Explanation: A single run of 12 'w's collapses to "w12". Multi-digit counts are
             written in full decimal.
```

## Hint

Use **Run-Length Encoding**: make one linear pass, count how long each block of
identical characters lasts, and emit the character plus its count whenever the
character changes (or you reach the end).
