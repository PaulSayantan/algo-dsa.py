# Count Distinct Bracelets

**Difficulty:** Hard

**Source:** Classic combinatorics-on-strings problem (bracelet / turnover-necklace
canonicalization; a standard extension of necklace counting).

## Description

A **bracelet** (also called a "free necklace" or "turnover necklace") is a string
considered up to **both rotation and reflection**. Physically, a bracelet can be rotated
*and* flipped over, so a string, all its rotations, and all rotations of its reverse
represent the **same** bracelet.

For example, `"abc"` and `"acb"` are the *same* bracelet: reversing `"abc"` gives `"cba"`,
and `"acb"` is a rotation of `"cba"` (rotations of `"cba"` are `"cba"`, `"bac"`, `"acb"`).

You are given a list of strings `words`. Count how many **distinct bracelets** it
contains — group strings so that any two that are related by a rotation, a reflection, or
a rotation-of-a-reflection fall in the same group, and return the number of groups.

Strings of different lengths are always distinct bracelets.

## Constraints

- `1 <= len(words) <= 10^5`
- `1 <= len(words[i]) <= 10^5`
- Total number of characters across all words is at most `10^6`.
- Characters come from a fixed, totally ordered alphabet (e.g. lowercase letters).

## Examples

### Example 1

```
Input:  words = ["abcd", "dcba", "xyyx"]
Output: 2
Explanation: "dcba" is the reverse of "abcd"; a bracelet may be flipped, so
             {"abcd","dcba"} is ONE bracelet. "xyyx" is a different bracelet.
             (As plain necklaces there would be 3 — the reflection is what merges
             "abcd" and "dcba".) Distinct bracelets = 2.
```

### Example 2

```
Input:  words = ["abc", "acb"]
Output: 1
Explanation: reverse("abc") = "cba"; the rotations of "cba" include "acb".
             So "acb" is a reflected rotation of "abc" -> the same bracelet.
             (As necklaces these are 2 distinct necklaces.) Distinct bracelets = 1.
```

### Example 3

```
Input:  words = ["ab", "ba", "aab"]
Output: 2
Explanation: "ab" and "ba" are rotations of each other -> one bracelet.
             "aab" (different length) -> another bracelet. Distinct bracelets = 2.
```

## Hint

Canonicalize each string under rotation **and** reflection: take the smaller of the least
rotation of `s` and the least rotation of `reverse(s)`. Compute both least rotations with
**Booth's Algorithm** in `O(len)`, then count distinct canonical strings.
