# Count Distinct Substrings

**Difficulty:** Medium

Source: Classic (SPOJ DISUBSTR / competitive programming staple)

## Description

Given a string `s`, count the number of **distinct non-empty substrings** of
`s`. Two substrings are considered the same if they are equal as strings, no
matter where they occur, so each distinct string is counted exactly once.

Return the count as an integer.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- The answer can be as large as about `n(n+1)/2 ~= 5 * 10^9`, so use 64-bit
  integers (Python `int` is unbounded, so this is automatic there).

## Examples

### Example 1
```
Input:  s = "banana"
Output: 15
Explanation: The total number of substrings (with repeats) is
  6*7/2 = 21. The distinct substrings are:
    length 1: a, b, n              (3)
    length 2: an, ba, na           (3)
    length 3: ana, ban, nan        (3)
    length 4: anan, bana, nana     (3)
    length 5: anana, banan         (2)
    length 6: banana               (1)
  Total = 3+3+3+3+2+1 = 15.
```

### Example 2
```
Input:  s = "aaa"
Output: 3
Explanation: The only distinct substrings are "a", "aa", and "aaa".
  There are 3*4/2 = 6 substrings counting repeats, but 3 of them are duplicates.
```

### Example 3
```
Input:  s = "abc"
Output: 6
Explanation: All substrings are distinct: a, b, c, ab, bc, abc -> 6 = 3*4/2.
```

## Hint

Build the **Suffix Array** and its **LCP array (Kasai's algorithm)**. Every
substring is a prefix of exactly one suffix; a suffix of length `L` contributes
`L` prefixes, but the first `LCP[i]` of them were already contributed by the
previous suffix in sorted order. Sum the *new* prefixes.
