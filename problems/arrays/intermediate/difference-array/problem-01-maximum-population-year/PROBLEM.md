# Maximum Population Year

**Difficulty:** Easy

**Source:** LeetCode 1854 — Maximum Population Year

## Description

You are given a 2D integer array `logs` where each `logs[i] = [birth_i, death_i]`
indicates the birth and death years of the `i`-th person.

The **population** of some year `x` is the number of people alive during that
year. A person is counted in year `x` if they satisfy `birth_i <= x < death_i`.
In other words, the person is counted in the year they are born but **not** in
the year they die.

Return the **earliest** year with the **maximum** population.

The years in the input fall in the range `[1950, 2050]`.

## Constraints

- `1 <= logs.length <= 100`
- `1950 <= birth_i < death_i <= 2050`

## Examples

### Example 1

```
Input:  logs = [[1993, 1999], [2000, 2010]]
Output: 1993
```

**Explanation:** The years 1993 through 1998 each have a population of 1
(the first person). The years 2000 through 2009 also have a population of 1
(the second person). No year ever reaches a population of 2, so the maximum
population is 1, and the earliest year achieving it is 1993.

### Example 2

```
Input:  logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
Output: 1960
```

**Explanation:** The maximum population is 2, reached in years 1960 (persons 1
and 2 both alive) and 1970 (persons 2 and 3 both alive). Note person 1 dies in
1961 so is not counted in 1961, but person 2 born in 1960 overlaps in 1960.
Between 1960 and 1970 the peak of 2 first occurs in 1960, so return the earliest
such year, 1960.

## Hint

Instead of iterating over every year for every person, record a `+1` at each
birth year and a `-1` at each death year, then sweep. This is the
**Difference Array** technique: the running prefix sum at year `x` is exactly the
population alive in year `x`.
