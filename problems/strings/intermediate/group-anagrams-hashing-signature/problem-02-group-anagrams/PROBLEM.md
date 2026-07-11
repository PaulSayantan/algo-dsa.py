# Group Anagrams

**Difficulty:** Medium

**Source:** LeetCode 49 — Group Anagrams

## Description

Given an array of strings `strs`, group the **anagrams** together. You can return
the answer in **any order**, and the groups themselves may be listed in any
order.

An **anagram** is a word formed by rearranging the letters of another word,
using all the original letters exactly once. Every string that is an anagram of
another must end up in the same group; strings that are not anagrams of any
other string form a group of size one.

This is the canonical application of the **hashing signature** idea: compute a
canonical key for each word so that all anagrams collapse to the same key, then
use that key to bucket the words in a single pass.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
Explanation: "eat", "tea", "ate" all sort to "aet"; "tan", "nat" both sort to
"ant"; "bat" sorts to "abt" alone. The three signatures produce three groups.
```

### Example 2

```
Input:  strs = [""]
Output: [[""]]
Explanation: A single empty string has signature "" and forms one group by
itself.
```

### Example 3

```
Input:  strs = ["a"]
Output: [["a"]]
Explanation: A single one-letter word forms its own group.
```

## Hint

Map every word to a canonical **Group Anagrams (hashing signature)** — the sorted
characters or a character-count tuple — and use that signature as a dictionary
key so all anagrams accumulate in the same bucket.
