# Solution — Range Addition

## Brute Force

Loop over every update and, inside it, loop over every index in `[start, end]`
adding `inc`.

```python
def getModifiedArray(length, updates):
    arr = [0] * length
    for start, end, inc in updates:
        for i in range(start, end + 1):
            arr[i] += inc
    return arr
```

- **Time:** `O(U * length)` where `U = len(updates)`. With `length = 10^5` and
  `U = 10^4`, that is up to `10^9` operations — too slow.
- **Space:** `O(length)` for the output.

## Optimal Approach (Difference Array)

This is the textbook use case. Keep a difference array `diff` of size
`length + 1`. To add `inc` over `[start, end]`, record just two deltas:

```
diff[start]   += inc     # every position from start onward gains inc
diff[end + 1] -= inc     # cancel the gain the moment we pass end
```

Each update is therefore **O(1)**. After all updates are recorded, the original
array is the **prefix sum** of `diff`:

```
arr[0] = diff[0]
arr[i] = arr[i - 1] + diff[i]
```

```python
def getModifiedArray(length, updates):
    diff = [0] * (length + 1)          # extra slot so end + 1 == length is safe
    for start, end, inc in updates:
        diff[start] += inc
        diff[end + 1] -= inc
    arr = [0] * length
    running = 0
    for i in range(length):
        running += diff[i]
        arr[i] = running
    return arr
```

- **Time:** `O(U + length)` — O(U) to record deltas, O(length) to materialize.
- **Space:** `O(length)`.

**Why it is correct:** a range increment is, in "difference space," just a step
up at `start` and a matching step down right after `end`. The prefix sum is the
exact inverse of the difference operation, so summing the recorded deltas
reconstructs precisely the array you would get by applying every increment
directly — while paying only two writes per update.

## Key Insights & Edge Cases

- **The `end + 1` slot.** Sizing `diff` as `length + 1` lets you always write
  `diff[end + 1]` even when `end == length - 1`; that final `-inc` simply lands
  in the sentinel slot and is never read into the output.
- **Empty updates.** If `updates` is empty, the difference array stays all zero
  and the prefix sum yields the all-zeros array — correct by construction.
- **Overlapping ranges add up naturally.** Deltas accumulate, so overlapping or
  nested updates combine correctly without any special handling.
- **Negative increments** work identically; nothing about the method assumes
  positive values.
- **In-place variant.** You can materialize the prefix sum directly over `diff`
  (dropping the sentinel) to avoid a second array — a common interview follow-up.
