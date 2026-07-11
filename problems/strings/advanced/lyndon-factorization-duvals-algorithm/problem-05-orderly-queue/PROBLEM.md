# Orderly Queue

**Difficulty:** Hard

**Source:** LeetCode 899 — "Orderly Queue"

## Description

You are given a string `s` and an integer `k`. In one move you may choose one of the
**first `k`** characters of `s`, remove it, and append it to the **end** of the string.

Return the lexicographically **smallest** string you can obtain after applying any number
of such moves.

Two regimes:

- If `k == 1`, you can only ever move the very first character to the back. The set of
  reachable strings is exactly the set of **rotations** of `s`, so the answer is the
  lexicographically smallest rotation.
- If `k >= 2`, you can effectively perform adjacent swaps and reach **any permutation** of
  the characters, so the answer is just the sorted string.

## Constraints

- `1 <= s.length <= 1000`
- `1 <= k <= s.length`
- `s` consists of lowercase English letters.

## Examples

### Example 1
```
Input:  s = "cba", k = 1
Output: "acb"
Explanation: k = 1, so only rotations are reachable: "cba" -> "bac" -> "acb" -> "cba".
             The smallest rotation is "acb".
```

### Example 2
```
Input:  s = "baaca", k = 3
Output: "aaabc"
Explanation: k = 3 >= 2, so any permutation is reachable; the smallest is the sorted
             string "aaabc".
```

### Example 3
```
Input:  s = "dcba", k = 1
Output: "adcb"
Explanation: k = 1. Rotations: "dcba", "cbad", "badc", "adcb". The smallest is "adcb".
```

## Hint

The `k == 1` case is exactly "smallest rotation", which **Lyndon Factorization (Duval's
algorithm)** solves in `O(n)` by scanning `s + s`. For `k >= 2` just return
`"".join(sorted(s))`.
