# Generalized Suffix Structures

A **generalized suffix structure** is a single suffix automaton (SAM) or suffix
tree built over a **set of strings** `{s_1, s_2, ..., s_n}` instead of just one.
It recognizes exactly the **union of all substrings** of all input strings, while
still keeping track of *which* of the input strings each substring belongs to.
This lets you answer "multi-string" substring questions — longest common
substring of many strings, substrings shared by at least `k` strings, distinct
substrings across a whole collection — in near-linear total time.

Two concrete realizations exist:

- **Generalized Suffix Automaton (GSA)** — build one SAM and insert each string
  in turn, resetting the "last" pointer to the root before each new string. The
  `sa_extend` routine is adapted so that when the transition being added already
  exists (because a previous string created it), it reuses or clones the existing
  state instead of blindly making a new one. This is the approach used in every
  solution here — it is the shortest to code correctly.
- **Generalized Suffix Tree** — concatenate the strings with distinct sentinel
  separators `s_1 # s_2 $ ...` and build one suffix tree (Ukkonen) over the
  concatenation, or build a generalized suffix tree directly. Each leaf is
  labeled with the string it came from.

Both structures share the same core idea: a node/state groups substrings by their
**end-position set (`endpos`)**, and the suffix links form a tree over those
classes. Annotating each state with the **set of string-IDs** appearing in its
`endpos` is what unlocks the multi-string queries.

## When to reach for it

Reach for a generalized suffix structure when the input is **several strings** and
the question is about **shared / common / collective substrings**:

- Longest common substring of `k` strings (all of them).
- Longest substring occurring in **at least `k`** of `n` strings.
- Counting distinct substrings across an entire collection (union).
- Counting distinct substrings common to every string (intersection).
- Per-string statistics about substrings shared with the rest of the set.

If you only have **one** string, a plain suffix automaton / suffix array is
enough; if you have **two** strings, you can also build a SAM of one and stream
the other through it. The generalized structure shines from three strings up, or
whenever you need to attribute substrings to their source strings.

## How the generalized SAM tracks ownership

1. Build the GSA by inserting every string (reset `last = root` per string).
2. For each character added, the `extend` call returns the state that represents
   the current prefix's longest suffix ending there — mark that state with the
   current string's ID (a **primary occurrence**).
3. `endpos(v)` equals the union of the `endpos` of `v`'s children in the
   suffix-link tree, plus `v`'s own primary occurrences. So **propagate the marks
   upward along suffix links** (a reverse-topological / DFS pass) to compute, for
   each state, the set of string-IDs whose occurrences pass through it.

Because all substrings inside one state share the exact same `endpos`, "state `v`
is owned by string `i`" means **every** substring in `v`'s length interval
`(len[link[v]], len[v]]` occurs in string `i`. That single fact powers all the
intersection/union counting below.

## Complexity

| Quantity | Bound |
|---|---|
| States in GSA | `<= 2 * L` where `L = sum of string lengths` |
| Transitions | `O(L)` (constant alphabet) / `O(L * |Sigma|)` array form |
| Build time | `O(L)` (fixed alphabet) / `O(L log |Sigma|)` with hash maps |
| Ownership propagation (bitmask, `n` small) | `O(states)` |
| Ownership propagation (small-to-large sets, any `n`) | `O(L log L)` |
| Space | `O(L)` states + `O(L * |Sigma|)` transitions |

Here `L` is the total length of all input strings. Everything is linear (or
`L log L`) in `L`, independent of how the length is split across strings.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Distinct Substrings in a Collection](problem-01-distinct-substrings-in-collection/PROBLEM.md) | Count distinct substrings across the union of many strings | Medium |
| 2 | [Maximum Length of Repeated Subarray](problem-02-maximum-length-repeated-subarray/PROBLEM.md) | LeetCode 718 — longest common contiguous block of two arrays | Medium |
| 3 | [Longest Common Substring of K Strings](problem-03-longest-common-substring-of-k-strings/PROBLEM.md) | SPOJ LCS2 — longest substring present in *every* string | Hard |
| 4 | [Count Distinct Common Substrings](problem-04-count-distinct-common-substrings/PROBLEM.md) | How many distinct substrings appear in *all* given strings | Hard |
| 5 | [Longest Substring in At Least K Strings](problem-05-longest-substring-in-at-least-k-strings/PROBLEM.md) | Longest substring occurring in `>= k` of `n` strings | Hard |
