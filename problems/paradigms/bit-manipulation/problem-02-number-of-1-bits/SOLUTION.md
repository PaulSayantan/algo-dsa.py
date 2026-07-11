# Number of 1 Bits — Solution

## Brute Force

Check each bit position individually. For a 32-bit integer, loop `i` from 0 to 31 and
test `(n >> i) & 1`, adding to a counter when the bit is set.

```python
count = 0
for i in range(32):
    count += (n >> i) & 1
return count
```

- **Time:** O(w) where `w` is the word size (32) — always 32 iterations regardless of
  how many bits are set.
- **Space:** O(1).

(String counting `bin(n).count("1")` also works and is O(w), but the task is to
practice bitwise reasoning.)

## Optimal Approach (Bit Manipulation)

**Brian Kernighan's algorithm.** The key identity:

> `n & (n - 1)` clears the **lowest set bit** of `n`.

Why: subtracting 1 flips the lowest set bit to 0 and turns all the lower 0s into 1s;
ANDing with the original `n` wipes out that lowest set bit and everything below it stays
0. So each `n &= n - 1` removes exactly one set bit. Counting how many times we can do
this before `n` becomes 0 gives the number of set bits.

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1   # drop the lowest set bit
            count += 1
        return count
```

### Step-by-step on `n = 11` (`1011`)

| iteration | n (binary) | n - 1 | n & (n-1) | count |
|---|---|---|---|---|
| 1 | `1011` | `1010` | `1010` | 1 |
| 2 | `1010` | `1001` | `1000` | 2 |
| 3 | `1000` | `0111` | `0000` | 3 |
| stop | `0000` | — | — | 3 |

Result `3`.

- **Time:** O(k) where `k` is the number of set bits (at most `w`). Faster than the
  naive loop when the value is sparse.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Why `n & (n - 1)` works:** borrowing during `-1` toggles a contiguous low run of
  bits; AND keeps only the higher bits that were unaffected, deleting the lowest 1.
- **`n = 0`:** the `while` loop never executes, correctly returning 0.
- **Loop count is data-dependent:** the Kernighan loop iterates once per set bit, so a
  power of two (single bit) finishes in one step.
- **Language note:** in Python integers are unbounded and non-negative here, so
  `n & (n - 1)` behaves cleanly. In fixed-width languages, treat `n` as unsigned to
  avoid sign-extension issues with the top bit.
- **Related built-in:** Python 3.10+ offers `int.bit_count()`, and many CPUs expose a
  hardware `POPCNT` instruction — both compute this in effectively O(1).
