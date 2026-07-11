# Distinct Echo Substrings

**Difficulty:** Hard

**Source:** LeetCode 1316 — "Distinct Echo Substrings"

## Description

Return the number of **distinct** non-empty substrings of `text` that can be
written as the concatenation of some string with itself (i.e. it can be written
as `a + a` where `a` is some non-empty string).

An "echo" substring has even length `2·L` and its first half equals its second
half.

Rabin–Karp makes this tractable: precompute **prefix hashes** of `text` so the
hash of any substring is available in `O(1)`. Then for each candidate window of
even length `2·L`, compare `hash(left half)` with `hash(right half)` in `O(1)`,
and store the hash of each confirmed echo substring in a set to count only the
**distinct** ones.

## Constraints

- `1 <= text.length <= 2000`
- `text` has only lowercase English letters.

## Examples

### Example 1

```
Input:  text = "abcabcabc"
Output: 3
Explanation:
  The 3 distinct echo substrings are "abcabc" (= "abc" + "abc"),
  "bcabca" (= "bca" + "bca"), and "cabcab" (= "cab" + "cab").
```

### Example 2

```
Input:  text = "leetcodeleetcode"
Output: 2
Explanation:
  The 2 distinct echo substrings are "ee" (= "e" + "e") and
  "leetcodeleetcode" (= "leetcode" + "leetcode").
```

### Example 3

```
Input:  text = "aaa"
Output: 1
Explanation:
  The only distinct echo substring is "aa" (= "a" + "a"). Even though "aa"
  appears at index 0 and index 1, it is counted once because we count
  DISTINCT substrings.
```

## Hint

Precompute **prefix hashes**. For every even-length window, use **Rabin–Karp**
to test in `O(1)` whether the two halves are equal, and insert the substring's
hash into a set to deduplicate.
