# Linear Search

**Linear Search** (also called *sequential search*) is the most fundamental search
technique. You walk through a collection one element at a time, from the first
position to the last, comparing each element against what you are looking for. The
moment you find a match (or satisfy some condition) you stop; if you reach the end
without a match, the target is not present.

## When to reach for it

- The data is **unsorted** (binary search needs sorted data — linear search does not care about order).
- The collection is **small**, or you only search occasionally, so building an index / hash map is not worth it.
- You need to **visit every element anyway** — e.g. find the maximum, count occurrences, or aggregate a value. In these cases a single linear pass is optimal.
- The structure only supports **sequential access** (e.g. a singly linked list, a stream, a file read top to bottom).

## Complexity

| Case | Comparisons | Time |
|------|-------------|------|
| Best (target is first / found immediately) | 1 | O(1) |
| Average | ~n/2 | O(n) |
| Worst (target is last or absent) | n | O(n) |

- **Time:** O(n) — proportional to the number of elements.
- **Space:** O(1) — only a loop index / a couple of accumulator variables.

Linear search is the correct choice whenever you cannot exploit structure (sorting,
hashing, indexing) to do better, and it is the baseline every other search algorithm
is compared against.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Linear Search](problem-01-linear-search/PROBLEM.md) | Return the index of a target value in an array, or -1 if absent. | Easy |
| 2 | [Find the Maximum Element](problem-02-find-maximum-element/PROBLEM.md) | Scan once, tracking the largest value seen so far. | Easy |
| 3 | [Count Occurrences of a Value](problem-03-count-occurrences/PROBLEM.md) | Count how many times a target appears in an array. | Easy |
| 4 | [Find Numbers with Even Number of Digits](problem-04-find-numbers-with-even-digits/PROBLEM.md) | Count array elements whose digit-count is even (LeetCode 1295). | Easy |
| 5 | [Richest Customer Wealth](problem-05-richest-customer-wealth/PROBLEM.md) | Scan a 2D grid, summing each row and tracking the maximum (LeetCode 1672). | Easy-Medium |
