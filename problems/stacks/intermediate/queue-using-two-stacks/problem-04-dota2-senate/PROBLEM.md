# Dota2 Senate

**Difficulty:** Medium

**Source:** LeetCode 649 — Dota2 Senate

## Description

Given a string `senate` where each character is `'R'` (Radiant) or `'D'` (Dire), senators vote in rounds in the given index order, repeating in the same order across rounds. In each turn the current senator may ban the next senator (from the other party) who still has voting rights; a banned senator loses all future turns. When only one party still has active senators, that party wins. Return `"Radiant"` or `"Dire"`.

## Examples

### Example 1

```
Input:  senate = "RD"
Output: 'Radiant'
```

**Explanation:** `R` at index 0 acts first and bans `D`; only Radiant remains, so Radiant wins.

## Hint

Put each party's senator indices in its own two-stack FIFO queue; each round pop one index from each front, the smaller index bans the other, and re-enqueue the winner with its index bumped by `n` to schedule its next round.
