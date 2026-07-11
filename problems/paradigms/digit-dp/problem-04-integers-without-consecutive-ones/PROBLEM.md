# Non-negative Integers Without Consecutive Ones

**Difficulty:** Hard

**Source:** LeetCode 600 — Non-negative Integers without Consecutive Ones

## Description

Given a positive integer `n`, return the count of integers in the **inclusive**
range `[0, n]` whose **binary representations do NOT contain two adjacent `1`s**.

In other words, count the integers `x` with `0 <= x <= n` such that the binary
form of `x` has no position `i` where both bit `i` and bit `i + 1` are `1`.

## Constraints

- `1 <= n <= 10^9`

## Examples

### Example 1

```
Input:  n = 5
Output: 5
Explanation: Below are the binary representations of 0..5 and whether they are
             valid (no two consecutive 1s):
             0 :  0    valid
             1 :  1    valid
             2 : 10    valid
             3 : 11    INVALID (two adjacent 1s)
             4 : 100   valid
             5 : 101   valid
             Valid numbers: 0, 1, 2, 4, 5  ->  count = 5.
```

### Example 2

```
Input:  n = 1
Output: 2
Explanation: 0 (binary 0) and 1 (binary 1) both have no consecutive ones.
             Count = 2.
```

### Example 3

```
Input:  n = 2
Output: 3
Explanation: 0 (0), 1 (1), and 2 (10) are all valid. 
             Count = 3.
```

## Hint

The constraint is about **adjacent bits**, so process the number in **base 2**
rather than base 10. This is a binary **Digit DP**: scan bits from the most
significant, carry the previous bit and a *tight* flag, and forbid placing a `1`
right after another `1`.
