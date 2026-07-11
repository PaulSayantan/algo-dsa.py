# String Compression

**Difficulty:** Medium

Source: LeetCode 443 — "String Compression"

## Description

Given an array of characters `chars`, compress it **in place** using a variant of
**Run-Length Encoding**:

- Begin with an empty compressed result at the front of `chars`.
- For each group of consecutive repeating characters:
  - If the group's length is `1`, append just the character.
  - Otherwise, append the character followed by the group length written as
    individual digit characters (e.g. a group of `12` becomes the three
    characters `'c', '1', '2'`).

The compressed result must be written into the beginning of the same `chars`
array. After you finish, return the new length of the compressed array. The
characters beyond that length do not matter.

You must use only **constant extra space** (aside from the input array).

## Constraints

- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, an uppercase English letter, a digit,
  or a symbol.
- The compression must be done in place with `O(1)` auxiliary space.

## Examples

### Example 1
```
Input:  chars = ['a','a','b','b','c','c','c']
Output: 6, chars = ['a','2','b','2','c','3', ...]
Explanation: Groups "aa","bb","ccc" compress to "a2","b2","c3".
             The first 6 characters become a,2,b,2,c,3.
```

### Example 2
```
Input:  chars = ['a']
Output: 1, chars = ['a', ...]
Explanation: The single group "a" has length 1, so no count is written.
```

### Example 3
```
Input:  chars = ['a','b','b','b','b','b','b','b','b','b','b','b','b']
Output: 4, chars = ['a','b','1','2', ...]
Explanation: "a" (length 1) -> "a"; then twelve 'b's -> "b12".
             The count 12 is written as the two digit characters '1' and '2',
             giving a,b,1,2.
```

## Hint

This is **Run-Length Encoding** with two twists: runs of length 1 omit the count,
and you must write the answer back into the same array. Use a read pointer to
scan runs and a separate write pointer to place characters and digit characters.
