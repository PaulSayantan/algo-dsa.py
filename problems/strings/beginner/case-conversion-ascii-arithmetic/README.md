# Case Conversion & ASCII Arithmetic

## What it is

Every character in a string is stored as an integer code (its ASCII / Unicode
code point). "Case conversion & ASCII arithmetic" is the beginner-level technique
of treating characters as numbers so you can compute with them directly:

- `ord(c)` gives the integer code of a character; `chr(n)` maps an integer back to a character.
- Because the ASCII table lays out `'A'..'Z'` contiguously (65..90), `'a'..'z'`
  contiguously (97..122), and `'0'..'9'` contiguously (48..57), you can do
  arithmetic on the codes to derive positions, convert case, or build new characters.

Common building blocks:

| Goal | Formula |
|---|---|
| Letter index `a`->0 ... `z`->25 | `ord(c) - ord('a')` |
| Letter index `A`->0 ... `Z`->25 | `ord(c) - ord('A')` |
| Digit char to int | `ord(c) - ord('0')` |
| Uppercase -> lowercase | `chr(ord(c) + 32)` |
| Lowercase -> uppercase | `chr(ord(c) - 32)` |
| Toggle case (letters) | `chr(ord(c) ^ 32)` |
| Index -> lowercase letter | `chr(ord('a') + i)` |
| Rotate/shift within alphabet | `chr((ord(c) - ord('a') + k) % 26 + ord('a'))` |

The magic constant `32` is the distance between an uppercase letter and its
lowercase counterpart (`'a' - 'A' == 32`), which is also bit `0x20`, so XOR with
`32` toggles case.

## When to reach for it

Reach for ASCII arithmetic when a problem asks you to change case, map letters to
indices (for a fixed-size frequency array), interpret letters as digits in a base
(e.g. Excel columns as base-26), or rotate letters around the alphabet. It removes
the need for lookup tables or big `if/elif` chains and keeps everything O(1) per
character.

## Typical complexity

Each character is processed in **O(1)** time and space, so a full pass over a
string of length `n` is **O(n) time** and **O(1) auxiliary space** (or O(n) if you
must materialize a new string, since strings are immutable in Python).

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [To Lower Case](problem-01-to-lower-case/PROBLEM.md) | Lowercase every uppercase letter using its code point | Easy |
| 2 | [Find the Difference](problem-02-find-the-difference/PROBLEM.md) | Detect the one extra character added to a shuffled string via code sums / XOR | Easy |
| 3 | [Excel Sheet Column Number](problem-03-excel-sheet-column-number/PROBLEM.md) | Read a column title as a base-26 number using letter indices | Easy |
| 4 | [Excel Sheet Column Title](problem-04-excel-sheet-column-title/PROBLEM.md) | Encode a number as an Excel column title (bijective base-26) | Medium |
| 5 | [Shifting Letters](problem-05-shifting-letters/PROBLEM.md) | Apply cumulative modular shifts to each lowercase letter | Medium |
