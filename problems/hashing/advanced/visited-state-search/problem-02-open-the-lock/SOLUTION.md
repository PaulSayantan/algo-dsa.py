# Open the Lock — Solution

## Optimal Approach

Standard BFS over 4-digit strings; each state expands to 8 neighbors. The visited set (plus deadends) bounds work to O(10^4) states.

### Reference implementation

```python
class Solution:
    def slidingPuzzle(self, board):
        start = "".join(str(c) for row in board for c in row)
        target = "123450"
        nbr = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        q = deque([(start, 0)])
        seen = {start}                      # hashed states in a visited set
        while q:
            state, d = q.popleft()
            if state == target:
                return d
            z = state.index("0")
            for nb in nbr[z]:
                lst = list(state)
                lst[z], lst[nb] = lst[nb], lst[z]
                ns = "".join(lst)
                if ns not in seen:
                    seen.add(ns)
                    q.append((ns, d + 1))
        return -1

    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            state, d = q.popleft()
            if state == target:
                return d
            for i in range(4):
                for delta in (-1, 1):
                    nd = (int(state[i]) + delta) % 10
                    ns = state[:i] + str(nd) + state[i + 1:]
                    if ns not in dead and ns not in seen:
                        seen.add(ns)
                        q.append((ns, d + 1))
        return -1

    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, d = q.popleft()
            if word == endWord:
                return d
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nw = word[:i] + c + word[i + 1:]
                    if nw in words and nw not in seen:
                        seen.add(nw)
                        q.append((nw, d + 1))
        return 0
```

### Complexity

O(10^4 * 8) transitions; O(10^4) visited space.

## Key Insights & Edge Cases

Case 1 threads around the deadends in 6 moves. Case 2 reaches '0009' in a single backward turn of the last wheel (0->9 wraps in one move). Case 3 is -1 because '0000' is itself a deadend, so BFS can't even start — a clean edge case the visited/deadend check must handle.
