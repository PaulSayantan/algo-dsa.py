# Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium

**Source:** LeetCode 1456 — Maximum Number of Vowels in a Substring of Given Length

## Description

Given a string `s` and an integer `k`, return the maximum number of vowels (`a`, `e`, `i`, `o`, `u`) in any substring of `s` of length `k`.

Constraints: `1 <= s.length <= 10^5`, `s` consists of lowercase English letters, `1 <= k <= s.length`.

## Examples

### Example 1

```
Input:  s="abciiidef", k=3
Output: 3
```

**Explanation:** The substring `"iii"` contains 3 vowels, the maximum possible.

## Hint

Treat the vowel count of a size-`k` window as a moving sum: as the window slides, add 1 if the entering char is a vowel and subtract 1 if the leaving char was — track the running maximum.
