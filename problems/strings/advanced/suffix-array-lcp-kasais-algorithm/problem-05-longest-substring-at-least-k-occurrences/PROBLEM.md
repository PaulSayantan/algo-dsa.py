# Longest Substring With At Least K Occurrences

**Difficulty:** Hard

Source: Classic (competitive programming; e.g. Codeforces / SPOJ style "repeated at least K times")

## Description

Given a string `s` and an integer `k`, find the **longest substring that occurs
at least `k` times** in `s`. Occurrences may overlap. Return the substring
itself; if several achieve the maximum length, return any one of them.

If `k <= 1`, the whole string trivially occurs at least once, so return `s`. If
no substring occurs `k` or more times (only possible when `k > len(s)`), return
`""`.

## Constraints

- `1 <= len(s) <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= 10^5`
- Overlapping occurrences count separately (e.g. in `"aaaaa"`, `"aaa"` occurs 3
  times: at indices 0, 1, 2).

## Examples

### Example 1
```
Input:  s = "banana", k = 2
Output: "ana"
Explanation: "ana" occurs twice (indices 1 and 3). No longer substring occurs
  at least twice, so the answer has length 3.
```

### Example 2
```
Input:  s = "banana", k = 3
Output: "a"
Explanation: We now need a substring appearing at least 3 times. "a" occurs 3
  times (indices 1, 3, 5). "ana" only occurs twice, so it no longer qualifies;
  the best length-3-occurrence substring has length 1.
```

### Example 3
```
Input:  s = "mississippi", k = 2
Output: "issi"
Explanation: "issi" occurs twice (indices 1 and 4, overlapping). No longer
  substring repeats at least twice, so the answer has length 4.
```

## Hint

Build the **Suffix Array** and **LCP array (Kasai's algorithm)**. A substring
occurring at least `k` times corresponds to `k` suffixes sharing it as a prefix
— a block of `k` consecutive entries in the suffix array. The longest such
shared prefix over any window of `k` sorted suffixes is the **maximum of the
sliding-window minimums** over `k-1` consecutive LCP values.
