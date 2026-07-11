# Strassen's Matrix Multiplication

**Category:** Matrix / Advanced Divide-and-Conquer
**One-line:** Multiply two n x n matrices in O(n^log2(7)) ≈ O(n^2.807) instead of the naive O(n^3), by trading one of the eight recursive multiplications for a batch of cheap additions.

> Why this is a *study* note and not a set of practice problems: Strassen's algorithm is a
> theoretical complexity result / low-level numerical subroutine, not a puzzle that shows up
> as a standalone LeetCode or competitive-programming task. Real "matrix multiply" problems
> expect the plain O(n^3) triple loop (or sparsity tricks); Strassen is almost never the
> *idiomatic* answer to a coding-interview question because of its large constant factor,
> recursion overhead, and numerical stability concerns. It belongs in the same family as the
> Coppersmith-Winograd complexity result — worth understanding deeply, but studied rather
> than drilled. This file therefore gives intuition, a full derivation, a worked numeric
> example, complexity analysis, and reference pseudocode.

---

## 1. The Problem

Given two matrices `A` (dimensions n x n) and `B` (dimensions n x n), compute the product
`C = A · B`, where

```
C[i][j] = sum over k of  A[i][k] * B[k][j]
```

The standard (schoolbook) algorithm computes each of the n^2 entries with a length-n dot
product, giving `n^2 * n = n^3` scalar multiplications and roughly the same number of
additions: **O(n^3)** time.

The natural question (asked by Volker Strassen in 1969) is: can we do asymptotically better?
Strassen showed the answer is yes, breaking the long-standing belief that O(n^3) was optimal.

---

## 2. Intuition

Divide-and-conquer alone does NOT help. If you split each n x n matrix into four (n/2) x (n/2)
blocks:

```
    | A11  A12 |         | B11  B12 |
A = |          |   B =   |          |
    | A21  A22 |         | B21  B22 |
```

then the four blocks of `C` are formed by the standard block formulas:

```
C11 = A11·B11 + A12·B21
C12 = A11·B12 + A12·B22
C21 = A21·B11 + A22·B21
C22 = A21·B12 + A22·B22
```

That is **8 multiplications** of (n/2) x (n/2) matrices plus 4 additions. The recurrence is

```
T(n) = 8·T(n/2) + O(n^2)   =>   T(n) = O(n^log2(8)) = O(n^3)
```

So naive blocking buys nothing — you still get n^3.

**Strassen's key insight:** multiplication is expensive, addition is cheap. By forming 7
cleverly chosen *products* of sums/differences of blocks, we can reconstruct all four `C`
blocks using only **7** recursive multiplications (plus extra additions). Since additions are
O(n^2) and thus asymptotically negligible in the recursion, dropping from 8 to 7
multiplications changes the exponent:

```
T(n) = 7·T(n/2) + O(n^2)   =>   T(n) = O(n^log2(7)) ≈ O(n^2.807)
```

This is the whole trick: pay a bit more in cheap additions to save one costly multiplication
at every level of the recursion.

---

## 3. The Seven Products (the heart of the algorithm)

Split `A` and `B` into four (n/2) x (n/2) blocks as above. Define seven matrix products
(each is a single recursive Strassen multiply of half-size matrices):

```
M1 = (A11 + A22) · (B11 + B22)
M2 = (A21 + A22) ·  B11
M3 =  A11        · (B12 - B22)
M4 =  A22        · (B21 - B11)
M5 = (A11 + A12) ·  B22
M6 = (A21 - A11) · (B11 + B12)
M7 = (A12 - A22) · (B21 + B22)
```

Then reassemble the four blocks of `C` using only additions and subtractions:

```
C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
```

**Why it is correct.** Each `C` block formula is an algebraic identity — expand the `M`
terms and the cross terms cancel exactly, leaving the schoolbook block formulas. For example,
expanding C12:

```
C12 = M3 + M5
    = A11·(B12 - B22) + (A11 + A12)·B22
    = A11·B12 - A11·B22 + A11·B22 + A12·B22
    = A11·B12 + A12·B22        <-- exactly the block formula for C12
```

