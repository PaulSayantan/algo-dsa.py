# Base Conversion via Stack

Converting a number to another base produces its digits **least-significant first** (via repeated division + remainder), but we print most-significant first. A stack neatly reverses this: push each remainder, then pop to read the converted representation.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Decimal to Binary](problem-01-decimal-to-binary/PROBLEM.md) | Remainder stack | Easy |
| 2 | [Convert to Base K](problem-02-convert-to-base-k/PROBLEM.md) | General base stack | Easy |
| 3 | [Excel Sheet Column Title](problem-03-excel-sheet-column-title/PROBLEM.md) | Bijective base-26 stack | Easy |
| 4 | [Convert a Number to Hexadecimal](problem-04-decimal-to-hexadecimal/PROBLEM.md) | Base-16 with two's complement | Easy |
| 5 | [Base 7](problem-05-base-seven/PROBLEM.md) | Signed base-7 stack | Easy |
