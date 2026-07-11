# Permutations

**Difficulty:** Medium

**Source:** LeetCode 46 (Permutations)

## Description

Given an array `nums` of **distinct** integers, return *all the possible
permutations*. You can return the answer in any order.

A collection of `n` distinct items has exactly `n!` orderings. The
brute-force / complete-search approach generates every one of them — trying each
element in each position — and collects the results.

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Examples

### Example 1

```
Input:  nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
Explanation: There are 3! = 6 orderings of three distinct numbers, and every one
appears exactly once. (Any ordering of these 6 permutations is accepted.)
```

### Example 2

```
Input:  nums = [0, 1]
Output: [[0,1], [1,0]]
Explanation: Two distinct elements yield 2! = 2 permutations.
```

### Example 3

```
Input:  nums = [1]
Output: [[1]]
Explanation: A single element has exactly 1! = 1 permutation: itself.
```

## Constraints on the answer

- The output contains exactly `n!` permutations.
- Every permutation is a rearrangement using each input element exactly once.
- No two output permutations are equal.

## Hint

Use **Brute Force / Complete Search**: systematically try every element in every
position (e.g. recursive backtracking over the remaining unused elements, or a
library routine that yields all orderings).
