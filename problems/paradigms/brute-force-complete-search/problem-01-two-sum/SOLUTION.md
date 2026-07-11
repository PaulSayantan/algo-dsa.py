# Two Sum — Solution

## Brute Force

The problem asks for *any* pair of distinct indices whose values sum to
`target`. The candidate space is simply the set of all unordered index pairs
`(i, j)` with `i < j`. Enumerate every one and test it.

```python
class Solution:
    def two_sum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # guaranteed unreachable by the problem's promise
```

- **Time:** `O(n^2)` — there are `n·(n-1)/2` pairs and each check is `O(1)`.
- **Space:** `O(1)` — no extra storage beyond a few scalars.

Since `n <= 10^4`, the worst case is about `5·10^7` comparisons, which runs well
within typical time limits — so brute force is a legitimate accepted solution
here, not merely a stepping stone.

## Optimal Approach

For Two Sum specifically, the exhaustive pair scan **is** the canonical
complete-search solution and the focus of this exercise, so we present it as the
"optimal" complete-search approach and analyze *why it is correct*:

**Correctness.** The problem guarantees exactly one valid pair exists. The
double loop visits every unordered pair `(i, j)` with `i < j` exactly once.
Therefore the unique valid pair is necessarily visited, and because we test the
exact condition `nums[i] + nums[j] == target`, we return it the first time we
encounter it. Requiring `j > i` guarantees the two indices are distinct, so no
element is ever reused.

**Step by step** on `nums = [3, 2, 4], target = 6`:

1. `i = 0` (value 3): `j = 1` → 3 + 2 = 5 ≠ 6; `j = 2` → 3 + 4 = 7 ≠ 6.
2. `i = 1` (value 2): `j = 2` → 2 + 4 = 6 ✓ → return `[1, 2]`.

- **Time:** `O(n^2)`.
- **Space:** `O(1)`.

> Aside: a hash-map pass can solve Two Sum in `O(n)` time / `O(n)` space by
> remembering, for each value seen so far, its index and looking up
> `target - nums[j]`. That is the *asymptotically* optimal solution, but it is a
> hashing technique rather than complete search; it is noted here only for
> completeness. This directory's purpose is to master the exhaustive baseline.

## Key Insights & Edge Cases

- **Start the inner loop at `i + 1`**, never at `0`, so you never pair an element
  with itself and never revisit the same unordered pair twice.
- **Duplicate values are fine:** `[3, 3]` with `target = 6` works because the two
  3's occupy distinct indices `0` and `1`.
- **Return indices, not values.** A common slip is returning `[nums[i], nums[j]]`.
- **Negative numbers and large magnitudes** need no special handling — Python
  integers are unbounded, and the sum comparison is exact.
- The exhaustive solution is also the perfect **reference oracle**: if you later
  write the `O(n)` hash-map version, stress-test it against this `O(n^2)` version
  on random arrays to catch bugs.
