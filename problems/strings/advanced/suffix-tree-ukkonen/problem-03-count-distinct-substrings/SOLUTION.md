# Solution — Count Distinct Substrings

## Brute Force

Insert every substring into a hash set and return its size:

```python
subs = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        subs.add(s[i:j])
return len(subs)
```

There are `O(n^2)` substrings and each slice/hash is `O(n)`, so this is
`O(n^3)` time and `O(n^2)` space (or `O(n^2)` time with incremental hashing but
still `O(n^2)` distinct strings stored). This blows up well before `n = 10^5`.

## Optimal Approach (Suffix Tree via Ukkonen)

**Key idea.** Consider the suffix tree of `s$`. Walk from the root along edges;
every position where you can *stop* — at a node, or partway along an edge — spells
out one distinct substring, and every distinct substring corresponds to exactly
one such stopping position. The number of distinct substrings therefore equals
the **total number of characters on all edge labels**:

```
distinct substrings = Σ (length of each edge label)
```

We build over `s$` and simply do **not count the sentinel character**: the
terminal `$` contributes exactly one character to each leaf edge (the final
`$`), and those "substrings ending in `$`" are not real substrings of `s`.
Excluding the sentinel character from every edge label removes precisely those.

### Steps

1. Append a unique terminal and build the suffix tree with **Ukkonen's
   algorithm** in `O(n)`.
2. DFS over all edges; for each edge add its label length, but if the label
   contains the sentinel, trim it at the sentinel (this drops the trailing `$`
   characters, one per relevant edge).
3. Return the sum.

### Why it is correct

Each edge of a suffix tree is a maximal non-branching path. If you enumerate all
prefixes of all root-to-node paths, you enumerate every distinct substring
exactly once: a substring `w` corresponds to the unique point reached by
spelling `w`, and different substrings reach different points (the tree is a
trie with compressed non-branching runs). The number of such points equals the
number of edge characters (each edge character advances you to one new point).
Building over `s$` adds exactly the substrings that end with `$` — i.e. the
strings `s[i:] + "$"`, which are not substrings of `s` — and each of those is the
last character on some edge. Trimming the sentinel removes all of them, leaving
exactly the distinct substrings of `s`.

For example on `"banana$"` the sum of trimmed edge lengths is `15`, matching the
brute-force count.

### Reference implementation

Reuse the `SuffixTree` class from Problem 1, then:

```python
class Solution:
    def countDistinctSubstrings(self, s):
        term = "\x00"                 # unique sentinel outside the alphabet
        st = SuffixTree(s + term)
        t = st.t
        total = 0

        def dfs(node):
            nonlocal total
            for child in node.children.values():
                label = t[child.start:st._edge_end(child)]
                cut = label.find(term)          # drop the sentinel if present
                if cut != -1:
                    label = label[:cut]
                total += len(label)
                dfs(child)

        dfs(st.root)
        return total
```

An equivalent, sentinel-free formulation counts it directly from the tree
structure: `distinct = (sum of all edge lengths over s$) - n - 1`, because the
`n + 1` suffixes of `s$` each contribute one trailing sentinel character. Trimming
per edge (above) is the most robust to get right.

### Complexity

- Build: `O(n)` time / `O(n)` space (Ukkonen).
- DFS over `O(n)` edges: `O(n)`.
- Overall: **`O(n)` time, `O(n)` space**.

(By contrast, a suffix array + LCP solution gives the same count as
`n(n+1)/2 - Σ LCP[i]` in `O(n log n)`; the suffix tree gives `O(n)`.)

## Key Insights & Edge Cases

- **Edge-length sum = distinct substrings.** This is the canonical suffix-tree
  counting identity; internalize it.
- **Handle the sentinel.** Forgetting to exclude the terminal character
  overcounts by exactly `n + 1` (the number of suffixes of `s$`). The examples
  (`"banana"` → 15) only work once the sentinel is removed.
- **Use big integers.** For `n = 10^5` the count approaches `5 * 10^9`, which
  overflows 32-bit ints; Python ints are unbounded, but in other languages use
  64-bit.
- **All-equal string** like `"aaa"`: the tree is a single path, giving exactly
  `n` distinct substrings (`"a"`, `"aa"`, `"aaa"`).
- **All-distinct string** like `"abc"`: no repeats, so the count is the full
  `n(n+1)/2` (here 6).
- **Recursion depth** on pathological inputs (e.g. `"aaaa...a"`): raise the limit
  or use an explicit stack.
