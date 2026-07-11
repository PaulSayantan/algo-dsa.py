# Shuffle an Array

**Difficulty:** Medium

**Source:** LeetCode 384 — Shuffle an Array

## Description

Given an integer array `nums`, design an algorithm to randomly shuffle the array. All
permutations of the array should be **equally likely** as a result of the shuffle.

Implement the `Solution` class:

- `Solution(nums)` — Initializes the object with the integer array `nums`.
- `reset()` — Resets the array to its original configuration and returns it.
- `shuffle()` — Returns a random shuffling of the array. Every one of the `n!` possible
  orderings must be equally probable.

Note that `reset()` must always restore the *original* order the object was constructed
with, no matter how many shuffles happened in between. Repeated calls to `shuffle()` should
produce independent random permutations.

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
```

**Explanation:**
- `Solution([1, 2, 3])` builds the object holding the original array `[1, 2, 3]`.
- `shuffle()` returns a random permutation, e.g. `[3, 1, 2]`. Each of the 6 (= 3!) orderings
  is equally likely, so `[3, 1, 2]` is one valid return among many.
- `reset()` returns the original array `[1, 2, 3]`.
- `shuffle()` again returns an independent random permutation, e.g. `[1, 3, 2]`.

### Example 2

```
Input:
["Solution", "shuffle", "shuffle", "reset"]
[[[7]], [], [], []]

Output:
[null, [7], [7], [7]]
```

**Explanation:** With a single element there is only `1! = 1` permutation, so every
`shuffle()` and every `reset()` must return `[7]`.

## Hint

Use **Randomization**: there is a classic in-place linear-time shuffle that, by swapping
each position with a uniformly chosen index from the not-yet-fixed suffix, produces every
permutation with exactly equal probability.
