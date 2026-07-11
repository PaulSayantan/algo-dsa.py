# Word Search II — Solution

## Brute Force

Run the single-word Word Search (LeetCode 79) once per word: for each word, DFS from every
cell trying to trace it, marking/unmarking cells along the way.

- **Time:** `O(W * m * n * 4^L)` where `W = len(words)` and `L` is the max word length.
- **Space:** `O(L)` recursion depth per search.

This repeats an enormous amount of work: two words that share a prefix (e.g. `"eat"` and
`"ear"`) each re-walk the same board cells for that shared prefix. With up to `3 * 10^4`
words this is far too slow. The fix is to search for **all words at once** using a Trie so
shared prefixes are explored a single time.

## Optimal Approach (Backtracking on Grid + Trie)

Build a Trie of all words, then run **one** DFS from each board cell that descends the Trie
by the current cell's letter. A single traversal simultaneously matches every word that has
the letters seen so far as a prefix.

**Algorithm**

1. **Build the Trie.** Insert each word; store the full word string at its terminal node
   (`node.word = w`) so that when you reach it you can emit the word directly.
2. `dfs(r, c, node)`:
   - Let `ch = board[r][c]`. If `ch` is not a child of `node`, this branch has no matching
     word — return.
   - Move to `child = node.children[ch]`.
   - If `child.word` is set, add it to the result and **clear it** (`child.word = None`) so
     the same word is not reported twice.
   - **Choose:** mark `(r, c)` used (set `board[r][c] = '#'`).
   - **Explore:** recurse into the four neighbors with `child`.
   - **Un-choose:** restore `board[r][c] = ch`.
   - **Optional pruning:** if `child` now has no children and no word, remove it from its
     parent so future traversals skip the dead branch.
3. Start `dfs(r, c, root)` from every cell; return the collected words.

**Why it is correct.** Descending the Trie by board letters means the path of cells visited
so far always spells a prefix present in the Trie; when that prefix equals a complete word
(`child.word` set) we have found a valid placement of that word (adjacent cells, none reused,
enforced by the `#` marking). Restoring the cell on backtrack keeps the "no reuse" rule local
to the current path. Clearing `child.word` after collecting guarantees uniqueness. Because we
launch from every cell and try every neighbor, we consider every possible placement of every
word, so no board word is missed.

**Reference implementation**

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:                       # build the Trie
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            child = node.children.get(ch)
            if not child:
                return
            if child.word is not None:
                result.append(child.word)
                child.word = None             # de-duplicate

            board[r][c] = "#"                 # choose
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, child)
            board[r][c] = ch                  # un-choose

            if not child.children:            # prune dead leaf
                node.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result
```

- **Time:** `O(m * n * 4 * 3^(L-1))` in the worst case, where `L` is the longest word — from
  each of the `m * n` cells the first step has 4 directions and each subsequent step has at
  most 3 (you never revisit the immediately previous cell). Trie construction is
  `O(total characters in words)`. This is independent of `W` beyond the Trie size, which is
  the whole point.
- **Space:** `O(total characters in words)` for the Trie plus `O(L)` recursion depth.

## Key Insights & Edge Cases

- **Trie over repeated single searches.** Storing all words in a Trie means shared prefixes
  are walked once, turning a `W`-fold repeated search into a single board traversal.
- **Store the word at the terminal node.** Keeping the whole string at `node.word` lets you
  append it directly on a hit — no need to reconstruct the path.
- **De-duplicate by clearing `node.word`.** The same word can be reachable via different
  starting cells; nulling it after the first hit keeps the output unique without a separate
  set.
- **Restore cells on backtrack** exactly as in single Word Search — the `#` sentinel must be
  reset so sibling branches can reuse the cell.
- **Leaf pruning** (removing exhausted Trie branches) is the key optimization that keeps
  large `words` fast; it steadily shrinks the Trie as words are found.
- **Edge cases:** a word requiring cell reuse (Example 2, `"abcb"`) is never matched because
  the cell is marked `#`; `"aa"` on a `1x1` board (Example 3) fails for the same reason,
  while `"a"` is found immediately at the root's child.
