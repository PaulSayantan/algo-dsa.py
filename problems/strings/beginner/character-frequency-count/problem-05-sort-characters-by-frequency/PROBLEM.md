# Sort Characters By Frequency

**Difficulty:** Medium

**Source:** LeetCode 451 — Sort Characters By Frequency

## Description

Given a string `s`, sort it in **decreasing order based on the frequency** of the
characters. The frequency of a character is the number of times it appears in the
string.

Return the sorted string. If there are multiple answers (characters that tie on
frequency can be output in any relative order), return **any** of them.

## Constraints

- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits.

## Examples

### Example 1

```
Input:  s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' each appear once. So 'e' must come
             before both 'r' and 't'. "eetr" is also a valid answer.
```

### Example 2

```
Input:  s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "aaaccc" and "cccaaa" are
             valid answers. All the same characters must be grouped together.
```

### Example 3

```
Input:  s = "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice, 'A' once, and 'a' once. Note that 'A' and 'a' are
             treated as different characters (case-sensitive). "bbaA" is also valid.
```

## Hint

First count how often each character occurs with a **Character Frequency Count**
(the alphabet here is a fixed 62 letters+digits, or use a hash map). Then emit each
character repeated by its count, ordered from most to least frequent.
