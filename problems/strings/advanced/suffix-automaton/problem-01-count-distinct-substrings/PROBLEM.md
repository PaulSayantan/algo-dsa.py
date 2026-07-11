# Count Distinct Substrings

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (equivalent to SPOJ SUBST1 /
CSES "Distinct Substrings"; also LeetCode 1698 "Number of Distinct Substrings in
a String").

## Description

Given a string `s`, count the number of **distinct non-empty substrings** of `s`.

A substring is any contiguous block of characters. Two substrings are the "same"
if they consist of the same sequence of characters, regardless of where they
appear. For example, in `"aa"` the substring `"a"` appears at index 0 and index
1 but should be counted only once.

Your goal is to return the size of the set of all distinct substrings without
ever materializing that (potentially quadratic) set.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- The answer can be large; it fits in a 64-bit integer (Python ints are
  unbounded, so no overflow concerns).

## Examples

### Example 1
```
Input:  s = "abc"
Output: 6
Explanation: The distinct substrings are "a", "b", "c", "ab", "bc", "abc".
             All 6 substrings of "abc" are already distinct, so the count is 6.
```

### Example 2
```
Input:  s = "aaa"
Output: 3
Explanation: The substrings are "a", "aa", "aaa". Although "a" occurs three
             times and "aa" occurs twice, each distinct string is counted once,
             giving 3.
```

### Example 3
```
Input:  s = "abab"
Output: 7
Explanation: Distinct substrings are "a", "b", "ab", "ba", "aba", "bab", "abab".
             (Note "ab" and "aba" repeat but are counted once each.)
```

## Hint

Build a **Suffix Automaton** of `s`. Each state (other than the initial state)
represents a contiguous range of substring lengths; summing those ranges gives
the number of distinct substrings in linear time.
