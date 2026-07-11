# Minimum ASCII Delete Sum for Two Strings

**Difficulty:** Medium

**Source:** LeetCode 712 — Minimum ASCII Delete Sum for Two Strings

## Description

Given two strings `s1` and `s2`, return the **lowest ASCII sum of deleted
characters** required to make the two strings equal.

As in the delete-only edit distance, you may delete characters from either
string. But instead of minimizing the *count* of deletions, you minimize the
total **ASCII value** of the deleted characters. Deleting `'a'` (ASCII 97) costs
more than deleting a character with a smaller code point, so the optimal set of
deletions is not necessarily the smallest in count.

## Constraints

- `1 <= s1.length, s2.length <= 1000`
- `s1` and `s2` consist of lowercase English letters.

## Examples

### Example 1

```
Input:  s1 = "sea", s2 = "eat"
Output: 231
Explanation: Delete 's' from "sea" (ASCII 115) to get "ea", and delete 't' from
"eat" (ASCII 116) to get "ea". The total deleted ASCII sum is 115 + 116 = 231.
Deleting different characters would cost at least as much.
```

### Example 2

```
Input:  s1 = "delete", s2 = "leet"
Output: 403
Explanation: The best plan keeps the common subsequence "let" in both strings.
From "delete" we delete 'd'(100), 'e'(101), and 'e'(101) = 302. From "leet" we
delete the extra 'e'(101) = 101. Both strings become "let" and the total deleted
ASCII sum is 302 + 101 = 403, which is the minimum possible.
```

### Example 3

```
Input:  s1 = "abc", s2 = "abc"
Output: 0
Explanation: The strings are already equal, so nothing is deleted.
```

## Hint

This is **Edit Distance (Levenshtein)** with only deletions, but each deletion
is *weighted* by the character's ASCII value instead of costing a flat 1. Adapt
the delete-only DP so that mismatched-character transitions add the ASCII code
of the character removed rather than adding 1.
