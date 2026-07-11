# Commentz-Walter Algorithm

Multi-pattern string search that combines the **trie + suffix-link** machinery of
Aho-Corasick with the **right-to-left scanning and skip heuristics** of Boyer-Moore.

---

## 1. The Problem It Solves

Given a set of keywords `K = {P_1, P_2, ..., P_r}` and a text `T` of length `n`,
find **every occurrence of every keyword** in `T`.

The naive approach runs a single-pattern matcher once per keyword: with Boyer-Moore
that is `O(r * n)` in the worst case and you re-scan the whole text `r` times.
Aho-Corasick solves the multi-pattern problem in `O(n + total pattern length + matches)`
by walking the text **once** through a keyword automaton — but it inspects **every**
text character (it never skips).

Commentz-Walter (CW) asks: *can we get Aho-Corasick's "one pass over the text" while
also skipping characters the way Boyer-Moore does?* The answer is yes, and on average
it is **sublinear** in `n`.

---

## 2. Key Idea

CW is to Aho-Corasick what Boyer-Moore is to naive/KMP:

- **Boyer-Moore** aligns a single pattern against a window, compares **right-to-left**,
  and on a mismatch shifts the window right by the maximum of a *good-suffix* and a
  *bad-character* heuristic — often skipping many characters.
- **Commentz-Walter** does the same for a *set* of patterns. To compare "the tail of
  every pattern first," it builds a **trie of the REVERSED keywords**. Scanning the
  window from its right end and walking this reversed trie is exactly "matching the
  suffixes of the keywords, longest-common-suffix first."

So the two ingredients are:

1. A **reversed-keyword trie** (essentially the Aho-Corasick goto structure built on
   `P_i^R`), giving fast suffix matching for all patterns at once.
2. **Generalized Boyer-Moore shift functions** (`shift1`, `shift2`, and a bad-character
   table `char`) defined over the trie so that after a match or mismatch we can shift the
   window by the largest provably safe amount.

The scanning window has width `wmin = min_i |P_i|` (the shortest keyword length): no
occurrence can be shorter than that, so a window narrower than `wmin` could never end a
match, and a wider fixed window could miss short patterns.

---

## 3. Preprocessing

### 3.1 Reversed-pattern trie

Insert `P_i^R` (each keyword reversed) into a trie. The root is at depth 0. A node `v`
spells a string `s(v)` along the path from the root; because we inserted reversals,
`s(v)^R` is a **suffix** of one or more keywords. A node is *terminal* (an output node)
when `s(v)^R` is a complete keyword.

Let `depth(v)` be the number of edges from the root to `v`, and `wmin = min_i |P_i|`.

### 3.2 The three shift tables

**Bad-character table `char(x)`** — the shallowest depth at which symbol `x` appears as
an edge label in the trie (capped at `wmin + 1`):

```
char(x) = min( { depth(v) : v != root, edge into v is labeled x }  U  { wmin + 1 } )
```

Intuitively, if the mismatching text symbol `x` first appears at depth `d` among the
reversed patterns, the window can be slid until that occurrence lines up.

**Good-suffix tables `shift1` (weak) and `shift2` (strong)** — defined via the suffix
relation among node strings. For a node `u`:

```
set1(u) = { depth(w) - depth(u) : w is a node, s(u) is a PROPER suffix of s(w) }
set2(u) = { depth(w) - depth(u) : w is a TERMINAL node, s(u) is a PROPER suffix of s(w) }
```

```
shift1(root) = 1
shift1(u)    = min( set1(u)  U { wmin } )                   for u != root

shift2(root) = wmin
shift2(u)    = min( set2(u)  U { shift2(parent(u)) } )      for u != root
```

`shift1` is the minimal shift that keeps the already-matched suffix consistent with the
trie *somewhere*; `shift2` is the stronger shift that keeps it consistent with a place
where a **full keyword** could end. (`set2 ⊆ set1`.) Both are safe lower bounds on how
far the window must move before the next possible alignment.

---

## 4. The Search Loop

Keep the window's right end at text index `i` (1-based), starting at `i = wmin`.
Read the window **right-to-left**, following trie edges. Let `j` be the number of
characters matched so far (`= depth` of the current node `v`).

