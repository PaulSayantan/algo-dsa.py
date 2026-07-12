# Count Pattern Occurrences

**Difficulty:** Medium

**Source:** Classic — Rabin-Karp occurrence count

## Description

Given a `text` and a `pattern`, return how many times `pattern` occurs in `text`, counting overlapping occurrences. Reuse the rolling-hash match scan and return the number of verified matches.

## Examples

### Example 1

```
Input:  text = "mississippi", pattern = "iss"
Output: 2
```

## Hint

Count the verified hash hits produced by the rolling-hash scan.
