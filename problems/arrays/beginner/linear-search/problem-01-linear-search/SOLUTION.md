# Solution — Linear Search

## Brute Force

There is essentially only one natural approach for an **unsorted** array, and it is
already linear. A "more brute" variant might compare the target against every element
even after finding a match, but that just wastes work. The natural approach below
stops early on the first match.

- **Time:** O(n)
- **Space:** O(1)

## Optimal Approach (Linear Search)

Walk through the array from index 0 to the last index. At each position `i`, compare
`nums[i]` with `target`. Return `i` on the first match. If the loop finishes with no
match, return `-1`.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, value in enumerate(nums):
            if value == target:
                return i
        return -1
```

**Why it is correct:** The loop maintains the invariant that *every element before
index `i` has already been checked and did not equal the target*. Therefore the first
index we return is guaranteed to be the first occurrence. If we exhaust the array, the
invariant at termination says no element equals the target, so `-1` is correct.

**Step by step** on `nums = [10, 50, 30, 70], target = 30`:

1. `i=0`, `10 != 30` → continue.
2. `i=1`, `50 != 30` → continue.
3. `i=2`, `30 == 30` → return `2`.

- **Time:** O(n) — worst case (target absent or last) touches every element.
- **Space:** O(1) — only a loop index.

## Key Insights & Edge Cases

- Because the array is **unsorted**, binary search is not applicable; O(n) is optimal
  here — you cannot rule out any element without looking at it.
- **First occurrence:** returning on the first match naturally yields the earliest index.
- **Empty-ish inputs:** the constraints guarantee at least one element, but the loop
  still returns `-1` correctly for an empty list.
- **Duplicates:** if the target appears multiple times, the earliest index is returned.
- **Not found:** the trailing `return -1` handles the "absent" case; forgetting it is
  the most common bug.
