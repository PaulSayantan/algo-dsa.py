# Distinct Substrings in a Collection

**Difficulty:** Medium

**Source:** Classic generalized suffix automaton exercise (union-of-substrings
counting; cf. CSES "Distinct Substrings" generalized to many strings).

## Description

You are given a list of `n` strings `words = [w_1, w_2, ..., w_n]`. Consider the
set that contains **every** contiguous substring of **every** string in the list.
Substrings are compared by their *content*, so a substring that appears in more
than one string (or several times within one string) is counted **only once**.

Return the number of **distinct** substrings in this union.

Formally, return `|{ t : t is a non-empty substring of some w_i }|`.

## Constraints

- `1 <= n <= 10^4`
- `1 <= len(w_i)` and `sum(len(w_i)) <= 2 * 10^5`
- All strings consist of lowercase English letters.
- The empty string is **not** counted.

## Examples

### Example 1
```
Input:  words = ["ab", "ba"]
Output: 4
Explanation: Substrings of "ab": {"a", "b", "ab"}.
             Substrings of "ba": {"b", "a", "ba"}.
             Union = {"a", "b", "ab", "ba"} -> 4 distinct.
             ("a" and "b" are shared, so counted once.)
```

### Example 2
```
Input:  words = ["aa", "aaa"]
Output: 3
Explanation: Substrings of "aaa" are {"a", "aa", "aaa"}, which already contain
             every substring of "aa". Union = {"a", "aa", "aaa"} -> 3 distinct.
```

### Example 3
```
Input:  words = ["abc", "bcd"]
Output: 9
Explanation: "abc" -> {"a","b","c","ab","bc","abc"} (6).
             "bcd" -> {"b","c","d","bc","cd","bcd"}; new ones are
             {"d","cd","bcd"} (3). Total 6 + 3 = 9 distinct.
```

## Hint

Build one **Generalized Suffix Structure** (a suffix automaton fed all the
strings, resetting to the root before each string). Every distinct substring of
the whole collection corresponds to exactly one path in the automaton, and each
state `v` accounts for `len[v] - len[link[v]]` distinct substrings — sum that
over all states.
