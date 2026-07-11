# Add Bold Tag in a String

**Difficulty:** Medium

**Source:** LeetCode 616 / 758 — Add Bold Tag in a String (a.k.a. Bold Words in
String)

## Description

You are given a string `s` and a list of strings `words`. You want to add closed
pairs of bold tags `<b>` and `</b>` to wrap the substrings of `s` that exist in
`words`.

- If two such substrings overlap, wrap them together with only one pair of bold
  tags.
- If two wrapped substrings are consecutive (touching with no gap between them),
  combine them into one pair of bold tags.

Return `s` after adding the bold tags.

## Constraints

- `1 <= s.length <= 1000`
- `0 <= words.length <= 100`
- `1 <= words[i].length <= 1000`
- `s` and `words[i]` consist of lowercase and uppercase English letters and
  digits.
- (Classic variant allows `words.length` up to `10^4` and larger `s`, which is
  exactly where Aho–Corasick becomes necessary.)

## Examples

### Example 1

```
Input:  s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"
Explanation: "abc" occupies indices [0,2] and "123" occupies [6,8]. They do not
overlap, so each gets its own pair of tags.
```

### Example 2

```
Input:  s = "aaabbee", words = ["aaa","aab","bc","aaabbee"]
Output: "<b>aaabbee</b>"
Explanation: "aaa" covers [0,2], "aab" covers [1,3], and "aaabbee" covers [0,6].
The union of all covered positions is the whole string [0,6], so a single pair
of tags wraps everything.
```

### Example 3

```
Input:  s = "leetcode", words = []
Output: "leetcode"
Explanation: There are no words, so nothing is bolded and s is returned as is.
```

## Hint

Build an **Aho–Corasick Automaton** over `words` and scan `s` once to find the
`[start, end]` interval of **every** occurrence of **every** word (use the
dictionary-suffix links so nested/overlapping words are all reported). Mark
covered positions, then merge contiguous covered runs into single `<b>…</b>`
segments.
