# Group Anagrams

**Difficulty:** Medium

**Source:** LeetCode 49 — Group Anagrams

## Description

Given an array of strings `strs`, group **the anagrams** together. You can return
the answer in **any order**, and the groups themselves may be in any order.

An **anagram** is a word formed by rearranging the letters of another word, using
all the original letters exactly once. Two strings belong in the same group if and
only if they have identical character counts.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: "eat", "tea", "ate" share the counts a:1,e:1,t:1 -> one group.
             "tan", "nat" share a:1,n:1,t:1 -> one group.
             "bat" (a:1,b:1,t:1) stands alone. Group order may differ.
```

### Example 2

```
Input:  strs = [""]
Output: [[""]]
Explanation: A single empty string forms its own group (its frequency signature is
             all zeros).
```

### Example 3

```
Input:  strs = ["a"]
Output: [["a"]]
Explanation: One string means one group containing just that string.
```

## Hint

Two words are anagrams exactly when their **Character Frequency Counts** are
identical. Turn each word's 26-length count vector into a hashable signature and
bucket words that share the same signature together in a hash map.
