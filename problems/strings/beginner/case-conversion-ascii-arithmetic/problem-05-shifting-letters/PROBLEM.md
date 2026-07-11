# Shifting Letters

**Difficulty:** Medium

**Source:** LeetCode 848 (Shifting Letters)

## Description

You are given a string `s` of lowercase English letters and an integer array
`shifts` of the same length.

Shifting a letter means advancing it forward through the alphabet, wrapping around
so that `'z'` becomes `'a'`. For example, shifting `'a'` by 3 gives `'d'`, and
shifting `'y'` by 3 gives `'b'`.

For each index `i`, you must shift the first `i + 1` letters of `s` (that is,
`s[0]`, `s[1]`, ..., `s[i]`) forward by `shifts[i]`. Because the shift at index `i`
affects every position at or before `i`, the total amount applied to position `j`
is the sum `shifts[j] + shifts[j+1] + ... + shifts[n-1]` (a suffix sum).

Return the final string after all shifts are applied.

Use ASCII arithmetic to shift a single letter: convert to a 0..25 index with
`ord(c) - ord('a')`, add the total shift, take it modulo 26, and convert back with
`chr(index + ord('a'))`.

## Constraints

- `1 <= s.length == shifts.length <= 10^5`
- `0 <= shifts[i] <= 10^9`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "abc", shifts = [3, 5, 9]
Output: "rpl"
Explanation:
Suffix totals: position 0 gets 3+5+9 = 17, position 1 gets 5+9 = 14, position 2
gets 9.
'a' shifted by 17 -> (0 + 17) % 26 = 17 -> 'r'.
'b' shifted by 14 -> (1 + 14) % 26 = 15 -> 'p'.
'c' shifted by  9 -> (2 +  9) % 26 = 11 -> 'l'.
Result: "rpl".
```

### Example 2

```
Input:  s = "aaa", shifts = [1, 2, 3]
Output: "gfd"
Explanation:
Suffix totals: 1+2+3 = 6, 2+3 = 5, 3.
'a' + 6 -> 'g'; 'a' + 5 -> 'f'; 'a' + 3 -> 'd'. Result: "gfd".
```

### Example 3

```
Input:  s = " z", shifts = [52]   (read as s = "z", shifts = [52])
Output: "z"
Explanation:
'z' is index 25; (25 + 52) % 26 = 77 % 26 = 25 -> 'z'. A shift of a multiple of 26
leaves a letter unchanged.
```

## Hint

Use **Case Conversion & ASCII Arithmetic** together with a running suffix sum: fold
the shifts from right to left so each position knows its total shift in O(1), then
rotate each letter with `(ord(c) - ord('a') + total) % 26`.
