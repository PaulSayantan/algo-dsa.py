# Solution — Missing Number

## Brute Force

Sort the array, then scan for the first index `i` where `nums[i] != i`; if none, the
answer is `n`. Or use a boolean/`set` of seen values and check `0..n`.

- **Sort + scan:** O(n log n) time, O(1) space.
- **Hash set:** O(n) time, **O(n) space**.

Both are fine but either pay a log factor or use extra memory. Other O(n)/O(1)
tricks exist (Gauss sum `n(n+1)/2 - sum(nums)`, or XOR of indices and values); the
cyclic-sort version below generalizes to the other problems in this folder.

## Optimal Approach (Cyclic Sort)

Here the range is `[0, n]` but the array has only `n` slots (indices `0..n-1`), so
the natural home for value `v` is index `v` — **not** `v - 1`. One value in `[0, n]`
has no slot (that's the missing one), and value `n`, if present, also has no slot.

1. Walk with pointer `i`. Let `j = nums[i]` be the target index.
2. If `nums[i] < n` **and** `nums[i] != nums[j]`, swap it home. (Skip the swap when
   `nums[i] == n` because index `n` doesn't exist, and skip when it's already home.)
3. Otherwise advance `i`.
4. After placing, scan: the first index `i` with `nums[i] != i` is the missing
   number. If every index matches, the missing number is `n`.

```python
def missingNumber(self, nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i]
        if j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i:
            return i
    return n
```

### Why it is correct

After the cyclic pass, every value `v` in `[0, n-1]` that is present sits at index
`v`. Exactly one index is left holding a "wrong" value — that index is precisely the
missing number, because it is the only slot whose rightful owner never showed up. If
all `n` indices are correct, then `0..n-1` are all present and the missing value must
be `n`.

### Step-by-step on `[3, 0, 1]`  (n = 3)

```
i=0: nums[0]=3, 3 < 3 is false -> can't place (that's value n), advance i=1
i=1: nums[1]=0 -> home idx 0. nums[0]=3 != 0, swap -> [0, 3, 1]
i=1: nums[1]=3, 3 < 3 false -> advance i=2
i=2: nums[2]=1 -> home idx 1. nums[1]=3 != 1, swap -> [0, 1, 3]
i=2: nums[2]=3, 3 < 3 false -> advance i=3, loop ends
scan: idx0=0 ok, idx1=1 ok, idx2=3 != 2 -> return 2
```

### Complexity

- **Time:** O(n) — cyclic placement is O(n), final scan is O(n).
- **Space:** O(1) — in place.

## Key Insights & Edge Cases

- **`[0..n]` range means home index is `v`, not `v - 1`.** Off-by-one here is the
  most common bug.
- **Bounds-check before swapping:** value `n` has no valid index, so guard with
  `nums[i] < n`. Forgetting this causes an out-of-range access.
- **The answer can be `n` itself** (when `0..n-1` are all present), which the final
  `return n` handles.
- Values are guaranteed distinct, so the `nums[i] != nums[j]` guard never loops
  forever.
