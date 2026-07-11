# Number of Ways to Wear Different Hats to Each Other

**Difficulty:** Hard

**Source:** LeetCode 1434 (Number of Ways to Wear Different Hats to Each Other)

## Description

There are `n` people and `40` types of hats labeled `1` to `40`.

You are given a list `hats`, where `hats[i]` is a list of all the hat types that
person `i` likes. Assign each person **exactly one** hat that they like, such
that **no two people wear the same type of hat**.

Return the number of ways to make this assignment. Since the answer may be very
large, return it **modulo `10^9 + 7`**.

## Constraints

- `n == len(hats)`
- `1 <= n <= 10`
- `1 <= len(hats[i]) <= 40`
- `1 <= hats[i][j] <= 40`
- `hats[i]` contains a list of **unique** integers.

## Examples

### Example 1

```
Input: hats = [[3, 4], [4, 5], [5]]
Output: 1
```

Explanation: There is only one way to assign the hats. Person 2 can only wear
hat 5, which forces person 1 to wear hat 4, which forces person 0 to wear
hat 3. Result: `(3, 4, 5)`.

### Example 2

```
Input: hats = [[3, 5, 1], [3, 5]]
Output: 4
```

Explanation: The four valid assignments (person 0's hat, person 1's hat) are
`(3, 5)`, `(5, 3)`, `(1, 3)`, and `(1, 5)`.

### Example 3

```
Input: hats = [[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]
Output: 111
```

Explanation: There are 111 distinct ways to give every one of the 5 people a
hat they like with no repeated hat type.

## Hint

`n <= 10` people but up to `40` hats — so mask over **people**, not hats.
Process hats one at a time and let the bitmask record which people already have
a hat. This is **Bitmask DP** (an assignment / matching DP).
