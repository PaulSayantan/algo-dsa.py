# String Matching in an Array

**Difficulty:** Easy

**Source:** LeetCode 1408 — String Matching in an Array

## Description

Given an array of strings `words`, return **all strings in `words` that are a
substring of another word in `words`**. You can return the answer in **any
order**.

A string `a` is a substring of string `b` if `a` occurs as a contiguous block of
characters inside `b`. A word is **not** considered a substring of itself; it
must appear inside a *different* element of the array.

Although the constraints are small enough for a brute-force pairwise check, the
intended "scalable" way to think about this is: treat every word as a pattern,
build one automaton over all of them, then push each word through the automaton
and see which *other* patterns it contains. This is the multi-pattern matching
setup that Aho–Corasick was designed for.

## Constraints

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- `words[i]` consists of lowercase English letters only.
- All the strings in `words` are **distinct**.

## Examples

### Example 1

```
Input:  words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is a substring of "mass" and "hero" is a substring of
"superhero". ["hero","as"] is also a valid answer.
```

### Example 2

```
Input:  words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et" and "code" are both substrings of "leetcode".
```

### Example 3

```
Input:  words = ["blue","green","bu"]
Output: []
Explanation: No word is a substring of any other word, so the answer is empty.
```

## Hint

Build a single **Aho–Corasick Automaton** over all the words, then feed each word
through it; any *other* word whose full pattern is matched inside it belongs in
the answer. (For the tiny constraints a nested `in` check also works — use it to
validate your automaton.)
