# Count Pattern Occurrences in a Text

**Difficulty:** Medium

Source: Classic (competitive programming; the substring-search primitive behind SPOJ "SubString Search", closely related to LeetCode 28 "Find the Index of the First Occurrence in a String")

## Description

You are given a fixed **text** `text` and a list of **query patterns**
`patterns`. For each pattern `p`, report how many times `p` occurs in `text` as
a contiguous substring. Occurrences are allowed to **overlap** — in the text
`"aaaa"` the pattern `"aa"` occurs three times (at indices 0, 1, and 2).

Return a list of counts, one per query, in the same order as `patterns`.

Because there can be many queries against the *same* text, you should do heavy
preprocessing on `text` **once** and then answer each query quickly (in time
proportional to the pattern length, not the text length).

Return `0` for any pattern that does not occur.

## Constraints

- `1 <= len(text) <= 10^5`
- `1 <= len(patterns) <= 10^5`
- `1 <= len(p) <= len(text)` for each pattern `p`
- `text` and every pattern consist of lowercase English letters.
- Overlapping occurrences are counted separately.

## Examples

### Example 1
```
Input:  text = "banana", patterns = ["ana", "na", "ban", "xyz"]
Output: [2, 2, 1, 0]
Explanation:
  "ana" occurs at indices 1 and 3 (they overlap) -> 2
  "na"  occurs at indices 2 and 4               -> 2
  "ban" occurs at index 0                       -> 1
  "xyz" never occurs                            -> 0
```

### Example 2
```
Input:  text = "aaaa", patterns = ["a", "aa", "aaa", "aaaa"]
Output: [4, 3, 2, 1]
Explanation: A pattern of length L fits in "aaaa" starting at indices
  0 .. 4 - L, giving 4 - L + 1 overlapping occurrences: 4, 3, 2, and 1.
```

### Example 3
```
Input:  text = "mississippi", patterns = ["issi", "ss", "ppi", "sip"]
Output: [2, 2, 1, 1]
Explanation:
  "issi" occurs at indices 1 and 4 (overlapping)       -> 2
  "ss"   occurs at indices 2 and 5                      -> 2
  "ppi"  occurs at index 8                              -> 1
  "sip"  occurs at index 6                              -> 1
```

## Hint

Append a unique terminal character to `text` and build a **Suffix Tree with
Ukkonen's algorithm** in linear time. Every occurrence of a pattern `p` is a
suffix of `text` that starts with `p`, i.e. a leaf in the subtree you reach by
spelling out `p` from the root. Precompute the number of leaves below every node
so each query is answered by one walk down the tree.
