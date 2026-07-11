# Sliding Window

## What it is

The **Sliding Window** technique maintains a *moving contiguous range* (a "window")
over a sequence — an array or a string — and updates an aggregate about that range
**incrementally** as the window moves, instead of recomputing it from scratch.

A window is defined by two indices, typically `left` and `right`. As `right` advances
we **include** a new element into our running state (sum, character counts, distinct
count, ...). When some condition is violated (or a fixed size is exceeded) we advance
`left` and **remove** the element leaving the window. Because each element is added
once and removed at most once, the whole scan is linear.

There are two common flavors:

- **Fixed-size window** — the window always spans exactly `k` elements. Slide by
  adding the incoming element and subtracting the outgoing one.
- **Variable-size window** — the window grows and shrinks to satisfy a constraint
  (e.g. "at most K distinct chars", "sum ≥ target"). You expand `right` to include
  more, and contract `left` while the constraint is broken or to search for a better
  answer.

## When to reach for it

Reach for Sliding Window when **all** of these hold:

- The problem is about a **contiguous** subarray / substring (not subsequences).
- You are asked for an optimum (longest / shortest / max sum / count) or an
  existence check over such windows.
- The aggregate for a window can be updated **incrementally** in O(1) (or O(1)
  amortized) when one element enters or leaves — sums, frequency counts, a running
  max via a monotonic deque, etc.

A brute force over all subarrays is O(n^2) or O(n^2 · k). Sliding Window usually
collapses this to **O(n)** time (sometimes O(n · Σ) where Σ is a small alphabet)
and **O(1)** or **O(Σ)** extra space.

## Core template (variable window)

```
left = 0
for right in range(n):
    include(a[right])            # extend the window
    while window_is_invalid():
        remove(a[left])          # shrink from the left
        left += 1
    update_answer(left, right)   # window [left, right] is now valid
```

## Problems

| # | Problem | Technique flavor | Difficulty |
|---|---------|------------------|------------|
| 1 | [Maximum Average Subarray I](problem-01-maximum-average-subarray/PROBLEM.md) | Fixed-size window running sum | Easy |
| 2 | [Longest Substring Without Repeating Characters](problem-02-longest-substring-without-repeating/PROBLEM.md) | Variable window + last-seen map | Medium |
| 3 | [Minimum Size Subarray Sum](problem-03-minimum-size-subarray-sum/PROBLEM.md) | Variable window, shrink while sum ≥ target | Medium |
| 4 | [Permutation in String](problem-04-permutation-in-string/PROBLEM.md) | Fixed window + frequency match | Medium |
| 5 | [Longest Repeating Character Replacement](problem-05-longest-repeating-character-replacement/PROBLEM.md) | Variable window + max-frequency | Medium |
| 6 | [Minimum Window Substring](problem-06-minimum-window-substring/PROBLEM.md) | Variable window + need/have counts | Hard |

Work through them top to bottom — they progress from a plain fixed-size sum to a full
"smallest window covering a multiset" problem that stresses every part of the pattern.
