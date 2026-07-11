# Longest Common Prefix of Two Strings

**Difficulty:** Easy

Source: Classic interview warm-up (GeeksforGeeks — "Longest Common Prefix using two
strings"); the primitive underlying LeetCode 14.

## Description

Given two strings `a` and `b`, return their **longest common prefix**: the longest string
`p` such that `p` is a prefix of `a` **and** a prefix of `b`. If they share no leading
character, return the empty string `""`.

Because a prefix cannot be longer than the shorter of the two inputs, you only ever need
to compare up to `min(len(a), len(b))` characters — scanning left to right and stopping
at the first position where the two characters differ (or where one string ends).

## Constraints

- `0 <= len(a), len(b) <= 200`
- `a` and `b` consist of printable ASCII characters (letters, digits, symbols).
- Comparison is case-sensitive (`'A' != 'a'`).

## Examples

### Example 1
- **Input:** `a = "flower"`, `b = "flight"`
- **Output:** `"fl"`
- **Explanation:** Column 0 is `'f' == 'f'`, column 1 is `'l' == 'l'`, column 2 is
  `'o' != 'i'`, so scanning stops and the common prefix is `"fl"`.

### Example 2
- **Input:** `a = "dog"`, `b = "cat"`
- **Output:** `""`
- **Explanation:** The very first characters differ (`'d' != 'c'`), so there is no common
  prefix.

### Example 3
- **Input:** `a = "interspecies"`, `b = "interstellar"`
- **Output:** `"inters"`
- **Explanation:** The strings agree on `i, n, t, e, r, s` (6 characters). At the next
  column `'p' != 't'`, so the answer is `"inters"`.

### Example 4
- **Input:** `a = "abc"`, `b = "abcde"`
- **Output:** `"abc"`
- **Explanation:** All of `"abc"` matches; `a` then ends, capping the prefix at its own
  length.

## Hint

Use the **Longest Common Prefix (vertical/binary)** technique: compare the two strings
column by column up to their shorter length, or binary search on the prefix length using
a "do the first `L` characters match?" check.
