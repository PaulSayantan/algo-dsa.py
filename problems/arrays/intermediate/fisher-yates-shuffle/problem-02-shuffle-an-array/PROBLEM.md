# Shuffle an Array

**Difficulty:** Medium

**Source:** LeetCode 384 — Shuffle an Array

## Description

Design a class that, given an integer array `nums`, supports two operations:

- `reset()` — resets the array to its **original** configuration and returns it.
- `shuffle()` — returns a **random shuffling** of the array. All permutations of the
  array should be **equally likely**.

Implement the `Solution` class:

- `Solution(nums)` initializes the object with the integer array `nums`.
- `int[] reset()` resets the array to its original configuration and returns it.
- `int[] shuffle()` returns a random shuffling of the array.

The two methods can be called in any order, any number of times. `shuffle()` must draw
from a **uniform** distribution over all `n!` orderings, and `reset()` must always
restore the exact original array (not the last shuffled state).

## Constraints

- `1 <= nums.length <= 50`
- `-10^6 <= nums[i] <= 10^6`
- All the elements of `nums` are **unique**.
- At most `10^4` calls in total will be made to `reset` and `shuffle`.

## Examples

### Example 1

```
Input:
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]

Output:
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation:
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();  // returns e.g. [3, 1, 2] — must be one of the 6 orderings,
                     // each with probability 1/6.
solution.reset();    // returns [1, 2, 3] — the original array is restored.
solution.shuffle();  // returns e.g. [1, 3, 2] — another uniformly random ordering.
```

### Example 2

```
Input:
["Solution", "reset", "shuffle"]
[[[7]], [], []]

Output:
[null, [7], [7]]

Explanation: A single-element array has only 1! = 1 ordering, so both reset() and
shuffle() always return [7].
```

## Hint

Keep an untouched copy of the original array for `reset()`. For `shuffle()`, apply the
**Fisher–Yates Shuffle** to a working copy: walk from the last index down and swap each
position with a uniformly random earlier-or-equal index. Do not mutate the saved
original.
