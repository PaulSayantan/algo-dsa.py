# Count Substring Occurrences

**Difficulty:** Medium

**Source:** Classic Suffix Automaton application (equivalent to SPOJ NSUBSTR
"Long Substrings" family and standard `endpos`-size queries; also the core of
many "how many times does pattern p occur in text s" problems).

## Description

You are given a text string `s` and a list of query patterns `queries`. For each
query pattern `p`, report the number of times `p` occurs as a (possibly
overlapping) substring of `s`.

Occurrences may overlap. For example, `"aa"` occurs **twice** in `"aaa"` (at
index 0 and index 1). If a pattern does not appear in `s` at all, its answer is
`0`.

You should preprocess `s` once so that each query is answered in time
proportional to the length of the pattern, not the length of `s`.

## Constraints

- `1 <= len(s) <= 10^5`
- `1 <= len(queries) <= 10^5`
- `1 <= len(p) <= len(s)` for each query `p`.
- All strings consist of lowercase English letters.
- Overlapping occurrences are counted separately.

## Examples

### Example 1
```
Input:  s = "abcbc", queries = ["bc", "b", "abc", "xyz"]
Output: [2, 2, 1, 0]
Explanation:
  "bc"  occurs at indices 1 and 3  -> 2
  "b"   occurs at indices 1 and 3  -> 2
  "abc" occurs at index 0          -> 1
  "xyz" does not occur             -> 0
```

### Example 2
```
Input:  s = "aaaa", queries = ["a", "aa", "aaa", "aaaa"]
Output: [4, 3, 2, 1]
Explanation:
  "a"    starts at indices 0,1,2,3 -> 4
  "aa"   starts at indices 0,1,2   -> 3
  "aaa"  starts at indices 0,1     -> 2
  "aaaa" starts at index 0         -> 1
```

## Hint

Build a **Suffix Automaton** of `s`. The number of occurrences of a substring
equals the size of its `endpos` set. Seed each non-clone state with count 1, then
propagate counts up the **suffix-link tree** (children to parents). Walk a query
along the automaton's transitions to find its state, then read that state's
count.
