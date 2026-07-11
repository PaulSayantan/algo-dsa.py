# Backtracking

**Backtracking** is a systematic way to explore the space of all candidate
solutions by building a partial solution one *choice* at a time, and abandoning
("backtracking" from) a branch as soon as it is clear it cannot lead to a valid
or optimal complete solution. It is a depth-first search (DFS) over an implicit
tree of decisions, augmented with two ideas:

- **Pruning** — cut off a branch early when a partial solution already violates
  a constraint (e.g., two queens attack each other), so you never explore the
  doomed subtree.
- **Undo (state restoration)** — after exploring a choice, revert the change to
  the shared state so the next choice starts from a clean slate. This "choose →
  recurse → un-choose" rhythm is the signature of backtracking.

## When to reach for it

Reach for backtracking when the problem asks you to **enumerate** or **search
for** solutions that are built from a sequence of discrete choices, and the
answer is naturally a combination / permutation / assignment / partition. Tell-tale
phrasings: "find *all* ...", "count the number of ways ...", "is there an
arrangement such that ...", "return every valid ...". If the constraints let you
reject partial candidates early, backtracking is usually the idiomatic tool.

If you only need *one* yes/no answer or an optimum and there is heavy overlap
between subproblems, consider dynamic programming instead; if choices are
independent and greedy-safe, consider greedy.

## Typical complexity

Backtracking explores a decision tree, so the cost is roughly *(number of nodes
visited) × (work per node)*. Without pruning this is exponential (or factorial):

| Shape | Rough time |
|-------|-----------|
| Subsets of `n` items | `O(n · 2^n)` |
| Permutations of `n` items | `O(n · n!)` |
| N-Queens (n×n) | `O(n!)` worst case, far less with pruning |

Space is `O(depth)` for the recursion stack plus the current partial solution;
the output itself can be exponential and is usually not counted against the
auxiliary bound. Good pruning does not change the worst case but dramatically
shrinks the *typical* running time.

## The universal template

```python
def backtrack(state, choices):
    if is_complete(state):
        record(state)
        return
    for choice in choices:
        if not is_valid(state, choice):
            continue          # prune
        make(state, choice)   # choose
        backtrack(state, next_choices)
        undo(state, choice)   # un-choose
```

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Subsets](problem-01-subsets/PROBLEM.md) | Enumerate the power set of a distinct-valued array | Easy/Medium |
| 2 | [Permutations](problem-02-permutations/PROBLEM.md) | Generate every ordering of distinct numbers | Medium |
| 3 | [Combination Sum](problem-03-combination-sum/PROBLEM.md) | All multisets of candidates (reuse allowed) summing to a target | Medium |
| 4 | [Word Search](problem-04-word-search/PROBLEM.md) | Find a word as a connected path in a character grid | Medium |
| 5 | [Palindrome Partitioning](problem-05-palindrome-partitioning/PROBLEM.md) | Split a string into all-palindrome substrings, every way | Medium |
| 6 | [N-Queens](problem-06-n-queens/PROBLEM.md) | Place `n` non-attacking queens on an `n×n` board | Hard |
