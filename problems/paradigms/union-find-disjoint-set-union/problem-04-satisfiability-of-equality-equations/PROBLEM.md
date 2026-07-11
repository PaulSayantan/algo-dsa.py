# Satisfiability of Equality Equations

**Difficulty:** Medium

**Source:** LeetCode 990 — Satisfiability of Equality Equations

## Description

You are given an array of strings `equations` that represent relationships between variables
where each string `equations[i]` is of length `4` and takes one of two different forms:
`"xi==yi"` or `"xi!=yi"`. Here, `xi` and `yi` are lowercase letters (not necessarily different)
that represent one-letter variable names.

Return `true` if it is possible to assign integers to variable names so as to satisfy **all** the
given equations, or `false` otherwise.

## Constraints

- `1 <= equations.length <= 500`
- `equations[i].length == 4`
- `equations[i][0]` is a lowercase letter.
- `equations[i][1]` is either `'='` or `'!'`.
- `equations[i][2]` is `'='`.
- `equations[i][3]` is a lowercase letter.

## Examples

### Example 1

```
Input:  equations = ["a==b","b!=a"]
Output: false
```

Explanation: The first equation forces `a == b`, but the second demands `a != b`. No assignment
of integers can satisfy both, so the system is unsatisfiable.

### Example 2

```
Input:  equations = ["b==a","a==b"]
Output: true
```

Explanation: Both equations say the same thing, `a == b`. Assigning `a = b = 1` (any common
value) satisfies them, so the answer is `true`.

### Example 3

```
Input:  equations = ["a==b","b==c","a!=c"]
Output: false
```

Explanation: `a == b` and `b == c` together force `a == c` by transitivity, which directly
contradicts `a != c`. The system is unsatisfiable.

### Example 4

```
Input:  equations = ["c==c","b==d","x!=z"]
Output: true
```

Explanation: `c == c` is trivially true, `b == d` merges `b` and `d`, and `x != z` is fine
because `x` and `z` are never forced equal. A valid assignment exists, so the answer is `true`.

## Hint

Union all the `==` pairs first, then verify that no `!=` pair shares a root. Grouping equal
variables into equivalence classes is exactly what **Union-Find (Disjoint Set Union)** does.
