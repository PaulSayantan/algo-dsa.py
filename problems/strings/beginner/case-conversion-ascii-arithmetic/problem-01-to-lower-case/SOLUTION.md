# Solution — To Lower Case

## Brute Force

The most naive "manual" approach builds an explicit mapping from each of the 26
uppercase letters to its lowercase counterpart (for example a dictionary
`{'A': 'a', 'B': 'b', ...}`), then walks the string and replaces any character
found in that map. Building the map is a fixed amount of work, and scanning the
string is one pass.

- **Time:** O(n) to scan the string of length `n` (map lookups are O(1)).
- **Space:** O(n) for the output string, plus O(1) (a constant 26-entry table).

This works but the lookup table is unnecessary — the ASCII layout already encodes
the relationship.

## Optimal Approach (Case Conversion & ASCII Arithmetic)

Key fact: in ASCII the uppercase letters occupy the contiguous block
`'A'` (65) through `'Z'` (90), and each lowercase letter sits exactly 32 positions
above its uppercase form (`'a'` is 97, and `97 - 65 == 32`). So for any single
character:

1. Compute its integer code with `ord(c)`.
2. If the code is between `ord('A')` and `ord('Z')` inclusive, it is an uppercase
   letter; produce the lowercase version with `chr(ord(c) + 32)`.
3. Otherwise (digit, punctuation, space, or an already-lowercase letter) leave it
   untouched.

Join the transformed characters into the result.

```python
class Solution:
    def toLowerCase(self, s: str) -> str:
        out = []
        for c in s:
            code = ord(c)
            if ord('A') <= code <= ord('Z'):
                out.append(chr(code + 32))
            else:
                out.append(c)
        return "".join(out)
```

**Why it is correct:** the check `ord('A') <= code <= ord('Z')` isolates exactly
the uppercase letters and nothing else, because the uppercase block is contiguous
and disjoint from digits, symbols, and the lowercase block. Adding the constant 32
maps each uppercase code onto the unique lowercase code at the same alphabet
position, so `'A'->'a'`, ..., `'Z'->'z'`. All non-uppercase characters skip the
branch and are copied verbatim, satisfying the "leave everything else unchanged"
requirement.

A neat bitwise variant: since 32 is `0b100000` (`0x20`), and no uppercase letter
already has that bit set, `chr(code | 32)` also lowercases uppercase letters. Be
careful — OR-ing 32 into arbitrary characters (like digits) would corrupt them, so
still guard with the uppercase range check.

- **Time:** O(n) — one O(1) operation per character.
- **Space:** O(n) for the new string (strings are immutable in Python); O(1)
  auxiliary beyond the output.

## Key Insights & Edge Cases

- The magic number 32 is simply `ord('a') - ord('A')`; prefer writing it that way
  or as a named constant so the intent is obvious.
- Only shift characters you have confirmed are uppercase. Blindly adding 32 to
  every character would mangle digits, spaces, and punctuation.
- Characters already lowercase (`'a'..'z'`) must NOT be shifted again — the range
  check handles this automatically.
- Non-letter characters (digits `'0'..'9'`, symbols) are passed through unchanged.
- Empty-ish inputs: constraints guarantee at least one character, but the loop
  naturally handles a hypothetical empty string by returning `""`.
