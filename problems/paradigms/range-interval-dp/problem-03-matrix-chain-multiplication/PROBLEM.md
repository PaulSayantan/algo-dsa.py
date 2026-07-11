# Matrix Chain Multiplication

**Difficulty:** Medium/Hard

**Source:** Classic (CLRS, Chapter 15 — "Matrix-chain multiplication"); also
GeeksforGeeks "Matrix Chain Multiplication".

## Description

You are given a chain of `n` matrices `A[1], A[2], …, A[n]` to be multiplied
together, in that order. Matrix multiplication is **associative**, so the final
product is the same regardless of how you parenthesize it — but the *number of
scalar multiplications* performed can differ dramatically depending on the
parenthesization.

The dimensions are given by an array `dims` of length `n + 1`, where matrix
`A[i]` has dimensions `dims[i-1] x dims[i]`. Multiplying a `p x q` matrix by a
`q x r` matrix costs `p * q * r` scalar multiplications and produces a `p x r`
matrix.

Return the **minimum number of scalar multiplications** needed to compute the
product of the whole chain.

## Constraints

- `2 <= dims.length <= 100` (so there are `dims.length - 1` matrices, at least 1).
- `1 <= dims[i] <= 500`.
- Answer fits in a 64-bit integer.

## Examples

### Example 1
```
Input:  dims = [40, 20, 30, 10, 30]
Output: 26000
Explanation: The matrices are A1(40x20), A2(20x30), A3(30x10), A4(10x30).
The optimal parenthesization is ((A1(A2 A3))A4):
- A2 x A3: 20*30*10 = 6000, result 20x10
- A1 x (A2 A3): 40*20*10 = 8000, result 40x10
- (A1 A2 A3) x A4: 40*10*30 = 12000, result 40x30
Total = 6000 + 8000 + 12000 = 26000, which is the minimum.
```

### Example 2
```
Input:  dims = [10, 20, 30]
Output: 6000
Explanation: Only two matrices, A1(10x20) and A2(20x30). There is a single way
to multiply them: 10*20*30 = 6000.
```

### Example 3
```
Input:  dims = [10, 30, 5, 60]
Output: 4500
Explanation: Matrices A1(10x30), A2(30x5), A3(5x60).
- ((A1 A2) A3): (10*30*5) + (10*5*60) = 1500 + 3000 = 4500.
- (A1 (A2 A3)): (30*5*60) + (10*30*60) = 9000 + 18000 = 27000.
The minimum is 4500.
```

## Hint

Think **Range / Interval DP**: let `dp[i][j]` be the minimum cost to multiply
the sub-chain `A[i..j]`, and try every place `k` to make the **last** (outermost)
multiplication.
