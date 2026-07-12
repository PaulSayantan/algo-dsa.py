# Robot Collisions

**Difficulty:** Medium

**Source:** LeetCode 2751 — Robot Collisions

## Description

There are `n` 1-indexed robots on a line, each with a unique starting position in `positions`, a `healths` value, and a moving direction in `directions` (each character `'L'` or `'R'`). All robots move simultaneously at the same speed. When two robots moving toward each other collide, the one with **lower** health is removed and the survivor loses `1` health; if healths are equal, **both** are removed. Robots moving the same way never collide.

Return the healths of the surviving robots, ordered by their **original index** in the input. All positions are distinct.

## Examples

### Example 1

```
Input:  positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
Output: [14]
```

**Explanation:** In position order the right-movers are index 2 (`R`, health 15) then index 0 (`R`, health 10). The left-mover index 1 (`L`, health 10) hits index 0 with equal health, so both die. The next left-mover index 3 (`L`, health 12) then hits index 2 (health 15); index 2 wins and drops to 14. Only that robot survives, so the answer is `[14]`.

## Hint

Sort robots by position and push right-movers onto a stack; a left-mover fights the stack top exactly like a negative asteroid annihilating positive survivors.
