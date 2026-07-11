# Solution — Find All Numbers Disappeared in an Array

## Brute Force

Build a `set` of the array's values, then walk `1..n` collecting any value not in the
set.

- **Time:** O(n).
- **Space:** **O(n)** for the set.

This meets the time bound but violates the O(1)-extra-space follow-up. Cyclic sort
gets us to O(1).

## Optimal Approach (Cyclic Sort)

Values live in `[1, n]`, so value `v` belongs at index `v - 1`. Run the standard
cyclic-sort loop, guarding the swap by **value equality** so that duplicates don't
cause an infinite loop:

1. For pointer `i`, target index `j = nums[i] - 1`.
2. If `nums[i] != nums[j]`, swap it home. (When a duplicate already occupies the
   home slot, this guard is false, so we stop trying and advance.)
3. Otherwise advance `i`.
4. After placing, any index `i` where `nums[i] != i + 1` means the value `i + 1`
   never made it home — it is disappeared.

```python
def findDisappearedNumbers(self, nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return [i + 1 for i in range(n) if nums[i] != i + 1]
```

### Why it is correct

Cyclic sort places each distinct value `v` at index `v - 1`. The only slots that end
up **not** holding their rightful value `i + 1` are exactly those whose owner is
missing — a duplicate had to sit there instead. Collecting `i + 1` for every such
mismatched index yields precisely the disappeared numbers.

### Step-by-step on `[4, 3, 2, 7, 8, 2, 3, 1]`  (n = 8)

```
Start:                         [4, 3, 2, 7, 8, 2, 3, 1]
After the cyclic pass:         [1, 2, 3, 4, 3, 2, 7, 8]
scan mismatches:
  idx4 has 3 != 5  -> 5 disappeared
  idx5 has 2 != 6  -> 6 disappeared
Result: [5, 6]
```

### Complexity

- **Time:** O(n) — at most `n` home-placing swaps plus a linear final scan.
- **Space:** O(1) extra (the output list is not counted).

## Key Insights & Edge Cases

- **Guard the swap by `nums[i] != nums[j]` (values), never by `i != j`.** With
  duplicates present, an index guard would spin forever swapping two equal values;
  the value guard detects "the home is already occupied by an equal value" and moves
  on.
- **Duplicates are what create the disappeared numbers** — every extra copy of some
  value displaces exactly one absent value from its slot.
- Alternative O(1)-space trick: negate `nums[abs(x) - 1]` as a "seen" marker, then
  the still-positive indices are the answer. Cyclic sort is the more transferable
  pattern here.
- Edge cases like `[1, 1]` and `[2, 2]` fall out correctly.
