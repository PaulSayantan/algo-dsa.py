# Single Number II — Solution

## Brute Force

Count occurrences with a hash map (`collections.Counter`) and return the key whose count
is 1. Or sort and scan in groups of three.

```python
from collections import Counter
def singleNumber(self, nums):
    return next(v for v, c in Counter(nums).items() if c == 1)
```

- **Hash-map time:** O(n), **space:** O(n).
- **Sort time:** O(n log n), **space:** O(1) (in place).

Both violate the "linear time **and** constant space" requirement (hash map uses O(n)
space; sorting is superlinear).

## Optimal Approach (Bit Manipulation)

### Idea: count each bit modulo 3

Look at one bit position `b` at a time. Every value that appears three times contributes
either 0 or 3 to the count of 1s at position `b` — always a multiple of 3. The single
number contributes its own bit (0 or 1). Therefore:

```
(total number of 1s at bit b) mod 3 == (bit b of the single number)
```

Reconstruct the answer bit by bit:

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for b in range(32):
            bit_sum = 0
            for x in nums:
                bit_sum += (x >> b) & 1     # treat x as 32-bit; & 1 ignores sign issues per bit
            if bit_sum % 3:
                result |= (1 << b)
        # Handle negative numbers: bit 31 is the sign bit in 32-bit two's complement.
        if result >= (1 << 31):
            result -= (1 << 32)
        return result
```

- **Time:** O(32 * n) = O(n).
- **Space:** O(1).

### Faster variant: two-mask finite state machine

Track two bitmasks, `ones` and `twos`, encoding how many times (mod 3) each bit has been
seen: a bit is in `ones` if it has appeared 1 time (mod 3), in `twos` if 2 times. When a
bit reaches 3 it is cleared from both. After processing all numbers, bits seen exactly
once remain in `ones`.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for x in nums:
            ones = (ones ^ x) & ~twos
            twos = (twos ^ x) & ~ones
        return ones
```

This runs in O(n) time, O(1) space, with only a handful of bitwise ops per element, and
Python's arbitrary-precision integers handle the sign automatically (negative `x` behaves
consistently across the loop since every value is XORed three times except the answer).

### Step-by-step (bit-count method) on `[2, 2, 3, 2]`

Binary: 2 = `10`, 3 = `11`.

| bit b | 1s contributed by [2,2,3,2] | sum | sum % 3 | result bit |
|---|---|---|---|---|
| 0 | 2:0, 2:0, 3:1, 2:0 | 1 | 1 | 1 |
| 1 | 2:1, 2:1, 3:1, 2:1 | 4 | 1 | 1 |

`result = 0b11 = 3`. Correct.

## Key Insights & Edge Cases

- **Why mod 3:** triples vanish under modulo-3 counting exactly the way pairs vanish
  under XOR (which is modulo-2 counting). Generalizes: for "appears k times except one,"
  count bits mod k.
- **Negative numbers:** in the bit-count method you must interpret the result as signed
  32-bit — if bit 31 is set, subtract 2^32. The two-mask method sidesteps this because it
  never reconstructs bits by hand.
- **Single-element input** (`[5]`): bit sums equal that element's bits, mod 3 leaves them,
  so it is returned directly.
- **Constant space:** neither optimal method allocates memory proportional to `n`.
- **Common bug:** forgetting the sign-fix step, which makes negative single numbers come
  back as large positive values (e.g. `-4` appearing as `4294967292`).
