# K-th Smallest Distinct Substring

**Difficulty:** Hard

Source: Classic (competitive programming; e.g. SPOJ SUBLEX "Lexicographical Substring Search")

## Description

Given a string `s` and an integer `k`, return the **k-th lexicographically
smallest distinct substring** of `s`. Distinct means duplicated substrings are
considered a single entry, so the ranking is over the *set* of distinct
substrings sorted lexicographically (`1`-indexed).

If `k` exceeds the number of distinct substrings, return `"-1"`.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= 10^9`
- Ranking is `1`-indexed: `k = 1` asks for the smallest distinct substring.

## Examples

### Example 1
```
Input:  s = "dbac", k = 3
Output: "b"
Explanation: The distinct substrings of "dbac" in sorted order are:
  1: a
  2: ac
  3: b
  4: ba
  5: bac
  6: c
  7: d
  8: db
  9: dba
  10: dbac
  The 3rd is "b".
```

### Example 2
```
Input:  s = "dbac", k = 5
Output: "bac"
Explanation: From the sorted list above, the 5th distinct substring is "bac".
```

### Example 3
```
Input:  s = "banana", k = 6
Output: "b"
Explanation: The sorted distinct substrings of "banana" begin:
  1: a, 2: an, 3: ana, 4: anan, 5: anana, 6: b, ...
  so the 6th is "b".
```

## Hint

Build the **Suffix Array** and **LCP array (Kasai's algorithm)**. Walking the
suffix array in sorted order visits substrings in lexicographic order; sorted
suffix `i` contributes `(n - SA[i]) - LCP[i]` *new* distinct prefixes. Subtract
these counts from `k` until you land inside the block that contains the answer.
