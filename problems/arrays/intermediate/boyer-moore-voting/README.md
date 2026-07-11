# Boyer–Moore Voting

The **Boyer–Moore Voting Algorithm** finds a **majority element** — a value that
appears **more than ⌊n/2⌋ times** — in a sequence using a single pass and only
**O(1) extra space**. It was published by Robert S. Boyer and J Strother Moore in 1981
as "a fast majority vote algorithm."

## Core Idea

Keep one `candidate` and one integer `count`. Sweep left to right:

- If `count == 0`, adopt the current element as the new `candidate`.
- If the current element **equals** `candidate`, increment `count`.
- Otherwise, decrement `count`.

Intuition: think of it as pairwise **cancellation**. Every element that differs from the
candidate cancels one vote for the candidate. If some value truly occupies more than half
the array, it has more votes than *all other values combined*, so it can never be fully
cancelled — it survives as the final candidate.

```
count = 0
candidate = None
for x in nums:
    if count == 0:
        candidate = x
    count += 1 if x == candidate else -1
return candidate
```

## The Two Phases (and a critical caveat)

Boyer–Moore has **two phases**:

1. **Voting phase** — the single pass above produces a *candidate*.
2. **Verification phase** — a second pass that counts the candidate's real occurrences.

The voting phase only guarantees this: **if** a strict majority exists, it *is* the surviving
candidate. It does **not** prove one exists. Whenever the problem does not *guarantee* a
majority, you must run the verification pass; otherwise you can skip it.

## Generalizations

- **> ⌊n/3⌋** (at most two such values): track **two** candidates with two counts.
- **> ⌊n/k⌋** (at most k−1 such values): track **k−1** candidates — this is the
  **Misra–Gries** frequent-items sketch. Verification is mandatory here.

## When to Reach for It

- You need the majority / dominant / "leader" element and want **O(1) space** (beats the
  obvious hash-map counting, which is O(n) space).
- Streaming settings where you cannot store all the data — the voting phase is a natural
  single-pass online algorithm.
- As a **subroutine**: the per-segment majority merges associatively, so it plugs into
  segment trees for subarray-majority queries.

## Complexity

| Metric | Cost |
|--------|------|
| Time   | **O(n)** — one voting pass (plus one O(n) verification pass when required) |
| Space  | **O(1)** — a constant number of candidate/count variables |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Majority Element](problem-01-majority-element/PROBLEM.md) | Find the element appearing more than ⌊n/2⌋ times (majority guaranteed). | Easy |
| 2 | [Majority Element II](problem-02-majority-element-ii/PROBLEM.md) | Find all elements appearing more than ⌊n/3⌋ times using two candidates. | Medium |
| 3 | [Elements More Than ⌊n/k⌋ Times](problem-03-elements-more-than-n-over-k/PROBLEM.md) | Generalize to k−1 candidates (Misra–Gries) and verify. | Medium |
| 4 | [EquiLeader](problem-04-equi-leader/PROBLEM.md) | Count split points where both halves share the same leader (majority). | Medium |
| 5 | [Online Majority Element in Subarray](problem-05-online-majority-element-in-subarray/PROBLEM.md) | Answer subarray-majority queries with a Boyer–Moore segment tree. | Hard |
