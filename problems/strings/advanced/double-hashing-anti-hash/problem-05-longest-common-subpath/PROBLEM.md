# Longest Common Subpath

**Difficulty:** Hard

**Source:** LeetCode 1923 — Longest Common Subpath

## Description

There is a country of `n` cities numbered from `0` to `n - 1`. In this country,
there is a road connecting every pair of cities.

There are `m` friends numbered from `0` to `m - 1` who are traveling through the
country. Each friend's path is given as `paths[i]`, an integer array
representing an **ordered** list of cities the `i`-th friend visits. A path may
visit the same city more than once, but consecutive cities in a path are
distinct.

Given `n` and `paths`, return the length of the **longest common subpath** that
is shared by **every** friend's path. A *subpath* is a contiguous subsequence of
a path. If there is no common subpath at all, return `0`.

Because a subpath is a contiguous block of integers, this is a "longest common
substring across many sequences" problem. The length is **monotone** (if a
common subpath of length `L` exists, so does one of length `L-1`), so we
**binary search** `L`. For each `L`, collect the double hashes of every
length-`L` window of the first path into a set, then intersect with the window
hashes of each other path. Two moduli keep the intersection from being polluted
by hash collisions across many arrays.

## Constraints

- `1 <= n <= 10^5`
- `m == paths.length`
- `2 <= m <= 10^5`
- `1 <= paths[i].length <= 10^5`
- `0 <= paths[i][j] < n`
- The same city number will not appear **consecutively** in a single path.
- The sum of `paths[i].length` is at most `10^5`.

## Examples

**Example 1**

```
Input:  n = 5, paths = [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]
Output: 2
Explanation: The longest common subpath is [2,3]. It appears in all three
paths: positions 2..3 of path 0, positions 0..1 of path 1, and positions 3..4
of path 2. No common subpath of length 3 exists (e.g. [2,3,4] is missing from
the third path).
```

**Example 2**

```
Input:  n = 3, paths = [[0], [1], [2]]
Output: 0
Explanation: The three paths share no city, so no common subpath exists.
```

**Example 3**

```
Input:  n = 5, paths = [[0,1,2,3,4], [4,3,2,1,0]]
Output: 1
Explanation: Each path is the reverse of the other, so the longest common
contiguous subpath is a single city, e.g. [0].
```

## Hint

Use **Double Hashing / Anti-Hash**: binary search the length `L`; for each `L`,
hash every length-`L` window (rolling, two moduli) of every path and keep the
set of hash pairs common to all paths. Double hashing prevents cross-array
collisions from faking a common subpath.
