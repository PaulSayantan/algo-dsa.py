# Solution — Contiguous Array

## Brute Force

Check every subarray. For each start `i`, extend `j` and track a running balance
of ones minus zeros; whenever it hits `0`, the subarray `nums[i..j]` is balanced.

```python
def findMaxLength(nums):
    best = 0
    for i in range(len(nums)):
        ones = zeros = 0
        for j in range(i, len(nums)):
            if nums[j] == 1:
                ones += 1
            else:
                zeros += 1
            if ones == zeros:
                best = max(best, j - i + 1)
    return best
```

- **Time:** O(n^2).
- **Space:** O(1).

With `n` up to `10^5`, O(n^2) is ~10^10 operations — far too slow.

## Optimal Approach (Prefix Sum, 1D + Hash Map)

**Transform** the array: map `0 -> -1` and `1 -> +1`. Now a subarray has equal
numbers of 0s and 1s **iff** its transformed sum is `0`.

Let `count` be the running transformed prefix sum. A subarray `nums[i+1..j]` has
sum `0` exactly when the prefix sums at positions `i` and `j` are **equal**:

```
prefix[j] - prefix[i] = 0   <=>   prefix[j] = prefix[i]
```

So, for each running value, we want the **earliest** index at which it first
appeared — that gives the longest balanced subarray ending here. Store
`first_index[value] = the earliest position where this prefix sum was seen`.

Reference implementation:

```python
def findMaxLength(nums):
    first_index = {0: -1}  # prefix sum 0 occurs "before" index 0
    count = 0
    best = 0
    for i, x in enumerate(nums):
        count += 1 if x == 1 else -1
        if count in first_index:
            best = max(best, i - first_index[count])
        else:
            first_index[count] = i
    return best
```

**Why it is correct:** `count` after processing index `i` is the transformed
prefix sum through `i`. If the same `count` was first seen at index `p < i`,
then the elements in `(p, i]` sum to `0` under the transform — equal +1s and
-1s, hence equal 1s and 0s — with length `i - p`. To maximize length we only
ever want the *first* occurrence of each value, so we store an index only when
the value is new and never overwrite it. Seeding `{0: -1}` lets a balanced
prefix that starts at index 0 be measured as `i - (-1) = i + 1`.

**Step by step** on `nums = [0, 0, 1, 0, 0, 0, 1, 1]`:

| i | nums[i] | count | first_index (state)                | best |
|---|---------|-------|------------------------------------|------|
| - | -       | 0     | {0: -1}                            | 0    |
| 0 | 0       | -1    | {0: -1, -1: 0}                     | 0    |
| 1 | 0       | -2    | {0: -1, -1: 0, -2: 1}              | 0    |
| 2 | 1       | -1    | seen at 0 -> len 2-0 = 2           | 2    |
| 3 | 0       | -2    | seen at 1 -> len 3-1 = 2           | 2    |
| 4 | 0       | -3    | {..., -3: 4}                       | 2    |
| 5 | 0       | -4    | {..., -4: 5}                       | 2    |
| 6 | 1       | -3    | seen at 4 -> len 6-4 = 2           | 2    |
| 7 | 1       | -2    | seen at 1 -> len 7-1 = 6           | **6** |

Result = 6.

- **Time:** O(n) — single pass.
- **Space:** O(n) for the hash map.

## Key Insights & Edge Cases

- The `0 -> -1` transform is the crux: it converts "equal counts" into "sum is
  zero," which is exactly what prefix sums detect. This same relabeling trick
  appears whenever you need to balance two categories.
- **Store the earliest index, never overwrite.** Overwriting with a later index
  would shrink the candidate subarray and give a wrong (smaller) answer.
- **Seed `{0: -1}`** so subarrays starting at index 0 are measured correctly.
  A common off-by-one bug is seeding `{0: 0}`.
- **No balanced subarray:** e.g. `[1, 1, 1]` never revisits a prefix value
  (besides the seed, which never re-matches), so `best` stays `0`.
- Odd-length arrays can never be balanced as a whole, but a balanced *subarray*
  may still exist inside them, as in Example 2.
