# Count Collisions on a Road

**Difficulty:** Medium

**Source:** LeetCode 2211 — Count Collisions on a Road

## Description

`directions` is a string where the `i`-th car moves left (`'L'`), right (`'R'`), or stays still (`'S'`). All moving cars travel at the same speed on an infinite line.

- A moving car that reaches a **stationary** car collides and then stays still: `1` collision.
- Two moving cars heading toward each other collide, both stop, and each collision of the pair counts, so a head-on `R`…`L` meeting contributes `2` collisions.

Return the **total number of collisions** that occur. Constraints: `1 <= directions.length <= 10^5`.

## Examples

### Example 1

```
Input:  directions = "RLRSLL"
Output: 5
```

**Explanation:** The first `R` and `L` collide head-on (2). The next `R` hits the now-stopped pile / the `S` (1). Then the two trailing `L`s crash into the stopped mass one after another (2). Total `2 + 1 + 2 = 5`.

## Hint

Push moving cars onto a stack; an approaching `L` or `S` annihilates the `R`s on top just like a left-moving asteroid, and each destroyed car adds to the count.
