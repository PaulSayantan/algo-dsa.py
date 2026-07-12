# Find and Replace Pattern

**Difficulty:** Medium

**Source:** LeetCode 890 — Find and Replace Pattern

## Description

Given a list of `words` and a `pattern`, return the words that match the pattern. A word matches if there is a bijection between letters so that replacing each pattern letter yields the word. Return the matching words in the **same order** as the input.

## Examples

### Example 1

```
Input:  words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
```

## Hint

Normalize each string to its first-occurrence index pattern (e.g. 'abb' -> [0,1,1]); a word matches iff its normalized form equals the pattern's.
