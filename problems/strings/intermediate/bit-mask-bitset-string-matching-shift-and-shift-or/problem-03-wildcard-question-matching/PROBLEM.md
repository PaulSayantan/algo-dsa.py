# Wildcard `?` Pattern Search

**Difficulty:** Medium

**Source:** Classic bit-parallel pattern matching (the `?` wildcard extension of
Shift-And; related to glob matching and LeetCode 44's single-character wildcard).

## Description

Given a `text` and a `pattern` that may contain the wildcard character `?`, return
all start indices where `pattern` matches a substring of `text`. The wildcard `?`
matches **any single character**. Every non-`?` character must match exactly, and
the pattern occupies a contiguous window of length `len(pattern)` (there is no `*`
multi-character wildcard in this problem).

This is a substring search (the pattern can match anywhere inside `text`), not a
full-string match. Occurrences may overlap and must be returned in increasing order.

The elegance of the bit-parallel approach: a `?` at pattern position `j` should
match *whatever* character appears there, so you simply treat position `j` as
"always matching" by OR-ing its bit into every character's mask.

## Constraints

- `1 <= len(text) <= 10^5`
- `1 <= len(pattern) <= len(text)`
- `text` consists of printable ASCII characters (no `?`).
- `pattern` consists of printable ASCII characters and the wildcard `?`.

## Examples

### Example 1
```
Input:  text = "abcabd", pattern = "a?c"
Output: [0]
Explanation: At index 0 the window "abc" matches "a?c": 'a'=='a', '?' matches 'b',
             'c'=='c'. No other window of length 3 matches (e.g. "bca", "cab", "abd" fail).
```

### Example 2
```
Input:  text = "mississippi", pattern = "is?i"
Output: [1, 4]
Explanation: Window "issi" at index 1 matches "is?i" ('?' -> 's'); window "issi" at
             index 4 matches as well. "isip"/"ippi" etc. do not.
```

### Example 3
```
Input:  text = "xyzxyz", pattern = "?y?"
Output: [0, 3]
Explanation: "xyz" at index 0 matches "?y?" (the middle 'y' must match, the ends are
             free), and "xyz" at index 3 matches for the same reason.
```

## Hint

Use **Bit-mask / Bitset String Matching (Shift-And / Shift-Or)**. Build the normal
character masks `B[c]`, plus a wildcard mask `Q` holding the bit positions of every
`?`. Then run `D = ((D << 1) | 1) & (B.get(c, 0) | Q)` — OR-ing `Q` in makes the
wildcard positions match any text character, and the rest is ordinary Shift-And.
