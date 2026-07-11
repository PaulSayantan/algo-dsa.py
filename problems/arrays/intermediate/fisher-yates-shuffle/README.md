# Fisher–Yates Shuffle

The **Fisher–Yates shuffle** (also called the **Knuth shuffle**) produces an
**unbiased** random permutation of an array **in place** in **O(n)** time using
**O(1)** extra space. Every one of the `n!` possible orderings is generated with
exactly equal probability `1/n!`.

The core loop walks from the last index down to the first. At each position `i` it
picks a uniformly random index `j` in the range `[0, i]` (inclusive) and swaps
`arr[i]` with `arr[j]`. Once `arr[i]` is fixed, index `i` is never touched again:

```
for i from n-1 down to 1:
    j = random integer in [0, i]     # note: inclusive of i
    swap(arr[i], arr[j])
```

## Why it is unbiased

By induction, after choosing the element for position `i`, each of the `i+1`
remaining candidates is equally likely to have landed there. The probability that any
particular element ends up in a particular slot is exactly `1/n`, and the joint
distribution over all slots is uniform over all `n!` permutations.

Contrast this with the **naive** shuffle that picks `j` from the *full* range
`[0, n-1]` every iteration: that variant produces `n^n` equally likely swap
sequences, which does **not** divide evenly into `n!` outcomes, so some permutations
become more likely than others. The subtle "`[0, i]` inclusive" bound is what makes
Fisher–Yates correct.

## When to reach for it

- You need a **uniform random permutation** or to **shuffle a deck / playlist / test
  set** with provably no bias.
- You need to **sample `k` distinct items without replacement** — run only the first
  `k` iterations (a *partial* Fisher–Yates).
- You need to pick random items from a huge virtual range **without materializing it**
  — combine Fisher–Yates with a **hash map** that records only the swaps performed.
- You want to **randomize input** before a fixed-pivot Quick Sort / Quickselect to
  dodge adversarial worst cases.

Prefer **reservoir sampling** instead when the input is a stream of unknown length, or
when `n` is enormous and you only need a few samples but cannot random-access elements.

## Complexity

| Aspect            | Value                                   |
|-------------------|-----------------------------------------|
| Time              | O(n) (O(k) for a partial shuffle of k)  |
| Extra space       | O(1) in place (O(k) if map-backed)      |
| Distribution      | Uniform over all n! permutations        |
| Random calls      | n - 1 (one per iteration)               |

## Problems

| # | Problem | Technique | Difficulty |
|---|---------|-----------|------------|
| 1 | [Generate a Random Permutation](problem-01-generate-random-permutation/PROBLEM.md) | Textbook in-place Fisher–Yates | Easy |
| 2 | [Shuffle an Array](problem-02-shuffle-an-array/PROBLEM.md) | Fisher–Yates with reset to original | Medium |
| 3 | [Sample K Distinct Elements](problem-03-sample-k-distinct-elements/PROBLEM.md) | Partial Fisher–Yates (first k swaps) | Medium |
| 4 | [Random Pick with Blacklist](problem-04-random-pick-with-blacklist/PROBLEM.md) | Fisher–Yates-style remap into a hash map | Medium |
| 5 | [Random Flip Matrix](problem-05-random-flip-matrix/PROBLEM.md) | Map-backed Fisher–Yates over a virtual array | Hard |
