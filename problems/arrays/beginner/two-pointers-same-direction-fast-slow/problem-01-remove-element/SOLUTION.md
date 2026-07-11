# Remove Element — Solution

## Brute Force

Build a brand-new list containing only the elements that are not equal to `val`,
then (if the language allows) copy it back over `nums` and return its length.

```python
def removeElement(nums, val):
    kept = [x for x in nums if x != val]
    nums[:len(kept)] = kept
    return len(kept)
```

- **Time:** O(n) — one pass to filter, one to copy back.
- **Space:** O(n) — the auxiliary `kept` list violates the O(1)-space rule.

This works but allocates a second array, which the problem forbids in spirit
(the whole point is an in-place O(1) transformation).

## Optimal Approach (Two Pointers, same direction)

Keep two indices that both move left to right:

- `write` — the position where the next kept element belongs. Everything in
  `nums[0 .. write-1]` is already a confirmed "not equal to val" element.
- `read` — scans every index `0 .. n-1`.

For each `read`, if `nums[read] != val`, it belongs in the output, so copy it to
`nums[write]` and advance `write`. If `nums[read] == val`, skip it (advance only
`read`). At the end, `write` equals `k`, the count of kept elements.

```python
def removeElement(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write
```

### Why it is correct

**Invariant:** before processing index `read`, the subarray `nums[0 .. write-1]`
contains exactly the kept elements found among `nums[0 .. read-1]`, in their
original relative order. Each iteration preserves this: a kept element is
appended at `write` (extending the good region by one) and a removed element is
ignored. Because `write <= read` always holds, the write never clobbers an
element the reader has not yet examined. When the loop ends, `read == n`, so
`nums[0 .. write-1]` holds every kept element and `write == k`.

### Complexity

- **Time:** O(n) — a single pass; each element is examined once.
- **Space:** O(1) — only two integer indices, all work done in `nums`.

## Key Insights & Edge Cases

- **`write <= read` guarantees safety.** The writer never overtakes the reader,
  so overwriting in place can never destroy an unread value.
- **Empty array** (`nums = []`): the loop body never runs and we return `0`.
- **No matches:** every element is copied onto itself, returning `n` — harmless.
- **All matches:** nothing is copied, `write` stays `0`, return `0`.
- **Order not required here** — a swap-with-end variant also works and can do
  fewer writes when `val` is rare, but the reader/writer version is simpler and
  still O(n).
