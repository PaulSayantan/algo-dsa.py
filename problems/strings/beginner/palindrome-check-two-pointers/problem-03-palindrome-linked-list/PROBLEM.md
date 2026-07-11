# Palindrome Linked List

**Difficulty:** Easy (borderline Medium — O(1)-space variant)

**Source:** LeetCode 234 — Palindrome Linked List

## Description

Given the `head` of a singly linked list, return `True` if the list is a
palindrome (its values read the same front-to-back as back-to-front), or
`False` otherwise.

A follow-up asks you to solve it in **O(n)** time and **O(1)** extra space,
i.e. without copying all values into another container.

## Constraints

- The number of nodes in the list is in the range `[1, 10^5]`.
- `0 <= Node.val <= 9`

## Examples

### Example 1
```
Input:  head = [1, 2, 2, 1]
Output: True
Explanation: Reading forward gives 1,2,2,1; reading backward gives the same
             sequence, so it is a palindrome.
```

### Example 2
```
Input:  head = [1, 2]
Output: False
Explanation: Forward is 1,2 but backward is 2,1, so the first and last
             values (1 and 2) do not match.
```

### Example 3
```
Input:  head = [1, 2, 3, 2, 1]
Output: True
Explanation: The odd-length list mirrors around the middle value 3, so it
             reads the same in both directions.
```

## Hint

Use the **Palindrome Check (two pointers)** technique. A singly linked list
cannot be indexed from the end, so first use a slow/fast pointer pair to find
the middle, reverse the second half in place, then walk one pointer from the
head and one from the (reversed) tail comparing values as they move inward.
