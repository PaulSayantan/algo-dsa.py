# K-th Lexicographically Smallest Distinct Substring

**Difficulty:** Hard

**Source:** Classic Suffix Automaton application (Codeforces 128B "String" is the
canonical version; also SPOJ SUBLEX "Lexicographical Substring Search").

## Description

Given a string `s` and an integer `k` (1-indexed), find the **k-th
lexicographically smallest distinct substring** of `s`.

Consider the set of all distinct non-empty substrings of `s`, sorted in
lexicographic (dictionary) order. Return the substring at position `k` in that
ordering. If `k` exceeds the number of distinct substrings, return an empty
string `""` (or report that no such substring exists).

Distinct means duplicates are removed before sorting: each distinct string
appears exactly once in the ordering.

## Constraints

- `1 <= len(s) <= 10^5`
- `1 <= k <= 10^{18}` (may exceed the number of distinct substrings)
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "aab", k = 3
Output: "aab"
Explanation: Distinct substrings sorted: ["a", "aa", "aab", "ab", "b"].
             The 3rd one is "aab".
```

### Example 2
```
Input:  s = "aba", k = 2
Output: "ab"
Explanation: Distinct substrings sorted: ["a", "ab", "aba", "b", "ba"].
             The 2nd one is "ab".
```

### Example 3
```
Input:  s = "aba", k = 6
Output: ""
Explanation: There are only 5 distinct substrings, so k = 6 is out of range and
             the answer is the empty string.
```

## Hint

Build a **Suffix Automaton** of `s` and treat it as a DAG. For each state,
precompute the number of distinct substrings reachable from it (itself plus all
paths onward). Then walk the DAG greedily: at each step try outgoing edges in
increasing character order, subtracting subtree counts until you locate the
`k`-th path.
