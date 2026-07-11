# Solution — Excel Sheet Column Number

## Brute Force

You could sum each letter's positional contribution explicitly: the rightmost
letter is worth `value * 26^0`, the next `value * 26^1`, and so on. Iterate from
the last character to the first, tracking a running power of 26.

```python
def titleToNumber(columnTitle):
    result = 0
    power = 1
    for c in reversed(columnTitle):
        value = ord(c) - ord('A') + 1
        result += value * power
        power *= 26
    return result
```

- **Time:** O(L) where L is the length of the title (at most 7).
- **Space:** O(1).

This is already efficient; it just tracks an extra `power` variable. Horner's
method removes that.

## Optimal Approach (Case Conversion & ASCII Arithmetic)

Treat the title as a base-26 number with 1-based digits. Each letter's digit value
is `ord(c) - ord('A') + 1`, giving `'A'=1 ... 'Z'=26`. Scan left to right and apply
Horner's rule: multiply the running result by 26 (shifting existing digits up one
place) and add the current digit.

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            digit = ord(c) - ord('A') + 1
            result = result * 26 + digit
        return result
```

### Step-by-step for `"ZY"`

1. Start `result = 0`.
2. `'Z'`: digit = `ord('Z') - ord('A') + 1 = 25 + 1 = 26`. `result = 0*26 + 26 = 26`.
3. `'Y'`: digit = `ord('Y') - ord('A') + 1 = 24 + 1 = 25`. `result = 26*26 + 25 = 676 + 25 = 701`.
4. Return `701`.

**Why it is correct:** a title `c_1 c_2 ... c_k` represents
`sum(value(c_i) * 26^(k-i))`. Horner's rule factors this as
`(((value(c_1))*26 + value(c_2))*26 + ...) + value(c_k)`, which is exactly what the
loop computes: each iteration multiplies everything accumulated so far by 26 before
adding the new least-significant digit. The 1-based digit mapping comes straight
from the contiguous ASCII layout of `'A'..'Z'`, so `ord(c) - ord('A')` yields
0..25 and the `+ 1` makes it the required 1..26.

- **Time:** O(L) — one O(1) step per character.
- **Space:** O(1).

## Key Insights & Edge Cases

- This is **bijective base-26** (digits 1..26), not ordinary base-26 (digits
  0..25) — there is no "zero" letter, which is why we add 1. This is the exact
  inverse of the "Excel Sheet Column Title" problem.
- Single letters map directly: `"A" -> 1`, `"Z" -> 26`.
- The largest valid input `"FXSHRXW"` fits comfortably in a machine integer
  (it equals 2,147,483,647), and Python integers never overflow regardless.
- Do not forget the `+ 1`; `ord(c) - ord('A')` alone would make `'A'` worth 0 and
  produce wrong totals for any multi-letter title.
- Input is guaranteed non-empty and all-uppercase, so no case handling or
  empty-string guard is required.
