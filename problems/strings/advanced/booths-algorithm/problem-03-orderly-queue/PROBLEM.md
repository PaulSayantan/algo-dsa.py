# Orderly Queue

**Difficulty:** Medium–Hard

**Source:** LeetCode 899 "Orderly Queue".

## Description

You are given a string `s` and an integer `k`. In one move you may choose one of the
**first `k` characters** of `s`, remove it, and append it to the **end** of `s`.

Return the **lexicographically smallest** string you can obtain after applying any
number of such moves (including zero).

The catch is a beautiful case split:

- If `k == 1`, the only legal move is to take the very first character and move it to
  the back. Repeatedly doing this generates **exactly the rotations** of `s` and nothing
  else. So the answer is the **lexicographically smallest rotation** of `s`.
- If `k >= 2`, you have enough freedom to perform adjacent transpositions, which lets
  you realize **any permutation** of the characters. The smallest permutation is simply
  the sorted string.

## Constraints

- `1 <= len(s) <= 1000`
- `1 <= k <= len(s)`
- `s` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  s = "cba", k = 1
Output: "acb"
Explanation: With k = 1 only rotations are reachable: "cba" -> "bac" -> "acb" -> "cba".
             The smallest rotation is "acb".
```

### Example 2

```
Input:  s = "baaca", k = 3
Output: "aaabc"
Explanation: With k >= 2 any arrangement is reachable, so the answer is the sorted
             string. Sorting "baaca" gives "aaabc".
```

### Example 3

```
Input:  s = "nlarb", k = 2
Output: "ablnr"
Explanation: k >= 2, so we can reach any permutation; the sorted string is "ablnr".
```

## Hint

Split on `k`. When `k >= 2`, return `"".join(sorted(s))`. When `k == 1`, you need the
**lexicographically smallest rotation**, which **Booth's Algorithm** finds in `O(n)`
(a simple `O(n^2)` rotation scan also passes at `n <= 1000`, but Booth's is the
principled linear-time answer).
