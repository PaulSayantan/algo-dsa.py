# Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium

**Source:** LeetCode 1456 — "Maximum Number of Vowels in a Substring of Given Length"

## Description

Given a string `s` and an integer `k`, return the **maximum number of vowel letters**
in any **substring** of `s` with length exactly `k`.

The vowel letters are `a`, `e`, `i`, `o`, and `u`. A substring is a contiguous run of
characters.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`

## Examples

### Example 1

```
Input:  s = "abciiidef", k = 3
Output: 3
```

**Explanation:** The substring `"iii"` (indices 3–5) contains 3 vowels, which is the
maximum possible for a window of length 3.

### Example 2

```
Input:  s = "aeiou", k = 2
Output: 2
```

**Explanation:** Every character is a vowel, so any length-2 window (e.g. `"ae"`)
contains 2 vowels.

### Example 3

```
Input:  s = "leetcode", k = 3
Output: 2
```

**Explanation:** Windows such as `"lee"` and `"eet"` each contain 2 vowels (`e`,`e`).
No length-3 window contains 3 vowels, so the answer is 2.

## Hint

Use a **Sliding Window (fixed size)**. Count the vowels in the first `k` characters,
then slide: when a character enters on the right add 1 if it is a vowel, and when a
character leaves on the left subtract 1 if it was a vowel. Track the maximum count.
