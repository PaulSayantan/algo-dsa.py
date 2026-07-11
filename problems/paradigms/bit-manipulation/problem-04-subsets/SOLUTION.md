# Subsets — Solution

## Brute Force

The classic approaches are **backtracking** (recurse, choosing to include or exclude
each element) or **iterative cascading** (start with `[[]]` and, for each new element,
append it to copies of every subset built so far).

```python
def subsets(self, nums):
    res = [[]]
    for x in nums:
        res += [subset + [x] for subset in res]
    return res
```

- **Time:** O(n * 2^n) — there are 2^n subsets and building each costs up to O(n).
- **Space:** O(n * 2^n) for the output.

These are correct and efficient; they are labeled "brute force" here only to contrast
with the bitmask formulation below, which has the same asymptotics but exposes the
in/out choice explicitly.

## Optimal Approach (Bit Manipulation)

There is a natural bijection between subsets of an `n`-element set and the integers
`0 .. 2^n - 1`. Interpret an `n`-bit **mask** as: bit `j` is 1 iff `nums[j]` belongs to
the subset. Enumerating all masks enumerates all subsets exactly once.

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for mask in range(1 << n):          # 0 .. 2^n - 1
            subset = []
            for j in range(n):
                if (mask >> j) & 1:          # is bit j set?
                    subset.append(nums[j])
            result.append(subset)
        return result
```

### Step-by-step on `nums = [1, 2, 3]`

`n = 3`, so masks run `000` to `111`:

| mask (bin) | bits set (j) | subset |
|---|---|---|
| 000 | — | `[]` |
| 001 | 0 | `[1]` |
| 010 | 1 | `[2]` |
| 011 | 0,1 | `[1, 2]` |
| 100 | 2 | `[3]` |
| 101 | 0,2 | `[1, 3]` |
| 110 | 1,2 | `[2, 3]` |
| 111 | 0,1,2 | `[1, 2, 3]` |

All 8 subsets, each produced once.

- **Time:** O(n * 2^n) — 2^n masks, O(n) work per mask to test each bit.
- **Space:** O(n * 2^n) for the result (O(n) auxiliary per subset).

## Key Insights & Edge Cases

- **Bijection guarantees no duplicates:** distinct masks map to distinct subsets, so as
  long as `nums` has unique elements the output has no repeats. (If `nums` could contain
  duplicates you would need the "Subsets II" dedup logic instead.)
- **`1 << n` overflow / feasibility:** this technique is practical only for small `n`
  (here `n <= 10`, so at most 1024 masks). For large `n`, 2^n is astronomically large
  regardless of method — the output itself is exponential.
- **Empty subset:** `mask = 0` yields `[]`, so the empty set is included automatically.
- **Iteration order:** masks ascend numerically, giving a deterministic order; the
  problem accepts any order.
- **Bit test idiom:** `(mask >> j) & 1` isolates bit `j`. Equivalent: `mask & (1 << j)`.
- **Handy for more than listing:** the same mask loop underpins bitmask DP (e.g.
  Travelling Salesman, assignment problems) where each mask is a compressed state.
