# Maximum Length × Occurrences of a Palindromic Substring

**Difficulty:** Hard

Source: Codeforces 17E "Palisan"-style / classic eertree exercise (a.k.a.
"palindromic characteristic" — maximize `length × number_of_occurrences`).

## Description

For a string `s`, consider every **distinct** palindromic substring `P`. Let
`|P|` be its length and `occ(P)` be the number of times `P` occurs in `s` (as a
contiguous substring, counting overlapping occurrences). Define the *self-
reference value* of `P` as `|P| * occ(P)`.

Return the **maximum** value of `|P| * occ(P)` over all palindromic substrings
`P` of `s`. Intuitively this rewards palindromes that are both long and frequent.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- The answer can be large; use 64-bit integers (Python `int` is unbounded).

## Examples

### Example 1

```
Input:  s = "aaaaa"
Output: 9
Explanation: Candidate values: "a" -> 1*5 = 5, "aa" -> 2*4 = 8,
             "aaa" -> 3*3 = 9, "aaaa" -> 4*2 = 8, "aaaaa" -> 5*1 = 5.
             The maximum is 9 (from "aaa", which occurs 3 times).
```

### Example 2

```
Input:  s = "ababa"
Output: 6
Explanation: "aba" has length 3 and occurs 2 times -> 6. "ababa" gives 5*1 = 5,
             "a" gives 1*3 = 3, "b" gives 1*2 = 2, "bab" gives 3*1 = 3.
             The maximum is 6.
```

### Example 3

```
Input:  s = "abacaba"
Output: 7
Explanation: The whole string "abacaba" is a palindrome of length 7 occurring
             once -> 7. Shorter palindromes such as "aba" (length 3, occurs 2
             times -> 6) give less, so the maximum is 7.
```

## Hint

Build a **Palindromic Tree (Eertree)**, compute each node's occurrence count by
propagating along suffix links (as in the "count all" problem), then take the
maximum of `length[node] * occ[node]` over all non-root nodes.
