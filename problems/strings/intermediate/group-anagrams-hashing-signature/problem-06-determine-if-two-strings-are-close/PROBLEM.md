# Determine if Two Strings Are Close

**Difficulty:** Medium

**Source:** LeetCode 1657 — Determine if Two Strings Are Close

## Description

Two strings are considered **close** if you can attain one from the other using
the following operations any number of times:

- **Operation 1:** Swap any two *existing* characters.
  Example: `"abcde" -> "aecdb"`.
- **Operation 2:** Transform every occurrence of one existing character into
  another existing character, and do the same with the other character.
  Example: `"aacabb" -> "bbcbaa"` (all `a`'s become `b`'s and all `b`'s become
  `a`'s).

You can use each operation as many times as you want, in any order.

Given two strings `word1` and `word2`, return `true` if they are **close**, and
`false` otherwise.

This reduces to a **hashing signature** comparison. Operation 1 lets you reorder
characters freely, so only the multiset of counts matters, not positions.
Operation 2 lets you relabel characters, so the *specific* letters do not matter
— only **which letters appear** and the **multiset of their frequencies**. The
signature is therefore: (a) the set of characters present, and (b) the sorted
list of character counts.

## Constraints

- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` contain only lowercase English letters.

## Examples

### Example 1

```
Input:  word1 = "abc", word2 = "bca"
Output: true
Explanation: Same character set {a,b,c}, and each appears once, so the sorted
count signatures both equal [1,1,1]. Operation 1 (swaps) alone reorders "abc"
into "bca".
```

### Example 2

```
Input:  word1 = "a", word2 = "aa"
Output: false
Explanation: Both use only {a}, but the count multisets differ ([1] vs [2]) and
no operation changes a character's total count, so they are not close.
```

### Example 3

```
Input:  word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: Both use the set {a,b,c}. word1 counts are a:2, b:3, c:1 -> sorted
[1,2,3]; word2 counts are a:1, b:2, c:3 -> sorted [1,2,3]. Same character set
and same sorted counts, so Operation 2 (relabeling) plus swaps make them close.
```

## Hint

Compare two things as a **Group Anagrams (hashing signature)**: the *set* of
distinct characters must be identical, and the *sorted multiset of character
counts* must be identical.
