# Group Anagrams

**Difficulty:** Medium

**Source:** LeetCode 49 (Group Anagrams)

## Description

Given an array of strings `strs`, group the anagrams together. Two strings are
anagrams if one can be formed by rearranging the letters of the other (using every
letter exactly once).

Return a list of groups. The groups may be returned in any order, and the strings
within each group may be in any order.

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters (an empty string is possible).

## Examples

### Example 1

```
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Explanation: "eat", "tea", and "ate" all use the letters {a, e, t}; "tan" and
"nat" both use {a, n, t}; "bat" is alone. Group order and within-group order may
differ.
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

Use **Hashing**: give every string a *canonical key* that is identical for
anagrams (for example, its letters sorted, or a 26-length letter-count signature).
Use a hash map from that key to the list of original strings that share it.
