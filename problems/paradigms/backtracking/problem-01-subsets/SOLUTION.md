# Subsets — Solution

## Brute Force

Each of the `n` elements is either **in** or **out** of a subset, so there is a
one-to-one correspondence between subsets and `n`-bit binary numbers. Iterate a
counter `mask` from `0` to `2^n - 1`; for each `mask`, include `nums[i]` whenever
bit `i` of `mask` is set.

```python
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result
```

- **Time:** `O(n · 2^n)` — `2^n` masks, and each takes `O(n)` to materialize.
- **Space:** `O(n · 2^n)` for the output; `O(n)` auxiliary.

This is perfectly correct and often the cleanest solution for the power set. It
is called "brute force" here only because it does not use the recursive
choose/undo structure that generalizes to the harder problems in this folder.

## Optimal Approach (Backtracking)

The complexity is the same, but the backtracking formulation is the pattern you
will reuse for combinations, permutations, partitions, etc. Think of building a
subset by scanning the array left to right; at index `start`, you decide which
of the *remaining* elements to append next.

```python
def subsets(nums):
    result = []
    path = []

    def backtrack(start):
        # Every node of the recursion tree is itself a valid subset.
        result.append(path[:])           # record a copy
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose nums[i]
            backtrack(i + 1)             # explore with later elements only
            path.pop()                   # un-choose (undo)

    backtrack(0)
    return result
```

**Why it is correct.** Passing `i + 1` (never revisiting earlier indices)
guarantees each subset is generated in strictly increasing index order, so no
subset is produced twice and none is missed. Recording `path` at *every* node
(not just leaves) captures subsets of all sizes, including the empty set (the
root) and the full set (the deepest leaf).

**Step by step for `nums = [1, 2, 3]`:**

1. Record `[]` (root).
2. Choose `1` → record `[1]`.
   - Choose `2` → record `[1,2]`.
     - Choose `3` → record `[1,2,3]`; pop `3`.
   - Pop `2`. Choose `3` → record `[1,3]`; pop `3`.
   - Pop `1`.
3. Choose `2` → record `[2]`.
   - Choose `3` → record `[2,3]`; pop `3`. Pop `2`.
4. Choose `3` → record `[3]`; pop `3`.

That yields all 8 subsets.

- **Time:** `O(n · 2^n)` — `2^n` nodes, `O(n)` to copy `path` at each.
- **Space:** `O(n)` recursion depth + current path (output not counted).

## Key Insights & Edge Cases

- **Copy the path** (`path[:]`), never append the mutable list itself — otherwise
  every entry in `result` ends up pointing at the same (eventually empty) list.
- **Record at every node** distinguishes subset generation from fixed-size
  combination generation (where you record only at the target depth).
- **Uniqueness comes for free** here because inputs are distinct and we only move
  forward via `i + 1`. If duplicates were allowed (LeetCode 90, "Subsets II"),
  sort first and skip `nums[i] == nums[i-1]` when `i > start`.
- **Smallest input** `n = 1` yields `[[], [x]]`; the empty set is always present.
