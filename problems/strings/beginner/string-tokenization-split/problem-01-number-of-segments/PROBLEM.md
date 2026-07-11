# Number of Segments in a String

**Difficulty:** Easy

**Source:** LeetCode 434 — Number of Segments in a String

## Description

You are given a string `s`. A **segment** is defined to be a contiguous sequence
of **non-space** characters.

Return the number of segments in `s`.

Segments are separated by one or more spaces. Leading and trailing spaces, as
well as multiple consecutive spaces between segments, should not be counted as
segments themselves.

## Constraints

- `0 <= s.length <= 300`
- `s` consists of lowercase and uppercase English letters, digits, or one of the
  following characters: `"!@#$%^&*()_+-=',.:"`.
- The only space character in `s` is `' '`.

## Examples

**Example 1**

```
Input:  s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"].
```

**Example 2**

```
Input:  s = "Hello"
Output: 1
Explanation: A single segment with no spaces at all.
```

**Example 3**

```
Input:  s = "   "
Output: 0
Explanation: The string is only spaces, so there are no non-space segments.
```

## Hint

Use **String Tokenization / Split**: break the string on whitespace and count how
many non-empty tokens remain.
