# Trapping Rain Water — Solution

## Brute Force

For each index, the water it holds is `min(max_left, max_right) - height[i]` (if
positive). Compute the two maxima by scanning outward each time.

```python
def brute(height):
    n = len(height)
    total = 0
    for i in range(n):
        left = max(height[:i + 1])
        right = max(height[i:])
        total += min(left, right) - height[i]
    return total
```

- **Time:** `O(n^2)` (a scan for each index).
- **Space:** `O(1)` beyond the input slices.

(An easy `O(n)` improvement precomputes `prefix_max` and `suffix_max` arrays, or
uses the two-pointer method. Below is the monotonic-stack view, which computes
the water *layer by horizontal layer*.)

## Optimal Approach (Monotonic Stack)

Keep a stack of **indices** whose heights are **decreasing** from bottom to top.
Walk left to right. When the current bar `height[i]` is taller than the bar on
top of the stack, that current bar can act as a **right wall** for water sitting
above the popped bar:

1. Pop the top index `bottom` (the floor of a potential basin).
2. If the stack is now empty there is no left wall, so stop.
3. Otherwise the new top `left` is the left wall. The water is a horizontal slab:
   - bounded width `= i - left - 1`
   - bounded height `= min(height[left], height[i]) - height[bottom]`
   - add `width * bounded_height` to the total.
4. Repeat while `height[i]` still exceeds the new top.
5. Push `i`.

```python
def optimal(height):
    stack = []   # indices, heights decreasing bottom -> top
    total = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = i - left - 1
            bounded = min(height[left], h) - height[bottom]
            total += width * bounded
        stack.append(i)
    return total
```

### Why it is correct

The stack holds descending "walls" awaiting a taller bar on the right. When `h`
exceeds the top, the popped bar `bottom` is the floor of a basin whose right wall
is `i` and whose left wall is the next stacked bar `left`. Water fills the slab
between them at height `min(height[left], h)` minus the floor `height[bottom]`.
By always subtracting the floor already accounted for, successive pops add the
water in **horizontal layers**, never double-counting. Every unit of trapped
water is added exactly once, when its enclosing right wall is first encountered.

### Step-by-step on `[4, 2, 0, 3, 2, 5]`

| i | h | action                                                        | added | total | stack after |
|---|---|---------------------------------------------------------------|-------|-------|-------------|
| 0 | 4 | push                                                          | 0     | 0     | [0]         |
| 1 | 2 | push (2 < 4)                                                  | 0     | 0     | [0,1]       |
| 2 | 0 | push (0 < 2)                                                  | 0     | 0     | [0,1,2]     |
| 3 | 3 | pop 2 (h=0): left=1,w=3-1-1=1,bd=min(2,3)-0=2 -> +2; pop 1 (h=2): left=0,w=3-0-1=2,bd=min(4,3)-2=1 -> +2 | 4 | 4 | [0,3] |
| 4 | 2 | push (2 < 3)                                                  | 0     | 4     | [0,3,4]     |
| 5 | 5 | pop 4 (h=2): left=3,w=5-3-1=1,bd=min(3,5)-2=1 -> +1; pop 3 (h=3): left=0,w=5-0-1=4,bd=min(4,5)-3=1 -> +4 | 5 | 9 | [0,5] |

Total trapped water is `9`.

- **Time:** `O(n)` — each index is pushed once and popped once.
- **Space:** `O(n)` for the stack.

## Key Insights & Edge Cases

- Water is added **horizontally** here (layer by layer), unlike the prefix/suffix
  or two-pointer methods which add it vertically (column by column). All three
  give the same total.
- After popping `bottom`, if the stack is empty there is no left wall, so that
  water spills off the left edge — break out.
- Use `<` (strict) to pop; equal-height bars trap no water between them but the
  bookkeeping stays correct because `bounded` becomes `0` for equal walls.
- Fewer than 3 bars, monotonic non-decreasing, or monotonic non-increasing
  inputs all trap `0` water.
- The two-pointer method solves this in `O(n)` time and `O(1)` space and is worth
  knowing, but the stack framing is the one that generalizes to the "next
  greater/smaller wall" family.
