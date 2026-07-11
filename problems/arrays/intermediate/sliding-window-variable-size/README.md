# Sliding Window (Variable Size)

## What it is

The **variable-size sliding window** maintains a contiguous range `[left, right]`
over a sequence (array or string). Unlike the *fixed-size* window (where the
width never changes), here the window **grows** by advancing `right` and
**shrinks** by advancing `left`, so its width adapts until it satisfies a
constraint.

The window carries some running state — a sum, a count of distinct elements, a
frequency map, a count of zeros, etc. As you advance `right` to include a new
element, you update that state. Whenever the window **violates** the constraint
(or once it **satisfies** it, depending on the flavor), you advance `left` to
restore the invariant, updating the state as elements leave.

Two common flavors:

- **Longest window with a property.** Expand `right` always; when the constraint
  breaks, shrink `left` just enough to make it valid again. Record the best
  length whenever the window is valid.
- **Shortest window with a property.** Expand `right` until the window becomes
  valid; then shrink `left` as far as possible while it stays valid, recording
  the best length each time it is valid.

## When to reach for it

Reach for a variable-size sliding window when:

- You are asked for the **longest / shortest / max / min contiguous subarray or
  substring** satisfying a monotone-ish constraint (sum `>=` target, at most `k`
  distinct characters, at most `k` zeros, no repeats, contains all of `t`, ...).
- Growing the window makes the constraint "more satisfied" in one direction and
  shrinking makes it "more satisfied" in the other — i.e. there is a monotone
  boundary you can chase with two pointers.

It is the go-to upgrade over the brute-force "check every subarray" approach and
often turns an `O(n^2)` or `O(n^3)` solution into `O(n)`.

## Typical complexity

- **Time:** `O(n)` — each of `left` and `right` moves forward at most `n` times,
  so the total pointer movement is `O(n)`. With a frequency map the constant may
  include the alphabet size or an `O(1)`/`O(k)` map update.
- **Space:** `O(1)` for numeric windows, or `O(k)` / `O(alphabet)` when a hash
  map or counter tracks the window contents.

## Core template (longest window)

```
left = 0
for right in range(n):
    include arr[right] into window state
    while window is INVALID:
        remove arr[left] from window state
        left += 1
    best = max(best, right - left + 1)   # window [left, right] is valid here
```

## Core template (shortest window)

```
left = 0
for right in range(n):
    include arr[right] into window state
    while window is VALID:
        best = min(best, right - left + 1)
        remove arr[left] from window state
        left += 1
```

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Minimum Size Subarray Sum](problem-01-minimum-size-subarray-sum/PROBLEM.md) | Shortest window with `sum >= target` | Medium |
| 2 | [Longest Substring Without Repeating Characters](problem-02-longest-substring-without-repeating-characters/PROBLEM.md) | Longest window with all-unique chars | Medium |
| 3 | [Max Consecutive Ones III](problem-03-max-consecutive-ones-iii/PROBLEM.md) | Longest window with at most `k` zeros | Medium |
| 4 | [Fruit Into Baskets](problem-04-fruit-into-baskets/PROBLEM.md) | Longest window with at most 2 distinct values | Medium |
| 5 | [Longest Substring with At Most K Distinct Characters](problem-05-longest-substring-with-at-most-k-distinct/PROBLEM.md) | Longest window with at most `k` distinct chars | Medium |
| 6 | [Minimum Window Substring](problem-06-minimum-window-substring/PROBLEM.md) | Shortest window covering a multiset of chars | Hard |
