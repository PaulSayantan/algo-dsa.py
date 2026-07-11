# Excel Sheet Column Title

**Difficulty:** Medium

**Source:** LeetCode 168 (Excel Sheet Column Title)

## Description

Given a positive integer `columnNumber`, return its corresponding column title as
it appears in a spreadsheet.

The mapping is: `1 -> "A"`, `2 -> "B"`, ..., `26 -> "Z"`, `27 -> "AA"`,
`28 -> "AB"`, ..., `52 -> "AZ"`, `53 -> "BA"`, and so on.

This is the inverse of reading an Excel column title as a base-26 number. The twist
is that the system is **bijective base-26**: there is no digit `0` — the digits run
from 1 (`A`) to 26 (`Z`). To peel off one letter at a time you subtract 1 before
each `% 26` / `// 26` step, then turn the remainder into a letter with
`chr(ord('A') + remainder)`.

## Constraints

- `1 <= columnNumber <= 2^31 - 1`

## Examples

### Example 1

```
Input:  columnNumber = 1
Output: "A"
Explanation: (1 - 1) % 26 = 0, and chr(ord('A') + 0) = 'A'.
```

### Example 2

```
Input:  columnNumber = 28
Output: "AB"
Explanation: 28 -> (28-1)%26 = 1 -> 'B'; then 28 becomes 27//26 = 1 -> (1-1)%26 = 0
-> 'A'. Reading the letters in reverse order of extraction gives "AB".
```

### Example 3

```
Input:  columnNumber = 701
Output: "ZY"
Explanation: (701-1)%26 = 700%26 = 24 -> 'Y'; then (701-1)//26 = 26; (26-1)%26 = 25
-> 'Z'. Reversed, the title is "ZY".
```

## Hint

Use **Case Conversion & ASCII Arithmetic**: repeatedly subtract 1, take the value
mod 26 as a 0..25 offset, map it to a letter with `chr(ord('A') + offset)`, and
divide by 26 to move to the next place.
