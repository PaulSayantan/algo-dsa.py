# Longest Repeated Substring

**Difficulty:** Medium-Hard

**Source:** Classic (CLRS/competitive-programming staple; e.g. SPOJ, "Longest Repeated Substring").

## Description

Given a string `S`, find the **longest substring that appears at least twice** in
`S`. The two occurrences are allowed to **overlap**. If several substrings share
the maximum length, return any one of them (the examples pick a specific valid
answer). If no character repeats, return the empty string `""`.

**Key observation.** A repeated substring is a common prefix of two different
suffixes of `S`. If we sort all suffixes (suffix array) and compute the
**LCP array** (longest common prefix between each pair of *adjacent* sorted
suffixes), then the answer's length is exactly `max(LCP)`, and the substring is
the corresponding shared prefix. Adjacent suffixes in sorted order are the ones
sharing the longest prefixes, so the global maximum repeated length must appear
between some adjacent pair.

## Constraints

- `1 <= len(S) <= 2 * 10^5`
- `S` consists of lowercase English letters (method generalizes to any alphabet).
- Overlapping occurrences are permitted.

## Examples

### Example 1
```
Input:  S = "banana"
Output: "ana"
Explanation: "ana" occurs at index 1 and index 3 (overlapping). No repeated
substring is longer than 3. Sorted suffixes ..., "ana"(3), "anana"(1), ... share
the prefix "ana", giving LCP = 3, the maximum.
```

### Example 2
```
Input:  S = "abcpqrabcxyz"
Output: "abc"
Explanation: "abc" appears at index 0 and index 6. It is the longest repeated
block; nothing of length 4 repeats.
```

### Example 3
```
Input:  S = "abcd"
Output: ""
Explanation: Every character is distinct, so no substring repeats; the longest
repeated substring is empty.
```

## Hint

Use **Suffix Array (prefix-doubling / DC3)** together with the **LCP array**
(Kasai's algorithm). The answer length is `max(LCP)`; the substring is the shared
prefix of the adjacent suffix pair achieving that maximum.
