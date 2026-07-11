# Find and Replace Pattern

**Difficulty:** Medium

**Source:** LeetCode 890 — Find and Replace Pattern

## Description

Given a list of strings `words` and a string `pattern`, return a list of the
words in `words` that **match** the given pattern. You may return the answer in
any order.

A word matches the pattern if there is a **bijection** (a one-to-one and onto
mapping) of letters `p` such that applying `p` to every letter of `pattern`
produces the word. Formally, no two distinct pattern letters map to the same word
letter, and no two distinct word letters come from the same pattern letter — the
letter substitution must be a permutation.

This is a **hashing signature** problem: reduce each word (and the pattern) to a
canonical *isomorphism signature* — for example, replace each character by the
index of its first occurrence — so that `word` matches `pattern` exactly when
their signatures are equal.

## Constraints

- `1 <= pattern.length <= 20`
- `1 <= words.length <= 50`
- `words[i].length == pattern.length`
- `pattern` and `words[i]` are lowercase English letters.

## Examples

### Example 1

```
Input:  words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: The pattern "abb" normalizes to (0,1,1). "mee" -> (0,1,1) and
"aqq" -> (0,1,1) match. "abc" -> (0,1,2), "deq" -> (0,1,2), "dkd" -> (0,1,0),
"ccc" -> (0,0,0) all differ from the pattern's signature.
```

### Example 2

```
Input:  words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
Explanation: Every single-letter word normalizes to (0), the same as the
pattern, so all of them match.
```

### Example 3

```
Input:  words = ["xyx","yxy","xxx"], pattern = "aba"
Output: ["xyx","yxy"]
Explanation: "aba" normalizes to (0,1,0). "xyx" -> (0,1,0) and "yxy" -> (0,1,0)
match, but "xxx" -> (0,0,0) does not because it collapses two pattern letters
into one word letter (not a bijection).
```

## Hint

Convert each word and the pattern to a canonical **Group Anagrams (hashing
signature)** based on the first-occurrence index of each character, then keep the
words whose signature equals the pattern's.
