# Invert a Matrix

**Difficulty:** Easy–Medium

**Source:** Classic linear-algebra exercise (matrix inversion via Gauss–Jordan)

## Description

Given an `n × n` matrix `A`, compute and return its inverse `A⁻¹` — the unique
matrix such that `A · A⁻¹ = A⁻¹ · A = I`, the identity matrix.

If `A` is **singular** (not invertible, i.e. `det(A) = 0`), return `None`.

Entries of the answer are real numbers; values within `1e-6` of the true entry are
accepted.

## Constraints

- `1 ≤ n ≤ 200`
- `A` is `n × n`.
- `-1000 ≤ A[i][j] ≤ 1000`
- Return `None` exactly when `A` has no inverse.

## Examples

### Example 1

```
Input:
  A = [[4, 7],
       [2, 6]]

Output:
  [[ 0.6, -0.7],
   [-0.2,  0.4]]

Explanation:
  det(A) = 4·6 - 7·2 = 10, so A⁻¹ = (1/10)·[[6, -7], [-2, 4]].
  Check: [[4,7],[2,6]] · [[0.6,-0.7],[-0.2,0.4]] = [[1,0],[0,1]].
```

### Example 2

```
Input:
  A = [[1, 2],
       [2, 4]]

Output: None

Explanation:
  det(A) = 1·4 - 2·2 = 0, so row 2 is twice row 1. A is singular
  and has no inverse.
```

### Example 3

```
Input:
  A = [[1, 2, 3],
       [0, 1, 4],
       [5, 6, 0]]

Output:
  [[-24.0,  18.0,   5.0],
   [ 20.0, -15.0,  -4.0],
   [ -5.0,   4.0,   1.0]]

Explanation:
  Reducing [A | I] to RREF turns the left block into I; the right
  block is then A⁻¹. Multiplying A by this matrix yields the 3×3 identity.
```

## Hint

Augment `A` with the identity matrix to form the `n × 2n` block `[A | I]`, then run
**Gauss–Jordan Elimination** until the left block becomes the identity. Whatever
the right block turns into is `A⁻¹`. If at some pivot step no non-zero pivot exists
in the current column, `A` is singular — return `None`.
