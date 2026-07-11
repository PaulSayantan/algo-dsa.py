# Group Anagrams

**Difficulty:** Medium

Source: LeetCode 49 — Group Anagrams

## Description

Given an array of strings `strs`, group the anagrams together. You can return the
answer in **any order**, and the strings within each group may also be in any order.

An **anagram** is a word formed by rearranging the letters of another word, using all
the original letters exactly once. Two strings belong to the same group if and only if
one is an anagram of the other.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters (the empty string is allowed).

## Examples

### Example 1

```
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Explanation: "eat", "tea", "ate" all share the letters a/e/t. "tan" and "nat" share
a/n/t. "bat" has no partner. (Any ordering of the groups or of members within a group
is accepted.)
```

### Example 2

```
Input:  strs = [""]
Output: [[""]]
Explanation: A single empty string forms one group by itself.
```

### Example 3

```
Input:  strs = ["a"]
Output: [["a"]]
Explanation: A single one-letter string forms one group by itself.
```

## Hint

Use an **Anagram Check (sort or count)** to compute a canonical *signature* for each
string (its sorted letters, or its 26-length count tuple). Strings with the same
signature are anagrams — group them with a hash map keyed by that signature.
