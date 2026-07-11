# Coppersmith–Winograd (and Successors)

**Category:** Matrix / Advanced
**One-line:** The theoretical fastest-known family of matrix-multiplication algorithms, obtained by algebraic (tensor / bilinear) reductions rather than by clever index bookkeeping — currently around O(n^2.371).

> This is a *study note*, not a practice problem. The Coppersmith–Winograd (CW) algorithm and its
> successors are **galactic algorithms**: they lower the asymptotic exponent of matrix multiplication
> but only beat simpler methods for astronomically large inputs. You will essentially never *implement*
> CW; you *cite* it when reasoning about the theoretical cost of anything built on matrix multiplication.

---

## 1. The problem and the quantity ω

Multiplying two `n × n` matrices `C = A · B` with the schoolbook (definition) algorithm costs
`Θ(n^3)` scalar multiplications and additions, because each of the `n^2` output entries is a dot
product of length `n`.

The central question of the field is: **what is the smallest exponent achievable?** We define

```
ω = inf { c : two n×n matrices can be multiplied using O(n^c) arithmetic operations }
```

`ω` is called the **exponent of matrix multiplication**. Two facts frame the whole subject:

- **Lower bound:** `ω ≥ 2`. You must read `2n^2` input entries and produce `n^2` outputs, so no
  algorithm can run in less than `Ω(n^2)` time.
- **Conjecture:** most researchers believe `ω = 2` (i.e. `n^{2+ε}` for every `ε > 0`), but this is open.

Every improvement below is a smaller and smaller upper bound on `ω`.

---

## 2. Timeline of upper bounds on ω

| Year | Author(s) | Bound on ω | Idea |
|------|-----------|------------|------|
| —    | Schoolbook | 3.0000 | Definition |
| 1969 | Strassen | 2.8074 | 7 multiplications for a 2×2 block product |
| 1978 | Pan | 2.796 | Trilinear aggregation |
| 1979 | Bini, Capovani, Romani, Lotti | 2.7799 | **Border rank** / approximate bilinear algorithms |
| 1981 | Schönhage | 2.522 | **Asymptotic sum inequality** (partial matrix products) |
| 1981–82 | Coppersmith–Winograd | 2.496 | Combining Schönhage's τ-theorem with a good base tensor |
| 1986 | Strassen | 2.479 | **Laser method** (degenerating tensor powers) |
| 1990 | **Coppersmith–Winograd** | **2.3755** | Laser method applied to the *CW tensor* |
| 2010 | Stothers | 2.3737 | Analyzing the 4th tensor power |
| 2012 | Vassilevska Williams | 2.372873 | General framework, 8th power |
| 2014 | Le Gall | 2.3728639 | 16th/32nd power, tighter optimization |
| 2020 | Alman–Vassilevska Williams | 2.3728596 | Refined "laser" analysis |
| 2022 | Duan–Wu–Zhou | 2.371866 | Fixing "combination loss" in the laser method |
| 2024 | Williams–Xu–Xu–Zhou | 2.371552 | Further asymmetric-loss corrections |

Everything from Coppersmith–Winograd 1990 onward is what people mean by "**Coppersmith–Winograd and
its successors**": the CW tensor plus increasingly sophisticated analysis of its high tensor powers.

> **Naming caution.** "Strassen–Winograd" (a variant of Strassen with 15 additions instead of 18) is a
> *different* result and *is* used in practice. The **Coppersmith–Winograd** algorithm here is the
> `n^2.376` theoretical result and is *not* used in practice.

---

## 3. Warm-up you can actually understand: Strassen (the seed idea)

The whole family grows from one observation of Strassen. To multiply two `2 × 2` matrices you would
naively use 8 scalar multiplications. Strassen does it with **7**. With `A = [[a,b],[c,d]]`,
`B = [[e,f],[g,h]]`:

```
M1 = (a + d)(e + h)
M2 = (c + d) e
M3 = a (f - h)
M4 = d (g - e)
M5 = (a + b) h
M6 = (c - a)(e + f)
M7 = (b - d)(g + h)

C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
```

Applied recursively to `(n/2) × (n/2)` *blocks* (the entries `a…h` become sub-matrices), the number
of multiplications drops from 8 to 7 at each level:

```
T(n) = 7 · T(n/2) + Θ(n^2)   ⇒   T(n) = Θ(n^{log2 7}) = Θ(n^2.807)
```

**Worked numeric check.** `A = [[1,2],[3,4]]`, `B = [[5,6],[7,8]]`.

```
M1 = (1+4)(5+8) = 5·13 = 65
M2 = (3+4)·5    = 7·5  = 35
M3 = 1·(6-8)    = -2
M4 = 4·(7-5)    = 8
M5 = (1+2)·8    = 24
M6 = (3-1)(5+6) = 2·11 = 22
M7 = (2-4)(7+8) = -2·15 = -30

C11 = 65 + 8 - 24 - 30 = 19
C12 = -2 + 24          = 22
C21 = 35 + 8           = 43
C22 = 65 - 35 - 2 + 22 = 50
```