And C21:

```
C21 = M2 + M4
    = (A21 + A22)·B11 + A22·(B21 - B11)
    = A21·B11 + A22·B11 + A22·B21 - A22·B11
    = A21·B11 + A22·B21        <-- exactly the block formula for C21
```

C11 and C22 verify the same way — the extra `M` products are constructed precisely so their
unwanted cross terms telescope away. Crucially, these identities use only commutative scalar
arithmetic within the additions and DO NOT rely on the blocks commuting under multiplication,
so the scheme is valid for matrix blocks (matrix multiply is not commutative).

---

## 4. Fully Worked Numeric Example (2 x 2)

Let

```
A = | 1  2 |      B = | 5  6 |
    | 3  4 |          | 7  8 |
```

For a 2 x 2 the blocks are scalars: A11=1, A12=2, A21=3, A22=4, B11=5, B12=6, B21=7, B22=8.

Compute the seven products:

```
M1 = (A11 + A22)(B11 + B22) = (1 + 4)(5 + 8) = 5 · 13 = 65
M2 = (A21 + A22) B11        = (3 + 4)·5      = 7 · 5  = 35
M3 =  A11 (B12 - B22)       = 1·(6 - 8)      = 1·(-2) = -2
M4 =  A22 (B21 - B11)       = 4·(7 - 5)      = 4·2    = 8
M5 = (A11 + A12) B22        = (1 + 2)·8      = 3·8    = 24
M6 = (A21 - A11)(B11 + B12) = (3 - 1)(5 + 6) = 2·11   = 22
M7 = (A12 - A22)(B21 + B22) = (2 - 4)(7 + 8) = -2·15  = -30
```

Reassemble:

```
C11 = M1 + M4 - M5 + M7 = 65 + 8 - 24 - 30 = 19
C12 = M3 + M5           = -2 + 24          = 22
C21 = M2 + M4           = 35 + 8           = 43
C22 = M1 - M2 + M3 + M6 = 65 - 35 - 2 + 22 = 50
```

So

```
C = | 19  22 |
    | 43  50 |
```

Check against the schoolbook product:

```
C11 = 1·5 + 2·7 = 5 + 14 = 19   ✓
C12 = 1·6 + 2·8 = 6 + 16 = 22   ✓
C21 = 3·5 + 4·7 = 15 + 28 = 43  ✓
C22 = 3·6 + 4·8 = 18 + 32 = 50  ✓
```

The results agree — Strassen used 7 scalar multiplications and 18 add/subtracts, versus the
schoolbook 8 multiplications and 4 adds. At the 2 x 2 scale Strassen is actually *more* total
work; the asymptotic win only appears once the recursion runs deep on large matrices.

---

## 5. Complexity Analysis

**Time.** With 7 recursive multiplications on half-size inputs plus O(n^2) work for the
additions and combines:

```
T(n) = 7·T(n/2) + O(n^2)
```

By the Master Theorem, compare n^2 with n^log2(7). Since log2(7) ≈ 2.807 > 2, the leaf/recursion
term dominates (Case 1):

```
T(n) = O(n^log2(7)) = O(n^2.807...)
```

Contrast with naive block D&C, `T(n) = 8·T(n/2) + O(n^2) = O(n^3)`. The improvement is purely
from 8 -> 7 in the branching factor: `log2(8) = 3` versus `log2(7) ≈ 2.807`.

**Space.** The recursion depth is O(log n), and each level allocates a handful of temporary
(n/2) x (n/2) matrices for the 10 sums (A/B combinations) and 7 products. Summing the geometric
series of temporaries gives **O(n^2)** auxiliary space (asymptotically the same order as the
output), though the constant is noticeably larger than the naive algorithm, which can run
essentially in-place aside from the output.

**Constant factors.** Strassen has a large hidden constant (many matrix additions per level and
memory allocation/traffic), so it only beats the cache-friendly naive algorithm above a
crossover size — typically somewhere in the n ≈ 100 to 1000+ range depending on hardware and
implementation. Real libraries switch to the naive (or a highly tuned BLAS) kernel for blocks
below the crossover threshold.

