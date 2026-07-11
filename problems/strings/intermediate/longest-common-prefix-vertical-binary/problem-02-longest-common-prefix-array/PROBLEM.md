# Longest Common Prefix

**Difficulty:** Easy

Source: LeetCode 14 — "Longest Common Prefix".

## Description

Write a function to find the longest common prefix string amongst an array of strings
`strs`.

If there is no common prefix, return the empty string `""`.

The common prefix is the longest string that is a prefix of **every** string in the
array. A natural way to see it: line the strings up in a grid, one per row, and read
down each **column**. As long as every row has the same character in a column, that
character extends the answer; the first column that disagrees (or the first string that
runs out) ends it.

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

## Examples

### Example 1
- **Input:** `strs = ["flower", "flow", "flight"]`
- **Output:** `"fl"`
- **Explanation:** All three share `f` at column 0 and `l` at column 1. At column 2 the
  characters are `o`, `o`, `i` — a mismatch — so the common prefix is `"fl"`.

### Example 2
- **Input:** `strs = ["dog", "racecar", "car"]`
- **Output:** `""`
- **Explanation:** The strings do not share a common leading character (column 0 is
  `d`, `r`, `c`), so there is no common prefix.

### Example 3
- **Input:** `strs = ["interspecies", "interstellar", "interstate"]`
- **Output:** `"inters"`
- **Explanation:** All three agree on the first 6 characters `inters`; at column 6 they
  read `p`, `t`, `t`, which disagree.

### Example 4
- **Input:** `strs = ["throne"]`
- **Output:** `"throne"`
- **Explanation:** With a single string, the whole string is the common prefix.

## Hint

Use the **Longest Common Prefix (vertical/binary)** technique: scan the columns of the
strings left to right until a column disagrees, or binary search on the prefix length
(bounded by the shortest string) using a "does every string start with this prefix?"
check.
