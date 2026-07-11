# Solution — Add and Search Word

## Brute Force

Keep all added words in a list, bucketed by length. For a search, scan every word of the
matching length and compare character by character, treating `.` as an automatic match.

- `addWord`: O(1) append.
- `search`: O(K · L) where `K` is the number of words of that length and `L` the length.

With up to 10^4 calls this can approach 10^4 · 10^4 · 25 character comparisons in the worst
case. The Trie prunes shared prefixes so most branches die early, and wildcards only branch
where they must.

## Optimal Approach (Trie + DFS backtracking)

Store words in a standard Trie with an `is_end` flag. Search becomes a recursive descent:

- **Normal character `c`:** follow the single edge `c`; if it is missing, fail.
- **Wildcard `.`:** it could be any letter, so recurse into **every** child and succeed if
  *any* branch matches the rest of the pattern.
- **End of pattern:** succeed only if the current node has `is_end == True` (this enforces
  the equal-length requirement — the pattern must terminate exactly at a stored word).

### Reference implementation

```python
class Node:
    __slots__ = ("children", "is_end")
    def __init__(self) -> None:
        self.children: dict[str, "Node"] = {}
        self.is_end = False

class WordDictionary:
    def __init__(self) -> None:
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, Node())
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: Node, i: int) -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            nxt = node.children.get(ch)
            return nxt is not None and dfs(nxt, i + 1)
        return dfs(self.root, 0)
```

**Why it is correct.** For a concrete character the match is forced, so there is exactly one
child to follow. For `.`, a match exists iff *some* letter continues to a full match — exactly
the `any(...)` over children. Requiring `is_end` at the pattern's end guarantees we matched a
complete stored word of the same length, so `"aa"` cannot match the single-letter word `"a"`.

**Complexity.**
- `addWord`: O(L).
- `search`: O(L) when there are no wildcards. With `d` dots the worst case branches into up
  to 26 children per dot, giving **O(26^d · L)**. Here `d <= 2`, so it stays small in
  practice; early edge misses prune most branches.
- Space: O(total characters added) for the Trie plus O(L) recursion depth.

## Key Insights & Edge Cases

- **`.` = branch over all children**, then OR the results. This backtracking DFS is the heart
  of the problem.
- **Terminal check `is_end`** enforces length equality; forgetting it makes prefixes falsely
  match (e.g. `"b.."` would wrongly match a stored `"b"`).
- **Missing edge for a concrete letter** fails that branch immediately — cheap pruning.
- **All-dots query** like `".."` matches any stored word of that exact length.
- **Recursion depth** is bounded by the word length (≤ 25), so plain recursion is safe; no
  need for an explicit stack.
- Iterating `node.children.values()` (only existing children) is far better than looping over
  all 26 letters when the Trie is sparse.
