# All Pattern Match Indices (Rabin-Karp)

**Difficulty:** Medium

**Source:** Classic — Rabin-Karp rolling hash

## Description

Given a `text` and a `pattern`, return the sorted list of all 0-based start indices where `pattern` occurs in `text` (occurrences may overlap). Use a polynomial rolling hash with a fixed base and modulus, verifying each hash hit. By convention an empty pattern matches at every position `0..len(text)`.

## Examples

### Example 1

```
Input:  text = "abababab", pattern = "ab"
Output: [0, 2, 4, 6]
```

## Hint

Roll the window hash: whash = ((whash - ord(text[i])*B^(m-1))*B + ord(text[i+m])) % M; verify on a hit.
