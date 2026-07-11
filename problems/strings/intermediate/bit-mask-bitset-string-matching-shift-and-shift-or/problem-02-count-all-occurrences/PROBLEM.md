# Count All Occurrences of a Pattern

**Difficulty:** Easy

**Source:** Classic string-matching exercise (generalizes LeetCode 28; "find all
occurrences" is a staple of GeeksforGeeks / competitive programming).

## Description

Given a `text` and a `pattern`, return a list of **all** start indices where
`pattern` occurs in `text`, in increasing order. Occurrences may **overlap**.

For example, in `"aaaaa"` the pattern `"aa"` occurs at indices `0, 1, 2, 3`
(overlapping is allowed). If the pattern never occurs, return an empty list.

Solve this by scanning the text once with a **bit-parallel** matching automaton:
maintain a state word so that whenever the highest pattern bit becomes set, you
record the corresponding start index — without restarting the scan.

## Constraints

- `1 <= len(text) <= 10^5`
- `1 <= len(pattern) <= len(text)`
- Both strings consist of printable ASCII characters.
- The number of occurrences can be up to `len(text) - len(pattern) + 1`.

## Examples

### Example 1
```
Input:  text = "abababab", pattern = "abab"
Output: [0, 2, 4]
Explanation: "abab" starts at index 0 ("[abab]abab"), index 2 ("ab[abab]ab"),
             and index 4 ("abab[abab]"). These overlap, which is allowed.
```

### Example 2
```
Input:  text = "aaaaa", pattern = "aa"
Output: [0, 1, 2, 3]
Explanation: "aa" begins at every index from 0 through 3 (four overlapping matches).
```

### Example 3
```
Input:  text = "ababcabab", pattern = "abab"
Output: [0, 5]
Explanation: The pattern occurs once at the start (index 0) and once after the 'c'
             (index 5). The 'c' at index 4 prevents any match crossing it.
```

## Hint

Use **Bit-mask / Bitset String Matching (Shift-And / Shift-Or)**. The same running
state word `D = ((D << 1) | 1) & B[c]` that finds the first match also finds them
all: every time the top bit `1 << (m-1)` is set after reading `text[i]`, append the
start index `i - m + 1` and keep scanning — no reset needed, so overlaps are found
for free.
