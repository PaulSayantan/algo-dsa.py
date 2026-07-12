# Isomorphic Strings

**Difficulty:** Easy

**Source:** LeetCode 205 — Isomorphic Strings

## Description

Given two strings `s` and `t`, determine if they are isomorphic. Two strings are isomorphic if the characters of `s` can be replaced to get `t`, where each character maps to exactly one character and no two characters map to the same one (the mapping must be a bijection). Order is preserved.

## Examples

### Example 1

```
Input:  s = "egg", t = "add"
Output: true
```

### Example 2

```
Input:  s = "foo", t = "bar"
Output: false
```

**Explanation:** 'o' would need to map to both 'a' and 'r'.

## Hint

Keep two maps s->t and t->s; every position must agree with both or it's not a bijection.
