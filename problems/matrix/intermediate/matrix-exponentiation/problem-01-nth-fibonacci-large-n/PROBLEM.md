# N-th Fibonacci Number for Very Large N

**Difficulty:** Easy

Classic problem (see also LeetCode 509 "Fibonacci Number", generalized to enormous `n`).

## Description

The Fibonacci sequence is defined by

```
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)   for n >= 2
```

Given an integer `n`, return `F(n)` **modulo `10^9 + 7`**.

The twist that makes this interesting: `n` can be as large as `10^18`. A straightforward
`O(n)` loop that adds the two previous terms is far too slow at that scale, so you must
advance the recurrence in a way that costs only `O(log n)` work.

## Constraints

- `0 <= n <= 10^18`
- Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  n = 2
Output: 1
Explanation: F(0)=0, F(1)=1, F(2)=F(1)+F(0)=1.
```

### Example 2

```
Input:  n = 10
Output: 55
Explanation: The sequence is 0,1,1,2,3,5,8,13,21,34,55, so F(10)=55.
```

### Example 3

```
Input:  n = 50
Output: 586268941
Explanation: F(50) = 12586269025, and 12586269025 mod (10^9 + 7) = 586268941.
```

## Hint

The pair `(F(n), F(n-1))` transforms linearly into `(F(n+1), F(n))`. Encode that step as a
fixed 2×2 matrix and use **Matrix Exponentiation** (fast power) to apply it `n` times in
`O(log n)` matrix multiplications.
