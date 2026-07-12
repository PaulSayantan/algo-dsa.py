# Word Ladder

**Difficulty:** Hard

**Source:** LeetCode 127 — Word Ladder

## Description

Given `beginWord`, `endWord`, and a `wordList`, transform `beginWord` into `endWord` changing exactly one letter at a time, where every intermediate word must be in `wordList`. Return the number of words in the shortest such sequence (counting both endpoints), or 0 if no sequence exists. BFS over word states with a visited set.

## Examples

### Example 1

```
Input:  begin="hit", end="cog", list=["hot","dot","dog","lot","log","cog"]
Output: 5
```

**Explanation:** hit -> hot -> dot -> dog -> cog is length 5.

### Example 2

```
Input:  begin="hit", end="cog", list=["hot","dot","dog","lot","log"]
Output: 0
```

**Explanation:** endWord 'cog' is not in the list.

## Hint

BFS; neighbors differ by one letter and must be in the word set; return the level count.