```
i = wmin
while i <= n:
    v = root
    j = 0
    # walk the reversed-pattern trie leftward from the window's right end
    while (i - j >= 1) and (v has a child on symbol T[i - j]):
        v = child(v, T[i - j])
        j = j + 1
        if v is terminal:
            report keyword s(v)^R ending at position i   # spans [i - j + 1 .. i]

    # mismatch (or ran off the left end): compute the shift
    if i - j >= 1:
        x = T[i - j]                                     # the mismatching symbol
        shift = min( shift2(v),
                     max( shift1(v), char(x) - j - 1 ) )
    else:
        shift = shift2(v)

    i = i + shift                                        # shift >= 1 always -> progress
```

At the root (`j = 0`, `shift1(root) = 1`, `shift2(root) = wmin`) the rule collapses to
`min(wmin, max(1, char(x) - 1))` — precisely a Boyer-Moore-Horspool bad-character shift
generalized to the whole keyword set. The `min(shift2, ...)` cap and `max(shift1, ...)`
floor guarantee `shift >= 1`, so the loop always advances.

---

## 5. Worked Example

Patterns `K = {"cat", "cart", "art"}`, so `wmin = 3` (`"cat"`, `"art"`).
Reversed keywords: `"tac"`, `"trac"`, `"tra"`. Trie:

```
root
 └─t─ n1
      ├─a─ n2 ──c─ n3*        s(n3)="tac"  -> "cat"
      └─r─ n4 ──a─ n5* ──c─ n6*   s(n5)="tra"->"art", s(n6)="trac"->"cart"
```

`char`:  `t→1`, `a→2` (shallowest of depths 2 and 3), `r→2`, `c→3` (shallowest of 3,4),
everything else `→ wmin+1 = 4`.
No node string is a proper suffix of another here, so `set1 = set2 = {}` for all nodes,
giving `shift1 = shift2 = wmin = 3` everywhere except `shift1(root) = 1`.

Text `T = "the cart art"` (1-indexed): `t h e _ c a r t _ a r t` (positions 1..12).

| `i` | window right end `T[i]` | trie walk (right-to-left)                        | shift computed                                                  | new `i` |
|-----|--------------------------|--------------------------------------------------|-----------------------------------------------------------------|---------|
| 3   | `e`                      | root has no `e` edge; `j=0`                       | `min(3, max(1, char(e)-1)) = min(3, max(1,3)) = 3`              | 6       |
| 6   | `a`                      | root has no `a` edge; `j=0`                       | `min(3, max(1, char(a)-1)) = min(3, max(1,1)) = 1`              | 7       |
| 7   | `r`                      | root has no `r` edge; `j=0`                       | `min(3, max(1, char(r)-1)) = 1`                                 | 8       |
| 8   | `t`                      | `t→r→a` reaches n5* (**"art"** [6..8]), `→c` reaches n6* (**"cart"** [5..8]); then `T[4]=space` mismatch, `j=4` | `min(3, max(3, char(' ')-4-1)) = min(3, max(3,-1)) = 3` | 11      |
| 11  | `r`                      | root has no `r` edge; `j=0`                       | `1`                                                             | 12      |
| 12  | `t`                      | `t→r→a` reaches n5* (**"art"** [10..12]); then `T[9]=space` mismatch, `j=3` | `min(3, max(3, char(' ')-3-1)) = 3`             | 15 → stop |

Reported matches: `"art"` at 6..8, `"cart"` at 5..8, `"art"` at 10..12 — all correct,
and `"cat"` (never present) is never reported.

Notice the skips: the unseen symbol `e` lets the window jump a full `wmin = 3`
(the window at 1..3 is discarded entirely), and after the `"cart"` match a
`wmin` shift jumps past the whole word. Here the *bad-character* rule does the visible
work because these patterns share no common suffix; when patterns **do** share suffixes
(e.g. `{"acbab", "ccbab"}` both ending in `bab`), `shift1`/`shift2` become the larger,
more interesting shifts.

---

## 6. Complexity

| Phase          | Time                                  | Space                                 |
|----------------|----------------------------------------|----------------------------------------|
| Preprocessing  | `O(m)` to `O(m · \|Σ\|)` (trie + shift tables), where `m = Σ\|P_i\|` | `O(m)` for the trie plus `O(m)` for shift tables and `O(\|Σ\|)` for `char` |
| Search (avg)   | **Sublinear**, often `~O(n / wmin)` comparisons | `O(1)` beyond the tables |
| Search (worst) | `O(n · m)` (degenerate texts/patterns) | — |

