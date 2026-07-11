# Solution — First Missing Positive

## Brute Force

Put every value into a hash set, then probe `1, 2, 3, ...` until you find one
that is absent.

```python
def firstMissingPositive(nums):
    present = set(nums)
    i = 1
    while i in present:
        i += 1
    return i
```

- **Time:** `O(n)` — building the set and probing are each linear (you probe at
  most `n + 1` values).
- **Space:** `O(n)` — the hash set.

Correct and simple, but it uses `O(n)` extra space, which the problem forbids.

## Optimal Approach (Cyclic Sort / Index Placement)

**Two key facts:**

1. With `n` elements, the answer is always in `[1, n + 1]`. If `1..n` are all
   present the answer is `n + 1`; otherwise it is the smallest gap in `1..n`.
2. Values outside `[1, n]` (negatives, zero, or `> n`) can never *be* the
   answer, so they are irrelevant except as "garbage" occupying slots.

This lets us use the array as a hash table where **value `v` lives at index
`v - 1`**.

### Step by step

1. **Place pass (cyclic sort).** For each index `i`, repeatedly swap
   `nums[i]` toward its home slot while it is a placeable, misplaced value:
   - the value `v = nums[i]` is in range `1 <= v <= n`, **and**
   - it is not already home, i.e. `nums[v - 1] != v`.

   Each swap moves one value into its correct slot, so the total number of swaps
   is bounded by `n`.
2. **Scan pass.** Walk the array; the first index `i` where `nums[i] != i + 1`
   means `i + 1` is missing — return `i + 1`.
3. If every slot matches (`nums[i] == i + 1` for all `i`), then `1..n` are all
   present, so return `n + 1`.

```python
def firstMissingPositive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```

### Why it is correct

- **The `while` loop terminates.** We only swap when the destination slot
  `nums[v-1]` does **not** already hold `v`; after the swap that slot *does* hold
  `v`, so a value is never swapped into a position twice. Across the whole
  algorithm at most `n` productive swaps occur, keeping total work `O(n)`.
- **Out-of-range values are skipped**, so they simply come to rest in whatever
  slots the in-range values did not claim — exactly the slots that expose the
  missing positive during the scan.
- **The scan is exhaustive.** After placement, slot `i` holds `i + 1` iff the
  value `i + 1` exists in the array. The first mismatch is the smallest missing
  positive; no mismatch means the full range `1..n` is present, answer `n + 1`.
- **Swap the value, not `i`.** A subtle bug is writing
  `nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]` in Python: the left-hand
  `nums[nums[i]-1]` re-evaluates `nums[i]` *after* it was reassigned. Capture the
  target index (`target = nums[i] - 1`) first, as shown above.

### Complexity

- **Time:** `O(n)` — the amortized swap count is `O(n)` plus one linear scan.
- **Space:** `O(1)` extra — all work happens inside `nums`.

### Trace of `[3,4,-1,1]`

```
start:        [3, 4, -1, 1]
i=0: 3 -> slot 2, swap  [-1, 4, 3, 1]   (nums[0]=-1 now out of range, stop)
i=1: 4 -> slot 3, swap  [-1, 1, 3, 4]   nums[1]=1 -> slot 0, swap [1, -1, 3, 4]
                                        nums[1]=-1 out of range, stop
i=2: 3 already at slot 2 (nums[2]==3), stop
i=3: 4 already at slot 3 (nums[3]==4), stop
placed:       [1, -1, 3, 4]
scan: index 0 holds 1 (ok); index 1 holds -1 != 2 -> answer 2
```

## Key Insights & Edge Cases

- **Answer bounded by `n + 1`:** this is what makes an array of size `n` a
  sufficient hash table; nothing outside `1..n` can matter until everything in
  `1..n` is present.
- **Duplicates and garbage are harmless:** the `nums[v-1] != v` guard stops a
  duplicate from cycling forever and prevents infinite swapping.
- **All present:** `[1,2,3]` places to itself and the scan finds no mismatch ->
  return `n + 1 = 4`.
- **All non-positive / all huge:** `[7,8,9,11,12]` has no in-range value, so no
  swaps happen and slot 0 already mismatches -> answer `1`.
- **Single element:** `[1]` -> `2`; `[2]` -> `1`.
