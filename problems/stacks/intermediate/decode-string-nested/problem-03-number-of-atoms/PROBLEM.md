# Number of Atoms

**Difficulty:** Medium

**Source:** LeetCode 726 — Number of Atoms

## Description

Given a chemical `formula` (a valid string), return the count of each atom.

An atom name starts with an uppercase letter followed by zero or more lowercase
letters (e.g. `H`, `Mg`). A name may be followed by a count `>= 1` (omitted means
`1`). Parentheses group a sub-formula and may be followed by a multiplier that
scales every atom inside; groups may be nested.

Return the atoms as a single string: names in **sorted (alphabetical) order**,
each followed by its total count only when that count is greater than `1`.

## Examples

### Example 1

```
Input:  formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
```

**Explanation:** `K4` gives `K:4`. Inside the outer group `ON(SO3)2` has `O:1, N:1` plus `(SO3)2 = S:2, O:6`, i.e. `N:1, O:7, S:2`; the outer `*2` yields `N:2, O:14, S:4`. Sorted: `K4N2O14S4`.

## Hint

Push a fresh atom-count map on `(`, and on `)<mult>` pop it and merge every count times `mult` into the map beneath it — the decode-string-nested two-stack idea over counters instead of strings.
