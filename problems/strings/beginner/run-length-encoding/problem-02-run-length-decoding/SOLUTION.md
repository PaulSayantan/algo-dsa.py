# Solution — Run-Length Decoding

## Brute Force

Decoding is naturally linear, so there is no wasteful alternative to speak of.
The only "slow" version is building the result with repeated string
concatenation (`result += ch * count`) inside a loop, which in Python creates a
new string each time and degrades toward `O(m^2)` for output length `m`. Using a
list of chunks plus a single `join` fixes that.

- **Time (naive concat):** up to `O(m^2)`.
- **Space:** `O(m)` for the output.

## Optimal Approach (Run-Length Encoding, inverted)

Walk the encoded string with an index `i`. At each block, the character comes
first, then a maximal run of digits gives the count.

Step by step:

1. Initialize `i = 0` and an empty list `out`.
2. While `i < len(encoded)`:
   - Let `ch = encoded[i]` (the run character); advance `i` by 1.
   - Read consecutive digits starting at `i`, accumulating them into an integer
     `count` (e.g. `count = count * 10 + int(digit)`), advancing `i` past all of
     them. This handles multi-digit counts.
   - Append `ch * count` to `out`.
3. Return `"".join(out)`.

```python
def run_length_decode(encoded: str) -> str:
    out = []
    i = 0
    n = len(encoded)
    while i < n:
        ch = encoded[i]
        i += 1
        count = 0
        while i < n and encoded[i].isdigit():
            count = count * 10 + (ord(encoded[i]) - ord("0"))
            i += 1
        out.append(ch * count)
    return "".join(out)
```

**Why it is correct:** The RLE grammar is unambiguous — every block is exactly
one non-digit character followed by its digit-run. Reading a character and then
greedily consuming all following digits recovers each `(char, count)` pair
exactly, and repeating the character `count` times reproduces the original run.
Since blocks are processed in order, concatenation restores the original string.

- **Time:** `O(len(encoded) + m)` where `m` is the decoded length — each input
  character is read once and each output character is written once.
- **Space:** `O(m)` for the output.

## Key Insights & Edge Cases

- **Multi-digit counts:** the inner `while ... isdigit()` loop is essential;
  reading a single digit would break on `"w12"` (yielding 1 `w` then a stray
  `"2"`).
- **Empty input** returns `""`.
- **Count of 1:** `ch * 1 == ch`, handled with no special case.
- **`str.isdigit()` gotcha:** it returns `True` for some non-ASCII digit
  characters (e.g. superscripts). Given the constraints only ASCII digits appear,
  but comparing `"0" <= c <= "9"` is a safer digit test in adversarial inputs.
- Prefer `"".join(list)` over `+=` to keep the whole thing linear.
- This function is the exact inverse of Problem 1's encoder, so
  `decode(encode(s)) == s` for any input `s` without digits.
