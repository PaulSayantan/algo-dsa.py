# Solution — Count Pattern Occurrences in a Text

## Brute Force

For each pattern `p`, slide it over `text` and compare:

```python
def count(text, p):
    c = 0
    for i in range(len(text) - len(p) + 1):
        if text[i:i + len(p)] == p:
            c += 1
    return c
```

With `q` queries this is `O(q * n * m)` in the worst case (`n = len(text)`,
`m = max pattern length`). Using KMP or the Z-algorithm per query drops it to
`O(q * (n + m))`, but every query still re-scans the whole text — expensive when
`q` and `n` are both large (up to `10^5` here).

## Optimal Approach (Suffix Tree via Ukkonen)

**Key idea.** Every occurrence of a pattern `p` in `text` is the start of a
suffix of `text` that begins with `p`. In the suffix tree of `text$`, the set of
suffixes starting with `p` is exactly the set of **leaves in the subtree you
reach by spelling `p` from the root**. So:

```
occurrences(p) = number of leaves under the node/edge where the spelling of p ends
```

### Steps

1. Append a unique terminal character (here `"\x00"`) to `text` so every suffix
   ends at its own leaf, then build the suffix tree with **Ukkonen's algorithm**
   in `O(n)`.
2. Run one DFS to precompute `leaf_count(v)` for every node `v` (a leaf counts as
   1; an internal node is the sum over its children).
3. To answer a query, walk down from the root matching the characters of `p`
   along edges. If a mismatch or missing edge occurs, `p` is absent → return `0`.
   Otherwise you finish on some node (or partway along an edge into node `v`);
   the answer is `leaf_count(v)`. Each query costs `O(m)`.

### Why it is correct

The path from the root spelling a string `w` is unique because edges out of a
node start with distinct characters. When you have spelled all of `p` and land
in (or on the edge into) node `v`, the leaves of `v`'s subtree are precisely the
suffixes whose prefix is `p`. Each such suffix start `i` means `text[i:i+m] == p`,
i.e. one occurrence, and every occurrence yields such a suffix — so the counts
match exactly. Overlaps are handled automatically because distinct start indices
are distinct suffixes (distinct leaves).

### Reference implementation

```python
class SuffixTree:
    class _Node:
        __slots__ = ("start", "end", "children", "link", "leaf_idx")
        def __init__(self, start, end):
            self.start = start        # edge label = text[start:end]
            self.end = end            # None on a leaf edge => grows with global END
            self.children = {}        # first-char -> child node
            self.link = None          # suffix link
            self.leaf_idx = -1        # suffix start index for a leaf

    def __init__(self, text):
        self.t = text
        self.n = len(text)
        self.root = self._Node(-1, -1)
        self.root.link = self.root
        self._END = 0
        self._build()

    def _edge_end(self, node):
        return self._END if node.end is None else node.end

    def _build(self):
        t, root = self.t, self.root
        active_node, active_edge, active_length = root, -1, 0
        remainder = 0
        for i in range(self.n):
            self._END = i + 1            # Rule 1: extend all leaves in O(1)
            remainder += 1
            last_new = None
            while remainder > 0:
                if active_length == 0:
                    active_edge = i
                first = t[active_edge]
                if first not in active_node.children:
                    leaf = self._Node(i, None)          # Rule 2: new leaf
                    leaf.leaf_idx = i - remainder + 1
                    active_node.children[first] = leaf
                    if last_new is not None:
                        last_new.link = active_node
                        last_new = None
                else:
                    nxt = active_node.children[first]
                    elen = self._edge_end(nxt) - nxt.start
                    if active_length >= elen:           # skip/count: walk down
                        active_edge += elen
                        active_length -= elen
                        active_node = nxt
                        continue
                    if t[nxt.start + active_length] == t[i]:   # Rule 3: already present
                        active_length += 1
                        if last_new is not None:
                            last_new.link = active_node
                        break
                    split = self._Node(nxt.start, nxt.start + active_length)  # split edge
                    active_node.children[first] = split
                    leaf = self._Node(i, None)
                    leaf.leaf_idx = i - remainder + 1
                    split.children[t[i]] = leaf
                    nxt.start += active_length
                    split.children[t[nxt.start]] = nxt
                    if last_new is not None:
                        last_new.link = split
                    last_new = split
                remainder -= 1
                if active_node is root and active_length > 0:
                    active_length -= 1
                    active_edge = i - remainder + 1
                elif active_node is not root:
                    active_node = active_node.link       # follow suffix link

    def leaf_counts(self):
        cnt = {}
        def dfs(node):
            if not node.children:
                cnt[id(node)] = 1
                return 1
            c = sum(dfs(ch) for ch in node.children.values())
            cnt[id(node)] = c
            return c
        dfs(self.root)
        return cnt

    def count(self, pattern, cnt):
        node, i, m = self.root, 0, len(pattern)
        while i < m:
            ch = pattern[i]
            if ch not in node.children:
                return 0
            nxt = node.children[ch]
            j, end = nxt.start, self._edge_end(nxt)
            while j < end and i < m:
                if self.t[j] != pattern[i]:
                    return 0
                i += 1; j += 1
            node = nxt
        return cnt[id(node)]


class Solution:
    def count_occurrences(self, text, patterns):
        st = SuffixTree(text + "\x00")     # unique terminal not in the alphabet
        cnt = st.leaf_counts()
        return [st.count(p, cnt) for p in patterns]
```

### Complexity

- Build: `O(n)` time / `O(n)` space (constant alphabet; `O(n log |Σ|)` with map
  children, which is what the dict-based code above effectively does).
- Leaf-count DFS: `O(n)`.
- Each query: `O(m)`. Total: `O(n + Σ m_i)` — independent of re-scanning the text
  per query.

## Key Insights & Edge Cases

- **Unique terminal is mandatory.** Without a sentinel, a suffix that is a prefix
  of another suffix (e.g. `"na"` inside `"banana"`) would end in the middle of an
  edge rather than at a leaf, and leaf-counting would undercount. The terminal
  guarantees every suffix is explicit.
- **Landing mid-edge is fine.** A pattern often ends partway along an edge; you
  still take the leaf count of the child node that edge leads into — every leaf
  below it is a valid occurrence.
- **Absent pattern:** any missing edge or character mismatch during the walk
  means `0`.
- **Overlapping occurrences** are counted correctly for free, since occurrences
  correspond to distinct suffix start positions (distinct leaves).
- **Pattern equal to the whole text** occurs exactly once (`1`), because only one
  suffix — the full string — begins with it.
- Watch the terminal: never let a query match into the sentinel character. Since
  the sentinel is outside the input alphabet, real queries never contain it, so
  matching stops naturally at the right place.
