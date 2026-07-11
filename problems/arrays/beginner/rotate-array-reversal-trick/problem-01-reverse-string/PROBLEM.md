# Reverse String

**Difficulty:** Easy

**Source:** LeetCode 344 — Reverse String

## Description

Write a function that reverses a list of characters. The input list is given as
an array of characters `s`.

You must do this by modifying the input array **in place** with **O(1) extra
memory** — you may not allocate a second array or use a language built-in that
does the reversal for you.

This is the foundational subroutine behind the reversal trick: rotating an array
or reversing word order is built entirely out of in-place reversals like this
one, so it is worth mastering the two-pointer swap pattern first.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Examples

### Example 1

```
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

Explanation: The first and last characters swap, then the second and
second-to-last swap; the middle character `l` stays put.

### Example 2

```
Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

Explanation: With an even length, every character participates in exactly one
swap: `H`↔`h`, `a`↔`a`, `n`↔`n`.

## Hint

Use the **Rotate Array (reversal trick)** building block: two pointers, one at
each end, swapping inward until they meet.
