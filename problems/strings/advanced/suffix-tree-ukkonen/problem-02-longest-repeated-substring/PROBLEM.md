# Longest Duplicate Substring

**Difficulty:** Medium

Source: LeetCode 1044 "Longest Duplicate Substring" (also a classic string problem)

## Description

Given a string `s`, a **duplicated substring** is a contiguous substring that
occurs **at least twice** in `s`. The two occurrences are allowed to **overlap**
(for example, in `"aaaa"` the substring `"aaa"` occurs at indices 0 and 1, which
overlap).

Return **any** longest duplicated substring of `s`. If `s` has no duplicated
substring (every character is distinct), return the empty string `""`.

## Constraints

- `1 <= len(s) <= 3 * 10^4`
- `s` consists of lowercase English letters.
- A substring is a contiguous, non-empty slice of `s`.
- Overlapping occurrences count as two occurrences.
- If several duplicated substrings share the maximum length, returning any one
  of them is acceptable.

## Examples

### Example 1
```
Input:  s = "banana"
Output: "ana"
Explanation: "ana" occurs at indices 1 and 3 (overlapping). No length-4
  substring repeats, so "ana" (length 3) is a longest duplicated substring.
```

### Example 2
```
Input:  s = "abcd"
Output: ""
Explanation: Every character is distinct, so no substring occurs twice.
```

### Example 3
```
Input:  s = "abcabcabc"
Output: "abcabc"
Explanation: "abcabc" occurs at indices 0 and 3 (overlapping). No length-7
  substring repeats, so length 6 is the maximum.
```

## Hint

Append a unique terminal character and build a **Suffix Tree with Ukkonen's
algorithm**. A substring is duplicated **iff** it corresponds to a path ending
at (or passing through) an **internal branching node** — an internal node is
shared by at least two suffixes, so its path-label repeats. The answer is the
deepest internal node measured by the number of characters on the path from the
root (its "string depth").
