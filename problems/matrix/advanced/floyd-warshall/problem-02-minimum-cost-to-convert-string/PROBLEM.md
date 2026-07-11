# Minimum Cost to Convert String I

**Difficulty:** Medium

**Source:** LeetCode 2976

## Description

You are given two strings `source` and `target`, both of length `n` and consisting of **lowercase English letters**. You are also given three arrays `original`, `changed`, and `cost`, all of the same length `z`, where `cost[i]` represents the cost of changing the character `original[i]` to the character `changed[i]`.

You start with the string `source`. In one operation, you can pick a character `x` from the string and change it to the character `y` at a cost of `z` **if** there exists **any** index `j` such that `cost[j] == z`, `original[j] == x`, and `changed[j] == y`.

Return the **minimum cost** to convert the string `source` to the string `target` using any number of operations. If it is impossible to convert `source` to `target`, return `-1`.

Note that there may be **multiple** ways to change a character, so conversions may be chained (e.g. `a → b → c`), and the effective cost of a single-character conversion is the cheapest chain between the two characters.

## Constraints

- `1 <= source.length == target.length <= 10^5`
- `source`, `target` consist of lowercase English letters.
- `1 <= cost.length == original.length == changed.length <= 2000`
- `original[i]`, `changed[i]` are lowercase English letters.
- `1 <= cost[i] <= 10^6`
- `original[i] != changed[i]`

## Examples

### Example 1

```
Input: source = "abcd", target = "acbe",
       original = ["a","b","c","c","e","d"],
       changed  = ["b","c","b","e","b","e"],
       cost     = [2, 5, 5, 1, 2, 20]
Output: 28
```

**Explanation:** Compare `source = "abcd"` with `target = "acbe"` position by position, using the cheapest chain for each character:

- Index 0: `'a' → 'a'`, cost 0 (already equal).
- Index 1: `'b' → 'c'`, direct rule `b→c` = 5.
- Index 2: `'c' → 'b'`, the cheapest chain is `c → e → b` = 1 + 2 = **3** (cheaper than the direct `c→b` = 5).
- Index 3: `'d' → 'e'`, direct rule `d→e` = 20.

Total: `0 + 5 + 3 + 20 = 28`. Note how chaining through `e` beats the direct `c→b` edge — exactly what the all-pairs matrix captures.

### Example 2

```
Input: source = "aaaa", target = "bbbb",
       original = ["a","c"], changed = ["c","b"], cost = [1, 2]
Output: 12
```

**Explanation:** To turn each `'a'` into `'b'` there is no direct rule, but `a → c` costs 1 and `c → b` costs 2, so the chain `a → b` costs 3. Four characters × 3 = `12`.

### Example 3

```
Input: source = "abcd", target = "abce",
       original = ["a"], changed = ["e"], cost = [10000]
Output: -1
```

**Explanation:** The only position that differs is index 3, where we need `'d' → 'e'`. The single rule converts `a → e`, and there is no way to reach `'e'` from `'d'`. Conversion is impossible, so return `-1`.

## Hint

There are only 26 letters. Treat each letter as a node and each conversion rule as a directed weighted edge, then precompute the cheapest cost between every pair of letters with Floyd–Warshall. The per-character answers are just lookups into that 26×26 matrix.
