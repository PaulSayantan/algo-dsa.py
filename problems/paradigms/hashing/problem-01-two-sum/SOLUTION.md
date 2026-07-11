# Two Sum — Solution

## Brute Force

Try every pair `(i, j)` with `i < j` and check whether `nums[i] + nums[j] == target`.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

- **Time:** O(n^2) — every pair is examined.
- **Space:** O(1) — no extra structures.

This is correct but wasteful: for each `nums[i]` it re-scans the rest of the array
looking for the complement `target - nums[i]`. That repeated *search* is exactly
what a hash map removes.

## Optimal Approach (Hashing)

Keep a hash map `seen` mapping **value -> index** for every element processed so
far. Walk the array once. For the current element `x = nums[i]`:

1. Compute the complement `need = target - x`.
2. If `need` is already a key in `seen`, then `seen[need]` and `i` are the answer.
3. Otherwise record `seen[x] = i` and continue.

```python
def twoSum(nums, target):
    seen = {}                      # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:           # complement seen earlier -> done
            return [seen[need], i]
        seen[x] = i                # remember x for a future complement
    return []                      # unreachable given the guarantee
```

**Why it is correct.** By the time we consider index `i`, `seen` contains exactly
the values at indices `0..i-1`. If some earlier index `j < i` forms a valid pair
with `i`, then `nums[j] == target - nums[i] == need`, so `need` is a key in `seen`
and we return `[j, i]`. We check the complement *before* inserting `x`, so an
element is never paired with itself. Because the problem guarantees exactly one
solution, the first pair we find is the answer.

- **Time:** O(n) — one pass, each lookup/insert is O(1) average.
- **Space:** O(n) — the map holds up to n entries.

## Key Insights & Edge Cases

- **Store value -> index, not just the value.** The problem asks for indices, so
  the map's value slot must carry the index.
- **Check before inserting.** Inserting first would let an element match itself
  when `target == 2 * x`.
- **Duplicate values** (e.g. `[3, 3]`): the check-before-insert order handles this
  correctly — the first `3` is stored, and the second `3` finds it as a complement.
- **Negative numbers and large magnitudes** are fine; hashing does not depend on
  sign or range.
- **No sorting needed.** Sorting + two pointers also solves this in O(n log n) but
  loses the original indices unless you track them separately; the hash map keeps
  indices for free and is faster.
