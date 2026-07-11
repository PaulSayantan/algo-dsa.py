# Employee Free Time

**Difficulty:** Hard

**Source:** LeetCode 759 — Employee Free Time

## Description

We are given a list `schedule` of employees, where each employee has a list of
**non-overlapping** `Interval`s sorted by start, representing their working
(busy) hours.

Return the list of finite intervals representing the **common free time** for
**all** employees, also sorted by start. In other words, return every maximal
interval during which *no* employee is working, excluding the unbounded free time
before the earliest work and after the latest work.

An `Interval` has integer fields `start` and `end` with `start < end`. Free-time
intervals of length zero (where one employee's shift ends exactly when the common
busy period resumes) should **not** be included.

## Constraints

- `1 <= schedule.length, schedule[i].length <= 50`
- `0 <= schedule[i][j].start < schedule[i][j].end <= 10^8`
- Each employee's intervals are non-overlapping and sorted by start.

## Examples

**Example 1**

```
Input:  schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: Flattening all busy intervals gives [1,2],[1,3],[4,10],[5,6].
             Merging overlaps yields the busy blocks [1,3] and [4,10].
             The only gap between merged busy blocks is [3,4], so everyone is
             free from 3 to 4. (Time before 1 and after 10 is unbounded and
             therefore excluded.)
```

**Example 2**

```
Input:  schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
Explanation: Merged busy blocks are [1,5], [6,7], and [9,12].
             The gaps between them are [5,6] (between [1,5] and [6,7]) and
             [7,9] (between [6,7] and [9,12]).
```

**Example 3**

```
Input:  schedule = [[[1,4]],[[2,4]],[[3,4]],[[5,7]]]
Output: [[4,5]]
Explanation: Merged busy blocks are [1,4] and [5,7], leaving the single gap [4,5].
```

## Hint

The employee boundaries are a red herring — flatten every interval from every
employee into one list and apply **Merge Intervals**. Sort all intervals by start,
merge overlaps into disjoint busy blocks, and the answer is precisely the **gaps
between consecutive merged blocks**.
