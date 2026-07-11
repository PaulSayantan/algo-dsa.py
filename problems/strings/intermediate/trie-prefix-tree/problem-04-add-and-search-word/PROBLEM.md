# Add and Search Word — Data Structure Design

**Difficulty:** Medium

**Source:** LeetCode 211 — Design Add and Search Words Data Structure

## Description

Design a data structure that supports adding new words and finding if a string matches any
previously added string, where the search string may contain the `.` wildcard.

Implement the `WordDictionary` class:

- `WordDictionary()` initializes the object.
- `void addWord(word)` adds `word` to the data structure so it can be matched later.
- `bool search(word)` returns `true` if there is any string in the data structure that
  matches `word`, or `false` otherwise. `word` may contain dots `.` where a `.` can match
  **any single letter**.

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consists of `.` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Examples

### Example 1

```
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output:
[null,null,null,null,false,true,true,true]
```

**Explanation:**
- Add `"bad"`, `"dad"`, `"mad"`.
- `search("pad")` -> `false` ("pad" was never added).
- `search("bad")` -> `true` (exact match).
- `search(".ad")` -> `true` (matches "bad", "dad", and "mad").
- `search("b..")` -> `true` (matches "bad").

### Example 2

```
Input:
["WordDictionary","addWord","search","search","search"]
[[],["a"],["a"],["."],["aa"]]

Output:
[null,null,true,true,false]
```

**Explanation:**
- Add `"a"`.
- `search("a")` -> `true` (exact match).
- `search(".")` -> `true` ("." matches the single letter "a").
- `search("aa")` -> `false` (no two-letter word was added; length must match).

## Hint

Store words in a **Trie (Prefix Tree)**. For a normal character follow the one matching
edge; for a `.` recurse into **all** children with DFS/backtracking, and only accept when
the entire pattern is consumed at a node marked as a word end.
