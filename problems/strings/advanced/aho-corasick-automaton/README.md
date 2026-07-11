# Aho–Corasick Automaton

The **Aho–Corasick automaton** is a data structure for **multi-pattern string
matching**: given a set of patterns `P = {p_1, …, p_k}` and a text `T`, it finds
**every occurrence of every pattern** in `T` in a single linear scan.

It is best understood as a **trie of the patterns augmented with "failure
links."** The trie encodes all pattern prefixes; a failure link from a node `u`
points to the node representing the **longest proper suffix of `u`'s string that
is also a prefix of some pattern** — exactly the Knuth–Morris–Pratt failure
function, generalized to many patterns at once. When you run the text through
the automaton and the current character has no outgoing trie edge, you follow
failure links (or use a precomputed *goto* transition table) instead of
restarting from the root. A secondary chain of failure links, the **dictionary
suffix links**, lets you report *all* patterns that end at the current position.

## When to reach for it

- You must match **many patterns simultaneously** against one text (or a stream)
  and a per-pattern KMP/`str.find` loop (`O(k · n)`) is too slow.
- The pattern set is **fixed / reused** across many texts or many queries — you
  pay the build cost once and then each text is linear.
- Problems that reduce to "for each position, what dictionary words end here?"
  — bold-tagging, streaming suffix checks, forbidden-substring windows, and
  dictionary-segmentation DPs.

## Complexity

Let `S = Σ|p_i|` be the total pattern length, `σ` the alphabet size, `n = |T|`,
and `z` the number of reported matches.

| Phase | Time | Space |
|-------|------|-------|
| Build trie | `O(S)` | `O(S · σ)` (array edges) or `O(S)` (hashmap edges) |
| Build failure / goto links (BFS) | `O(S · σ)` | — |
| Scan text (count only) | `O(n)` | `O(1)` extra |
| Scan text (report every match) | `O(n + z)` | `O(1)` extra |

The headline result: after an `O(S · σ)` build, matching is **`O(n + z)`**,
independent of the number of patterns.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [String Matching in an Array](problem-01-string-matching-in-array/PROBLEM.md) | Substring-of-another via one automaton | Easy |
| 2 | [Count Keyword Occurrences](problem-02-keywords-search/PROBLEM.md) | Total match count over a dictionary | Medium |
| 3 | [Add Bold Tag in a String](problem-03-add-bold-tag-in-string/PROBLEM.md) | Report all matches + interval merge | Medium |
| 4 | [Stream of Characters](problem-04-stream-of-characters/PROBLEM.md) | Online suffix matching on a stream | Hard |
| 5 | [Longest Valid Substring](problem-05-longest-valid-substring/PROBLEM.md) | Shortest match per position + sliding window | Hard |
| 6 | [Construct String with Minimum Cost](problem-06-construct-string-min-cost/PROBLEM.md) | Automaton-driven DP over the target | Hard |

Work them top to bottom: problems 1–3 build fluency with construction and match
reporting, while 4–6 combine the automaton with streaming, two-pointer, and
dynamic-programming layers.
