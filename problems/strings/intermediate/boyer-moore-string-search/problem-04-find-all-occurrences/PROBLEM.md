# Find All Occurrences of a Pattern

**Difficulty:** Medium

**Source:** Classic string-matching exercise (CLRS Ch. 32; equivalent to
Python's `str.find` loop / `re.finditer` for a literal pattern)

## Description

Given a text `text` and a non-empty pattern `pattern`, return a list of **all
start indices** (0-based, in increasing order) at which `pattern` occurs in
`text`. Occurrences may **overlap**.

If the pattern does not occur, return an empty list.

This is the general form of substring search — instead of stopping at the first
match, keep going and report every alignment that matches. Boyer–Moore handles
this directly: after a full match, apply the good-suffix shift for a matched
pattern and continue scanning.

## Constraints

- `1 <= pattern.length <= text.length <= 10^5`
- `text` and `pattern` consist of printable ASCII characters.
- Overlapping matches must all be reported (e.g. `"aa"` in `"aaaa"` occurs at
  indices `0, 1, 2`).

## Examples

### Example 1
```
Input:  text = "ababab", pattern = "ab"
Output: [0, 2, 4]
Explanation: "ab" starts at indices 0, 2, and 4.
```

### Example 2
```
Input:  text = "aabaacaadaabaaba", pattern = "aaba"
Output: [0, 9, 12]
Explanation: "aaba" matches starting at index 0 ("aaba"...),
             index 9 ("...aaba..."), and index 12 ("...aaba" at the end).
```

### Example 3
```
Input:  text = "abcxyz", pattern = "www"
Output: []
Explanation: "www" never appears, so the result is empty.
```

## Hint

Report matches instead of stopping at the first. Use **Boyer–Moore (string
search)**: on a mismatch shift by max(good-suffix, bad-character); on a full
match record the index and shift by the good-suffix value for a complete match.
