# Solution - Two Sum II

## Brute Force

Try every pair `(i, j)` with `i < j` and check whether
`numbers[i] + numbers[j] == target`.

```python
for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
```

- **Time:** `O(n^2)` — every pair is inspected.
- **Space:** `O(1)`.

This ignores the fact that the array is sorted, which is the whole point.

## Optimal Approach (Two Pointers)

Place `left` at the first element and `right` at the last element. Look at the
current sum `s = numbers[left] + numbers[right]`:

- If `s == target`, we found the pair; return `[left + 1, right + 1]`.
- If `s < target`, the sum is too small. Since the array is sorted, the only way
  to **increase** the sum is to move `left` rightward (to a larger value).
  Moving `right` left would only shrink the sum. So do `left += 1`.
- If `s > target`, the sum is too big. The only way to **decrease** it is to move
  `right` leftward (to a smaller value). So do `right -= 1`.

### Why it is correct

Consider the pair `(left, right)`. Suppose `s < target`. Every pair that uses
`left` together with some index `< right` has a sum `<= s < target` (because the
array is sorted, so those partners are `<= numbers[right]`). Therefore `left`
can never form a valid pair with anything to the left of `right`; the only
candidates involving `left` have already been ruled out, so we may safely
discard `left` by incrementing it. A symmetric argument justifies decrementing
`right` when `s > target`. No valid pair is ever skipped, and because the
problem guarantees a unique solution, the pointers must meet it.

### Step-by-step (numbers = [2, 7, 11, 15], target = 9)

| left | right | numbers[left] | numbers[right] | sum | action           |
|------|-------|---------------|----------------|-----|------------------|
| 0    | 3     | 2             | 15             | 17  | 17 > 9 → right-- |
| 0    | 2     | 2             | 11             | 13  | 13 > 9 → right-- |
| 0    | 1     | 2             | 7              | 9   | 9 == 9 → return  |

Return `[0 + 1, 1 + 1] = [1, 2]`.

### Reference implementation

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        if s < target:
            left += 1
        else:
            right -= 1
    return []  # unreachable given the problem guarantees a solution
```

- **Time:** `O(n)` — each iteration moves at least one pointer, and the pointers
  can move a combined total of at most `n` steps before they meet.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Sorted input is essential.** The comparison-driven pointer moves only make
  sense because larger indices hold larger-or-equal values.
- **Convert to 1-indexed only at the end** (`left + 1`, `right + 1`) to avoid
  off-by-one confusion inside the loop.
- **Negative numbers** are fine; sortedness, not sign, is what matters
  (Example 3).
- **Loop guard `left < right`** prevents reusing the same element and guarantees
  termination.
- If the guarantee of a unique solution were dropped, the same scan would find
  *a* valid pair if one exists and otherwise exit the loop empty.
