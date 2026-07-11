# Maximum Score Words Formed by Letters — Solution

## Brute Force

With at most 14 words, the number of word subsets is at most `2^14 = 16384`.
That is tiny, so we can afford to try **every** subset. For each subset:

1. Tally how many of each letter the subset needs (sum the letter counts of the
   chosen words).
2. Feasible only if, for every letter, `needed[c] <= available[c]`.
3. If feasible, compute its score and update the running maximum.

```python
from collections import Counter

class Solution:
    def max_score_words(self, words, letters, score):
        avail = Counter(letters)
        n = len(words)
        best = 0
        for mask in range(1 << n):                 # every subset of words
            need = Counter()
            for i in range(n):
                if mask >> i & 1:
                    need += Counter(words[i])
            if all(need[c] <= avail[c] for c in need):
                total = sum(score[ord(c) - 97] * cnt for c, cnt in need.items())
                best = max(best, total)
        return best
```

- **Time:** `O(2^n · (n · L + 26))` where `n = len(words)` and `L` is the max
  word length. Each of the `2^n` masks tallies up to `n` words of length `L` and
  checks 26 letters. With `n <= 14` and `L <= 15` this is well under `10^7`.
- **Space:** `O(26)` for the counters (plus `O(n)` for the mask bookkeeping).

This exhaustive search is the value used to verify the examples:
`["dog","cat","dad","good"]` yields **19** and `["xxxz","ax","bx","cx"]` yields
**18** for the letter multisets given in `PROBLEM.md`.

## Optimal Approach

Given the constraint `n <= 14`, complete search over the `2^14` subsets **is**
the intended optimal approach — there is no need for anything fancier, and the
problem is NP-hard in general (a variant of subset selection under a multiset
budget), so no polynomial algorithm is expected. Two implementation styles are
common; both are `O(2^n)` in the number of subsets:

**(a) Bitmask enumeration** — the version above; conceptually simplest.

**(b) Backtracking (include/exclude each word)** — often slightly faster in
practice because it can add and *subtract* letter counts incrementally instead of
recounting a whole subset, and it can prune as soon as a word does not fit:

```python
class Solution:
    def max_score_words(self, words, letters, score):
        avail = [0] * 26
        for ch in letters:
            avail[ord(ch) - 97] += 1

        def word_cost(w):
            c = [0] * 26
            for ch in w:
                c[ord(ch) - 97] += 1
            return c

        costs = [word_cost(w) for w in words]
        vals = [sum(score[i] * c[i] for i in range(26)) for c in costs]

        def dfs(i, remaining):
            if i == len(words):
                return 0
            best = dfs(i + 1, remaining)          # skip word i
            if all(costs[i][k] <= remaining[k] for k in range(26)):
                for k in range(26):
                    remaining[k] -= costs[i][k]
                best = max(best, vals[i] + dfs(i + 1, remaining))
                for k in range(26):               # backtrack
                    remaining[k] += costs[i][k]
            return best

        return dfs(0, avail)
```

**Why it is correct.** The optimal set of words is *some* subset of `words`.
Both formulations examine every subset (the bitmask loop directly; the DFS via a
binary include/exclude decision per word, whose leaves are exactly the `2^n`
subsets). A subset is admitted only if its total letter demand is componentwise
`<=` the available supply — which is precisely the "each letter used at most
once" rule, since letters are interchangeable and only their counts matter. We
return the maximum score over all admitted subsets, so we cannot miss the
optimum. The empty subset (score 0) is always feasible, so the answer is never
negative.

**Step by step** for Example 1, `words = ["dog","cat","dad","good"]`,
available `{a:2, c:1, d:3, g:1, o:2}`, scores `a=1,c=9,d=5,g=3`:

- Any subset containing `"cat"` needs a `'t'` (supply 0) -> infeasible, skip.
- `{}` -> 0.
- `{"dad"}` -> needs a:1,d:2; feasible; score 5+1+5 = 11.
- `{"good"}` -> needs g:1,o:2,d:1; feasible; score 3+0+0+5 = 8.
- `{"dad","good"}` -> needs a:1,d:3,g:1,o:2; d:3 == supply 3, feasible; 11+8 = 19.
- `{"dog"}` -> d:1,o:1,g:1; feasible; score 5+0+3 = 8.
- `{"dad","dog"}` -> d:3,a:1,o:1,g:1; feasible; 11+8 = 19.
- `{"dad","good","dog"}` -> d:4 > supply 3 -> infeasible.

The maximum feasible score is **19**.

- **Time:** `O(2^n · (n·L + 26))`.
- **Space:** `O(26)` auxiliary (plus recursion depth `O(n)` for the DFS variant).

## Key Insights & Edge Cases

- **Represent letter counts as a fixed length-26 array (or `Counter`).** This
  makes the feasibility check and score computation `O(26)` regardless of how
  many letters are available.
- **A word that needs a letter you lack can never be part of any valid subset.**
  The feasibility check handles this automatically — no special pre-filter is
  required (though pre-filtering such words is a valid optimization).
- **Duplicate words** are allowed as separate list entries; each has its own bit
  / decision, so taking both is fine as long as letters suffice.
- **The empty subset scores 0**, so the answer is always `>= 0`; initialize
  `best = 0`.
- **Score can be 0 for some letters** — those letters still consume supply, so a
  word full of zero-value letters can still block a better word by using up a
  shared letter. Complete search accounts for this because it evaluates the full
  letter demand, not just the scoring letters.
- **Why brute force is right here:** `n <= 14` caps the search at `2^14` subsets,
  and the problem is a budgeted subset-selection (NP-hard in general), so
  exhaustive search is the clean, correct, and intended solution.
