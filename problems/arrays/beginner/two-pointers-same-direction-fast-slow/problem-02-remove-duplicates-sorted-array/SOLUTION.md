# Remove Duplicates from Sorted Array — Solution

## Brute Force

Collect the distinct values (for example by iterating and remembering the last
value seen, or by pushing into an ordered set / auxiliary list), then copy them
back into the front of `nums`.

```python
def removeDuplicates(nums):
    seen = []
    for x in nums:
        if not seen or seen[-1] != x:
            seen.append(x)
    nums[:len(seen)] = seen
    return len(seen)
```

- **Time:** O(n).
- **Space:** O(n) for the `seen` buffer — violates the O(1)-space requirement.

## Optimal Approach (Two Pointers, same direction)

Because the array is **sorted**, all copies of a value sit next to each other.
That means we can decide whether a candidate is "new" by comparing it to the
**last value we kept** — no set needed.

- `write` — index of the most recently kept unique element. Everything in
  `nums[0 .. write]` is the distinct-so-far result.
- `read` — scans from index `1` to the end.

Start `write = 0` (the first element is always unique). For each `read`, if
`nums[read] != nums[write]`, we have found the next new value: advance `write`
and copy `nums[read]` there. Otherwise it is a duplicate of the current run and
we skip it. The answer `k` is `write + 1`.

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    write = 0
    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]
    return write + 1
```

### Why it is correct

**Invariant:** after processing index `read`, `nums[0 .. write]` contains the
distinct values seen in `nums[0 .. read]`, in order, and `nums[write]` is the
largest (most recent) of them. Sortedness guarantees a value equal to
`nums[write]` can only appear contiguously right after it, so testing
`nums[read] != nums[write]` correctly detects the first occurrence of every new
value. Since `write <= read`, copies never overwrite unread data.

### Complexity

- **Time:** O(n) — one linear scan.
- **Space:** O(1) — two indices only.

## Key Insights & Edge Cases

- **Sortedness is the enabler.** On an unsorted array this comparison-to-last
  trick fails; you would need a hash set (O(n) space) or a sort first.
- **`k = write + 1`, not `write`.** `write` is an index, so the count of kept
  elements is one more than the last written index.
- **Single element** (`[7]`): the loop over `range(1, 1)` never runs, and we
  return `0 + 1 = 1`.
- **All identical** (`[2, 2, 2]`): no `read` ever differs from `nums[write]`, so
  `write` stays `0` and we return `1`.
- **Already all-distinct:** every element is copied onto its own position,
  returning `n`.
