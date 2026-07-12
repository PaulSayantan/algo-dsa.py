# Word Pattern

**Difficulty:** Easy

**Source:** LeetCode 290 — Word Pattern

## Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern. Following means a **bijection** between each letter in `pattern` and a non-empty word in `s` (words are separated by single spaces).

## Examples

### Example 1

```
Input:  pattern = "abba", s = "dog cat cat dog"
Output: true
```

### Example 2

```
Input:  pattern = "abba", s = "dog dog dog dog"
Output: false
```

## Hint

Split s into words; enforce a bijection letter<->word with forward and reverse maps.
