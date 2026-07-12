# Reveal Cards in Increasing Order

**Difficulty:** Medium

**Source:** LeetCode 950 — Reveal Cards In Increasing Order

## Description

You are given a `deck` of distinct integer cards. Order the deck so that the following reveal procedure yields the cards in strictly increasing order: repeatedly reveal the top card, then if any cards remain, move the next top card to the bottom of the deck; continue until all cards are revealed. Return the deck ordering (a list) that produces an increasing reveal.

## Examples

### Example 1

```
Input:  deck = [17, 13, 11, 2, 3, 5, 7]
Output: [2, 13, 3, 11, 5, 17, 7]
```

**Explanation:** Revealing the returned ordering with the "reveal top, move next to bottom" rule produces `2, 3, 5, 7, 11, 13, 17`.

## Hint

Simulate the reveal on a FIFO queue of positions (built from two stacks): sort the cards, then for each card pop the front position to place it and rotate the next front position to the back.
