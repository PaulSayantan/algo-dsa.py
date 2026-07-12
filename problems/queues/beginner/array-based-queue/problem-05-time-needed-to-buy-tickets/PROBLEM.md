# Time Needed to Buy Tickets

**Difficulty:** Easy

**Source:** LeetCode 2073 — Time Needed to Buy Tickets

## Description

There are `n` people in a line queuing to buy tickets, where the `0`-th person is at the **front** and the `(n - 1)`-th person is at the **back**. You are given a 0-indexed array `tickets` where `tickets[i]` is the number of tickets the `i`-th person wants to buy.

Each person takes exactly **1 second** to buy a single ticket. A person can only buy **1 ticket at a time** and then must go to the **back** of the line (still queuing) to buy more. If a person has no tickets left to buy, they leave the line.

Return the number of seconds it takes for the person at position `k` (0-indexed) to finish buying all their tickets.

Constraints: `1 <= tickets.length <= 100`, `1 <= tickets[i] <= 100`, `0 <= k < tickets.length`.

## Examples

### Example 1

```
Input:  tickets = [2, 3, 2], k = 2
Output: 6
```

**Explanation:** Round 1 serves everyone once (3 s), leaving `[1, 2, 1]`. Round 2 serves everyone once again (3 s), and person 2 buys their last ticket on that pass, finishing at second 6.

## Hint

Model the line as a FIFO queue of `(index, remaining)`: dequeue the front, spend 1 second, and if that person still needs more, enqueue them at the rear. Stop the moment person `k` reaches 0 remaining.
