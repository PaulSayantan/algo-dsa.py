# Two Sum II — Solution

## Brute Force

Try every pair `(i, j)` with `i < j` and check whether
`numbers[i] + numbers[j] == target`.

```python
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            return [i + 1, j + 1]
```

- **Time:** `O(n^2)` — all pairs.
- **Space:** `O(1)`.

A hash map can bring this to `O(n)` time, but it costs `O(n)` extra space and
**ignores the fact that the array is already sorted**. The problem also demands
constant extra space, ruling out the hash-map trick.

## Optimal Approach (Two Pointers, opposite ends)

Set `left = 0` and `right = len(numbers) - 1` and let `s = numbers[left] +
numbers[right]`.

1. While `left < right`:
   - Compute `s = numbers[left] + numbers[right]`.
   - If `s == target`: return `[left + 1, right + 1]` (convert to 1-indexed).
   - If `s < target`: the sum is too small, and `numbers[left]` is the smallest
     value still available — move `left += 1` to increase the sum.
   - If `s > target`: the sum is too large, so move `right -= 1` to decrease it.

**Why it is correct.** Consider the current pair `(left, right)`.
- If `s < target`, then pairing `numbers[left]` with *any* index `< right`
  produces a value `<= numbers[right]`, so the sum stays `< target`. Thus
  `numbers[left]` can never form the target with anything at or below `right`;
  it is safe to discard `left`.
- Symmetrically, if `s > target`, `numbers[right]` is too big to pair with any
  index `> left`, so we discard `right`.

Each comparison eliminates one element while never discarding a possible
solution, so the unique guaranteed pair is found before the pointers cross.

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
    return []  # unreachable given the problem guarantee
```

- **Time:** `O(n)` — the pointers move a combined total of at most `n` steps.
- **Space:** `O(1)` — two indices only.

## Key Insights & Edge Cases

- **Sortedness is the engine.** Without it, moving a single pointer would not be
  justified. This is why the same trick does *not* apply to the unsorted
  LeetCode 1 "Two Sum".
- **1-indexing:** remember to add 1 to each returned index.
- **Negative numbers** are fine — the monotonic argument depends only on the
  sorted order, not on sign.
- **Duplicates** (e.g. `[3, 3]`, `target = 6`) are handled naturally; the two
  pointers land on the two distinct positions.
- The pointers never reference the **same element twice** because the loop
  condition is `left < right`, strictly.
