# Time Needed to Buy Tickets

**Difficulty:** Easy

**Source:** LeetCode 2073 — Time Needed to Buy Tickets

## Description

There are `n` people in a line to buy tickets; `tickets[i]` is the number of tickets person `i` wants. Each person buys **one** ticket per second and, if they still need more, immediately goes to the back of the line. Return the number of seconds it takes for the person at position `k` to finish buying all their tickets.

## Examples

### Example 1

```
Input:  tickets = [2, 3, 2], k = 2
Output: 6
```

### Example 2

```
Input:  tickets = [5, 1, 1, 1], k = 0
Output: 8
```

## Hint

Simulate the queue by index; each second the front buys one and rejoins the back unless done. Stop when k finishes.
