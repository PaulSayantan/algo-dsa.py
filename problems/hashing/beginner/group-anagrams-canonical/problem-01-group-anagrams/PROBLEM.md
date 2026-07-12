# Group Anagrams

**Difficulty:** Medium

**Source:** LeetCode 49 — Group Anagrams

## Description

Given an array of strings `strs`, group the anagrams together. Two strings are anagrams if one is a rearrangement of the other. You may return the groups in any order. The reference sorts each group and then sorts the list of groups so the output is canonical.

## Examples

### Example 1

```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["ate","eat","tea"],["bat"],["nat","tan"]]
```

## Hint

Key each word by its sorted letters; append into a dict of lists. Sort inner groups and the outer list for a stable answer.
