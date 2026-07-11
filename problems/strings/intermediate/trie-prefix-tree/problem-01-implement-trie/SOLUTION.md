# Solution — Implement Trie (Prefix Tree)

## Brute Force

Store every inserted word in a Python `list` (or `set`).

- `insert`: append the word — O(1) amortized (or O(L) to hash for a set).
- `search`: check membership — O(N·L) for a list, O(L) for a set.
- `startsWith`: scan every stored word and test `w.startswith(prefix)` — **O(N·L)** every
  call, which is the real problem. With up to 3·10^4 calls this degrades badly, and a set
  gives no help at all for prefix queries.

So a set solves `search` but not `startsWith` efficiently. We need a structure indexed by
character position.

## Optimal Approach (Trie)

Build a tree where each node has:

- a `children` map from a character to the next node, and
- an `is_end` flag marking that some inserted word ends at this node.

**Insert.** Start at the root. For each character, follow the existing child edge or create
a new node if it does not exist. After consuming all characters, set `is_end = True` on the
final node.

**Search.** Walk the characters from the root; if an edge is missing, return `False`. After
the walk, return the final node's `is_end` flag (the word must have been explicitly inserted,
not merely be a prefix).

**startsWith.** Identical walk, but success is simply *reaching* the last character — the
`is_end` flag is irrelevant.

The distinction between `search` and `startsWith` is the whole point: both traverse the same
path, but `search` additionally demands the terminal flag.

### Reference implementation

```python
class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def _walk(self, s: str) -> "TrieNode | None":
        node = self.root
        for ch in s:
            nxt = node.children.get(ch)
            if nxt is None:
                return None
            node = nxt
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
```

**Correctness.** Each node corresponds to exactly one prefix (the path from the root). A
word is present iff following its characters lands on a node whose `is_end` is `True`, which
only `insert` sets. A prefix exists iff the path can be followed to completion.

**Complexity.**
- `insert`, `search`, `startsWith`: **O(L)** time where `L` is the string length.
- Space: **O(total characters inserted)** across all words in the worst case; shared prefixes
  reduce this.

## Key Insights & Edge Cases

- **`search` vs `startsWith`:** the only difference is checking `is_end`. Getting this wrong
  is the classic bug — `search("app")` must be `False` after inserting only `"apple"`.
- **`setdefault` / `defaultdict`:** cleanly folds the "create-if-absent" logic into one line.
- **Array vs dict children:** with a known alphabet of 26 letters, a fixed `[None]*26` array
  is faster and cache-friendlier; a `dict` is simpler and better for sparse/large alphabets.
- **Duplicate inserts** are harmless — re-walking the path just re-sets `is_end = True`.
- **Empty string:** not possible under the given constraints (`length >= 1`), but a robust
  implementation would mark the root's `is_end` for it.
- **`__slots__`** on the node class trims per-node memory, which matters when millions of
  characters are stored.
