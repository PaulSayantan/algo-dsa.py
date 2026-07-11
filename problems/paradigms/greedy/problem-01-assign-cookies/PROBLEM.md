# Assign Cookies

**Difficulty:** Easy

**Source:** LeetCode 455 (Assign Cookies)

## Description

Assume you are a parent and want to give cookies to your children. Each child `i`
has a **greed factor** `g[i]`, the minimum size of a cookie that will make that
child content. Each cookie `j` has a **size** `s[j]`. If `s[j] >= g[i]`, you can
assign cookie `j` to child `i`, and that child will be content.

Each child can receive **at most one** cookie, and each cookie can be given to **at
most one** child. Your goal is to maximize the number of content children.

Return the maximum number of children you can make content.

## Constraints

- `1 <= g.length <= 3 * 10^4`
- `0 <= s.length <= 3 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  g = [1, 2, 3], s = [1, 1]
Output: 1
```

Explanation: You have 3 children with greed factors 1, 2, 3 and only 2 cookies of
size 1. You can satisfy the child with greed factor 1 using a size-1 cookie. The
remaining size-1 cookie is too small for the children needing size 2 or 3, so only
**1** child can be content.

### Example 2

```
Input:  g = [1, 2], s = [1, 2, 3]
Output: 2
```

Explanation: You have 2 children with greed factors 1 and 2, and 3 cookies of sizes
1, 2, 3. Give the size-1 cookie to the child with greed 1 and the size-2 (or 3)
cookie to the child with greed 2. Both children are content, so the answer is **2**.

### Example 3

```
Input:  g = [10, 9, 8, 7], s = [5, 6, 7, 8]
Output: 2
```

Explanation: Sorted greed is [7, 8, 9, 10] and sorted sizes are [5, 6, 7, 8]. Cookie
7 satisfies greed 7, cookie 8 satisfies greed 8; cookies 5 and 6 are too small for
anyone. Two children are content.

## Hint

Sort both arrays and use a **Greedy** matching: hand the smallest cookie that fits
to the least greedy remaining child, so no cookie is "wasted" on a child a smaller
cookie could have satisfied.
