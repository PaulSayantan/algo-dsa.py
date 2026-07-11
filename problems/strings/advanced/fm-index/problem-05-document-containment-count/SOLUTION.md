# Solution — Document Containment Count

## Brute Force

For each query, test every document with a substring search (`P in doc`, i.e. KMP
or the built-in search) and count how many contain `P`. If the total corpus
length is `N` and there are `D` documents, one query costs `O(N + D * m)`. Across
`q` queries this is `O(q * (N + D * m))` — every query rescans the whole corpus.

- Time: `O(q * (N + D * m))`
- Space: `O(N)` for the corpus

## Optimal Approach (FM-Index over a `$`-separated corpus + locate)

Index the entire corpus once, then answer each query by locating occurrences and
mapping them to documents.

### Building the corpus index

1. Concatenate the documents with a **unique separator** `#` between them and a
   terminal sentinel `$` at the end:
   `S = doc_0 + "#" + doc_1 + "#" + ... + "#" + doc_{D-1} + "$"`.
   The separator must not appear inside any document, and it must sort below the
   real alphabet; `$` sorts below `#`. The separator's job is to guarantee that
   **no matched pattern can straddle two documents** — backward search would have
   to consume a `#`, which no query pattern contains, so the interval empties.
2. Record the **start offset** of each document in `S`. With one separator after
   each document, `start[0] = 0` and `start[j] = start[j-1] + len(doc_{j-1}) + 1`.
3. Build the FM-Index over `S` (`SA`, `BWT`, `C[]`, rank table), keeping `SA` for
   locate.

### Answering a query

1. `locate(P)` via backward search gives all occurrence positions of `P` in `S`.
2. For each position `p`, find its document id by binary-searching the sorted
   `start[]` offsets: `doc = bisect_right(start, p) - 1`.
3. The answer is the number of **distinct** document ids among those positions.

```python
def document_count(self, pattern):
    positions = self.fm.locate(pattern)
    return len({ self._doc_of(p) for p in positions })

def _doc_of(self, position):
    import bisect
    return bisect.bisect_right(self.start, position) - 1
```

### Why it is correct

Because `#` and `$` never appear in any query pattern, every backward-search
match lies entirely inside a single document — the separator/terminal act as
hard walls. Each located position `p` therefore falls in exactly one document,
identified by the greatest `start[j] <= p`. Collecting the document ids into a set
removes the duplicates from multiple occurrences inside one document, so the set
size is precisely the number of distinct documents containing `P`.

### Complexity

- Build: `O(N)`–`O(N log N)` time, `O(N)` space (`N` = total corpus length).
- Query: `O(m)` backward search + `O(occ)` locate + `O(occ log D)` document
  mapping = `O(m + occ log D)`. With a sampled suffix array, locate is
  `O(m + occ * s)`.

### A note on optimality of the counting step

Mapping each of `occ` occurrences to a document can be wasteful when a pattern
occurs many times but in few documents (e.g. `"a"` in a corpus of `a`s). The
classic *document listing* result (Muthukrishnan) answers "list the `ndoc`
distinct documents" in `O(m + ndoc)` — independent of `occ` — using the FM-Index
interval plus a "document array" `DA[i]` (document of the `i`-th suffix) and a
precomputed *previous-occurrence* array with a range-minimum query. For the
counting variant you can likewise avoid enumerating all `occ` positions. The
enumerate-and-dedup approach here is the clear, teachable baseline; the RMQ-based
scheme is the asymptotically optimal upgrade.

## Key Insights & Edge Cases

- **Unique separators are the trick.** They make the multi-document problem a
  single-string FM-Index problem while forbidding cross-document matches.
- **Sort order:** put `$` below `#` below the letters so the terminals occupy the
  smallest suffix-array rows and never interfere with letter searches.
- **Distinct vs. total:** dedup by document id. Multiple hits in one document
  collapse to a single count (Example 2, `"abc"` occurs twice in `"abcabc"` but
  the document counts once).
- **Absent pattern:** empty locate interval -> empty set -> `0`.
- **Repeated documents:** identical documents are still distinct ids and each is
  counted separately.
- **Scaling:** for very frequent patterns, prefer the document-array + RMQ listing
  scheme so cost scales with the number of distinct documents rather than the raw
  occurrence count.
