# Count Keyword Occurrences

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (cf. HDU 2222 "Keywords
Search"; SPOJ / CSES multi-pattern counting)

## Description

You are given a list of **keywords** (patterns) and a single **text** string.
Count the **total number of keyword occurrences inside the text**, where every
occurrence at every position is counted, and occurrences may **overlap**.

More precisely, return the number of pairs `(k, i)` such that keyword `k`
appears in `text` starting at index `i`. If the same keyword appears twice in
the list it is treated as one keyword (deduplicate first): each *distinct*
keyword contributes once per starting position at which it occurs. Overlapping
occurrences of the same keyword (e.g. `"aa"` in `"aaa"`) all count.

This is the canonical setting for the Aho–Corasick automaton: many patterns, one
text, count all hits in a single linear pass.

## Constraints

- `1 <= keywords.length <= 10^4`
- `1 <= keywords[i].length <= 50`
- `1 <= text.length <= 10^6`
- All strings consist of lowercase English letters.
- Keywords may repeat; count each **distinct** keyword's occurrences.

## Examples

### Example 1

```
Input:  keywords = ["she","he","say","shr","her"], text = "yasherhs"
Output: 3
Explanation: Inside "yasherhs" we find "she" (at index 2), "he" (at index 3),
and "her" (at index 3). "say" and "shr" do not occur. Total = 3.
```

### Example 2

```
Input:  keywords = ["aa","aaa"], text = "aaaa"
Output: 5
Explanation: "aa" occurs at indices 0, 1, 2 (three overlapping times) and "aaa"
occurs at indices 0, 1 (two times). Total = 3 + 2 = 5.
```

### Example 3

```
Input:  keywords = ["abc","xyz"], text = "aaaaaa"
Output: 0
Explanation: Neither keyword appears in the text.
```

## Hint

Insert all distinct keywords into an **Aho–Corasick Automaton**, then scan the
text once; at each character follow the dictionary-suffix-link chain and add the
number of keywords ending at each visited node. Precomputing a per-node
"suffix count" lets each position be handled in amortized `O(1)`.
