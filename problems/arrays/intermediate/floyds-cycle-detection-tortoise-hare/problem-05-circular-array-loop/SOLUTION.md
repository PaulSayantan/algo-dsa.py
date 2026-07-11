# Solution — Circular Array Loop

## Brute Force

For each starting index, walk the movement rule and record visited indices in a
set for *this* start. If you revisit an index while staying in a single
direction and the cycle length is greater than 1, return `True`. Reset the
visited set for each new start.

```python
def circularArrayLoop(nums):
    n = len(nums)

    def nxt(i):
        return (i + nums[i]) % n

    for start in range(n):
        seen = {}
        i = start
        step = 0
        while True:
            # direction must stay consistent
            if nums[i] * nums[start] < 0:
                break
            if i in seen:
                if step - seen[i] > 1:   # cycle length > 1
                    return True
                break
            seen[i] = step
            step += 1
            i = nxt(i)
    return False
```

- **Time:** O(n^2) in the worst case (a fresh walk from every index).
- **Space:** O(n) for the per-start `seen` map.

## Optimal Approach — Floyd's Cycle Detection (Tortoise & Hare)

Model the array as the functional graph `next(i) = (i + nums[i]) mod n` and run
tortoise & hare from each unresolved start, but add the two problem-specific
guards:

1. **Single direction:** all moves in a valid cycle share a sign. So while
   walking from a given start, if a step's value has a different sign from the
   start's value, this path can never yield a valid cycle — stop.
2. **No length-1 cycles:** if `next(i) == i`, that index is a self-loop
   (`k == 1`) and is not allowed; treat it as a dead end.

```python
def circularArrayLoop(nums):
    n = len(nums)

    def nxt(i):
        return (i + nums[i]) % n

    for start in range(n):
        if nums[start] == 0:            # already-marked dead index
            continue
        slow = fast = start
        # A valid cycle keeps the same sign as nums[start].
        while (nums[slow] * nums[nxt(slow)] > 0
               and nums[fast] * nums[nxt(fast)] > 0
               and nums[nxt(fast)] * nums[nxt(nxt(fast))] > 0):
            slow = nxt(slow)
            fast = nxt(nxt(fast))
            if slow == fast:
                if slow == nxt(slow):   # length-1 self loop -> invalid
                    break
                return True             # valid cycle of length > 1
        # Mark this whole path dead so we never re-walk it: O(n) total work.
        i = start
        val = nums[start]
        while nums[i] * val > 0:
            j = nxt(i)
            nums[i] = 0
            i = j
    return False
```

### Why it is correct

Within a fixed direction, `next` is a deterministic single-successor function,
so any walk is eventually periodic and Floyd's pointers meet iff there is a
cycle reachable from the start. The sign guard ensures we only ever accept a
loop composed entirely of same-direction moves: the instant the sign flips, the
path leaves the "valid" subgraph and we abort before a false positive. The
`slow == nxt(slow)` check discards `k == 1` self-loops, which the problem
explicitly forbids. Marking every index on a failed path to `0` guarantees each
index is walked a constant number of times overall, giving linear total work.

### Step-by-step on `nums = [2, -1, 1, 2, 2]` (n = 5)

`next(i) = (i + nums[i]) % 5`: `next(0)=2, next(2)=3, next(3)=0`. All of
`nums[0], nums[2], nums[3]` are positive, so the sign guard passes throughout.

Start at index 0, `slow = fast = 0`:

| Step | slow                | fast                         |
|------|---------------------|------------------------------|
| 1    | next(0)=2           | next(next(0))=next(2)=3      |
| 2    | next(2)=3           | next(next(3))=next(0)=2      |
| 3    | next(3)=0           | next(next(2))=next(3)=0      |

`slow == fast == 0`, and `next(0)=2 != 0`, so it is not a self-loop -> return
`True`. The cycle `0 -> 2 -> 3 -> 0` has length 3 and is all-positive.

- **Time:** O(n) — each index is visited a constant number of times because
  failed paths are marked dead.
- **Space:** O(1) extra (the `nums[i] = 0` marking reuses the input; if the
  array must stay pristine, use an O(n) visited array instead).

## Key Insights & Edge Cases

- **Sign guard is essential.** Plain cycle detection would happily report loops
  that alternate direction; the multiplicative sign test `nums[a]*nums[b] > 0`
  filters those out.
- **Reject length-1 cycles** with `slow == next(slow)`. A single index whose
  jump lands on itself (after modular wrap) is not a valid loop.
- **`% n` on jumps** must handle negatives correctly. In Python `(i + nums[i]) %
  n` already yields a non-negative index; in languages with truncated modulo you
  must add `n` and take modulo again.
- **Marking visited to `0`** keeps the algorithm O(n). If modifying `nums` is
  disallowed, fall back to an O(n) `visited`/direction array — you still avoid
  the O(n^2) blowup of naive re-walking.
- **Single element `[x]`:** `next(0) = 0`, a self-loop of length 1, so the
  answer is correctly `False`.
