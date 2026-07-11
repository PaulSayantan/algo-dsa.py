# Solution: Contains Duplicate

## Brute Force

Compare every pair of elements. For each index `i`, scan every later index `j`
and check whether `nums[i] == nums[j]`.

```python
def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

- **Time:** `O(n^2)` — every pair is compared.
- **Space:** `O(1)` — no extra storage.

This is too slow for `n` up to `10^5` (about `10^10` comparisons in the worst
case).

## Optimal Approach

Use a hash set (a degenerate frequency map where we only care whether a count is
`>= 1`). Iterate once; for each value, check if it is already in the set. If it
is, we found a duplicate and return `True`. Otherwise add it and continue.

**Why it is correct:** A duplicate exists if and only if, while scanning left to
right, we reach a value that we have already inserted. The set records exactly
the values seen so far, so the membership check is both necessary and
sufficient.

**Step by step:**
1. Create an empty set `seen`.
2. For each value `v` in `nums`:
   - If `v` is in `seen`, return `True`.
   - Otherwise insert `v` into `seen`.
3. If the loop finishes without returning, return `False`.

```python
def containsDuplicate(nums):
    seen = set()
    for v in nums:
        if v in seen:
            return True
        seen.add(v)
    return False
```

A one-liner equivalent compares sizes: `len(set(nums)) != len(nums)`.

- **Time:** `O(n)` — one pass, `O(1)` average per hash operation.
- **Space:** `O(n)` — up to `n` distinct values stored.

## Key Insights & Edge Cases

- **Early exit matters:** Returning as soon as a repeat is found avoids building
  the full set when a duplicate appears early.
- **Set vs. full count map:** Here we never need the actual counts, only
  presence, so a set is the cleanest tool. It is still "frequency counting" —
  the frequency threshold we test is simply "seen at least once."
- **Single-element array:** `[5]` has no duplicate, returns `False`.
- **Negative and large values:** Values range widely, but hashing handles any
  integer, so no special casing is needed.
- **Time/space trade-off:** We trade `O(n)` extra space for a drop from
  `O(n^2)` to `O(n)` time — usually the right call for large inputs.
