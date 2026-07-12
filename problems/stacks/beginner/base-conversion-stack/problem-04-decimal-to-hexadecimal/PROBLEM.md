# Convert a Number to Hexadecimal

**Difficulty:** Easy

**Source:** LeetCode 405 — Convert a Number to Hexadecimal

## Description

Given a 32-bit integer `num`, return its hexadecimal representation as a lowercase
string using digits `0-9` and `a-f`. For negative numbers, use the *two's complement*
32-bit encoding. The result must not contain leading zeros, except that `0` maps to
`"0"`. Do not use any built-in library conversion (e.g. `hex`). Use a stack of
remainders from repeated division by 16.

Constraints: `-2^31 <= num <= 2^31 - 1`.

## Examples

### Example 1

```
Input:  num = 26
Output: "1a"
```

**Explanation:** 26 % 16 = 10 -> 'a', 26 // 16 = 1; 1 % 16 = 1 -> '1'. Pop to read "1a".

## Hint

Mask `num` to 32 bits (`num & 0xffffffff`), then push `num % 16` mapped to a hex digit and `num //= 16`; pop the remainder stack.
