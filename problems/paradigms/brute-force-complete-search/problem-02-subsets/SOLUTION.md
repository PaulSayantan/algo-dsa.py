# Subsets — Solution

## Brute Force

Every subset corresponds to a yes/no decision for each of the `n` elements.
Encode those decisions as the bits of an integer `mask` ranging from `0` to
`2^n - 1`. Bit `i` set means "include `nums[i]`". Iterate all masks and build
the matching subset. This *is* complete search: we visit every point in the
`2^n` decision space exactly once.

```python
class Solution:
    def subsets(self, nums):
        n = len(nums)
        result = []
        for mask in range(1 << n):            # 0 .. 2^n - 1
            subset = [nums[i] for i in range(n) if mask >> i & 1]
            result.append(subset)
        return result
```

- **Time:** `O(2^n · n)` — `2^n` masks, and building each subset scans `n` bits.
- **Space:** `O(2^n · n)` for the output (unavoidable — that's the answer size);
  `O(n)` auxiliary beyond the output.

## Optimal Approach

Any algorithm that returns the full power set must produce `2^n` subsets, so
`O(2^n · n)` is asymptotically optimal — you cannot beat the size of the output.
The bitmask enumeration above is the cleanest complete-search realization. An
equivalent recursive formulation (choose/skip each element) has the same
complexity:

```python
def subsets(nums):
    result = []
    def dfs(i, current):
        if i == len(nums):
            result.append(current[:])
            return
        dfs(i + 1, current)                 # skip nums[i]
        current.append(nums[i])
        dfs(i + 1, current)                 # take nums[i]
        current.pop()
    dfs(0, [])
    return result
```

**Why it is correct.** There is a bijection between subsets of an `n`-element set
and length-`n` binary strings (equivalently, integers in `[0, 2^n)`): bit `i`
tells whether element `i` is present. The loop `for mask in range(1 << n)` hits
every such integer exactly once, so it generates every subset exactly once — no
omissions, no duplicates. Uniqueness of the input elements guarantees no two
distinct masks map to equal subsets.

**Step by step** for `nums = [1, 2, 3]` (bit 0 = element 1, bit 1 = 2, bit 2 = 3):

| mask (binary) | included bits | subset      |
|---------------|---------------|-------------|
| 000           | —             | `[]`        |
| 001           | 0             | `[1]`       |
| 010           | 1             | `[2]`       |
| 011           | 0,1           | `[1, 2]`    |
| 100           | 2             | `[3]`       |
| 101           | 0,2           | `[1, 3]`    |
| 110           | 1,2           | `[2, 3]`    |
| 111           | 0,1,2         | `[1, 2, 3]` |

That is all `2^3 = 8` subsets.

- **Time:** `O(2^n · n)`.
- **Space:** `O(2^n · n)` output.

## Key Insights & Edge Cases

- **`mask >> i & 1`** extracts bit `i`. In Python, `>>` binds tighter than `&`,
  so the parentheses are optional, but write them if unsure.
- **`1 << n` is `2^n`.** With `n <= 10` the largest mask count is `1024`, tiny.
- **Empty subset:** `mask = 0` naturally yields `[]`; do not special-case it.
- **Uniqueness of inputs is given**, so you never need to deduplicate. If the
  input *could* contain duplicates (LeetCode 90, "Subsets II"), the bitmask
  approach would produce duplicate subsets and you would need to sort each and
  drop repeats — a different problem.
- **Order is unconstrained**, so the bitmask order shown above is acceptable as
  is; no sorting required.
