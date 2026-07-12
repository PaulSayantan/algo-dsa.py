# Excel Sheet Column Title

**Difficulty:** Easy

**Source:** LeetCode 168 — Excel Sheet Column Title

## Description

Given a positive integer `columnNumber`, return its corresponding column title as it
appears in an Excel sheet. Columns are numbered `1 -> "A"`, `2 -> "B"`, ...,
`26 -> "Z"`, `27 -> "AA"`, `28 -> "AB"`, and so on. This is a *bijective* base-26
system (there is no digit for zero), so subtract 1 before taking each remainder.
Use a stack of letters.

Constraints: `1 <= columnNumber <= 2^31 - 1`.

## Examples

### Example 1

```
Input:  columnNumber = 28
Output: "AB"
```

**Explanation:** 28 -> (28-1)%26 = 1 -> 'B', carry 1; 1 -> (1-1)%26 = 0 -> 'A'. Pop to read "AB".

## Hint

Repeatedly do `columnNumber -= 1`, push `'A' + columnNumber % 26`, then `columnNumber //= 26`; pop the stack to build the title.
