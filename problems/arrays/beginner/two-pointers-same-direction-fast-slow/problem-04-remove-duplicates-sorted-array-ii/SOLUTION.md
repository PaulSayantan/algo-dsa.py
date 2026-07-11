# Remove Duplicates from Sorted Array II — Solution

## Brute Force

Walk the array counting the length of each equal run, and copy at most two of
each value into an auxiliary list; copy it back at the end.

```python
def removeDuplicates(nums):
    out = []
    count = 0
    for i, x in enumerate(nums):
        if i > 0 and x == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count <= 2:
            out.append(x)
    nums[:len(out)] = out
    return len(out)
```

- **Time:** O(n).
- **Space:** O(n) for `out` — violates the O(1)-space requirement.

## Optimal Approach (Two Pointers, same direction)

The key trick: since the array is sorted, if the value we are about to keep is
allowed to appear **at most twice**, then a candidate `nums[read]` can be kept
only if it differs from the element **two slots back in the output**,
`nums[write - 2]`. If `nums[read] == nums[write - 2]`, keeping it would create a
third copy, so we skip it.

- `write` — number of elements committed so far / index of the next free slot.
- `read` — scans every index.

We always keep the first two elements unconditionally (there cannot be a "third
copy" among the first two positions), then apply the `nums[write - 2]` test.

```python
def removeDuplicates(nums):
    write = 0
    for read in range(len(nums)):
        if write < 2 or nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1
    return write
```

### Why it is correct

**Invariant:** `nums[0 .. write-1]` is a valid output prefix — sorted, in
original order, with every value appearing at most twice — built from
`nums[0 .. read-1]`. When we consider `nums[read]`:

- If `write < 2`, the output has fewer than two elements, so appending cannot
  exceed the "twice" cap; keep it.
- Otherwise `nums[write - 2]` is the earlier of the two most recently written
  elements. Because the input is sorted and the output stays sorted, the only
  way `nums[read]` could be a **third** identical copy is if it equals that
  element two slots back. If `nums[read] != nums[write - 2]`, keeping it leaves
  at most two copies, so we append; if equal, we skip.

`write <= read` throughout (we never write more than we have read), so in-place
overwrites are safe. This generalizes to "at most `m` copies" by testing
`nums[read] != nums[write - m]`.

### Complexity

- **Time:** O(n) — single pass.
- **Space:** O(1) — two indices.

## Key Insights & Edge Cases

- **Compare to `write - 2`, not `read - 2`.** The decision must be relative to
  what is already in the *output*, because skipped duplicates shift positions.
- **Length <= 2:** the `write < 2` branch keeps everything; correct for `[1]`
  and `[1, 1]`.
- **All identical** (`[5, 5, 5, 5]`): first two kept, the rest match
  `nums[write - 2] == 5` and are dropped, returning `2`.
- **Already valid** (each value <= twice): every element passes the test and is
  copied onto its own spot, returning `n`.
- **General template:** replace the constant `2` with any `m` to allow at most
  `m` copies of each value.
