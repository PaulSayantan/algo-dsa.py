# Permutations — Solution

## Brute Force

The most literal approach is to defer to the standard library or to build
permutations by repeatedly inserting each new element into every position of the
permutations of the prefix.

```python
from itertools import permutations
def permute(nums):
    return [list(p) for p in permutations(nums)]
```

Or the "insert into every gap" method: start with `[[]]`; for each number, take
every partial arrangement and splice the number into each of its `k+1` gaps.

- **Time:** `O(n · n!)` — there are `n!` results, each of length `n`.
- **Space:** `O(n · n!)` output; `O(n)` auxiliary for the recursion/iteration.

This works, but hides the choose/undo mechanics. The backtracking version below
makes them explicit and is what interviewers expect.

## Optimal Approach (Backtracking)

Build the permutation one slot at a time. Track which elements are already
placed with a `used` boolean array (or by swapping in place). At depth `d` you
choose any unused element for position `d`.

```python
def permute(nums):
    n = len(nums)
    result = []
    path = []
    used = [False] * n

    def backtrack():
        if len(path) == n:            # all positions filled -> a full permutation
            result.append(path[:])
            return
        for i in range(n):
            if used[i]:
                continue              # prune: element already placed
            used[i] = True            # choose
            path.append(nums[i])
            backtrack()               # recurse on the next position
            path.pop()                # undo
            used[i] = False

    backtrack()
    return result
```

**Why it is correct.** Every complete branch fixes an element for each of the
`n` positions with no repeats (the `used` guard), so each leaf is a valid
permutation. Because at position `d` we iterate over *all* currently-unused
elements, we generate every possible arrangement exactly once — two distinct
permutations must differ at some earliest position, and the loop at that
position explores both choices.

**Step by step for `nums = [1, 2, 3]`:**

- Position 0 picks `1` → position 1 picks `2` → position 2 picks `3` → `[1,2,3]`.
  Undo `3`; position 2 picks nothing else. Undo `2`; position 1 picks `3` →
  position 2 picks `2` → `[1,3,2]`.
- Undo back to position 0, pick `2` → `[2,1,3]`, `[2,3,1]`.
- Undo, pick `3` → `[3,1,2]`, `[3,2,1]`.

Six permutations, matching `3! = 6`.

- **Time:** `O(n · n!)` — `n!` leaves, `O(n)` to copy each.
- **Space:** `O(n)` for `path`, `used`, and recursion depth.

## Key Insights & Edge Cases

- **`used` array vs. swapping.** A common alternative avoids `used` by swapping
  `nums[d]` with `nums[i]` for `i >= d`, recursing on `d+1`, then swapping back.
  Same complexity, less extra space, but the `used` version is easier to read.
- **Copy on record** (`path[:]`) — same trap as in Subsets; appending the live
  list corrupts all results.
- **Distinct inputs** are guaranteed, so no dedup is needed. For arrays with
  duplicates (LeetCode 47, "Permutations II"), sort and skip `nums[i]` when it
  equals `nums[i-1]` and `nums[i-1]` is not currently used in this branch.
- **Single element** `[x]` returns `[[x]]`; the base case fires immediately.
