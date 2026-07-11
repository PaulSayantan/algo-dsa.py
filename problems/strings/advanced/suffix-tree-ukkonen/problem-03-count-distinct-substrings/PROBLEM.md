# Count Distinct Substrings

**Difficulty:** Hard

Source: Classic (SPOJ "DISUBSTR" / "SUBST1"; LeetCode 1698 "Number of Distinct Substrings in a String")

## Description

Given a string `s`, count the number of **distinct non-empty substrings** of
`s`. Two substrings are the same if they are equal as strings, regardless of
where they occur; each distinct string is counted once.

Return that count as an integer.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- A substring is a contiguous, non-empty slice of `s`.
- The count can be as large as about `n * (n + 1) / 2` (roughly `5 * 10^9` for
  `n = 10^5`), so use a 64-bit / arbitrary-precision integer.

## Examples

### Example 1
```
Input:  s = "banana"
Output: 15
Explanation: There are 6 + 5 + 4 + 3 + 2 + 1 = 21 substrings counting
  positions, but duplicates ("a", "an", "ana", "n", "na", "nan") collapse.
  The 15 distinct substrings are:
    a, an, ana, anan, anana, b, ba, ban, bana, banan, banana, n, na, nan, nana.
```

### Example 2
```
Input:  s = "aaa"
Output: 3
Explanation: The only distinct substrings are "a", "aa", and "aaa".
```

### Example 3
```
Input:  s = "abc"
Output: 6
Explanation: All 6 substrings are distinct: a, b, c, ab, bc, abc.
```

## Hint

Append a unique terminal character and build a **Suffix Tree with Ukkonen's
algorithm**. Each distinct substring is a distinct place where a path (ending at
a node or partway along an edge) can stop. That count equals the **sum of the
lengths of all edge labels** in the tree — just remember to exclude the single
edge character contributed by the terminal sentinel.
