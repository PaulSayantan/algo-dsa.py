# Word Ladder — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in words and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return 0
```
