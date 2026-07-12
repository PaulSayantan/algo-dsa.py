# Word Pattern

**Difficulty:** Easy

**Source:** LeetCode 290 — Word Pattern

## Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern. Here *follow* means a full bijection between each letter of `pattern` and each space-separated word in `s`.

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

**Explanation:** 'a' and 'b' both map to 'dog'.

## Hint

Split s on spaces; enforce a bijection between pattern letters and words with two maps.
