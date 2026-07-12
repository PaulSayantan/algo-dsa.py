# Matching Bracket Indices

**Difficulty:** Easy

**Source:** Classic — matching bracket positions

## Description

Given a **balanced** bracket string `s` containing only the characters `()[]{}`, return an array `match` where `match[i]` is the index of the bracket that pairs with the bracket at position `i`. Each opener is paired with the closer that closes it, and vice versa.

`s` is guaranteed to be a valid (balanced, correctly nested) bracket string.

## Examples

### Example 1

```
Input:  s = "([])"
Output: [3, 2, 1, 0]
```

**Explanation:** Index 0 `(` pairs with index 3 `)`, and index 1 `[` pairs with index 2 `]`.

### Example 2

```
Input:  s = "()[]"
Output: [1, 0, 3, 2]
```

**Explanation:** The two independent pairs `()` and `[]` point at their immediate partners.

## Hint

Push each opener's *index* onto a stack; on a closer, pop the top index and record the two indices as each other's partner.
