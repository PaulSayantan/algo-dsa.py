# Repeated String Match

**Difficulty:** Medium

**Source:** LeetCode 686 — "Repeated String Match"

## Description

Given two strings `a` and `b`, return the **minimum number of times** you should
repeat string `a` so that string `b` becomes a **substring** of the repeated
string. If it is impossible for `b` to be a substring of `a` repeated any number
of times, return `-1`.

For example, with `a = "abcd"` and `b = "cdabcdab"`, repeating `a` three times
gives `"abcdabcdabcd"`, and `"cdabcdab"` is a substring of it, so the answer is
`3`.

The crux is a single substring search of `b` inside a bounded repetition of `a`:
you only ever need `ceil(len(b)/len(a))` copies, or one extra to cover an offset
start — so build that string and search for `b` inside it.

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist of lowercase English letters.

## Examples

### Example 1
```
Input:  a = "abcd", b = "cdabcdab"
Output: 3
Explanation: Repeating a three times gives "abcdabcdabcd"; "cdabcdab" is a
             substring of it. Two copies ("abcdabcd") are not enough.
```

### Example 2
```
Input:  a = "a", b = "aa"
Output: 2
Explanation: "a" repeated twice is "aa", which contains "aa".
```

### Example 3
```
Input:  a = "abc", b = "wxyz"
Output: -1
Explanation: No number of repetitions of "abc" ever contains "wxyz".
```

## Hint

Repeat `a` about `ceil(len(b)/len(a))` times (try one extra to cover an offset),
then check whether `b` is a substring. Perform that substring check with
**Boyer–Moore (string search)**.
