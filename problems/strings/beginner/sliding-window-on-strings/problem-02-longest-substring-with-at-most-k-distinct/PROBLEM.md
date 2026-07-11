# Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium

**Source:** LeetCode 340 — Longest Substring with At Most K Distinct Characters

## Description

Given a string `s` and an integer `k`, return the length of the **longest
substring** of `s` that contains **at most `k` distinct characters**.

A substring is a contiguous run of characters. "At most `k` distinct" means the
number of *unique* character values appearing in the substring is `<= k`
(a character may repeat any number of times). If `k` is `0`, no non-empty
substring qualifies, so the answer is `0`.

## Constraints

- `1 <= len(s) <= 5 * 10^4`
- `0 <= k <= 50`
- `s` consists of English letters.

## Examples

### Example 1
```
Input:  s = "eceba", k = 2
Output: 3
Explanation: The substring "ece" has exactly 2 distinct characters
             ('e' and 'c') and length 3. No length-4 substring stays within
             2 distinct characters.
```

### Example 2
```
Input:  s = "aa", k = 1
Output: 2
Explanation: "aa" has only 1 distinct character, which is within the limit,
             so the whole string of length 2 qualifies.
```

### Example 3
```
Input:  s = "abaccc", k = 2
Output: 4
Explanation: The substring "accc" (indices 2..5) has 2 distinct characters
             ('a' and 'c') and length 4. The prefix "aba" has 2 distinct
             but only length 3; nothing reaches length 5 with 2 distinct.
```

## Hint

Use the **Sliding Window on Strings** technique with a character-count map:
grow the window on the right, and while the map holds more than `k` distinct
keys, shrink from the left (removing keys whose count hits zero). Track the
largest valid window.
