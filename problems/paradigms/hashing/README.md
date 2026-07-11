# Hashing

**Use hash maps/sets for O(1) average lookups, deduplication, and grouping.**

## What it is

Hashing stores keys (and optionally associated values) in a table indexed by a
hash of the key. This lets you answer "have I seen this before?", "what value is
attached to this key?", and "which items share this property?" in **O(1) average
time** instead of the O(n) a linear scan or O(log n) a balanced tree would cost.

In Python the two workhorses are:

- `dict` (hash map) — key -> value. Use it for counting frequencies, memoizing
  the last index/position of a value, and grouping items by a derived key.
- `set` (hash set) — membership only. Use it for deduplication and instant
  "is this element present?" checks.

## When to reach for it

Reach for hashing when a naive solution is quadratic because it repeatedly
*searches* a collection, and that search could instead be a direct lookup. Common
trigger phrases:

- "Does a complement / pair / duplicate exist?" -> store what you have seen.
- "Count / frequency of ..." -> `dict` from item to count.
- "Group things that share ..." -> `dict` from canonical key to a list.
- "How many subarrays sum to K?" -> `dict` of prefix-sum -> count.
- "Longest run of related values" -> `set` for O(1) neighbor checks.

The general pattern: **trade memory for time.** You spend O(n) extra space on the
table to remove a factor of n (or log n) from the running time.

## Typical complexity

| Operation                    | Average | Worst case* |
|------------------------------|---------|-------------|
| Insert / lookup / delete     | O(1)    | O(n)        |
| Building a table of n items  | O(n)    | O(n^2)      |
| Extra space                  | O(n)    | O(n)        |

\* Worst case occurs only with adversarial hash collisions; for typical data and
Python's randomized string hashing you get the average bounds in practice.

Caveat: hashing gives you fast *point* lookups but destroys ordering. If you need
sorted order, range queries, or predecessor/successor, a balanced BST or sorting
is the better tool.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Two Sum](problem-01-two-sum/PROBLEM.md) | Hash map: store seen value -> index, look up complement | Easy |
| 2 | [Contains Duplicate](problem-02-contains-duplicate/PROBLEM.md) | Hash set: detect a repeat in one pass | Easy |
| 3 | [Group Anagrams](problem-03-group-anagrams/PROBLEM.md) | Hash map: group by a canonical key | Medium |
| 4 | [Subarray Sum Equals K](problem-04-subarray-sum-equals-k/PROBLEM.md) | Hash map of prefix-sum -> count | Medium |
| 5 | [Longest Consecutive Sequence](problem-05-longest-consecutive-sequence/PROBLEM.md) | Hash set: O(1) neighbor checks, count only from run starts | Medium/Hard |
