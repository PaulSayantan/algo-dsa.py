# Sort Fixed-Length Strings

**Difficulty:** Medium

**Source:** Classic (CLRS, Section 8.3 — Radix Sort on strings / LSD string sort)

## Description

You are given a list of strings `words`, where **every string has exactly the
same length `L`** and consists only of lowercase English letters (`'a'`–`'z'`).

Return the list sorted in ascending **lexicographic** (dictionary) order.

You must not use the language's built-in sort. Because all strings share the
same length and the alphabet is small and fixed (26 symbols), each character
position is a natural "digit" and the list can be sorted in `O(L · (n + 26))`
time.

## Constraints

- `1 <= words.length <= 10^5`
- `1 <= L <= 50` and every `words[i]` has length exactly `L`
- Each character of `words[i]` is a lowercase English letter `'a'`–`'z'`
- The same string may appear more than once

## Examples

### Example 1

```
Input:  words = ["cba", "abc", "bca", "aaa"]
Output: ["aaa", "abc", "bca", "cba"]
Explanation: Compared character by character from the left, "aaa" < "abc"
because the second character 'a' < 'b'; then "bca" < "cba" because 'b' < 'c'.
```

### Example 2

```
Input:  words = ["dog", "cat", "cow", "cab"]
Output: ["cab", "cat", "cow", "dog"]
Explanation: All of "cab", "cat", "cow" share the first letter 'c', so they are
ordered by later letters: "cab" < "cat" (b < t) < "cow" (a < o). "dog" comes
last because 'd' > 'c'.
```

### Example 3

```
Input:  words = ["ba", "ab", "ba", "aa"]
Output: ["aa", "ab", "ba", "ba"]
Explanation: Duplicates ("ba" appears twice) are preserved and grouped together.
```

## Hint

Use **Radix Sort** over the character positions. Because a lexicographic
comparison weighs the leftmost character most heavily, treat the **rightmost
character as the least significant digit** and run a stable counting sort per
column from right to left.
