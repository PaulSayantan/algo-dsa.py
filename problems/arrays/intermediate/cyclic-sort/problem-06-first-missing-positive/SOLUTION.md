# Solution — First Missing Positive

## Brute Force

Put all values into a `set`, then check `1, 2, 3, ...` in order until you find one
missing.

- **Time:** O(n).
- **Space:** **O(n)** for the set.

Correct and simple, but the problem demands O(1) auxiliary space, which rules out the
set. Sorting first (`O(n log n)`) then scanning also violates the time bound. Cyclic
sort hits both O(n) time and O(1) space.

## Optimal Approach (Cyclic Sort)

The crucial insight: with `n = len(nums)`, the answer must lie in `[1, n + 1]`. If
`1..n` all appear, the answer is `n + 1`; otherwise it is the smallest gap in
`1..n`. So values `<= 0` or `> n` are noise — we simply never place them. Everything
else uses the `[1, n]` home rule: value `v` belongs at index `v - 1`.

1. Run cyclic sort, but only swap when the current value is **in range** `[1, n]`
   and **not already home** (`nums[i] != nums[j]`). Otherwise advance `i`.
2. Scan left to right for the first index `i` with `nums[i] != i + 1`; return
   `i + 1`.
3. If every slot matches, all of `1..n` are present, so return `n + 1`.

```python
def firstMissingPositive(self, nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1                      # home index for value nums[i]
        if 1 <= nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```

### Why it is correct

The `1 <= nums[i] <= n` guard confines placement to values that could possibly be
the answer, keeping every index access valid (no out-of-bounds). After the pass,
every in-range value that appeared sits at its home index. The first index missing
its rightful value `i + 1` is exactly the smallest absent positive. If none is
missing among `1..n`, the sequence is complete and the next positive, `n + 1`, is
the answer. The `nums[i] != nums[j]` guard prevents infinite loops on duplicates and
on out-of-range junk.

### Step-by-step on `[3, 4, -1, 1]`  (n = 4)

```
i=0: nums[0]=3 in [1,4] -> home idx 2. nums[2]=-1 != 3, swap -> [-1, 4, 3, 1]
i=0: nums[0]=-1 not in [1,4] -> advance i=1
i=1: nums[1]=4 in [1,4] -> home idx 3. nums[3]=1 != 4, swap -> [-1, 1, 3, 4]
i=1: nums[1]=1 in [1,4] -> home idx 0. nums[0]=-1 != 1, swap -> [1, -1, 3, 4]
i=1: nums[1]=-1 not in [1,4] -> advance i=2
i=2: nums[2]=3 -> home idx 2, already correct, advance i=3
i=3: nums[3]=4 -> home idx 3, already correct, advance i=4, loop ends
scan: idx0=1 ok, idx1=-1 != 2 -> return 2
```

### Complexity

- **Time:** O(n). Each swap finalizes one in-range value at its home, so at most `n`
  swaps; the `while` advances at most `2n` times overall. The final scan is O(n).
- **Space:** O(1) — all work is in place.

## Key Insights & Edge Cases

- **Answer range `[1, n + 1]` is the whole trick** — it lets us ignore any value
  outside `[1, n]`, which is why arbitrary junk (negatives, zeros, huge numbers)
  doesn't break the O(1)-space bound.
- **Two guards on the swap:** the range check `1 <= nums[i] <= n` keeps index
  accesses valid; the value check `nums[i] != nums[j]` prevents infinite swapping on
  duplicates. Both are required.
- **All values out of range** (e.g. `[7, 8, 9, 11, 12]`) leaves index 0 mismatched
  immediately, correctly returning `1`.
- **Fully packed `1..n`** (e.g. `[1, 2, 3]`) reaches the `return n + 1` fallback.
- Do not advance `i` after a productive swap — the freshly arrived value may itself
  need placing.
