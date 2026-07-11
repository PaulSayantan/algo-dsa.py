# Longest Tandem Repeat

**Difficulty:** Medium

Source: Classic competitive-programming problem (longest square substring).

## Description

A **tandem repeat** (**square**) is a non-empty substring of the form `XX`.
Its length is `2·|X|`, always even.

Given a string `s`, return the **longest** substring of `s` that is a tandem
repeat. If several squares share the maximum length, return the one that starts at
the **smallest index** (the leftmost). If `s` contains no square at all, return the
empty string `""`.

## Constraints

- `1 <= len(s) <= 100_000`
- `s` consists of lowercase English letters.
- The answer's length is always even (it is a full square `XX`), or `0` if none
  exists.

## Examples

### Example 1
```
Input:  s = "banana"
Output: "anan"
Explanation: The squares are "anan" (index 1, X = "an") and "nana" (index 2,
             X = "na"), both length 4. The leftmost of the two is "anan".
```

### Example 2
```
Input:  s = "abcabcabc"
Output: "abcabc"
Explanation: The longest squares have length 6: "abcabc" (index 0), "bcabca"
             (index 1), "cabcab" (index 2), "abcabc" (index 3). The leftmost
             starts at index 0, giving "abcabc".
```

### Example 3
```
Input:  s = "abcde"
Output: ""
Explanation: The string is square-free, so there is no tandem repeat.
```

## Hint

Enumerate every square in compressed form as O(n log n) ranges "all starts in
[lo, hi] begin a square of half length l" using the **Main–Lorentz Algorithm**,
then pick the range with the largest `l`, breaking ties by smallest start index.
