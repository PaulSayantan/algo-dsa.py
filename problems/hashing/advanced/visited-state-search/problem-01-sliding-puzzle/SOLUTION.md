# Sliding Puzzle — Solution

## Optimal Approach

BFS from the start string to the target, generating neighbors by swapping the blank with its board-adjacent cells, guarded by a visited set. First arrival at the target is the minimum move count.

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

O(6! * 6) states x transitions in the worst case; O(6!) space.

## Key Insights & Edge Cases

The state space is tiny and fixed (720 permutations), so the answer is a small deterministic integer. Case 1 needs a single swap; the second board lies in the unsolvable parity class, so BFS exhausts every reachable state and returns -1; the third takes 5 moves. Only the visited set keeps the search from cycling forever.
