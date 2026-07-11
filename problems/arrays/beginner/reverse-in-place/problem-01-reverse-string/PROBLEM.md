# Reverse String

**Difficulty:** Easy

**Source:** LeetCode 344 — Reverse String

## Description

Write a function that reverses a string. The input string is given as an array of
characters `s`.

You must do this by **modifying the input array in-place** with `O(1)` extra memory.
You may not allocate a second array to hold the result.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Examples

### Example 1

```
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

Explanation: The first and last characters swap (`h` <-> `o`), then the second and
second-to-last swap (`e` <-> `l`). The middle `l` stays put. The array now reads
backward compared to the input.

### Example 2

```
Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

Explanation: With even length 6 there is no fixed middle element. `H` <-> `h`,
`a` <-> `a`, and `n` <-> `n` are all swapped, producing the reversed array.

## Hint

Use **Reverse In-Place**: keep a pointer at each end of the array, swap the two
characters, and step both pointers inward until they meet.
