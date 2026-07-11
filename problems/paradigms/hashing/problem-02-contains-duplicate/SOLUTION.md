# Contains Duplicate — Solution

## Brute Force

Compare every pair of elements; if any two are equal, report a duplicate.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False
```

- **Time:** O(n^2) — every pair compared.
- **Space:** O(1).

A common intermediate approach is to **sort** and then check adjacent elements:

```python
nums.sort()
return any(nums[i] == nums[i + 1] for i in range(len(nums) - 1))
```

- **Time:** O(n log n).
- **Space:** O(1) to O(n) depending on the sort — and it mutates/copies the input.

We can do better in time.

## Optimal Approach (Hashing)

Maintain a hash set `seen`. Scan once; for each value `x`:

1. If `x` is already in `seen`, a duplicate exists -> return `True`.
2. Otherwise add `x` to `seen`.

If the loop finishes, every value was distinct -> return `False`.

```python
def containsDuplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:      # x was added on an earlier iteration
            return True
        seen.add(x)
    return False
```

A one-liner using the same idea: `return len(set(nums)) < len(nums)` — if
deduplicating shrinks the collection, there was a repeat. The explicit loop is
preferred when you want to **early-exit** as soon as the first duplicate appears
instead of always building the full set.

**Why it is correct.** After processing indices `0..i-1`, `seen` holds exactly the
values at those indices. If `nums[i]` equals any earlier value, that value is in
`seen`, so the membership test fires and we return `True` immediately. If no test
ever fires, no value equals an earlier one, meaning all values are distinct.

- **Time:** O(n) average — one pass, O(1) membership test and insert.
- **Space:** O(n) — the set holds up to n distinct values.

## Key Insights & Edge Cases

- **Set membership is the whole trick.** "Have I seen this before?" is precisely
  what a hash set answers in O(1) average time.
- **Single element** (`[7]`): the loop adds it and returns `False`. Correct — one
  element cannot duplicate.
- **All identical** (`[5, 5, 5]`): the second element triggers `True` right away.
- **Negatives and huge values** hash fine; no range assumptions are needed.
- **Early exit matters** for very large arrays with an early duplicate — you avoid
  scanning the rest.
