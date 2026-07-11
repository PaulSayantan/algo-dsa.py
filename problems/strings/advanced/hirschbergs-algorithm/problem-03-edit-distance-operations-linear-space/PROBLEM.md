# Edit Distance — Recover the Operations in Linear Space

**Difficulty:** Medium

**Source:** LeetCode 72 "Edit Distance" (extended: return the operations, in linear space)

## Description

Given two strings `word1` and `word2`, you may transform `word1` into `word2` using three
operations, each costing 1:

- **insert** a character,
- **delete** a character,
- **replace** a character.

Return an optimal (minimum-cost) **edit script**: the ordered list of operations that
turns `word1` into `word2`, together with its total cost (the classic Levenshtein
distance). Represent each step so it can be replayed left-to-right; for example a list of
tuples such as `("match", 'a')`, `("replace", 'a', 'b')`, `("insert", 'b')`,
`("delete", 'a')`.

The constraint that makes this a Hirschberg problem: recover the operations using only
**`O(min(len(word1), len(word2)))` extra space**, without ever storing the full
`O(n·m)` DP / traceback table.

## Constraints

- `0 <= len(word1), len(word2) <= 5000`
- `word1` and `word2` consist of lowercase English letters.
- Extra space (beyond inputs and the output script) must be `O(min(n, m))`.
- Any optimal script is accepted; several may share the minimum cost.

## Examples

### Example 1
```
Input:  word1 = "horse", word2 = "ros"
Output: cost = 3, e.g. operations:
        replace 'h'->'r', match 'o', delete 'r', match 's', delete 'e'
Explanation: horse -> rorse (replace h->r) -> rose (delete r) -> ros (delete e).
Three operations, which is optimal.
```

### Example 2
```
Input:  word1 = "intention", word2 = "execution"
Output: cost = 5
Explanation: One optimal script: delete 'i', replace 'n'->'e', replace 't'->'x',
match 'e', replace 'n'->'c', insert 'u', then match 't', 'i', 'o', 'n'. That is
5 paid operations (1 delete + 3 replaces + 1 insert). No transformation uses fewer.
```

### Example 3
```
Input:  word1 = "", word2 = "abc"
Output: cost = 3, operations: insert 'a', insert 'b', insert 'c'
Explanation: Turning the empty string into "abc" requires exactly 3 insertions.
```

## Hint

The min-cost alignment is monotone through the DP grid, so it must cross the middle row of
`word1` at exactly one column. Find that column with a forward and a backward linear-space
cost pass, split, and recurse — the linear-space traceback of **Hirschberg's Algorithm**,
applied to Levenshtein distance instead of LCS.
