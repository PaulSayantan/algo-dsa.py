# Shortest Unique Substring

**Difficulty:** Hard

Source: Classic (competitive programming; "shortest unique substring" / GeeksforGeeks)

## Description

Given a string `s`, a substring is **unique** if it occurs **exactly once** in
`s`. Find the **shortest** unique substring of `s` and return it.

The whole string `s` always occurs exactly once, so a unique substring always
exists; the interesting part is finding the *shortest* one. If several unique
substrings share the minimum length, returning any one of them is acceptable.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- A substring is a contiguous, non-empty slice of `s`.
- "Occurs exactly once" counts overlapping positions (as usual, each distinct
  start index is a separate occurrence).

## Examples

### Example 1
```
Input:  s = "cabca"
Output: "b"
Explanation: 'b' occurs exactly once (at index 2). Both 'a' and 'c' occur
  twice, so the shortest unique substring has length 1: "b".
```

### Example 2
```
Input:  s = "aabaaab"
Output: "ba"
Explanation: Every single character repeats ('a' 5 times, 'b' twice), so no
  length-1 substring is unique. Among length-2 substrings only "ba" occurs
  exactly once (at index 2), so it is the shortest unique substring.
```

### Example 3
```
Input:  s = "aaaa"
Output: "aaaa"
Explanation: "a" occurs 4 times, "aa" 3 times, "aaa" twice; only the whole
  string "aaaa" occurs exactly once, so it is the shortest unique substring.
```

## Hint

Append a unique terminal and build a **Suffix Tree with Ukkonen's algorithm**.
A substring occurs exactly once **iff** the node/edge point that spells it has
exactly **one leaf** below it. The shortest unique substring ends on a **leaf
edge** whose parent's subtree has more than one leaf; its length is
`(string depth of the parent) + 1`. Scan all such edges and keep the minimum.
