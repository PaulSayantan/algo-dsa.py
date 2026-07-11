# Sort the People

**Difficulty:** Easy

**Source:** LeetCode 2418 — "Sort the People".

## Description

You are given an array of strings `names` and an array `heights` that are of the **same length**.
For each index `i`, `names[i]` is the name of a person and `heights[i]` is their height in
centimeters. All the heights are **distinct**.

Return `names` sorted in **descending order** by the people's heights. In other words, the returned
list must list the tallest person first, then the next tallest, and so on.

Implement the reordering with **Selection Sort**: on each pass, find the person with the maximum
remaining height and move them to the next output position, keeping `names` and `heights` in step.

## Constraints

- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lowercase and uppercase English letters.
- All the values of `heights` are **distinct**.

## Examples

### Example 1

```
Input:  names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
Output: ["Mary", "Emma", "John"]
```

**Explanation:** Sorting by descending height gives `180 (Mary) > 170 (Emma) > 165 (John)`, so the
names come out as `["Mary", "Emma", "John"]`.

### Example 2

```
Input:  names = ["Alice", "Bob", "Bob"], heights = [155, 185, 150]
Output: ["Bob", "Alice", "Bob"]
```

**Explanation:** Heights sorted descending are `185, 155, 150`. The person of height `185` is the
first `"Bob"`, then `"Alice"` (155), then the second `"Bob"` (150). Duplicate *names* are fine
because we order strictly by the distinct heights.

### Example 3

```
Input:  names = ["Zoe"], heights = [42]
Output: ["Zoe"]
```

**Explanation:** A single person is trivially already in sorted order.

## Hint

Use **Selection Sort** on the heights, but every time you swap two heights, swap the corresponding
names at the same indices so the two parallel arrays stay aligned. Since you want tallest-first,
select the **maximum** each pass instead of the minimum.
