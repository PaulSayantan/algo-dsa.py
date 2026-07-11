# Longest Valid Substring

**Difficulty:** Hard

**Source:** LeetCode 2781 — Length of the Longest Valid Substring

## Description

You are given a string `word` and an array of strings `forbidden`.

A string is called **valid** if none of its substrings are present in
`forbidden`. Return the length of the **longest valid substring** of `word`.

A substring is a contiguous sequence of characters in a string, possibly empty.
The empty substring is trivially valid (length `0`), so the answer is always at
least `0`.

## Constraints

- `1 <= word.length <= 10^5`
- `1 <= forbidden.length <= 10^5`
- `1 <= forbidden[i].length <= 10`
- `word` and `forbidden[i]` consist of only lowercase English letters.

## Examples

### Example 1

```
Input:  word = "cbaaaabc", forbidden = ["aaa","cb"]
Output: 4
Explanation: The forbidden occurrences are "cb" at [0,1] and "aaa" at [2,4] and
[3,5]. The substring "aabc" (indices [4,7]) contains no forbidden string and has
length 4. No valid window of length 5 exists (any length-5 window either spans
"cb" or contains three consecutive 'a's), so the answer is 4.
```

### Example 2

```
Input:  word = "leetcode", forbidden = ["de","le","e"]
Output: 4
Explanation: "e" appears at several positions, "le" at [0,1], "de" at [5,6]. The
longest valid substring is "tcod" (indices [3,6]), which contains none of the
forbidden strings, so the answer is 4.
```

### Example 3

```
Input:  word = "aaa", forbidden = ["aaa"]
Output: 2
Explanation: The whole string "aaa" is forbidden, but "aa" (length 2) contains
no forbidden substring, so the answer is 2.
```

## Hint

Build an **Aho–Corasick Automaton** over `forbidden`. Scan `word` left to right;
at each right endpoint the automaton tells you the **shortest forbidden string
ending here** (track the minimum forbidden length reachable via dictionary-suffix
links). Use it to advance a sliding-window `left` boundary just past the start of
that shortest forbidden occurrence, and take the max window length.
