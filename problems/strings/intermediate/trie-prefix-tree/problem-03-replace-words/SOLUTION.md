# Solution — Replace Words

## Brute Force

For each word in the sentence, generate all of its prefixes (`word[:1]`, `word[:2]`, …) and
check whether any is in a `set(dictionary)`; keep the shortest one that matches.

- Building the set: O(total root characters).
- Per word of length `W`: up to `W` prefix slices, each hashing in O(W) -> **O(W²)** per word.

For the largest inputs (words up to length 1000, up to 1000 words) this is ~10^9 character
operations from the repeated slicing/hashing and is wasteful. A Trie removes the redundant
re-hashing by walking each word exactly once.

## Optimal Approach (Trie)

Insert every root into a Trie, marking `is_end` at each root's final node. To process a word,
walk down the Trie one character at a time:

1. If the current character has no child edge, there is no matching root — keep the word.
2. If the node we land on is `is_end`, we have found a root. Because we stop at the **first**
   such node, it is by construction the **shortest** root that is a prefix of the word.
3. Return the prefix consumed so far as the replacement.

Do this for each word and rejoin with spaces.

### Reference implementation

```python
class Node:
    __slots__ = ("children", "is_end")
    def __init__(self) -> None:
        self.children: dict[str, "Node"] = {}
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary, sentence):
        root = Node()
        for w in dictionary:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, Node())
            node.is_end = True

        def shortest_root(word: str) -> str:
            node = root
            for i, ch in enumerate(word):
                node = node.children.get(ch)
                if node is None:
                    return word          # no root is a prefix
                if node.is_end:
                    return word[: i + 1]  # first (shortest) matching root
            return word                   # word itself never hit a root end

        return " ".join(shortest_root(w) for w in sentence.split())
```

**Why "first match" = "shortest".** Walking the word from the start, the depth of a node
equals the length of the prefix. The first `is_end` we encounter is at minimum depth, hence
the shortest root prefix. Stopping there is correct and also lets us short-circuit.

**Complexity.**
- Build: O(D) where `D` = total characters across all roots.
- Query: O(W) per word, O(S) total where `S` = total sentence length.
- Overall **O(D + S)** time; O(D) space for the Trie.

## Key Insights & Edge Cases

- **Stop at the first `is_end`** — this is what makes it the shortest root; do not keep
  walking.
- **No matching root:** either an edge is missing mid-word, or you consume the whole word
  without ever hitting `is_end`. In both cases return the original word.
- **A root equal to the whole word** is a valid replacement (the word maps to itself).
- **Words with no root and unchanged tokens** (`"the"`, `"was"`) must be preserved exactly;
  `" ".join(...)` restores the single spaces required by the constraints.
- **Trie vs sorted-dictionary trick:** you can also sort roots by length and use a set, but
  the Trie is the idiomatic solution and avoids O(W²) prefix hashing.
