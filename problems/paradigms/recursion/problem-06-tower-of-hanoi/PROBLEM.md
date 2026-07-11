# Tower of Hanoi

**Difficulty:** Medium

**Source:** Classic problem (Édouard Lucas, 1883; CLRS / competitive programming staple)

## Description

You are given three pegs, labeled `'A'` (source), `'B'` (auxiliary), and `'C'`
(target), and `n` disks of distinct sizes stacked on peg `A` in decreasing size from
bottom to top (largest on the bottom). Move the entire stack from peg `A` to peg `C`,
obeying these rules:

1. Only **one disk** may be moved at a time.
2. Each move takes the **top** disk off one peg and places it on top of another peg.
3. A disk may **never** be placed on top of a **smaller** disk.

Return the sequence of moves as a list of `(from_peg, to_peg)` pairs, in the order they
should be performed.

This is the archetypal recursion problem. The insight: to move `n` disks from `A` to
`C`, first move the top `n - 1` disks out of the way onto `B`, move the largest disk
directly to `C`, then move the `n - 1` disks from `B` onto `C`. Each of those `n - 1`
moves is *the same problem, one disk smaller*.

## Constraints

- `1 <= n <= 20`
- The pegs are labeled with the strings `'A'`, `'B'`, and `'C'`.
- The number of moves in an optimal solution is exactly `2^n - 1`.

## Examples

### Example 1

```
Input:  n = 1
Output: [('A', 'C')]
```

Explanation: With a single disk, move it directly from the source `A` to the target
`C`. That is `2^1 - 1 = 1` move.

### Example 2

```
Input:  n = 2
Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

Explanation: Move the small disk `A -> B` to expose the large disk, move the large disk
`A -> C`, then move the small disk `B -> C` on top of it. That is `2^2 - 1 = 3` moves.

### Example 3

```
Input:  n = 3
Output: [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
```

Explanation: Move the top 2 disks from `A` to `B` (using `C` as auxiliary), move the
largest disk `A -> C`, then move the 2 disks from `B` to `C` (using `A` as auxiliary).
That is `2^3 - 1 = 7` moves.

## Hint

Use **Recursion**: to move `n` disks from `source` to `target` using `auxiliary`,
recursively move `n - 1` disks from `source` to `auxiliary`, record the single move of
disk `n` from `source` to `target`, then recursively move `n - 1` disks from
`auxiliary` to `target`. The base case is `n == 0` (nothing to move).
