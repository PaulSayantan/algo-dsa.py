# Substring Equality Queries

**Difficulty:** Medium

**Source:** Classic — polynomial prefix hashing

## Description

Given a string `s` and a list of queries `(a, b, length)`, answer for each whether `s[a : a+length]` equals `s[b : b+length]`. Build prefix hashes once and answer every query in O(1). Return a list of booleans.

## Examples

### Example 1

```
Input:  s = "ababab", queries = [(0,2,2),(0,1,2)]
Output: [True, False]
```

## Hint

hash(s[l..r]) = (H[r+1] - H[l]*PW[r-l+1]) % MOD; compare the two window hashes.
