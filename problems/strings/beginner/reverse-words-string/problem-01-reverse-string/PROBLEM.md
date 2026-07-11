# Reverse String

**Difficulty:** Easy

**Source:** LeetCode 344 — Reverse String

## Description

Write a function that reverses a string. The input string is given as an array
of characters `s`.

You must do this by **modifying the input array in place** with `O(1)` extra
memory. You may not allocate a second array to hold the answer (a constant
number of scalar variables is fine).

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character.

## Examples

### Example 1

```
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Explanation: The first and last characters swap, then the second and
second-to-last swap. The middle character 'l' stays put. Result reads "olleh".
```

### Example 2

```
Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
Explanation: With 6 characters (even length), all of them are swapped in
three pairs: (H,h), (a,a), (n,n). Result reads "hannaH".
```

## Hint

Use the **Reverse Words / String** technique: place one pointer at the start
and one at the end, swap the two characters, then step both pointers inward
until they meet.
