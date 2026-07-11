# Solution — Find All Duplicates in an Array

## Brute Force

Count occurrences with a hash map (or `collections.Counter`) and emit every key with
count 2.

- **Time:** O(n).
- **Space:** **O(n)** for the counter.

Correct, but the problem explicitly demands O(1) extra space. Cyclic sort delivers
that.

## Optimal Approach (Cyclic Sort)

Values are in `[1, n]`, so value `v`'s home is index `v - 1`. Run the standard
value-guarded cyclic sort:

1. For pointer `i`, target `j = nums[i] - 1`.
2. If `nums[i] != nums[j]`, swap it home. When the home slot already contains an
   equal value (its first copy), the guard is false — we leave the second copy where
   it is and advance.
3. After placement, every index `i` whose value is not `i + 1` is holding a *second*
   copy of some value — that value `nums[i]` is a duplicate.

```python
def findDuplicates(self, nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return [nums[i] for i in range(n) if nums[i] != i + 1]
```

### Why it is correct

Each distinct value's first copy lands at its home index `v - 1`. A value that
appears twice cannot place both copies (only one slot exists), so its second copy
ends up parked at some index `i` that rightfully belongs to a *missing* value —
hence `nums[i] != i + 1`. The value read at every such mismatched slot is exactly a
number that appeared twice. Values appearing once occupy their own home, producing
no mismatch.

### Step-by-step on `[4, 3, 2, 7, 8, 2, 3, 1]`  (n = 8)

```
Start:                    [4, 3, 2, 7, 8, 2, 3, 1]
After the cyclic pass:    [1, 2, 3, 4, 3, 2, 7, 8]
scan mismatches:
  idx4 holds 3 != 5  -> 3 is a duplicate
  idx5 holds 2 != 6  -> 2 is a duplicate
Result: [3, 2]   (order does not matter; [2, 3] equally valid)
```

### Complexity

- **Time:** O(n) — cyclic placement plus one linear scan.
- **Space:** O(1) extra.

## Key Insights & Edge Cases

- **This is the mirror of "disappeared numbers."** At a mismatched index `i`,
  problem 448 reports the *slot* (`i + 1`, the missing value) while this problem
  reports the *value sitting there* (`nums[i]`, the duplicate). Same array state,
  two different reads.
- **Value-guarded swap is essential:** comparing `nums[i] != nums[j]` prevents an
  infinite swap loop between two equal copies.
- **No duplicates** (e.g. `[1, 2, 3, 4]`) yields an empty result — every slot
  matches.
- Alternative O(1)-space trick: use sign flips (`nums[abs(x)-1] *= -1`); a value
  found already negative is a duplicate. Cyclic sort is shown here for consistency
  with the rest of the folder.
