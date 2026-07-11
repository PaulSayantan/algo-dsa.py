# Solution — Set Mismatch

## Brute Force

Count occurrences with a hash map over `1..n`. The key with count 2 is the
duplicate; the key in `1..n` with count 0 is the missing value.

- **Time:** O(n).
- **Space:** **O(n)** for the map.

Correct, but uses linear extra space. Cyclic sort finds both answers in a single
in-place pass.

## Optimal Approach (Cyclic Sort)

Values are in `[1, n]`, so value `v` belongs at index `v - 1`. Because exactly one
value is duplicated (which forces exactly one value missing), after a value-guarded
cyclic sort there will be **exactly one** index that is "wrong," and it encodes both
answers.

1. Run cyclic sort: for pointer `i`, `j = nums[i] - 1`; if `nums[i] != nums[j]`
   swap home, else advance.
2. Scan for the single index `i` with `nums[i] != i + 1`.
   - `nums[i]` is the **duplicated** value (the extra copy parked in the wrong slot).
   - `i + 1` is the **missing** value (the rightful owner that never arrived).

```python
def findErrorNums(self, nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    return []  # unreachable given the problem guarantees
```

### Why it is correct

Cyclic sort settles each value that has a distinct home. The duplicated value's
second copy has nowhere valid to go, so it occupies the slot of the missing value.
That slot `i` therefore holds `nums[i]` = the duplicate, while `i + 1` = the value
that should have lived there = the missing number. Exactly one such mismatched slot
exists, because exactly one value is duplicated.

### Step-by-step on `[1, 2, 2, 4]`  (n = 4)

```
i=0: nums[0]=1 -> home idx 0, already correct, advance i=1
i=1: nums[1]=2 -> home idx 1, already correct, advance i=2
i=2: nums[2]=2 -> home idx 1. nums[1]=2 == 2 (occupied by equal value), advance i=3
i=3: nums[3]=4 -> home idx 3, already correct, advance i=4
Array unchanged: [1, 2, 2, 4]
scan: idx2 holds 2 != 3 -> duplicate = 2, missing = 3
Result: [2, 3]
```

### Complexity

- **Time:** O(n) — cyclic placement plus one linear scan.
- **Space:** O(1) extra.

## Key Insights & Edge Cases

- **One mismatched slot yields both answers:** read the value for the duplicate,
  read the index+1 for the missing number. This is the elegant payoff of the
  pattern.
- **Value-guarded swap** (`nums[i] != nums[j]`) is mandatory — the duplicate would
  otherwise loop forever against its equal twin.
- A math alternative exists (solve using `sum` and `sum of squares`, or XOR
  partitioning), but cyclic sort avoids overflow concerns and reuses the folder's
  core pattern.
- Edge case `[1, 1]` -> the only wrong slot is index 0 (holds 1, should hold... it
  actually stays; the wrong slot is index 1 holding 1 != 2) -> `[1, 2]`.