So `C = [[19, 22], [43, 50]]`, which matches the schoolbook product
`[[1·5+2·7, 1·6+2·8], [3·5+4·7, 3·6+4·8]] = [[19,22],[43,50]]`. ✔

The key lesson: **fewer multiplications in a small base case ⇒ a smaller recursion exponent.** CW is
the same idea pushed to its algebraic extreme.

---

## 4. The algebraic framework CW actually uses

Strassen's "7 multiplications" is best understood not combinatorially but as a statement about a
**tensor**. This reframing is what unlocks the deeper results.

### 4.1 Matrix multiplication as a tensor

The bilinear map "multiply an `n×m` by an `m×p` matrix" is encoded by a 3-dimensional tensor
`⟨n, m, p⟩`. A **bilinear algorithm** that computes this map with `r` scalar multiplications
corresponds to writing the tensor as a sum of `r` rank-1 tensors — i.e. the **tensor rank** `R(⟨n,m,p⟩)`
equals the minimum number of *essential multiplications* needed. Then

```
ω = inf { τ : R(⟨n, n, n⟩) = O(n^τ) }.
```

Strassen's discovery is exactly `R(⟨2,2,2⟩) ≤ 7`, giving `ω ≤ log2 7`.

### 4.2 Border rank (Bini)

Approximate algorithms can use *fewer* multiplications if we allow an infinitesimal `ε` and take a
limit. This gives **border rank** `R̲(T) ≤ R(T)`. Crucially, border rank still bounds `ω` (the small
error is cleaned up by extra recursion levels at negligible cost). This lets us use tensors that are
"almost" low-rank.

### 4.3 Schönhage's asymptotic sum inequality (τ-theorem)

If a single algebraic construction simultaneously computes **many disjoint independent matrix
products** `⟨n_i, m_i, p_i⟩` with a small *total* border rank `r`, then

```
Σ_i (n_i · m_i · p_i)^{ω/3}  ≤  r.
```

This "you can pay for several products at once" inequality is the engine that converts a clever base
tensor into a bound on `ω`.

### 4.4 The laser method + the CW tensor

Coppersmith and Winograd chose a specific, easy-to-analyze **base tensor** (the **CW tensor**), which
is *not itself* a matrix-multiplication tensor:

```
CW_q =  Σ_{i=1}^{q} ( x0·yi·zi + xi·y0·zi + xi·yi·z0 )
        + x0·y0·z_{q+1} + x0·y_{q+1}·z0 + x_{q+1}·y0·z0
```

It has very low border rank (`q + 2`). The **laser method** then:

1. Takes a high tensor power `CW_q^{⊗N}`.
2. Partitions its variables into blocks and **zeroes out** (degenerates) carefully chosen blocks so
   that what remains is a large **direct sum of many independent small matrix-multiplication tensors**.
3. Optimizes the block/partition parameters (a constrained optimization / entropy-maximization
   problem) to maximize the "value" extracted.
4. Feeds the resulting disjoint products into Schönhage's asymptotic sum inequality to get a bound on `ω`.

For `CW_q` with the best `q`, step 4 yields `ω < 2.3755`. This is the 1990 result.

### 4.5 What the "successors" changed

Every successor uses the **same CW tensor** but analyzes **higher tensor powers** (2nd, 4th, 8th, …,
32nd) and solves the resulting larger optimization more cleverly:

- **Stothers / Vassilevska Williams / Le Gall** built a general, mechanizable framework for the
  power-`k` analysis, pushing `ω` down toward `2.37286`.
