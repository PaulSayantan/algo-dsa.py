# Implement Trie (Prefix Tree)

**Difficulty:** Medium

**Source:** LeetCode 208 — Implement Trie (Prefix Tree)

## Description

A trie (pronounced "try") or prefix tree is a tree data structure used to efficiently
store and retrieve keys in a dataset of strings. There are various applications of this
data structure, such as autocomplete and spellchecker.

Implement the `Trie` class:

- `Trie()` initializes the trie object.
- `void insert(String word)` inserts the string `word` into the trie.
- `boolean search(String word)` returns `true` if the string `word` is in the trie
  (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` returns `true` if there is a previously inserted
  string `word` that has the prefix `prefix`, and `false` otherwise.

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters `a`–`z`.
- At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

## Examples

### Example 1

```
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]
```

**Explanation:**
- `Trie()` creates the object.
- `insert("apple")` stores "apple".
- `search("apple")` -> `true` ("apple" was inserted).
- `search("app")` -> `false` ("app" was never inserted as a complete word).
- `startsWith("app")` -> `true` ("apple" has the prefix "app").
- `insert("app")` stores "app".
- `search("app")` -> `true` (now "app" is a complete word).

### Example 2

```
Input:
["Trie", "insert", "startsWith", "search"]
[[], ["banana"], ["ban"], ["ban"]]

Output:
[null, null, true, false]
```

**Explanation:**
- `insert("banana")` stores "banana".
- `startsWith("ban")` -> `true` ("banana" begins with "ban").
- `search("ban")` -> `false` ("ban" itself was never inserted as a full word).

## Hint

Model each character as an edge to a child node and mark the node where a word ends with a
boolean flag. This is exactly the **Trie (Prefix Tree)** data structure — `search` requires
the end flag while `startsWith` only requires reaching the last character.
