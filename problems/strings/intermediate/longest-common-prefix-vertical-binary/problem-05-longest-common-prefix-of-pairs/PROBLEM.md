# Find the Length of the Longest Common Prefix

**Difficulty:** Medium

Source: LeetCode 3043 — "Find the Length of the Longest Common Prefix".

## Description

You are given two arrays of **positive integers** `arr1` and `arr2`.

A **prefix** of a positive integer is an integer formed by one or more of its digits,
starting from its **leftmost** digit. For example, `123` is a prefix of `12345`, but
`234` is not.

A **common prefix** of two integers `a` and `b` is an integer `c` that is a prefix of
both `a` and `b`. For instance, `5655359` and `56554` have common prefixes `565` and
`5655`, but `1223` and `43456` have no common prefix.

Consider every pair `(x, y)` where `x` comes from `arr1` and `y` comes from `arr2`.
Return the length (in digits) of the **longest common prefix** among all such pairs. If
no pair shares a common prefix, return `0`.

Equivalently: write each integer as its decimal digit string, and find the maximum, over
all cross pairs, of the length of the longest common prefix of the two digit strings.

## Constraints

- `1 <= arr1.length, arr2.length <= 5 * 10^4`
- `1 <= arr1[i], arr2[i] <= 10^8`

## Examples

### Example 1
- **Input:** `arr1 = [1, 10, 100]`, `arr2 = [1000]`
- **Output:** `3`
- **Explanation:** Comparing each `x` against `1000` (digit string `"1000"`): `1` shares
  `"1"` (len 1), `10` shares `"10"` (len 2), `100` shares `"100"` (len 3). The longest is
  3, from the pair `(100, 1000)`.

### Example 2
- **Input:** `arr1 = [1, 2, 3]`, `arr2 = [4, 4, 4]`
- **Output:** `0`
- **Explanation:** Every pair disagrees on the first digit, so no pair has a common
  prefix and the answer is 0.

### Example 3
- **Input:** `arr1 = [12, 34]`, `arr2 = [123, 340]`
- **Output:** `2`
- **Explanation:** Pair `(12, 123)` shares `"12"` (len 2) and pair `(34, 340)` shares
  `"34"` (len 2). The cross pairs `(12, 340)` and `(34, 123)` differ at the first digit
  (len 0). The maximum is 2.

### Example 4
- **Input:** `arr1 = [5]`, `arr2 = [59, 512]`
- **Output:** `1`
- **Explanation:** `(5, 59)` and `(5, 512)` each share the single digit `"5"`, so the
  longest common prefix length is 1.

## Hint

Use the **Longest Common Prefix (vertical/binary)** technique on the decimal digit
strings. The per-pair primitive is a column scan of two digit strings; to avoid checking
all pairs, store every prefix of the `arr1` numbers (a prefix set / trie of digit
strings) and, for each `arr2` number, scan its digit prefixes against that set.
