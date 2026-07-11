# Boats to Save People

**Difficulty:** Medium

**Source:** LeetCode 881 (Boats to Save People)

## Description

You are given an array `people` where `people[i]` is the weight of the `i`-th person, and
an integer `limit` giving the maximum weight a single boat can carry.

Each boat carries **at most two people at the same time**, provided the sum of their
weights is at most `limit`. Return the **minimum number of boats** needed to carry every
person. (It is guaranteed that every individual weight is at most `limit`, so a solution
always exists.)

## Constraints

- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

## Examples

**Example 1**

```
Input:  people = [1, 2], limit = 3
Output: 1
Explanation: 1 + 2 = 3 <= 3, so both people fit in one boat.
```

**Example 2**

```
Input:  people = [3, 2, 2, 1], limit = 3
Output: 3
Explanation: One optimal set of boats is (1, 2), (2), and (3). The lightest person (1)
pairs with a person of weight 2; the remaining 2 and 3 each need their own boat because
2 + 3 = 5 > 3 and 3 + anything left > 3.
```

**Example 3**

```
Input:  people = [3, 5, 3, 4], limit = 5
Output: 4
Explanation: No two of these people fit together (the two lightest, 3 + 3 = 6 > 5), so
each of the four people needs a separate boat.
```

## Hint

Use **Sorting as Preprocessing**: sort the weights, then use two pointers to greedily try
to pair the **lightest remaining** person with the **heaviest remaining** person.
