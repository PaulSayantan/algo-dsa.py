# Sort the People

**Difficulty:** Medium

*Source: LeetCode 2418 (Sort the People).*

## Description

You are given an array of strings `names` and an array `heights` of **distinct** positive
integers, both of length `n`. For each index `i`, `names[i]` and `heights[i]` denote the name
and height of the `i`-th person.

Return `names` sorted in **descending order by the people's heights**.

For this exercise, implement the reordering with **Bubble Sort**: bubble the `(height, name)`
pairs so that taller people move toward the front, then read off the names.

## Constraints

- `n == names.length == heights.length`
- `1 <= n <= 1000`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lowercase and uppercase English letters.
- All values in `heights` are **distinct**.

## Examples

**Example 1**

```
Input:  names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
Output: ["Mary", "Emma", "John"]
```
Explanation: Mary is tallest (180), then Emma (170), then John (165).

**Example 2**

```
Input:  names = ["Alice", "Bob", "Bob"], heights = [155, 185, 150]
Output: ["Bob", "Alice", "Bob"]
```
Explanation: The person named "Bob" with height 185 is tallest, then "Alice" (155), then the
other "Bob" (150). Note the two "Bob"s are different people; heights are still distinct.

**Example 3**

```
Input:  names = ["Kai"], heights = [42]
Output: ["Kai"]
```
Explanation: A single person is already trivially ordered.

## Hint

Use **Bubble Sort** on the paired data: whenever an adjacent pair has the *shorter* person in
front of the *taller* person, swap the pairs (both the height and its name together). Because
you want descending order, swap when `heights[j] < heights[j+1]`.
