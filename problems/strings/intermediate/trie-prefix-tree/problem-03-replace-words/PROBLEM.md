# Replace Words

**Difficulty:** Medium

**Source:** LeetCode 648 — Replace Words

## Description

In English, we have a concept called **root**, which can be followed by some other word to
form another longer word — let's call this word a **successor**. For example, when the root
`"help"` is followed by the word `"ful"`, we can form a successor `"helpful"`.

Given a `dictionary` consisting of many roots and a `sentence` consisting of words separated
by spaces, replace all the successors in the sentence with the root forming it. If a
successor can be replaced by more than one root, replace it with the root that has the
**shortest length**.

Return the sentence after the replacement.

## Constraints

- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 100`
- `dictionary[i]` consists of only lowercase letters.
- `1 <= sentence.length <= 10^6`
- `sentence` consists of only lowercase letters and spaces.
- The number of words in `sentence` is in the range `[1, 1000]`.
- Every two consecutive words in `sentence` are separated by exactly one space.
- Each word in `sentence` has length in the range `[1, 1000]`.

## Examples

### Example 1

```
Input:  dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

**Explanation:**
- `"cattle"` has root `"cat"` -> becomes `"cat"`.
- `"rattled"` has root `"rat"` -> becomes `"rat"`.
- `"battery"` has root `"bat"` -> becomes `"bat"`.
- `"the"`, `"was"`, `"by"` have no dictionary root and stay unchanged.

### Example 2

```
Input:  dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
```

**Explanation:**
- `"aadsfasf"` starts with root `"a"` -> `"a"`.
- `"absbs"` starts with root `"a"` (shorter than any other match) -> `"a"`.
- `"bbab"` starts with root `"b"` -> `"b"`.
- `"cadsfafs"` starts with root `"c"` -> `"c"`.

## Hint

Insert all roots into a **Trie (Prefix Tree)**. For each word in the sentence, walk the trie
character by character and stop at the **first** node that marks the end of a root — that is
guaranteed to be the shortest matching root.
