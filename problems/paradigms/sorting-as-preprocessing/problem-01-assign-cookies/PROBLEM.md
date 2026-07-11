# Assign Cookies

**Difficulty:** Easy

**Source:** LeetCode 455 (Assign Cookies)

## Description

Assume you are a parent and want to give your children some cookies. Each child can
receive **at most one** cookie.

Each child `i` has a **greed factor** `g[i]`, which is the minimum size of a cookie that
will make that child content. Each cookie `j` has a **size** `s[j]`. If `s[j] >= g[i]`,
you can assign cookie `j` to child `i`, and the child becomes content.

Your goal is to **maximize the number of content children** and return that maximum
number.

## Constraints

- `1 <= g.length <= 3 * 10^4`
- `0 <= s.length <= 3 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

## Examples

**Example 1**

```
Input:  g = [1, 2, 3], s = [1, 1]
Output: 1
Explanation: You have 3 children with greed factors 1, 2, 3 and 2 cookies of size 1.
Only the child with greed factor 1 can be satisfied by a size-1 cookie, so at most
1 child is content.
```

**Example 2**

```
Input:  g = [1, 2], s = [1, 2, 3]
Output: 2
Explanation: You have 2 children with greed factors 1, 2 and 3 cookies of sizes 1, 2, 3.
The size-1 cookie satisfies the greed-1 child and the size-2 cookie satisfies the
greed-2 child, so both children are content.
```

**Example 3**

```
Input:  g = [10, 9, 8, 7], s = [5, 6, 7, 8]
Output: 2
Explanation: After considering all cookies, only the children with greed 7 and 8 can be
satisfied (by cookies of size 7 or 8), so at most 2 children are content.
```

## Hint

Use **Sorting as Preprocessing**: sort both the greed factors and the cookie sizes, then
sweep them together so the smallest adequate cookie always goes to the least greedy
unsatisfied child.
