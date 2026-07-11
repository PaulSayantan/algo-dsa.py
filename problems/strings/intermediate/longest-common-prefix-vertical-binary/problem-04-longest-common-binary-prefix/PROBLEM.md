# Longest Common Binary Prefix

**Difficulty:** Medium

Source: Classic bit-manipulation / networking problem ("shared subnet prefix length"),
posed as a fixed-width binary Longest Common Prefix.

## Description

You are given a list of non-negative integers `nums` and a bit width `width`. Interpret
each integer as its `width`-bit binary representation, **zero-padded on the left** so
every value becomes a binary string of exactly `width` characters (most significant bit
first).

Return the **length of the longest common binary prefix** shared by all of these
fixed-width binary strings — that is, the number of leading bits (reading from the most
significant bit) on which *every* value agrees. This is exactly the length of the common
network prefix if the values were addresses (like a CIDR prefix length).

Return an integer in the range `[0, width]`.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= width <= 32`
- `0 <= nums[i] < 2^width` (each value fits in `width` bits).

## Examples

### Example 1
- **Input:** `nums = [12, 13]`, `width = 8`
- **Output:** `7`
- **Explanation:** `12 = 00001100` and `13 = 00001101`. The first 7 bits `0000110`
  match; the 8th bit differs (`0` vs `1`), so the common binary prefix has length 7.

### Example 2
- **Input:** `nums = [8, 8, 8]`, `width = 4`
- **Output:** `4`
- **Explanation:** Every value is `1000`. All 4 bits agree, so the common prefix spans
  the full width.

### Example 3
- **Input:** `nums = [5, 6, 7]`, `width = 4`
- **Output:** `2`
- **Explanation:** `5 = 0101`, `6 = 0110`, `7 = 0111`. Bit column 0 is `0,0,0` and
  column 1 is `1,1,1` (both match), but column 2 reads `0,1,1` — a mismatch — so the
  common prefix is `01`, length 2.

### Example 4
- **Input:** `nums = [0, 15]`, `width = 4`
- **Output:** `0`
- **Explanation:** `0 = 0000` and `15 = 1111` differ at the very first bit, so no bits
  are shared.

## Hint

Use the **Longest Common Prefix (vertical/binary)** technique on the fixed-width binary
strings: scan the bit columns from the most significant bit until one disagrees, or
binary search on the prefix length. (There is also a neat closed form using the highest
differing bit of `max XOR min` — see the answer key.)
