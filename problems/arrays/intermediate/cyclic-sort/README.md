# Cyclic Sort

## What it is

**Cyclic Sort** is an in-place, comparison-free sorting pattern that works when an
array contains `n` numbers drawn from a **known, contiguous range** — classically
`[1..n]` or `[0..n]`. The key observation is that each value has exactly one
"correct" slot: value `v` belongs at index `v` (for a `[0..n-1]` range) or index
`v - 1` (for a `[1..n]` range).

The algorithm walks the array once. At each position `i` it repeatedly swaps the
current element into its correct slot until the element sitting at `i` already
belongs there. Because every swap sends at least one element home permanently, the
total number of swaps is bounded by `n`, giving **O(n)** time and **O(1)** extra
space.

```
i = 0
while i < n:
    correct = nums[i] - 1          # target index for value nums[i]
    if nums[i] != nums[correct]:   # not in place -> swap it home
        nums[i], nums[correct] = nums[correct], nums[i]
    else:
        i += 1                     # already correct (or a duplicate) -> advance
```

## When to reach for it

Reach for Cyclic Sort whenever the problem says something like *"an array of `n`
integers where each value is in the range `1..n` (or `0..n`)"* and asks you to find
a **missing number, a duplicate, all missing numbers, all duplicates, the first
missing positive**, or to sort such an array. The range constraint is the tell: it
lets you use the array's own indices as a hash table, which is how you hit O(1)
extra space.

After placing every value at its home index, a single final scan reveals the answer:
any index `i` whose value is **not** `i + 1` is where the "wrong" value lives —
that mismatch encodes both what is missing and what is duplicated.

## Complexity

| Metric | Cost |
| --- | --- |
| Time  | **O(n)** — each element is placed home at most once; the `while` advances at most `2n` times total |
| Space | **O(1)** — sorting/marking happens in place (output lists, when required, are not counted as extra working space) |

## Problems

| # | Problem | Summary | Difficulty |
| --- | --- | --- | --- |
| 1 | [Cyclic Sort](problem-01-cyclic-sort/PROBLEM.md) | Sort an array containing `1..n` in place, no comparisons | Easy |
| 2 | [Missing Number](problem-02-missing-number/PROBLEM.md) | One number missing from `[0..n]`; find it | Easy |
| 3 | [Find All Disappeared Numbers](problem-03-find-all-disappeared-numbers/PROBLEM.md) | Return every value in `[1..n]` absent from the array | Easy |
| 4 | [Find All Duplicates](problem-04-find-all-duplicates/PROBLEM.md) | Return every value in `[1..n]` that appears twice | Medium |
| 5 | [Set Mismatch](problem-05-set-mismatch/PROBLEM.md) | One value duplicated, one missing; return both | Easy/Medium |
| 6 | [First Missing Positive](problem-06-first-missing-positive/PROBLEM.md) | Smallest absent positive in an arbitrary array, O(n)/O(1) | Hard |
