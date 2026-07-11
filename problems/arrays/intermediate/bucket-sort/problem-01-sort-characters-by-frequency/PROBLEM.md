# Sort Characters By Frequency

**Difficulty:** Medium

**Source:** LeetCode 451 — Sort Characters By Frequency

## Description

Given a string `s`, sort its characters in **decreasing order based on the
frequency** of the characters. The frequency of a character is the number of
times it appears in the string.

Return the sorted string. If two characters have the same frequency, their
relative order in the answer does not matter, so **any valid answer is
accepted**.

For example, if the character `'e'` appears 3 times and `'r'` appears 2 times,
then all three `'e'`s must come before both `'r'`s in the output.

## Constraints

- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits.
- The maximum possible frequency of any single character is `s.length`.

## Examples

### Example 1

```
Input:  s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once. So 'e' must
appear before both 'r' and 't'. "eetr" is also a valid answer since the two
single-frequency characters can appear in any order.
```

### Example 2

```
Input:  s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "aaaccc" and "cccaaa"
are valid answers. Note that "aacccc" is incorrect: all three of a character's
occurrences must be grouped together.
```

### Example 3

```
Input:  s = "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice, 'A' and 'a' each appear once. "bbaA" is also
valid. Note that 'A' and 'a' are treated as different characters.
```

## Hint

Counts are integers bounded by `len(s)`. Create one bucket per possible
frequency and drop each character into the bucket matching its count, then read
the buckets from highest count to lowest. This is **Bucket Sort** by frequency
and avoids an `O(n log n)` comparison sort.
