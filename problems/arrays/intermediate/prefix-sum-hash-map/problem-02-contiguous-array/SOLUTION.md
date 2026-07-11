# Solution — Contiguous Array

## Brute Force

For every start `i`, extend to every end `j`, tracking the counts of `0`s and
`1`s (or a single balance counter). Record the length whenever the counts are
equal.

```python
best = 0
for i in range(len(nums)):
    zeros = ones = 0
    for j in range(i, len(nums)):
        if nums[j] == 0:
            zeros += 1
        else:
            ones += 1
        if zeros == ones:
            best = max(best, j - i + 1)
return best
```

- **Time:** O(n^2).
- **Space:** O(1).

## Optimal Approach — Prefix Sum + Hash Map

**Remap:** treat `0` as `-1` and `1` as `+1`. A subarray has equal 0s and 1s
**iff** its remapped sum is `0`.

Let `running` be the remapped prefix sum. A subarray `nums[i+1..j]` has sum `0`
**iff** `prefix[j] == prefix[i]`. So if the same prefix-sum value occurs at two
indices, the elements strictly between them are balanced, and its length is the
difference of those indices.

To maximize length we want the **earliest** index of each prefix-sum value.
Store `first_index[value] = earliest index where prefix sum == value`, and seed
it with `{0: -1}` (prefix sum is `0` before index `0`).

```python
def findMaxLength(nums):
    first_index = {0: -1}   # prefix sum 0 occurs "before" index 0
    running = 0
    best = 0
    for i, x in enumerate(nums):
        running += 1 if x == 1 else -1
        if running in first_index:
            best = max(best, i - first_index[running])
        else:
            first_index[running] = i   # keep only the earliest index
    return best
```

### Why it is correct

- If `prefix[j] == prefix[i]` with `i < j`, then `sum(nums[i+1..j]) = 0`, so
  that subarray (length `j - i`) is balanced.
- We only *write* a prefix sum the first time we see it, so `first_index` holds
  the leftmost occurrence — pairing a later index with it yields the longest
  balanced subarray ending there.
- The seed `{0: -1}` lets a balanced prefix `nums[0..j]` produce length
  `j - (-1) = j + 1`.

### Step by step on `nums = [0, 1, 0]`

Remapped: `[-1, +1, -1]`.

| i | x  | running | seen before? | first_index update | best |
|---|----|---------|--------------|---------------------|------|
| — | —  | 0       | seed         | {0:-1}              | 0    |
| 0 | 0  | -1      | no           | {0:-1, -1:0}        | 0    |
| 1 | 1  | 0       | yes (@ -1)   | —                   | 1-(-1)=2 |
| 2 | 0  | -1      | yes (@ 0)    | —                   | max(2, 2-0)=2 |

Result: **2** ✓.

- **Time:** O(n).
- **Space:** O(n).

## Key Insights & Edge Cases

- **The `0 -> -1` remap** is the crux: it converts an "equal counts" question
  into a "subarray sum equals 0" question, unlocking the prefix-sum technique.
- **Store earliest index, never overwrite.** For longest-subarray problems you
  want the smallest index for each prefix value; overwriting would shrink the
  answer.
- **Seed with `{0: -1}`**, not `{0: 0}`. Using index `-1` makes lengths come
  out as `i - (-1) = i + 1`, correctly counting a balanced prefix.
- An all-`0`s or all-`1`s array returns `0` — no prefix sum repeats except the
  seed, which never matches a same-value later index in a way that balances.
