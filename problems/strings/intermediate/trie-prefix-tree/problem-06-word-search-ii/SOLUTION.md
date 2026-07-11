# Solution — Word Search II

## Brute Force

Run the single-word "Word Search I" DFS once per word: for each word, start a
backtracking search from every cell trying to trace exactly that word.

- Each search is O(m · n · 4^L) where `L` is the word length.
- Total: **O(W · m · n · 4^L)** for `W` words.

With up to 3·10^4 words this repeats an enormous amount of work — every word independently
re-explores the same board prefixes. The key waste: two words sharing a prefix (`"eat"`,
`"east"`) each pay for exploring that prefix separately.

## Optimal Approach (Trie + DFS backtracking)

Insert **all** words into a Trie, then do a single DFS from each board cell, walking the
board and the Trie **together**. At a cell holding letter `c`, we only continue if the current
Trie node has a child `c`; otherwise the prefix matches no word and we prune immediately. When
we reach a Trie node marked as a word end, we record that word.

This shares prefix work across all words and prunes dead branches early.

### Reference implementation

```python
class Solution:
    def findWords(self, board, words):
        # Build the Trie. Store the full word at its end node for easy collection.
        root: dict = {}
        for w in words:
            node = root
            for ch in w:
                node = node.setdefault(ch, {})
            node["#"] = w                      # "#" marks end + holds the word

        R, C = len(board), len(board[0])
        found: list[str] = []

        def dfs(r: int, c: int, node: dict) -> None:
            ch = board[r][c]
            nxt = node.get(ch)
            if nxt is None:                    # prefix not in Trie -> prune
                return
            word = nxt.get("#")
            if word is not None:
                found.append(word)
                del nxt["#"]                   # de-duplicate: collect each word once

            board[r][c] = "*"                  # mark visited
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != "*":
                    dfs(nr, nc, nxt)
            board[r][c] = ch                   # restore (backtrack)

            # optional pruning: drop leaves that can lead nowhere
            if not nxt:
                del node[ch]

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        return found
```

**Why it is correct.** The DFS maintains the invariant that the path of board letters visited
so far equals the path of Trie edges followed, i.e. it is a valid prefix of at least one word.
Reaching a node with the end marker means those letters spell a complete word tracked along a
valid adjacent path with no reused cell (enforced by the `"*"` marking). Deleting the end
marker after collecting guarantees each word is reported once even if reachable via multiple
paths.

**Complexity.**
- Build Trie: O(total characters in `words`).
- Search: worst case O(m · n · 4^L) but with aggressive pruning it is far less in practice;
  crucially it is independent of `W` beyond the Trie size, since shared prefixes are explored
  once.
- Space: O(total characters in `words`) for the Trie plus O(L) recursion depth.

## Key Insights & Edge Cases

- **Trie-guided pruning is the whole point.** Descend the board and Trie in lockstep and abort
  the moment `node.get(ch)` is `None`.
- **Store the word at its end node** (`"#": word`) so you can append it directly without
  reconstructing the path.
- **De-duplicate by removing the end marker** once collected; the same word can be traceable
  by several paths, but must appear once in the output.
- **In-place visited marking** (`"*"`) avoids a separate visited set; always restore the cell
  on the way out (backtracking). Ensure `"*"` is not a real board letter.
- **Leaf pruning** (`del node[ch]` when a child empties out) shrinks the Trie as words are
  found, speeding up later cells — an important optimization for large `words`.
- **Cannot reuse a cell:** enforced because a marked cell is skipped by the neighbor check;
  this is why `"abcb"` on a 2x2 board is not found.
- **No shared board mutation across DFS roots** because every cell is restored before the next
  root starts.
