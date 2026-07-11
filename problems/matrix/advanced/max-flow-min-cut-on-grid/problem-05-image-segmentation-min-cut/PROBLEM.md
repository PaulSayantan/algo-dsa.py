# Image Segmentation Min-Cut

**Difficulty:** Hard

**Source:** Classic (Boykov–Kolmogorov graph-cut segmentation; Kleinberg & Tardos "Image Segmentation" §7.10)

## Description

You are segmenting an `R × C` image. Every pixel must be labeled either **foreground** or
**background**. You are given three inputs:

- `fg[i][j]` — the penalty (cost) of labeling pixel `(i, j)` as **foreground**,
- `bg[i][j]` — the penalty (cost) of labeling pixel `(i, j)` as **background**,
- `sep` — a smoothness penalty charged **once for every pair of orthogonally adjacent
  pixels that receive different labels** (this discourages a noisy, fragmented labeling).

The total cost of a labeling is:

```
  sum over pixels of (chosen label's penalty)
+ sep * (number of orthogonally adjacent pixel pairs with different labels)
```

Return the **minimum possible total cost** over all `2^(R*C)` labelings.

This is the textbook **minimum-cut** formulation. Create a source `S` (the "foreground"
terminal) and sink `T` (the "background" terminal). Connect `S → pixel` with capacity equal
to the pixel's background penalty and `pixel → T` with capacity equal to its foreground
penalty, and connect adjacent pixels with undirected edges of capacity `sep`. Any `S–T` cut
corresponds to a labeling (S-side = foreground, T-side = background), and its capacity is
exactly that labeling's total cost — so the **minimum cut** (= max flow) is the answer.

## Constraints

- `1 <= R, C <= 100`
- `0 <= fg[i][j], bg[i][j] <= 10^6`
- `0 <= sep <= 10^6`
- `fg` and `bg` are both `R × C` matrices of non-negative integers.

## Examples

### Example 1

```
Input:
fg  = [[3, 1]]
bg  = [[1, 4]]
sep = 2
Output: 4
Explanation: Label both pixels foreground. Data cost = fg[0][0] + fg[0][1] = 3 + 1 = 4.
The two pixels share the same label, so no separation penalty is charged. Total = 4.
(Making pixel (0,0) background and (0,1) foreground also costs 1 + 1 + 2 = 4; nothing
does better.)
```

### Example 2

```
Input:
fg  = [[1, 5],
       [5, 1]]
bg  = [[5, 1],
       [1, 5]]
sep = 1
Output: 8
Explanation: Each pixel prefers its cheaper label: (0,0)->FG(1), (0,1)->BG(1),
(1,0)->BG(1), (1,1)->FG(1) for data cost 4. All four adjacent pairs then differ,
adding 4*sep = 4. Total = 8. Forcing all pixels to one label costs 12, so 8 is optimal.
```

### Example 3

```
Input:
fg  = [[3]]
bg  = [[5]]
sep = 100
Output: 3
Explanation: A single pixel has no neighbors, so sep never applies. Choose the cheaper
label: foreground costs 3, background costs 5. Minimum total cost = 3.
```

## Hint

Turn the two labels into a source and a sink terminal; a pixel's label is decided by which
side of an `S–T` cut it lands on. Data penalties become terminal-edge capacities and the
smoothness penalty becomes inter-pixel edge capacity — then **Max-Flow / Min-Cut on Grid**
gives the minimum-cost labeling.
