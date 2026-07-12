# Longest Repeated Substring Length

**Difficulty:** Hard

**Source:** Classic — longest repeated substring

## Description

Given a string `s`, return the length of the longest substring that appears at least twice in `s` (occurrences may overlap), or `0` if no character repeats. This is the classic 'longest repeated substring' problem solved by binary search over the length plus rolling hashing.

## Examples

### Example 1

```
Input:  s = "mississippi"
Output: 4
```

**Explanation:** "issi" repeats

## Hint

Identical to the longest-duplicate-substring length via binary search + rolling hash.
