# Counting Bits — Solution

## Brute Force

For each `i` from 0 to `n`, compute its popcount independently (for example with Brian
Kernighan's loop from Problem 2, or `bin(i).count("1")`).

```python
def countBits(self, n: int) -> List[int]:
    ans = []
    for i in range(n + 1):
        count, x = 0, i
        while x:
            x &= x - 1
            count += 1
        ans.append(count)
    return ans
```

- **Time:** O(n * w) where `w` is the word size, or O(n log n) amortized since each
  popcount costs O(number of set bits).
- **Space:** O(1) beyond the output array.

## Optimal Approach (Bit Manipulation + DP)

We can compute each answer in **O(1)** by reusing an earlier result. Two classic
recurrences work:

### Recurrence A — drop the lowest set bit

`i & (i - 1)` clears the lowest set bit, producing a **smaller** number whose popcount we
already know. Adding back the one bit we removed:

```
ans[i] = ans[i & (i - 1)] + 1        for i >= 1
ans[0] = 0
```

### Recurrence B — shift right (last-bit DP)

`i >> 1` drops the lowest bit. The number of set bits in `i` equals the set bits in
`i >> 1` plus whether the lowest bit of `i` is 1:

```
ans[i] = ans[i >> 1] + (i & 1)       for i >= 1
ans[0] = 0
```

Both reference indices strictly less than `i`, so a single forward loop fills the array.

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)   # Recurrence B
        return ans
```

### Step-by-step with Recurrence B, `n = 5`

| i | binary | i >> 1 | ans[i>>1] | i & 1 | ans[i] |
|---|---|---|---|---|---|
| 0 | 000 | — | — | — | 0 |
| 1 | 001 | 0 | 0 | 1 | 1 |
| 2 | 010 | 1 | 1 | 0 | 1 |
| 3 | 011 | 1 | 1 | 1 | 2 |
| 4 | 100 | 2 | 1 | 0 | 1 |
| 5 | 101 | 2 | 1 | 1 | 2 |

Output `[0, 1, 1, 2, 1, 2]`.

- **Time:** O(n) — one O(1) step per index.
- **Space:** O(n) for the output (O(1) auxiliary).

## Key Insights & Edge Cases

- **Why the DP is valid:** both `i >> 1` and `i & (i - 1)` are strictly smaller than
  `i` for `i >= 1`, so the value they index has already been computed in a left-to-right
  fill — no recursion or memo table needed beyond the answer array itself.
- **`n = 0`:** returns `[0]`; the loop body never runs.
- **Even vs. odd insight (Recurrence B):** an even number has the same set-bit count as
  `i/2`; an odd number has one more than `i//2`. This is exactly `ans[i>>1] + (i & 1)`.
- **Output length:** must be `n + 1`, not `n` — index `n` is inclusive.
- **Overflow:** none in Python; in fixed-width languages the counts are tiny (<= 32) so
  a normal int suffices.
