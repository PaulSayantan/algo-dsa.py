# First Unique Character in a String

**Difficulty:** Medium

**Source:** LeetCode 387 — First Unique Character in a String

## Description

Given a string `s`, return the index of the first character that appears exactly once when scanning left to right. If no such character exists, return `-1`. Feed the characters through as a stream, tracking counts and a queue of candidate indices so the answer is the front candidate that is still unique.

## Examples

### Example 1

```
Input:  s = "leetcode"
Output: 0
```

**Explanation:** `'l'` is the first character that never repeats, at index 0.

### Example 2

```
Input:  s = "loveleetcode"
Output: 2
```

**Explanation:** `'l'`, `'o'`, `'e'` all repeat; `'v'` at index 2 is the first unique one.

## Hint

Count map + a deque of candidate indices; drop fronts whose character count has grown past one, then read the front.
