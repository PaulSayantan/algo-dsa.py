# Number of Distinct Substrings

**Difficulty:** Hard

**Source:** Classic (SPOJ DISUBSTR / SUBST1; CP-Algorithms "Number of different substrings").

## Description

Given a string `S`, count the number of **distinct non-empty substrings** of `S`.
Two substrings are the same if they are equal as strings, regardless of where they
occur; each distinct string is counted once.

**Key observation.** The total number of substrings (with multiplicity) is
`n + (n-1) + ... + 1 = n(n+1)/2`, since a substring is any suffix's prefix. When
suffixes are sorted, adjacent suffixes `SA[i-1]` and `SA[i]` share their first
`LCP[i]` characters, so `LCP[i]` prefixes of suffix `SA[i]` are duplicates already
contributed by earlier suffixes. Subtracting all these overlaps gives:

```
distinct substrings = n(n+1)/2 - sum(LCP[i])
```

Return this count as an integer.

## Constraints

- `1 <= len(S) <= 10^5`
- `S` consists of lowercase English letters (method works for any alphabet).
- The answer can be as large as ~`5 * 10^9`, so use 64-bit integers (Python ints are fine).

## Examples

### Example 1
```
Input:  S = "banana"
Output: 15
Explanation: n = 6, so total substrings with repeats = 6*7/2 = 21. The sorted
suffixes have LCP array (adjacent shared-prefix lengths) summing to 6, so distinct
= 21 - 6 = 15. Listing them confirms 15 unique substrings
("a","an","ana","anan","anana","b","ba", ... ,"nana").
```

### Example 2
```
Input:  S = "aaa"
Output: 3
Explanation: The only distinct substrings are "a", "aa", "aaa" -> 3. Total with
repeats = 3*4/2 = 6, sum(LCP) = 3, so 6 - 3 = 3.
```

### Example 3
```
Input:  S = "abc"
Output: 6
Explanation: All substrings are distinct: "a","b","c","ab","bc","abc" -> 6.
Total = 3*4/2 = 6 and sum(LCP) = 0, so 6 - 0 = 6.
```

## Hint

Use **Suffix Array (prefix-doubling / DC3)** plus the **LCP array**. Total prefixes
across all suffixes is `n(n+1)/2`; subtract `sum(LCP)` because each `LCP[i]` counts
prefixes of `SA[i]` already produced by the previous suffix.
