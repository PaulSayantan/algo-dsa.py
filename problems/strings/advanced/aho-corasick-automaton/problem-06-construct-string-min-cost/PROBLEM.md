# Construct String with Minimum Cost

**Difficulty:** Hard

**Source:** LeetCode 3213 — Construct String with Minimum Cost

## Description

You are given a string `target`, an array of strings `words`, and an integer
array `costs`, both arrays of the same length.

Imagine an empty string `s`. You can perform the following operation any number
of times (including zero):

- Choose an index `i` in the range `[0, words.length - 1]`.
- Append `words[i]` to `s`.
- The cost of this operation is `costs[i]`.

Return the **minimum cost** to make `s` equal to `target`. If it is not possible,
return `-1`.

Each append places a word at the current end of `s`, so building `target`
amounts to partitioning it into a sequence of dictionary words (with repetition
allowed) whose concatenation is exactly `target`, minimizing the total cost.

## Constraints

- `1 <= target.length <= 5 * 10^4`
- `1 <= words.length == costs.length <= 5 * 10^4`
- `1 <= words[i].length <= target.length`
- `sum(words[i].length) <= 5 * 10^4`
- `1 <= costs[i] <= 10^4`
- `target` and `words[i]` consist of only lowercase English letters.

## Examples

### Example 1

```
Input:  target = "abcdef", words = ["abdef","abc","d","def","ef"],
        costs = [100,1,1,10,5]
Output: 7
Explanation: Append "abc" (cost 1) -> "abc", then "d" (cost 1) -> "abcd", then
"ef" (cost 5) -> "abcdef". Total cost = 1 + 1 + 5 = 7. Using "def" (cost 10)
instead of "d"+"ef" would cost 11, so 7 is optimal.
```

### Example 2

```
Input:  target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]
Output: -1
Explanation: No combination of the available words can spell "aaaa", so it is
impossible and the answer is -1.
```

### Example 3

```
Input:  target = "abcabc", words = ["a","b","c","abc"], costs = [10,10,10,1]
Output: 2
Explanation: Append "abc" (cost 1) then "abc" (cost 1) to get "abcabc" for a
total cost of 2, cheaper than spelling it letter by letter (cost 60).
```

## Hint

Build an **Aho–Corasick Automaton** over `words` (keep the minimum cost per
distinct word at its terminal node). Run `target` through the automaton with a DP
where `dp[i]` = min cost to build `target[0..i-1]`; at each position, use the
dictionary-suffix links to enumerate every word ending here and relax
`dp[i] = min(dp[i], dp[i - len(word)] + cost(word))`.
