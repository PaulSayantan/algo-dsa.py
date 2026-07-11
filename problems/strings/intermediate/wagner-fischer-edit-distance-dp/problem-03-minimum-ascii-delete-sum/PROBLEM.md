# Minimum ASCII Delete Sum for Two Strings

**Difficulty:** Medium

**Source:** LeetCode 712 — Minimum ASCII Delete Sum for Two Strings

## Description

Given two strings `s1` and `s2`, return the **lowest ASCII sum of deleted characters** to
make the two strings equal.

As in the plain delete-only variant you may only delete characters, but now each deletion
does **not** cost `1` — it costs the **ASCII value** of the character you delete. Your goal
is to make `s1` and `s2` identical while minimizing the total ASCII value of everything you
removed from both strings.

## Constraints

- `1 <= s1.length, s2.length <= 1000`
- `s1` and `s2` consist of lowercase English letters.
  (Recall `ord('a') = 97`, …, `ord('z') = 122`.)

## Examples

**Example 1**

```
Input:  s1 = "sea", s2 = "eat"
Output: 231
Explanation: Delete 's' from "sea" (cost ord('s') = 115) leaving "ea", and delete 't' from
             "eat" (cost ord('t') = 116) leaving "ea". Total deleted ASCII = 115 + 116 = 231.
             Deleting 'e' and 't' instead would cost 101 + 116 = 217 but leaves "sa" vs "ea",
             which are not equal, so it is not a valid plan.
```

**Example 2**

```
Input:  s1 = "delete", s2 = "leet"
Output: 403
Explanation: The best shared leftover is "let". From "delete" (d-e-l-e-t-e) delete 'd' (100)
             and the two extra 'e's (101 + 101) to reach "let"; from "leet" (l-e-e-t) delete
             one 'e' (101) to reach "let". 100 + 101 + 101 + 101 = 403. No cheaper set of
             deletions makes the strings equal.
```

## Hint

Same table shape as delete-only edit distance, but the cell values are **weighted by ASCII
cost** instead of counting operations. Drive it with the **Wagner–Fischer (Edit Distance
DP)** recurrence, replacing the `+1` deletion penalty with `+ord(deleted_char)`.
