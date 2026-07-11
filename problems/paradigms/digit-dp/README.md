# Digit DP

**Digit DP** (digit dynamic programming) is a counting/aggregation technique for
answering questions of the form *"how many integers in `[L, R]` satisfy some
property that depends only on the digits?"* — or *"what is the sum / product /
count of some quantity over those integers?"*

Instead of iterating over every number in `[L, R]` (which is impossible when
`R` can be `10^18`), we build numbers **one digit at a time from the most
significant digit** and run a DP over:

- `pos` — the current digit position (0 = most significant).
- `tight` — a boolean "hugging the bound" flag. When `tight` is true, the digits
  chosen so far exactly match the prefix of the upper bound `N`, so the digit we
  place at `pos` is capped by `N[pos]`; when `tight` is false we already went
  strictly below `N`, so any digit `0..9` is allowed.
- **problem-specific state** — e.g. the last digit placed, a bitmask of used
  digits, a running remainder mod `k`, a parity balance, a "has the number
  started yet" (leading-zero) flag, etc.

The universal trick is **prefix counting**: to solve `[L, R]` compute
`f(R) - f(L - 1)`, where `f(x)` counts valid integers in `[0, x]`. Each `f(x)`
is a single digit DP over the ~`D = len(str(x))` digits.

## When to reach for it

- The answer is a *count* or *aggregate* over an interval of integers, and the
  interval is astronomically large (bounds up to `10^9`, `10^18`, or bigger).
- The property is a **local / accumulative function of the digits** (digit sum,
  divisibility, adjacent-digit relations, set of digits used, occurrences of a
  digit, binary-bit patterns, etc.).
- Brute-forcing every integer is infeasible but the number of *digits* is tiny.

## Complexity

For an upper bound with `D` digits, base `B` (10 for decimal, 2 for binary), and
a problem state with `S` reachable values:

- **Time:** `O(D * S * B)` — number of DP states times the branching over the
  next digit.
- **Space:** `O(D * S)` for the memo table (plus recursion depth `O(D)`).

Since `D <= 19` for 64-bit integers and `B <= 10`, digit DP is effectively
constant-time relative to the size of the numbers involved.

## Problems

| # | Problem | Technique flavor | Difficulty |
|---|---------|------------------|------------|
| 1 | [Number of Digit One](problem-01-number-of-digit-one/PROBLEM.md) | Aggregation: total occurrences of a digit | Medium |
| 2 | [Rotated Digits](problem-02-rotated-digits/PROBLEM.md) | Per-digit categorical state + "contains" flag | Medium |
| 3 | [Numbers At Most N Given Digit Set](problem-03-numbers-at-most-n-given-digit-set/PROBLEM.md) | Restricted digit alphabet + shorter lengths | Medium |
| 4 | [Non-negative Integers Without Consecutive Ones](problem-04-integers-without-consecutive-ones/PROBLEM.md) | Binary (base-2) digit DP with adjacency constraint | Hard |
| 5 | [Count Special Integers](problem-05-count-special-integers/PROBLEM.md) | Bitmask of used digits + leading zeros | Hard |
| 6 | [Beautiful Integers in the Range](problem-06-beautiful-integers-in-range/PROBLEM.md) | Two bounds + remainder mod k + parity balance | Hard |
