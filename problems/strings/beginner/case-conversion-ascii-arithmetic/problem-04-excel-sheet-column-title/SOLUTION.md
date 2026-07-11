# Solution — Excel Sheet Column Title

## Brute Force

There is no meaningful "search" brute force here — the answer is a direct base
conversion. A naive but valid attempt is to treat it like ordinary base-26
(digits 0..25) and try to patch up the off-by-one afterward, but that leads to
subtle bugs precisely at multiples of 26 (`26 -> "Z"`, `52 -> "AZ"`, `702 -> "ZZ"`).
The clean way is to handle the bijective offset directly, described below. For
completeness, one could also precompute titles iteratively from 1 upward until
reaching `columnNumber`, but that is O(columnNumber) time and pointless when a
digit-extraction runs in O(log n).

- **Naive incremental generation time:** O(columnNumber) — far too slow near 2^31.
- **Space:** O(1) besides the output.

## Optimal Approach (Case Conversion & ASCII Arithmetic)

This is **bijective base-26**: valid digits are 1..26 (`A..Z`) with no zero digit.
When peeling off the least-significant "digit" we must first subtract 1 so the
range becomes 0..25, which `chr(ord('A') + offset)` can map to a letter, and so the
integer division carries correctly.

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        while columnNumber > 0:
            columnNumber -= 1                     # shift to 0-based
            offset = columnNumber % 26            # 0..25
            chars.append(chr(ord('A') + offset))  # 'A'..'Z'
            columnNumber //= 26
        return "".join(reversed(chars))
```

### Step-by-step for `columnNumber = 28`

1. `28 > 0`: `28 - 1 = 27`; `27 % 26 = 1` -> `chr(65 + 1) = 'B'`; `27 // 26 = 1`.
   Now `columnNumber = 1`, collected `['B']`.
2. `1 > 0`: `1 - 1 = 0`; `0 % 26 = 0` -> `chr(65 + 0) = 'A'`; `0 // 26 = 0`.
   Now `columnNumber = 0`, collected `['B', 'A']`.
3. Loop ends. Reverse `['B', 'A']` -> `"AB"`.

### Step-by-step for `columnNumber = 701`

1. `701 - 1 = 700`; `700 % 26 = 24` -> `chr(65 + 24) = 'Y'`; `700 // 26 = 26`.
   `columnNumber = 26`, collected `['Y']`.
2. `26 - 1 = 25`; `25 % 26 = 25` -> `chr(65 + 25) = 'Z'`; `25 // 26 = 0`.
   `columnNumber = 0`, collected `['Y', 'Z']`.
3. Reverse -> `"ZY"`.

**Why it is correct:** ordinary positional numbering with digits 0..25 would have
a representation for 0, but spreadsheet columns start at 1 and skip a zero digit.
Subtracting 1 at the top of each iteration converts the current 1-based value into
a 0-based value whose remainder mod 26 is exactly the current letter's 0..25
offset, and whose quotient is the correctly carried remaining value. Because we
extract the least-significant letter first, we reverse the collected characters at
the end. The `chr(ord('A') + offset)` step is the ASCII-arithmetic inverse of the
`ord(c) - ord('A')` used to *read* a title, so this function and
`titleToNumber` are exact inverses.

- **Time:** O(log_26 n) — the number of letters produced.
- **Space:** O(log_26 n) for the output characters.

## Key Insights & Edge Cases

- The single most important line is `columnNumber -= 1` **before** the modulo. Skip
  it and you get wrong answers exactly at multiples of 26 (`26` would wrongly try
  to emit an offset of 0 and carry incorrectly).
- Multiples of 26 are the classic trap: `26 -> "Z"`, `52 -> "AZ"`, `702 -> "ZZ"`.
  Trace `702`: `701 % 26 = 25 ->'Z'`, `701 // 26 = 26`; then `25 % 26 = 25 ->'Z'`
  -> `"ZZ"`.
- Smallest input `1` yields a single `"A"` (offset 0).
- Largest input `2^31 - 1 = 2147483647` yields `"FXSHRXW"`; Python integers never
  overflow, so no special handling is needed.
- Remember to reverse at the end, since letters are generated least-significant
  first.
