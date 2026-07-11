# Glass Beads

**Difficulty:** Easy–Medium

**Source:** UVa 719 / POJ 1509 "Glass Beads" (classic least-rotation index problem).

## Description

A necklace is made of colored glass beads strung on a **circular** wire, so the
necklace is really a *cyclic* string. To sell it, the shopkeeper cuts the wire between
two adjacent beads and lays the beads out in a line, reading them off in a fixed
direction. Cutting at a different gap produces a **rotation** of the same cyclic string.

The shop wants a canonical way to name each necklace: the name is the
**lexicographically smallest** string obtainable by cutting the necklace at some gap.
Your job is not to print the name itself, but to report **where to cut** — that is, the
**1-based starting position** (in the original string `s`) of the lexicographically
smallest rotation.

If more than one starting position yields that same smallest string (which happens when
the necklace is periodic, e.g. `"abab"`), report the **smallest** such position.

## Constraints

- `1 <= len(s) <= 10^6`
- `s` consists of lowercase English letters `a`–`z` (`'a'` is the "lowest" color).
- Return a 1-based index in the range `[1, len(s)]`.

## Examples

### Example 1

```
Input:  s = "helloworld"
Output: 10
Explanation: Cutting before the last character 'd' (position 10, 1-based) gives
             "dhelloworl", which is the lexicographically smallest of all 10
             rotations (it is the only rotation starting with 'd', and no rotation
             starts with a letter smaller than 'd').
```

### Example 2

```
Input:  s = "abab"
Output: 1
Explanation: The rotations are "abab" (pos 1), "baba" (pos 2), "abab" (pos 3),
             "baba" (pos 4). The smallest string "abab" occurs at positions 1 and 3;
             we report the smaller position, 1.
```

### Example 3

```
Input:  s = "dontcallmebfu"
Output: 6
Explanation: Cutting before the 6th character gives "allmebfudontc", which starts
             with 'a' — the only rotation beginning with 'a' — so it is the smallest.
```

## Hint

This is the canonical "least rotation index" query. Run **Booth's Algorithm** on `s`
to get the 0-based start index of the smallest rotation in `O(n)`, then add 1. Booth's
naturally returns the smallest index when ties occur.
