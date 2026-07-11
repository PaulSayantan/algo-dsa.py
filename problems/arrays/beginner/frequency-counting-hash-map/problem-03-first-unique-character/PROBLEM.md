# First Unique Character in a String

**Difficulty:** Easy

**Source:** LeetCode 387 (https://leetcode.com/problems/first-unique-character-in-a-string/)

## Description

Given a string `s`, find the **first non-repeating character** in it and return
its index. If it does not exist, return `-1`.

A non-repeating (unique) character is one that appears exactly once in the
entire string. Among all such characters, we want the one that appears earliest
(leftmost) in `s`.

The natural strategy is two passes over the string: one to learn how many times
each character occurs, and one to find the first position whose character has a
count of exactly one.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples

### Example 1

```
Input:  s = "leetcode"
Output: 0
Explanation: 'l' occurs once and is the first character, so its index 0 is
returned.
```

### Example 2

```
Input:  s = "loveleetcode"
Output: 2
Explanation: 'l' and 'o' both repeat; 'v' at index 2 is the first character
that occurs exactly once.
```

### Example 3

```
Input:  s = "aabb"
Output: -1
Explanation: Every character repeats, so there is no unique character and we
return -1.
```

## Hint

Use **Frequency Counting with a Hash Map**: count every character first, then
scan left to right for the first character whose count equals one.
