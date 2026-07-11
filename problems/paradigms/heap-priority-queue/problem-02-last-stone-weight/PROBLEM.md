# Last Stone Weight

**Difficulty:** Easy

**Source:** LeetCode 1046 (Last Stone Weight)

## Description

You are given an array of integers `stones` where `stones[i]` is the weight of the
`i`-th stone.

We are playing a game with the stones. On each turn, we choose the **two heaviest**
stones and smash them together. Suppose the two heaviest stones have weights `x` and `y`
with `x <= y`. The result of the smash is:

- If `x == y`, both stones are **destroyed**.
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new
  weight `y - x`.

At the end of the game, **at most one** stone remains. Return the weight of that
remaining stone, or `0` if there are no stones left.

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Examples

### Example 1

```
Input:  stones = [2, 7, 4, 1, 8, 1]
Output: 1
```

Explanation:
```
Smash 7 and 8 -> 1, stones = [2, 4, 1, 1, 1]
Smash 2 and 4 -> 2, stones = [2, 1, 1, 1]
Smash 2 and 1 -> 1, stones = [1, 1, 1]
Smash 1 and 1 -> 0, stones = [1]
```
The last stone has weight **1**.

### Example 2

```
Input:  stones = [1]
Output: 1
```

Explanation: There is only one stone, so no smash ever happens and it remains with
weight **1**.

### Example 3

```
Input:  stones = [3, 3]
Output: 0
```

Explanation: The two heaviest (and only) stones are equal (`3 == 3`), so both are
destroyed and nothing remains, giving **0**.

## Hint

Use a **Heap / Priority Queue**. You repeatedly need the *two largest* current stones,
so a **max-heap** lets you pop the top two in `O(log n)` each and push the difference
back — no re-sorting the whole pile every turn.
