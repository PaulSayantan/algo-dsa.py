# Check if the Sentence Is Pangram

**Difficulty:** Easy

**Source:** LeetCode 1832 — Check if the Sentence Is Pangram

## Description

A pangram is a sentence that contains every letter of the English alphabet at least once. Given a string `sentence` of lowercase letters, return `true` if it is a pangram and `false` otherwise.

## Examples

### Example 1

```
Input:  sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
```

### Example 2

```
Input:  sentence = "leetcode"
Output: false
```

## Hint

Collect the distinct characters into a set; it's a pangram iff the set has all 26 letters.
