# Permutations — Solution

## Brute Force

Build a permutation position by position. At each step, try every element that
has not yet been used, recurse to fill the remaining positions, then undo the
choice (backtrack). When all `n` positions are filled, record the arrangement.
This walks the full `n!` tree of orderings.

```python
class Solution:
    def permute(self, nums):
        result = []
        used = [False] * len(nums)
        current = []

        def dfs():
            if len(current) == len(nums):
                result.append(current[:])   # copy the finished permutation
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                dfs()
                current.pop()               # backtrack
                used[i] = False

        dfs()
        return result
```

- **Time:** `O(n! · n)` — there are `n!` leaves and copying each finished
  permutation costs `O(n)`.
- **Space:** `O(n! · n)` output; `O(n)` recursion depth + `used` array auxiliary.

## Optimal Approach

Because the answer itself has `n!` entries of length `n`, `O(n! · n)` is the best
achievable — you cannot enumerate all permutations in less time than it takes to
write them down. The backtracking search above is the standard complete-search
solution. An equivalent one-liner uses the library generator (same complexity):

```python
from itertools import permutations

class Solution:
    def permute(self, nums):
        return [list(p) for p in permutations(nums)]
```

**Why it is correct.** Every permutation is a sequence of `n` distinct choices:
which element goes first, which of the remaining goes second, and so on. The
recursion mirrors exactly this decision tree — at depth `d` it branches over
every still-unused element. A root-to-leaf path therefore corresponds to one
complete ordering, and *every* ordering is some root-to-leaf path. The `used[]`
flags guarantee each element is placed exactly once per permutation, and since
inputs are distinct, no two leaves produce the same list.

**Step by step** for `nums = [1, 2, 3]` (first-position choice branches the tree):

- Place `1` first → then `{2,3}`: `[1,2,3]`, `[1,3,2]`
- Place `2` first → then `{1,3}`: `[2,1,3]`, `[2,3,1]`
- Place `3` first → then `{1,2}`: `[3,1,2]`, `[3,2,1]`

Total `3! = 6` permutations.

- **Time:** `O(n! · n)`.
- **Space:** `O(n! · n)` output.

## Key Insights & Edge Cases

- **Copy before appending** (`current[:]`): appending `current` directly stores a
  reference that later `pop()`s will mutate — a classic bug producing many empty
  or wrong lists.
- **Always undo both** the `current.append` and the `used[i] = True` when you
  backtrack, or state leaks into sibling branches.
- **`n = 1`** yields a single permutation `[[1]]`; the base case handles it with
  no special code.
- **Distinct inputs** mean no deduplication is needed. If duplicates were allowed
  (LeetCode 47, "Permutations II"), you would sort and skip equal siblings to
  avoid repeated permutations.
- **Small constraint (`n <= 6` ⇒ at most 720 permutations)** confirms that plain
  complete search is the intended, comfortably-fast solution.
