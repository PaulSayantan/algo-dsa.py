# Closest Approach of Two Moving Points

**Difficulty:** Medium

**Source:** Classic computational-geometry / kinematics problem (closest approach)

## Description

Two points move in the plane at constant velocity. Point `A` starts at `(ax, ay)` and
moves with velocity `(vax, vay)` per unit time; point `B` starts at `(bx, by)` and
moves with velocity `(vbx, vby)`. At time `t` their positions are

```
A(t) = (ax + vax * t, ay + vay * t)
B(t) = (bx + vbx * t, by + vby * t)
```

Given a time window `[0, T]`, return the **minimum Euclidean distance** between the two
points over that window, i.e. `min_{0 <= t <= T} |A(t) - B(t)|`.

Let `d(t) = |A(t) - B(t)|`. Then `d(t)^2` is a quadratic in `t` with a non-negative
leading coefficient, hence **convex** — so both `d(t)^2` and `d(t)` are **unimodal** on
`[0, T]`. Answers within an absolute or relative error of `1e-6` are accepted.

## Constraints

- All coordinates and velocity components are real numbers in `[-1000, 1000]`.
- `0 < T <= 10^4`.
- The answer is a real number; tolerance `1e-6`.

## Examples

### Example 1

```
Input:  A = (0, 0),  vA = (1, 0)
        B = (10, 0), vB = (-1, 0)
        T = 10
Output: 0.000000
```

Explanation: The points head toward each other along the x-axis. At `t = 5` both are at
`x = 5`, so they coincide and the distance is `0`.

### Example 2

```
Input:  A = (0, 0), vA = (0, 1)
        B = (5, 0), vB = (0, 1)
        T = 10
Output: 5.000000
```

Explanation: Both points move upward at the same velocity, so their separation never
changes. `d(t) = 5` for all `t`, and the minimum is `5`. (Here `d` is constant — still
unimodal, with the minimum attained everywhere.)

### Example 3

```
Input:  A = (0, 0), vA = (1, 0)
        B = (0, 10), vB = (0, -1)
        T = 10
Output: 7.071068
```

Explanation: `A` slides right along the x-axis while `B` slides down the y-axis. Their
separation is smallest at `t = 5`, where `A = (5, 0)` and `B = (0, 5)`, giving distance
`sqrt(5^2 + 5^2) = sqrt(50) ≈ 7.071068`.

## Hint

`d(t)^2` is a convex quadratic in `t`, so the distance is unimodal over `[0, T]`. Use
**Ternary Search** on the real time interval `[0, T]`, comparing `d(t)` (or `d(t)^2`,
which has the same minimizer) at the two one-third probes.
