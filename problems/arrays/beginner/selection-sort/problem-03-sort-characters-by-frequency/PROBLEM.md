# Sort Characters By Frequency

**Difficulty:** Medium

**Source:** LeetCode 451 — "Sort Characters By Frequency".

## Description

Given a string `s`, sort it in **decreasing order based on the frequency** of the characters. The
frequency of a character is the number of times it appears in the string.

Return the reordered string. If two characters have the same frequency, they may appear in **any**
relative order — multiple correct answers can exist.

The natural approach: count how many times each distinct character appears, then order the distinct
characters by that count using **Selection Sort** (selecting the most-frequent remaining character
each pass), and finally emit each character repeated by its count.

## Constraints

- `1 <= s.length <= 5 * 10^5`
- `s` consists of uppercase and lowercase English letters and digits.

## Examples

### Example 1

```
Input:  s = "tree"
Output: "eert"
```

**Explanation:** `'e'` appears twice while `'r'` and `'t'` each appear once, so `'e'` must come
first. `"eetr"` is also accepted since `'r'` and `'t'` tie in frequency.

### Example 2

```
Input:  s = "cccaaa"
Output: "aaaccc"
```

**Explanation:** Both `'a'` and `'c'` appear three times, so any order of their blocks is valid;
`"cccaaa"` would also be accepted. Characters must be grouped together.

### Example 3

```
Input:  s = "Aabb"
Output: "bbAa"
```

**Explanation:** `'b'` appears twice, and `'A'` and `'a'` each appear once. Uppercase `'A'` and
lowercase `'a'` are treated as **different** characters. `"bbaA"` is also accepted.

## Hint

Build a frequency map, then run **Selection Sort** over the list of `(char, count)` pairs, choosing
the pair with the largest `count` each pass. Emit `char * count` for each pair in that selected
order.
