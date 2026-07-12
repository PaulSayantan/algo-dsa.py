# Word Ladder

**Difficulty:** Hard

**Source:** LeetCode 127 — Word Ladder

## Description

Given `beginWord`, `endWord`, and a `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, changing one letter at a time with every intermediate word in `wordList`. Return `0` if no such sequence exists.

## Examples

### Example 1

```
Input:  beginWord="hit", endWord="cog", list=[hot,dot,dog,lot,log,cog]
Output: 5
```

## Hint

BFS over words; neighbors differ by one letter and are in the word set. Count levels (words).
