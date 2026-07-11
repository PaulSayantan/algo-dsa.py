# Bucket Sort

**Bucket Sort** is a distribution-based sorting technique. Instead of comparing
elements directly, it scatters the input into a number of *buckets* (sub-ranges
of the key space), sorts each bucket individually (often with a simpler sort or
recursively), and then concatenates the buckets in order to produce the final
result.

## The Core Idea

```
1. Create k empty buckets.
2. For each element, compute a bucket index from its key
   (e.g. index = floor(k * value) for values in [0, 1)).
3. Place the element into that bucket.
4. Sort every bucket (insertion sort, built-in sort, or recursion).
5. Walk the buckets in order and concatenate their contents.
```

The magic is in step 2: if you can map keys to buckets so the elements spread
out **uniformly**, each bucket ends up tiny and the per-bucket sort is nearly
free.

## When to Reach for Bucket Sort

- The keys are (or can be normalized to) a **bounded, roughly uniform** range —
  floating point numbers in `[0, 1)`, exam scores in `[0, 100]`, ages, etc.
- You are sorting or grouping **by frequency / count**, where the count itself
  is a small integer in `[0, n]`. Frequency is a perfect bucket index, and this
  is the most common interview flavor of the technique (Top-K frequent, sort by
  frequency, H-index).
- You want to beat the `O(n log n)` comparison-sort lower bound by exploiting
  structure in the keys, achieving average-case **O(n + k)**.

## Complexity

| Case    | Time         | Notes                                                   |
|---------|--------------|---------------------------------------------------------|
| Best    | `O(n + k)`   | Elements spread evenly, ~1 element per bucket.          |
| Average | `O(n + k)`   | Uniform distribution over `k` buckets.                  |
| Worst   | `O(n^2)`     | Every element lands in one bucket (adversarial input).  |

**Space:** `O(n + k)` for the buckets. Bucket sort is *not* in-place, and the
per-bucket sort determines whether it is stable.

The worst case is why bucket sort is a poor *general-purpose* comparison sort,
but a superb tool when you know the key distribution — especially the
"index a bucket by an integer count" pattern that shows up constantly in
frequency problems.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort Characters By Frequency](problem-01-sort-characters-by-frequency/PROBLEM.md) | Reorder a string so more frequent characters come first, bucketing by count. | Medium |
| 2 | [H-Index](problem-02-h-index/PROBLEM.md) | Find a researcher's H-index by bucketing papers by citation count. | Medium |
| 3 | [Top K Frequent Elements](problem-03-top-k-frequent-elements/PROBLEM.md) | Return the `k` most frequent values using frequency buckets in `O(n)`. | Medium |
| 4 | [Maximum Gap](problem-04-maximum-gap/PROBLEM.md) | Largest gap between successive sorted values, via pigeonhole buckets in `O(n)`. | Hard |
| 5 | [Contains Duplicate III](problem-05-contains-duplicate-iii/PROBLEM.md) | Detect near-duplicate values within index/value windows using value buckets. | Hard |
