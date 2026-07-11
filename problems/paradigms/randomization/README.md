# Randomization

**Randomization** is an algorithmic paradigm that deliberately injects randomness into a
procedure — through shuffling, random sampling, or randomly chosen pivots/witnesses — so
that the *expected* behavior is good regardless of the input. Instead of defending against
a worst-case adversary who could hand-craft a pathological input, a randomized algorithm
makes its own coin flips, so no fixed input can reliably trigger the worst case.

## What it is

There are two broad families:

- **Las Vegas algorithms** always return a correct answer; only the *running time* is
  random (e.g., randomized quicksort, quickselect). The randomness protects the *speed*.
- **Monte Carlo algorithms** run in bounded time but may be *wrong* with small probability
  (e.g., Miller-Rabin primality, randomized min-cut). The randomness protects the *time*,
  and error probability is driven down by repetition.

Many interview-style problems also use randomization simply to sample uniformly at
random from a stream or a dynamic set (reservoir sampling, `getRandom` in O(1)), or to
sample uniformly from a geometric region (rejection sampling).

## When to reach for it

- You need an element **uniformly at random** from a collection that changes or is streamed.
- A deterministic algorithm has a bad worst case that an adversary (or already-sorted /
  adversarial data) can trigger — a random pivot or an initial shuffle removes the
  dependence on input order (e.g., quicksort/quickselect).
- You want a simple algorithm with good *expected* performance and can tolerate variance,
  or a tiny, controllable probability of error.
- You must generate a uniform sample over a region and an exact closed-form is awkward, but
  rejection sampling from an easy enclosing region is simple.

## Typical complexity

- **Fisher-Yates shuffle:** O(n) time, O(1) extra space, provably uniform over all n!
  permutations.
- **Reservoir sampling (size k):** O(n) time over a stream, O(k) space.
- **Randomized quickselect:** O(n) *expected*, O(n^2) worst case (probability vanishingly small).
- **Randomized quicksort:** O(n log n) *expected*, O(n^2) worst case.
- **Rejection sampling:** O(1) *expected* iterations when the accept region is a constant
  fraction of the proposal region.

Randomized algorithms are analyzed with *expected* values and *high-probability* bounds
(via linearity of expectation, indicator variables, and tail inequalities), so the guarantee
is over the algorithm's coin flips, not over the inputs.

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Shuffle an Array](problem-01-shuffle-an-array/PROBLEM.md) | Fisher-Yates uniform shuffle | Medium |
| 2 | [Insert Delete GetRandom O(1)](problem-02-insert-delete-getrandom-o1/PROBLEM.md) | Array + hashmap, uniform index sampling | Medium |
| 3 | [Linked List Random Node](problem-03-linked-list-random-node/PROBLEM.md) | Reservoir sampling (k = 1) over a stream | Medium |
| 4 | [Generate Random Point in a Circle](problem-04-generate-random-point-in-a-circle/PROBLEM.md) | Rejection / inverse-transform sampling | Medium |
| 5 | [Kth Largest Element in an Array](problem-05-kth-largest-element-in-an-array/PROBLEM.md) | Randomized quickselect | Medium |
| 6 | [Sort an Array](problem-06-sort-an-array/PROBLEM.md) | Randomized quicksort (random pivot) | Medium/Hard |
