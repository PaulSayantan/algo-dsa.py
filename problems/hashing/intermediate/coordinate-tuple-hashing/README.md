# Coordinate / Tuple Hashing

Geometry problems become hashing problems once you pick an exact, integer key: store points as `(x, y)` tuples in a set, hash squared distances (no floats), or hash a slope normalized by its GCD and sign so collinear pairs collide exactly. The recurring trick is turning 'is there a matching point/slope/distance?' into an O(1) set/map lookup.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Max Points on a Line](problem-01-max-points-on-a-line/PROBLEM.md) | GCD-normalized slope keys | Hard |
| 2 | [Number of Boomerangs](problem-02-number-of-boomerangs/PROBLEM.md) | Squared-distance buckets | Medium |
| 3 | [Detect Squares](problem-03-detect-squares/PROBLEM.md) | Point-count map, diagonal corners | Medium |
| 4 | [Minimum Area Rectangle](problem-04-minimum-area-rectangle/PROBLEM.md) | Point-set corner lookup | Medium |
| 5 | [Line Reflection](problem-05-line-reflection/PROBLEM.md) | Mirror lookup in a point set | Medium |
