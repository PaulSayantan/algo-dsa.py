# Offline Query Processing

**Offline query processing** is a paradigm for answering a batch of queries when
you are allowed to see *all* of them before producing any answer. Instead of
responding to each query in the order it arrives (the *online* setting), you
**reorder** the queries into a friendlier sequence, answer them cheaply in that
order, and then map the answers back to the original positions.

The reordering turns work that would be expensive per query into work that is
shared across queries. Two dominant flavors:

1. **Sort-and-sweep.** Sort queries by some key (a threshold, a right endpoint,
   a value) and process them together with the data in the same sorted order.
   Elements are typically *added once* to a supporting structure (a Fenwick/BIT
   tree, a trie, a running maximum, a DSU) as a monotone pointer advances, so the
   total insertion cost is `O(n)` amortized instead of `O(n)` **per** query.
2. **Mo's algorithm (query square-root decomposition).** For range queries
   `[l, r]` where you can cheaply add/remove one element at an endpoint, sort the
   queries by `(l // block, r)` and move two pointers between consecutive
   queries. The pointers travel `O((n + q) * sqrt(n))` steps total.

## When to reach for it

- All queries are known up front (no query depends on a previous answer), i.e.
  there are **no interleaved updates you must honor in real time**.
- Each query in isolation is expensive, but a *good ordering* lets consecutive
  queries reuse almost all of the previous query's work.
- The per-query answer is a function of a **prefix/threshold** (sort by the
  threshold) or of a **contiguous range** (Mo's algorithm).

## Typical complexity

| Style                         | Time                          | Space      |
|-------------------------------|-------------------------------|------------|
| Sort + sweep + Fenwick/trie   | `O((n + q) log n)`            | `O(n)`     |
| Sort + two-pointer running agg| `O(n log n + q log q)`        | `O(n)`     |
| Mo's algorithm                | `O((n + q) * sqrt(n) * f)`    | `O(n)`     |

where `f` is the cost of one add/remove step (often `O(1)`), `n` is the data
size, and `q` is the number of queries. The `q log q` term is the cost of
sorting the queries; storing the answer at each query's original index is `O(q)`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Most Beautiful Item for Each Query](problem-01-most-beautiful-item-for-each-query/PROBLEM.md) | Sort queries + monotone sweep with running max | Medium |
| 2 | [K-query (count > k in a range)](problem-02-k-query-count-greater-than-k/PROBLEM.md) | Sort queries by threshold + Fenwick tree | Medium |
| 3 | [Maximum XOR With an Element From Array](problem-03-maximum-xor-with-element-from-array/PROBLEM.md) | Sort queries by cap + incremental binary trie | Hard |
| 4 | [D-query (distinct values in a range)](problem-04-d-query-distinct-in-range/PROBLEM.md) | Sort queries by right endpoint + Fenwick + last-occurrence | Hard |
| 5 | [Powerful Array](problem-05-powerful-array/PROBLEM.md) | Mo's algorithm (query sqrt decomposition) | Hard |
