# Top K Frequent Words

**Difficulty:** Medium

**Source:** LeetCode 692 — Top K Frequent Words

## Description

Given an array of strings `words` and an integer `k`, return the `k` most frequent
strings.

Return the answer **sorted by frequency from highest to lowest**. Words with the **same
frequency** must be sorted by their **lexicographical order** (alphabetically ascending).

## Constraints

- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, the number of unique words[i]]`.

## Examples

### Example 1

```
Input:  words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
```

**Explanation:** Frequencies are `{"i": 2, "love": 2, "leetcode": 1, "coding": 1}`. Both
`"i"` and `"love"` appear twice; since they tie on frequency, they are ordered
alphabetically: `"i"` before `"love"`.

### Example 2

```
Input:  words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
```

**Explanation:** Frequencies are `{"the": 4, "is": 3, "sunny": 2, "day": 1}`. Sorted by
descending frequency (no ties among the top 4): `"the"`, `"is"`, `"sunny"`, `"day"`.

## Hint

Count the words, then select the top `k` by frequency — breaking ties alphabetically. Use
**Top-K via Heap**, but be careful: the tie-break runs *opposite* to the frequency ordering,
so design the heap's comparison key accordingly.
