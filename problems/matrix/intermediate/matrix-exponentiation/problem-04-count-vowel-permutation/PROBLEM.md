# Count Vowel Permutation

**Difficulty:** Medium

LeetCode 1220 "Count Vowel Permutation" (presented here with a large-`n` follow-up that
demands Matrix Exponentiation).

## Description

Given an integer `n`, count how many strings of length `n` can be formed using only the
lowercase vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) subject to these rules:

- Each `'a'` may only be followed by an `'e'`.
- Each `'e'` may only be followed by an `'a'` or an `'i'`.
- Each `'i'` may **not** be followed by another `'i'`.
- Each `'o'` may only be followed by an `'i'` or a `'u'`.
- Each `'u'` may only be followed by an `'a'`.

Return the number of valid strings of length `n`, **modulo `10^9 + 7`**.

Because `n` can be very large (up to `10^18` in this variant), an `O(n)` dynamic program is
too slow; you must advance the per-vowel counts in `O(log n)` steps.

## Constraints

- `1 <= n <= 10^18`
- Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  n = 1
Output: 5
Explanation: All strings of length 1 are valid: "a", "e", "i", "o", "u".
```

### Example 2

```
Input:  n = 2
Output: 10
Explanation: The valid length-2 strings are "ae", "ea", "ei", "ia", "ie",
"io", "iu", "oi", "ou", "ua" — 10 in total.
```

### Example 3

```
Input:  n = 5
Output: 68
Explanation: There are 68 valid length-5 strings under the adjacency rules.
```

## Hint

The vector of counts "number of valid strings of each ending vowel" transforms by a fixed
5×5 rule at every extra character. Apply that rule `n-1` times with **Matrix Exponentiation**.