- **Average / best case is sublinear**, like Boyer-Moore: many windows are resolved by a
  single mismatched character and skip `wmin` positions at a time.
- **Worst case is `O(n · m)`** — the shift can degrade to 1 on adversarial inputs (e.g.
  highly self-similar patterns over a tiny alphabet). Unlike Aho-Corasick, CW does **not**
  offer a linear worst-case guarantee.

**Versus Aho-Corasick:** AC is `O(n + m + matches)` worst-case and reads every text
character exactly once — predictable and simple, but it can never skip. CW can be much
faster on average by skipping, at the cost of a worse worst case and a harder
implementation.

**Versus running Boyer-Moore once per pattern:** `r` independent BM passes cost roughly
`O(r · n)` and scan the text `r` times. CW performs a **single** skipping pass that
handles all `r` patterns simultaneously via the shared reversed trie.

---

## 7. When To Use It (and When Not To)

**Use CW when:**
- You have many patterns but want to avoid touching every text byte.
- Patterns are **long** and the **alphabet is large** (e.g. DNA k-mers over larger
  encodings, byte signatures, protocol tokens): large alphabets make the bad-character
  table sparse, so mismatches trigger big shifts and the sublinear behavior really pays.
- The text is large and read-mostly, so preprocessing cost is amortized.

**Prefer alternatives when:**
- You need a **guaranteed** linear bound or the simplest correct implementation →
  **Aho-Corasick** is the usual production choice (network IDS like Snort/Suricata, virus
  scanners, `grep -F` style multi-string search).
- Patterns are short or the alphabet is tiny (small alphabets shrink the achievable
  shifts toward 1, eroding CW's advantage).

**Limitations:**
- **Hard to implement correctly.** The `shift1`/`shift2`/`char` interplay and the
  off-by-one accounting are error-prone; the original paper and later refinements
  (e.g. Watson–Zwaan) describe several variants of the shift functions.
- No worst-case linear guarantee, so it can be a poor fit for adversarial or untrusted
  input where an attacker could force `O(n · m)` behavior.

---

## 8. Reference Pseudocode

### Preprocessing

```
function CW_PREPROCESS(K = {P_1..P_r}):
    trie = new Trie(); root = trie.root
    for P in K:
        insert reverse(P) into trie          # mark last node terminal, store P
    wmin = min(|P| for P in K)

    # depths via BFS/DFS from root
    for each node v: depth(v) = distance(root, v)

    # bad-character table
    for each symbol x in Σ: char(x) = wmin + 1
    for each edge (u -> v) labeled x:
        char(x) = min(char(x), depth(v))

    # good-suffix tables via the proper-suffix relation between node strings
    # (computed with suffix links over the reversed-pattern trie)
    shift1(root) = 1;  shift2(root) = wmin
    for each node u != root in increasing depth order:
        set1 = { depth(w) - depth(u) : s(u) is a proper suffix of s(w) }
        set2 = { d in set1 : the corresponding w is terminal }
        shift1(u) = min(set1 U { wmin })
        shift2(u) = min(set2 U { shift2(parent(u)) })

    return (trie, char, shift1, shift2, wmin)
```

### Search

```
function CW_SEARCH(T[1..n], trie, char, shift1, shift2, wmin):
    i = wmin
    while i <= n:
        v = root; j = 0
        while (i - j >= 1) and (v has child on T[i - j]):
            v = child(v, T[i - j]); j = j + 1
            if v is terminal:
                report(keyword(v), start = i - j + 1, end = i)
        if i - j >= 1:
            shift = min(shift2(v), max(shift1(v), char(T[i - j]) - j - 1))
        else:
            shift = shift2(v)
        i = i + shift            # shift >= 1 guarantees termination
```

---

## 9. See Also

- **Aho-Corasick** — same multi-pattern goal built on a *forward* keyword trie with
  failure links; linear worst case, no skipping. CW borrows its trie idea (over reversed
  patterns) and its suffix-link computation.
- **Boyer-Moore** — the single-pattern origin of the right-to-left scan and the
  good-suffix / bad-character shift heuristics that CW generalizes to a set of patterns.
- **Boyer-Moore-Horspool** — the simplified bad-character-only variant that the CW shift
  reduces to at the root node.
- **Set Backward Oracle Matching (SBOM) / Wu-Manber** — later multi-pattern skipping
  algorithms that are often easier to implement and competitive in practice.
