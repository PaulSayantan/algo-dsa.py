# Single Number — Solution

## Brute Force

For each element, scan the rest of the array to see whether it appears again; the one
without a partner is the answer. Alternatively, use a hash map / hash set to count
occurrences and return the value with count 1.

- **Nested-scan time:** O(n^2), **space:** O(1).
- **Hash-map time:** O(n), **space:** O(n).

The hash-map version hits linear time but violates the constant-space requirement.

## Optimal Approach (Bit Manipulation)

XOR (`^`) has three properties that make this a one-liner:

1. **Self-inverse:** `x ^ x = 0` — any value XORed with itself is 0.
2. **Identity:** `x ^ 0 = x` — XOR with 0 leaves a value unchanged.
3. **Commutative & associative:** the order of XOR operations does not matter.

If we XOR **every** element together, each value that appears twice cancels itself to 0,
and the lone value is XORed with 0, so it survives.

```
result = a1 ^ a1 ^ a2 ^ a2 ^ ... ^ single
       = (a1 ^ a1) ^ (a2 ^ a2) ^ ... ^ single
       = 0 ^ 0 ^ ... ^ single
       = single
```

### Reference implementation

```python
from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
        return result
        # equivalently: return reduce(xor, nums, 0)
```

### Step-by-step on `[4, 1, 2, 1, 2]`

| step | value | running XOR (binary) | running XOR (dec) |
|---|---|---|---|
| start | — | `000` | 0 |
| 1 | 4 | `100` | 4 |
| 2 | 1 | `101` | 5 |
| 3 | 2 | `111` | 7 |
| 4 | 1 | `110` | 6 |
| 5 | 2 | `100` | 4 |

Final result `4`, which is the single number.

- **Time:** O(n) — one pass.
- **Space:** O(1) — a single accumulator.

## Key Insights & Edge Cases

- **Why XOR beats a hash set:** identical space-free cancellation. No counting needed.
- **Works with negatives:** Python integers and two's-complement XOR handle negative
  values correctly; the pairing/cancellation argument is independent of sign.
- **Single-element input** (`[1]`): the loop XORs `0 ^ 1 = 1`, correct.
- **Order independence:** because XOR is commutative and associative, the array can be
  in any order — no sorting required.
- **Generalization:** this exact trick only works when non-unique elements appear an
  **even** number of times. For "every other element appears three times," see
  Single Number II, which needs a different bit-counting approach.
