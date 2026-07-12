# First Non-Repeating Word in a Stream

**Difficulty:** Medium

**Source:** Classic — First non-repeating word in a stream of tokens

## Description

You are given `words`, a list of tokens arriving one at a time as a stream. After reading each word, report the first word (in arrival order) that so far appears exactly once, or the empty string `""` when every word seen so far has repeated. Return the list of these per-step answers; its length equals `len(words)`.

## Examples

### Example 1

```
Input:  words = ["the", "day", "is", "the", "day"]
Output: ['the', 'the', 'the', 'day', 'is']
```

**Explanation:** Once `"the"` repeats at step 4 the front advances to `"day"`; when `"day"` repeats at step 5 it advances to `"is"`.

### Example 2

```
Input:  words = ["x", "x"]
Output: ['x', '']
```

**Explanation:** After the second `"x"` no word is unique, so the answer is `""`.

## Hint

Count map keyed by word + a deque of candidate words; enqueue on first sight, pop stale fronts, read the front (empty string if the deque drains).
