# Maximum XOR of a Subset

**Difficulty:** Medium

**Source:** Classic competitive-programming problem (GeeksforGeeks "Find maximum subset XOR";
appears on Codeforces / CSES as a linear-basis exercise).

## Description

You are given an array `nums` of `n` non-negative integers. Choose any subset of the
elements (the empty subset is allowed and XORs to `0`) and take the XOR of all chosen
elements. Return the **maximum XOR value** achievable over all subsets.

## Constraints

- `1 <= n <= 10^5`
- `0 <= nums[i] < 2^60`

## Examples

### Example 1

```
Input: nums = [1, 2, 3]
Output: 3

Explanation:
All subset XORs: {} -> 0, {1} -> 1, {2} -> 2, {3} -> 3, {1,2} -> 3,
{1,3} -> 2, {2,3} -> 1, {1,2,3} -> 0. The maximum is 3
(achieved by {3} or {1,2}).
```

### Example 2

```
Input: nums = [3, 8, 1]
Output: 11

Explanation:
{3,8} -> 3 XOR 8 = 11 (binary 0011 XOR 1000 = 1011). No other subset beats it:
{3}=3, {8}=8, {1}=1, {3,1}=2, {8,1}=9, {3,8,1}=10. The maximum is 11.
```

### Example 3

```
Input: nums = [0, 0]
Output: 0

Explanation:
Every subset XORs to 0, so the maximum is 0.
```

## Hint

Build a **linear basis over GF(2)** using **Gaussian Elimination**: insert the numbers,
reducing each by the current basis vectors (highest bit first). Then greedily combine
basis vectors from the highest bit down, taking a vector whenever it increases the running
answer.
