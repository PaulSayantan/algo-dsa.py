# First Non-Repeating Character in a Stream

**Difficulty:** Medium

**Source:** Classic / GfG — First non-repeating character in a stream

## Description

Process the characters of `stream` one at a time. After reading each character, report the first character that so far appears exactly once, using `'#'` when no such character currently exists. Return the concatenation of these per-step answers as a string (its length equals `len(stream)`).

## Examples

### Example 1

```
Input:  stream = "aabc"
Output: "a#bb"
```

**Explanation:** After 'a':'a'; 'aa':none->'#'; 'aab':'b'; 'aabc':'b'.

## Hint

Deque of candidate chars + a count map; after each char, pop non-unique fronts and read the front.
