# Matrix Exponentiation

## What it is

**Matrix exponentiation** is a technique for evaluating a *linear recurrence* (or, more
generally, any process whose next state is a fixed linear function of the current state)
in `O(k^3 log n)` time, where `k` is the size of the state vector and `n` is the number of
steps you want to advance.

The core idea: if a state vector `v` evolves by a fixed rule `v_{t+1} = M · v_t`, then
after `n` steps `v_n = M^n · v_0`. Computing `M^n` naively takes `n` matrix multiplications,
but using **binary (fast) exponentiation** — the exact same "square-and-multiply" trick used
for integer `pow(a, n)` — we only need `O(log n)` matrix multiplications. Each multiplication
of two `k × k` matrices costs `O(k^3)`, so the whole thing is `O(k^3 log n)`.

## When to reach for it

Reach for matrix exponentiation when **all** of the following hold:

- The quantity you want obeys a **linear recurrence with constant coefficients**, e.g.
  `f(n) = c1·f(n-1) + c2·f(n-2) + ... + ck·f(n-k)`, or the problem is a **count of length-`n`
  walks / sequences** governed by a fixed transition rule.
- `n` is **huge** (up to `10^9`, `10^18`, ...) so an `O(n)` dynamic program is too slow.
- The state size `k` is **small** (typically `k ≤ ~100`), so `k^3` stays manageable.

Typical signals: "count sequences of length `n` where ...", "number of paths of length `k`",
`n <= 10^18`, and "return the answer modulo `10^9 + 7`".

## How it works (in one glance)

1. Express the recurrence as a state vector `v_t` and a **transition matrix** `M` so that
   `v_{t+1} = M · v_t`.
2. Compute `M^n` with fast exponentiation (square-and-multiply).
3. Multiply by the initial state vector `v_0` (or read the entry you need directly out of `M^n`).

All arithmetic is usually done modulo a prime like `10^9 + 7` to avoid overflow.

## Complexity

- **Time:** `O(k^3 log n)` — `log n` matrix products, each `O(k^3)`.
- **Space:** `O(k^2)` for the matrices.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [N-th Fibonacci for Large N](problem-01-nth-fibonacci-large-n/PROBLEM.md) | Compute `F(n)` for `n` up to `10^18` via a 2×2 transition matrix. | Easy |
| 2 | [N-th Tribonacci for Large N](problem-02-nth-tribonacci-large-n/PROBLEM.md) | Extend to a 3-term recurrence with a 3×3 matrix. | Easy |
| 3 | [Number of Walks of Length K in a Graph](problem-03-walks-of-length-k/PROBLEM.md) | Count length-`k` walks between two nodes via powers of the adjacency matrix. | Medium |
| 4 | [Count Vowel Permutation](problem-04-count-vowel-permutation/PROBLEM.md) | Count length-`n` vowel strings under adjacency rules (LeetCode 1220). | Medium |
| 5 | [Knight Dialer](problem-05-knight-dialer/PROBLEM.md) | Count length-`n` knight-move phone numbers (LeetCode 935). | Medium |
| 6 | [Student Attendance Record II](problem-06-student-attendance-record-ii/PROBLEM.md) | Count valid length-`n` attendance records with a 6-state automaton (LeetCode 552). | Hard |
