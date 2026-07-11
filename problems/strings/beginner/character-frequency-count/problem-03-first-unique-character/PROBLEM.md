# First Unique Character in a String

**Difficulty:** Easy

**Source:** LeetCode 387 — First Unique Character in a String

## Description

Given a string `s`, find the **first non-repeating character** in it and return
its index. If it does not exist, return `-1`.

A non-repeating (unique) character is one that appears exactly once in the whole
string. "First" means the smallest index among all such characters.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples

### Example 1

```
Input:  s = "leetcode"
Output: 0
Explanation: Counts -> l:1, e:3, t:1, c:1, o:1, d:1. Scanning left to right, the
             first character with count 1 is 'l' at index 0.
```

### Example 2

```
Input:  s = "loveleetcode"
Output: 2
Explanation: 'l' appears twice and 'o' appears twice, but 'v' at index 2 appears
             only once, so index 2 is the first unique character.
```

### Example 3

```
Input:  s = "aabb"
Output: -1
Explanation: 'a' appears twice and 'b' appears twice. No character is unique, so
             the answer is -1.
```

## Hint

You need to know each character's total count before you can decide which is
unique. Precompute a **Character Frequency Count**, then scan the string once more
and return the index of the first character whose count is 1.
