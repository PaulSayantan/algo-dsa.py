# Distinct Echo Substrings

**Difficulty:** Hard

**Source:** LeetCode 1316 — Distinct Echo Substrings

## Description

Return the number of **distinct** non-empty substrings of `text` that can be
written as the concatenation of some string with **itself** (i.e. of the form
`a + a`, an "echo" / square string).

Two substrings are considered the same if they are equal *as strings*, even if
they occur at different positions — count each distinct value only once.

A substring `text[i..i+2L-1]` of even length `2L` is an echo exactly when its
first half equals its second half: `text[i..i+L-1] == text[i+L..i+2L-1]`.
Comparing halves by **substring hash** turns each check into `O(1)`, and storing
the hash of each discovered echo in a set handles the "distinct" requirement.
Use two moduli so distinct substrings are not accidentally merged and equal
halves are not accidentally rejected.

## Constraints

- `1 <= text.length <= 2000`
- `text` has only lowercase English letters.

## Examples

**Example 1**

```
Input:  text = "abcabcabc"
Output: 3
Explanation: The distinct echo substrings are "abcabc", "bcabca", and "cabcab".
```

**Example 2**

```
Input:  text = "leetcodeleetcode"
Output: 2
Explanation: The distinct echo substrings are "ee" and "leetcodeleetcode".
```

**Example 3**

```
Input:  text = "aaa"
Output: 1
Explanation: The only echo substring is "aa"; although it occurs twice
(positions 0 and 1) it is counted once because we count distinct values.
```

## Hint

Use **Double Hashing / Anti-Hash**: precompute prefix hashes, test whether the
two halves of each even-length window are equal in `O(1)`, and add the echo's
hash pair to a set to count distinct ones.