- **Duan–Wu–Zhou (2022)** and **Williams–Xu–Xu–Zhou (2024)** identified inefficiencies ("combination
  loss" / asymmetry loss) in how the laser method combines blocks and corrected them, reaching
  `≈ 2.3719` and `≈ 2.3716`.

There is also a proven **barrier**: the laser method applied to the CW tensor *cannot* by itself
reach `ω = 2` (Ambainis–Filmus–Le Gall, and later works). Getting to `ω = 2` will need a genuinely
new tensor or technique.

---

## 5. Complexity

| Quantity | Value |
|----------|-------|
| Time (arithmetic operations) | `O(n^ω)` with `ω ≈ 2.3716` (best known 2024); CW-1990 gives `≈ 2.3755` |
| Space | Polynomial, `O(n^2)`-ish, **but** with enormous hidden constants |
| Hidden constant factor | Astronomically large — grows with the tensor-power depth used in the analysis |
| Practical crossover `n` | So large it exceeds the number of atoms in the observable universe |

The `O(n^ω)` counts **arithmetic operations**; the constant hidden by the `O(·)` is so gigantic that
these algorithms are purely of theoretical interest.

---

## 6. When to use it (and when not to)

**Reach for it (conceptually) when:**
- You are proving an *asymptotic* bound and want to write "matrix multiplication in `O(n^ω)`".
  Many results in graph theory (all-pairs shortest paths variants, transitive closure, triangle
  detection), computational algebra (matrix inverse, determinant, LU/rank, characteristic polynomial —
  all reduce to matrix multiplication and inherit the `O(n^ω)` exponent), and parsing (Valiant's CFG
  parsing) are stated in terms of `ω`.
- You want the *theoretical* best exponent, not a runnable routine.

**Do NOT use it when:**
- You need to actually multiply matrices. For real workloads use blocked/tiled `O(n^3)` BLAS kernels
  (cache- and SIMD-optimized), and for very large `n` a small number of **Strassen** /
  **Strassen–Winograd** recursion levels on top of a BLAS base case. Those are the only "fast"
  algorithms with small enough constants to win on real hardware.
- Numerical stability matters: border-rank / approximate constructions and deep Strassen recursion can
  degrade accuracy relative to schoolbook multiplication.

---

## 7. Reference pseudocode

### 7.1 Strassen (concrete, implementable — the base idea)

```
function strassen(A, B):            # A, B are n×n, n a power of 2
    if n <= CUTOFF:                 # e.g. 64; fall back to a tuned schoolbook kernel
        return schoolbook(A, B)

    split A into A11, A12, A21, A22 # each (n/2)×(n/2)
    split B into B11, B12, B21, B22

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11,       B12 - B22)
    M4 = strassen(A22,       B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6
    return combine(C11, C12, C21, C22)

# Recurrence: T(n) = 7 T(n/2) + Θ(n^2) = Θ(n^{log2 7}) ≈ Θ(n^2.807)
```

### 7.2 Coppersmith–Winograd family (high-level template — NOT runnable)

```
# This is a *proof procedure*, not a matrix-multiplication routine you run per input.
function bound_omega(q, N):                 # q: CW tensor parameter, N: tensor power
    T   = CW_tensor(q)                      # low-border-rank base tensor
    Tn  = tensor_power(T, N)                # analyze the N-th power
    parts = choose_partition(Tn)            # block the x/y/z variable index sets

    best = +inf
    for assignment in valid_zeroings(parts):        # laser method: degenerate blocks
        products = disjoint_matrix_mults(Tn, assignment)   # a direct sum of ⟨n_i,m_i,p_i⟩
        r        = border_rank(T)^N                        # total (border) rank budget
        # Solve Schönhage's asymptotic sum inequality for the smallest feasible ω:
        #     Σ_i (n_i · m_i · p_i)^(ω/3) ≤ r
        w = solve_for_omega(products, r)               # constrained optimization
        best = min(best, w)
    return best                              # e.g. ≈ 2.3755 for CW-1990's optimal (q, N)
```

The successors keep `CW_tensor`, increase `N`, and make `choose_partition` /
`valid_zeroings` / `solve_for_omega` sharper.

---

## 8. Key takeaways

1. `ω` is the exponent of matrix multiplication; `2 ≤ ω < 2.372`, and `ω = 2` is conjectured but open.
2. Strassen (`ω ≤ log2 7 ≈ 2.807`) is the intuitive seed: fewer multiplications in a fixed-size base
   case ⇒ a smaller recursion exponent — and, viewed algebraically, a lower **tensor rank**.
3. Coppersmith–Winograd reframes everything as **tensor rank / border rank**, then uses the
   **laser method** on the **CW tensor** together with **Schönhage's asymptotic sum inequality** to
   reach `ω ≈ 2.3755` (1990).
4. All "successors" (Stothers, Vassilevska Williams, Le Gall, Alman–Vassilevska Williams,
   Duan–Wu–Zhou, Williams–Xu–Xu–Zhou) analyze **higher powers of the same CW tensor** more cleverly,
   inching `ω` down to `≈ 2.3716` by 2024.
5. These are **galactic algorithms**: correct and asymptotically superior, but with constants so large
   they never win in practice. Use BLAS `O(n^3)` kernels, or Strassen/Strassen–Winograd for large `n`,
   for real computation — and cite `O(n^ω)` only in asymptotic analysis.

---

## 9. Further reading

- Strassen, "Gaussian elimination is not optimal," *Numerische Mathematik* (1969).
- Coppersmith & Winograd, "Matrix multiplication via arithmetic progressions," *J. Symbolic
  Computation* (1990).
- Vassilevska Williams, "Multiplying matrices faster than Coppersmith–Winograd," STOC 2012.
- Le Gall, "Powers of tensors and fast matrix multiplication," ISSAC 2014.
- Alman & Vassilevska Williams, "A refined laser method and faster matrix multiplication," SODA 2021.
- Duan, Wu, Zhou, "Faster matrix multiplication via asymmetric hashing," FOCS 2023.
- Bläser, "Fast Matrix Multiplication" (survey, *Theory of Computing* Graduate Surveys).
