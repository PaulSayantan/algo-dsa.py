# Longest Substring with At Most K Distinct Characters

**Difficulty:** Medium

**Source:** LeetCode 340 — Longest Substring with At Most K Distinct Characters

## Description

Given a string `s` and an integer `k`, return the length of the **longest
substring** of `s` that contains **at most `k` distinct characters**.

This is the general form of "Fruit Into Baskets" (which fixes `k = 2`): now `k`
can be any non-negative integer, and the alphabet is arbitrary characters.

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `0 <= k <= 50`
- `s` consists of lowercase (and possibly other) characters.

## Examples

### Example 1

```
Input:  s = "eceba", k = 2
Output: 3
Explanation: The substring "ece" has 2 distinct characters {e, c} and length 3.
             Any window of length 4 here would need 3+ distinct characters.
```

### Example 2

```
Input:  s = "aa", k = 1
Output: 2
Explanation: The substring "aa" has 1 distinct character and length 2.
```

### Example 3

```
Input:  s = "abcadcacacaca", k = 3
Output: 11
Explanation: The substring "cadcacacaca" (from index 2 to 12) uses only the 3
             distinct characters {a, c, d} and has length 11.
```

## Hint

Use a **Sliding Window (variable size)** with a character-count map. Grow the
window while it holds at most `k` distinct characters; when the `(k+1)`-th distinct
character enters, shrink from the left until a character is fully removed.