---

## 6. Handling Non-Power-of-Two / Non-Square Sizes

The clean recursion assumes n is a power of two so blocks split evenly. Two standard fixes:

1. **Padding:** enlarge each matrix to the next power of two (or next even dimension at each
   level) by appending zero rows/columns, multiply, then crop the result. Padding can up to
   roughly double a dimension, but it keeps the code simple and does not change the asymptotic
   class.
2. **Dynamic peeling:** strip off an odd row/column, handle it separately with a rank-1 update,
   and recurse on the even remainder. More memory-efficient than padding but fiddlier.

For general (non-square) products A(m x k)·B(k x n), pad all three relevant dimensions to a
common power of two, or fall back to blocking that reduces to square sub-multiplies.

---

## 7. When / Why to Use It — and Limitations

**Reach for Strassen when:**
- Matrices are large and dense, well above the implementation's crossover size.
- You are in an exact-arithmetic setting (integers, modular arithmetic, symbolic) where the
  numerical-stability concerns below do not apply.
- You need the asymptotic edge and can afford the extra memory.

**Prefer naive / library BLAS when:**
- Matrices are small or below crossover — naive wins on constant factors and cache behavior.
- Matrices are sparse — use sparse-specific algorithms instead.
- You need top numerical accuracy in floating point.

**Limitations:**
- **Numerical stability:** the subtractions of block sums can cause more floating-point error
  growth than the schoolbook algorithm; Strassen satisfies only a weaker (norm-wise) error
  bound, not the component-wise bound of the naive method.
- **Large constant / memory overhead:** many temporaries and matrix additions per level;
  poor for cache locality unless carefully engineered.
- **Recursion / bookkeeping cost:** handling odd sizes (padding or peeling) adds complexity.
- **Not the theoretical optimum:** later algorithms (Coppersmith-Winograd, and modern
  refinements) push the exponent down toward ~2.37, but those are galactic algorithms with
  astronomically large constants and are not used in practice. The true optimal exponent
  (whether it is 2) is still open. Strassen remains the only sub-cubic method that is actually
  practical and used in real high-performance libraries.

---

## 8. Reference Pseudocode

```
function strassen(A, B):
    n = rows(A)                          # assume A, B are n x n

    # Base case: below the crossover threshold, use the naive multiply.
    if n <= CROSSOVER:                   # e.g. CROSSOVER = 64; minimally, n == 1
        return naive_multiply(A, B)

    # If n is odd, pad A and B with a zero row and column (or peel).
    if n is odd:
        A = pad_to_even(A); B = pad_to_even(B)
        m = n + 1
    else:
        m = n

    # Partition into four m/2 x m/2 blocks.
    (A11, A12, A21, A22) = split(A)
    (B11, B12, B21, B22) = split(B)

    # Seven recursive products.
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11,          sub(B12, B22))
    M4 = strassen(A22,          sub(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(sub(A21, A11), add(B11, B12))
    M7 = strassen(sub(A12, A22), add(B21, B22))

    # Combine into result blocks.
    C11 = add(sub(add(M1, M4), M5), M7)  # M1 + M4 - M5 + M7
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(add(sub(M1, M2), M3), M6)  # M1 - M2 + M3 + M6

    C = combine(C11, C12, C21, C22)
    return crop(C, n)                    # remove any padding
```

Helper `naive_multiply` is the standard triple loop; `add`/`sub` are element-wise O(n^2);
`split`/`combine` slice and stitch quadrants; `pad_to_even`/`crop` manage odd dimensions.

---

## 9. Key Takeaways

- The single idea is: **7 multiplications instead of 8**, purchased with extra cheap additions.
- Correctness comes from algebraic identities among the seven products; no commutativity of
  matrix multiplication is assumed.
- Asymptotics: `O(n^2.807)` time, `O(n^2)` extra space, but a large constant that mandates a
  crossover to the naive kernel for small blocks.
- It is a foundational *result* (first sub-cubic matrix multiply) more than an interview
  problem — understand the derivation and complexity rather than grinding practice problems.
