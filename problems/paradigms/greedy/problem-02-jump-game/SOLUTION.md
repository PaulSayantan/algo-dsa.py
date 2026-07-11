# Jump Game — Solution

## Brute Force

Explore every jump sequence with recursion/backtracking: from index `i`, try every
landing `j` in `[i+1, i+nums[i]]` and recurse until you reach the end or run out.

- **Time:** `O(2^n)` in the worst case (exponential branching). Memoizing reachability
  per index (top-down DP) brings it down to `O(n^2)` — for each index you may scan up
  to `n` forward jumps.
- **Space:** `O(n)` recursion stack (+ `O(n)` memo).

Correct, but wasteful: we don't actually care *how* we reach an index, only *whether*.

## Optimal Approach (Greedy)

**Idea:** Sweep left to right maintaining `farthest` = the maximum index reachable
using everything seen so far. At index `i`, if `i > farthest`, there is a gap we can
never cross, so return `False`. Otherwise extend the reach: `farthest = max(farthest,
i + nums[i])`. If `farthest` ever covers the last index, return `True`.

```python
def canJump(nums):
    farthest = 0
    last = len(nums) - 1
    for i, step in enumerate(nums):
        if i > farthest:          # current index is unreachable
            return False
        farthest = max(farthest, i + step)
        if farthest >= last:      # can already cover the end
            return True
    return True
```

**Why it is correct ("greedy stays ahead"):** `farthest` is exactly the set of
reachable indices `[0, farthest]` — reachability is a prefix, because if index `k` is
reachable then so is every index below it (you can always land short). We only need to
know the boundary of that prefix, and taking the max at every step keeps it as far
right as any strategy could. If a zero (or a run) ever puts `i` past the boundary, no
choice of earlier jumps could have done better, so failure is genuine.

- **Time:** `O(n)` — single pass.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **The key reframing:** don't track individual jumps, track the *reachable frontier*.
  This collapses an exponential search into one linear scan.
- **Single element** (`[0]`): you already stand on the last index → `True`.
- **Leading zero with length > 1** (`[0, 1]`): `farthest` stays 0, index 1 exceeds it →
  `False`.
- **Large jump early** short-circuits: once `farthest >= last` we can return immediately.
- Contrast with *Jump Game II* (LeetCode 45), which asks for the *minimum number of
  jumps* — also greedy, but you advance a BFS-style "current level end" pointer.
