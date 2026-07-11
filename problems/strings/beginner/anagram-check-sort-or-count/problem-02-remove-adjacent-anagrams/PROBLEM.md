# Remove Adjacent Anagrams

**Difficulty:** Easy

Source: LeetCode 1160-style / classic "Remove Anagrams" (Codeforces 1512C family)

## Description

You are given a list of lowercase words `words`. Repeatedly perform the following
operation: choose any index `i > 0` such that `words[i]` is an anagram of
`words[i - 1]`, and delete `words[i]` from the list. Keep doing this until no such
index remains.

Return the resulting list of words. It can be shown that the final list is unique and
does not depend on the order in which you perform the deletions.

Intuitively: scan left to right and drop every word that is an anagram of the word
immediately before it (the one that "survived"), collapsing each run of mutually
adjacent anagrams down to its first word.

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.

## Examples

### Example 1

```
Input:  words = ["abba", "baba", "bbaa", "cd", "cd"]
Output: ["abba", "cd"]
Explanation: "baba" is an anagram of "abba" -> delete it. Now "bbaa" is an anagram of
the surviving "abba" -> delete it. "cd" is not an anagram of "abba", so it stays. The
second "cd" is an anagram of the first "cd" -> delete it.
```

### Example 2

```
Input:  words = ["a", "b", "a"]
Output: ["a", "b", "a"]
Explanation: No word is an anagram of its immediate predecessor ("b" vs "a", and the
last "a" vs "b"), so nothing is removed.
```

### Example 3

```
Input:  words = ["hello", "olleh", "world"]
Output: ["hello", "world"]
Explanation: "olleh" is an anagram of "hello" and is removed; "world" is not an
anagram of "hello", so it stays.
```

## Hint

Walk the list once, keeping the last kept word. Use an **Anagram Check (sort or count)**
to decide whether the current word is an anagram of the one you last kept.
