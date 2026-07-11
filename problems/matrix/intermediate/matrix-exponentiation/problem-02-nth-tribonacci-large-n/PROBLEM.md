# N-th Tribonacci Number for Very Large N

**Difficulty:** Easy

Generalization of LeetCode 1137 "N-th Tribonacci Number" to enormous `n`.

## Description

The Tribonacci sequence `T` is defined by

```
T(0) = 0
T(1) = 1
T(2) = 1
T(n) = T(n - 1) + T(n - 2) + T(n - 3)   for n >= 3
```

Given an integer `n`, return `T(n)` **modulo `10^9 + 7`**.

As with Fibonacci, `n` can be extremely large (up to `10^18`), so an `O(n)` scan is not
acceptable. Each new term now depends on the **three** previous terms rather than two.

## Constraints

- `0 <= n <= 10^18`
- Return the answer modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  n = 4
Output: 4
Explanation: T(0)=0, T(1)=1, T(2)=1, T(3)=0+1+1=2, T(4)=1+1+2=4.
```

### Example 2

```
Input:  n = 10
Output: 149
Explanation: The sequence is 0,1,1,2,4,7,13,24,44,81,149, so T(10)=149.
```

### Example 3

```
Input:  n = 25
Output: 1389537
Explanation: Following the recurrence up to index 25 gives T(25)=1389537
(which is already below the modulus, so no reduction is needed).
```

## Hint

The triple `(T(n), T(n-1), T(n-2))` maps linearly to `(T(n+1), T(n), T(n-1))`. Encode that as
a fixed 3×3 transition matrix and apply **Matrix Exponentiation** to jump `n` steps in
`O(log n)` matrix multiplications.
