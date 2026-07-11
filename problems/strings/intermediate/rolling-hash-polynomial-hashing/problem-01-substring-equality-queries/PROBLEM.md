# Substring Equality Queries

**Difficulty:** Easy

**Source:** Classic competitive-programming exercise (e.g. CSES "String Matching"
family / SPOJ substring-equality drills). The canonical warm-up for polynomial
**prefix hashing**.

## Description

You are given a lowercase string `s` and a list of queries. Each query is a tuple
`(a, b, length)` asking a single yes/no question:

> Is the substring starting at index `a` of the given `length` **equal** to the
> substring starting at index `b` of the same `length`?

Formally, for a query `(a, b, length)` return `True` if
`s[a : a+length] == s[b : b+length]` and `False` otherwise. Return a list of
booleans, one per query, in the same order.

Indices are 0-based and every query is guaranteed to stay within bounds
(`a + length <= len(s)` and `b + length <= len(s)`).

The number of queries can be large, so you should be able to answer each query in
**O(1)** time after an **O(n)** preprocessing step, rather than slicing and
comparing the strings (which is `O(length)` per query).

## Constraints

- `1 <= len(s) <= 2 * 10^5`
- `s` consists of only lowercase English letters.
- `1 <= number of queries <= 2 * 10^5`
- For each query `(a, b, length)`: `0 <= a, b` and `1 <= length`, with
  `a + length <= len(s)` and `b + length <= len(s)`.

## Examples

### Example 1

```
Input:  s = "ababab", queries = [(0, 2, 2), (0, 1, 2), (0, 2, 4)]
Output: [True, False, True]
Explanation:
  (0, 2, 2): s[0:2] = "ab", s[2:4] = "ab"   -> equal      -> True
  (0, 1, 2): s[0:2] = "ab", s[1:3] = "ba"   -> not equal  -> False
  (0, 2, 4): s[0:4] = "abab", s[2:6] = "abab" -> equal    -> True
```

### Example 2

```
Input:  s = "aaaaa", queries = [(0, 1, 3), (2, 2, 2), (0, 3, 2)]
Output: [True, True, True]
Explanation:
  Every substring of "aaaaa" of a given length is "aaa...a", so any two
  same-length windows are equal. A query where a == b is trivially True.
```

## Hint

Precompute **polynomial prefix hashes** of `s` plus the powers of the base. The
hash of any substring `s[l..r]` is then recoverable in constant time from two
prefix hashes, so each equality query becomes a single integer comparison. This
is **Rolling Hash / Polynomial Hashing**.
