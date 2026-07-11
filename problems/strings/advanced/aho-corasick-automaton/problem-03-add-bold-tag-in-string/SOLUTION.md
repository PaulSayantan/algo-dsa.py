# Solution — Add Bold Tag in a String

## Brute Force

For each word, find all of its start positions in `s` (overlapping allowed) and
mark the interval `[start, start+len(word)-1]` as covered in a boolean array of
length `len(s)`. Then sweep the boolean array to build the output, opening a
`<b>` when a covered run begins and closing `</b>` when it ends.

```python
def addBoldTag(self, s, words):
    n = len(s)
    bold = [False] * n
    for w in words:
        start = s.find(w)
        while start != -1:
            for k in range(start, start + len(w)):
                bold[k] = True
            start = s.find(w, start + 1)
    # stitch
    out, i = [], 0
    while i < n:
        if bold[i]:
            j = i
            while j < n and bold[j]:
                j += 1
            out.append("<b>" + s[i:j] + "</b>")
            i = j
        else:
            out.append(s[i]); i += 1
    return "".join(out)
```

- **Time:** `O(W · n · L)` in the worst case (`W` words, each `find` scan `O(n)`,
  each match marks up to `L` cells). For LeetCode's small limits this passes, but
  with `10^4` words and long `s` it degrades badly.
- **Space:** `O(n)` for the boolean array.

The marking-then-merging skeleton is exactly what we keep; only the *find-all*
step is replaced.

## Optimal Approach (Aho–Corasick Automaton)

Replace the per-word search with a single automaton pass that reports **every**
occurrence of **every** word.

**Why it is correct.** Scanning `s` through the automaton, at text position `i`
the current node's dictionary-suffix-link chain enumerates *all* words that end
at `i`. For a word of length `len` ending at `i`, it covers `[i-len+1, i]`; mark
those positions. After the scan, `bold[k]` is true iff position `k` lies inside
some word occurrence — identical to the brute-force marking, but computed in one
linear sweep. Merging contiguous `True` runs then produces the minimal set of
tag pairs, which is precisely the "merge overlapping/consecutive" requirement.

**Interval marking without O(n·L) blowup.** If you mark cell-by-cell it is still
`O(n + z·L)`. A cleaner linear technique: keep `max_end`, the furthest position
covered so far. When a word of length `len` ends at `i`, you only need to record
that `[i-len+1, i]` is covered. Using a difference-style "furthest reach" scan
(track the rightmost covered index as you move left-to-right) collapses marking
to `O(n + z)`. In practice, for the given constraints, marking a boolean array
is fine.

```python
from collections import deque

class Solution:
    def addBoldTag(self, s, words):
        words = [w for w in set(words) if w]     # drop empties/dupes
        n = len(s)
        if not words or n == 0:
            return s

        nxt = [{}]; fail = [0]; length = [0]      # length of a word ending here (0 if none)
        dict_len = [0]                            # longest word ending via suffix links
        for w in words:
            cur = 0
            for ch in w:
                if ch not in nxt[cur]:
                    nxt.append({}); fail.append(0); length.append(0); dict_len.append(0)
                    nxt[cur][ch] = len(nxt) - 1
                cur = nxt[cur][ch]
            length[cur] = max(length[cur], len(w))

        q = deque()
        for ch, v in nxt[0].items():
            fail[v] = 0; q.append(v)
        while q:
            u = q.popleft()
            f = fail[u]
            dict_len[u] = max(length[u], dict_len[f])   # longest word ending at u
            for ch, v in nxt[u].items():
                g = fail[u]
                while g and ch not in nxt[g]:
                    g = fail[g]
                fail[v] = nxt[g].get(ch, 0) if (g or ch in nxt[0]) else 0
                if fail[v] == v:
                    fail[v] = 0
                q.append(v)

        bold = [False] * n
        cur = 0
        for i, ch in enumerate(s):
            while cur and ch not in nxt[cur]:
                cur = fail[cur]
            cur = nxt[cur].get(ch, 0)
            L = dict_len[cur]                # longest word ending exactly at i
            if L:
                for k in range(i - L + 1, i + 1):
                    bold[k] = True

        out, i = [], 0
        while i < n:
            if bold[i]:
                j = i
                while j < n and bold[j]:
                    j += 1
                out.append("<b>" + s[i:j] + "</b>")
                i = j
            else:
                out.append(s[i]); i += 1
        return "".join(out)
```

Using `dict_len` (the *longest* word ending at the position) is a neat trick:
the longest word's interval contains every shorter word's interval that ends at
the same spot, so marking just the longest is enough to cover them all.

- **Build:** `O(S · σ)` time / space.
- **Scan + mark:** `O(n + total covered length)`; with the "furthest reach"
  optimization, `O(n)`.
- **Overall:** `O(S · σ + n)`.

## Key Insights & Edge Cases

- **Empty `words`** (Example 3) or `words` containing empty strings: return `s`
  unchanged; skip empty patterns during construction.
- **Merging is automatic** from the boolean sweep — overlapping (`aaa`/`aab`) and
  consecutive matches collapse into one run, satisfying both merge rules.
- **Mark the longest word ending here**, not every word, to avoid redundant work;
  a shorter word ending at the same index is fully inside the longest one's span.
- **Case/character set**: patterns may contain uppercase and digits, so use a
  hashmap-based transition table (as above) rather than a fixed 26-slot array,
  or widen the array to the full byte range.
- **Root failure self-loop**: keep the `if fail[v] == v: fail[v] = 0` guard so
  the scan never infinite-loops on depth-1 nodes.
