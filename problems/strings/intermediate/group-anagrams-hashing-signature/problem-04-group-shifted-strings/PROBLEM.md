# Group Shifted Strings

**Difficulty:** Medium

**Source:** LeetCode 249 — Group Shifted Strings

## Description

We can **shift** a string by shifting each of its letters to its successor in the
alphabet. For example, `"abc"` can be shifted to `"bcd"`, then `"cde"`, and so
on. The shift wraps around: `"z"` shifts to `"a"`. A full sequence of shifts of
`"abc"` is:

```
"abc" -> "bcd" -> "cde" -> ... -> "xyz" -> "yza" -> "zab" -> "abc" -> ...
```

Given an array of strings `strings`, group all strings that belong to the same
shifting sequence. You may return the groups in any order.

This is a **hashing signature** problem where the signature is *not* the sorted
string but the tuple of **differences between consecutive characters** (mod 26).
Two strings are shifts of one another exactly when those difference tuples are
equal, so bucketing by that signature groups the shift-equivalent strings.

## Constraints

- `1 <= strings.length <= 200`
- `1 <= strings[i].length <= 50`
- `strings[i]` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["abc","bcd","xyz"],["acef"],["az","ba"],["a","z"]]
Explanation: "abc","bcd","xyz" share the diff signature (1,1). "az" has
(z-a) = (25) and "ba" has (a-b) = (-1 mod 26) = (25), so they share (25,).
Single characters "a" and "z" both have the empty diff signature (). "acef"
has diff signature (2,2,1) and stands alone.
```

### Example 2

```
Input:  strings = ["a","b","c"]
Output: [["a","b","c"]]
Explanation: Every single-character string has the empty difference signature,
so they all belong to the same shifting sequence.
```

### Example 3

```
Input:  strings = ["abc","cde","fgh"]
Output: [["abc","cde","fgh"]]
Explanation: All three have consecutive differences (1,1) — each is a shift of
the others — so they form one group.
```

## Hint

Build a **Group Anagrams (hashing signature)** from the gaps between adjacent
characters taken modulo 26; strings sharing that difference tuple are shifts of
each other and belong in the same bucket.
