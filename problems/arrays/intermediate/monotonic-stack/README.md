# Monotonic Stack

A **monotonic stack** is an ordinary stack that you deliberately keep in sorted
order (either always increasing or always decreasing from bottom to top). Before
you push a new element, you pop every element that would violate the ordering.
That single discipline turns a whole family of "for each element, look sideways
until a condition breaks" problems from `O(n^2)` brute force into a clean
`O(n)` sweep.

## The core idea

Many array problems ask, for every element, a question of the form:

- What is the **next greater** element to my right? (decreasing stack)
- What is the **next smaller** element to my right? (increasing stack)
- What is the **previous greater / previous smaller** element? (scan the other direction)
- How far can I extend before a taller/shorter bar stops me? (histogram, stock span)

In all of these, an element that is "dominated" by a later element can never be
the answer for anything further along, so it can be discarded permanently. The
stack holds exactly the set of elements that are still *candidates*, and each
element is pushed once and popped at most once.

## When to reach for it

Reach for a monotonic stack when:

- You need the **nearest** element (left or right) that is strictly/loosely
  greater or smaller than the current one.
- You are computing a span, a width, or an area bounded by "the first thing
  bigger/smaller in each direction."
- A brute-force solution is a nested loop that walks outward from each index
  until some monotone condition fails.

## Complexity

- **Time:** `O(n)` — each element is pushed once and popped at most once, so the
  total number of stack operations is at most `2n`, even though there is an inner
  `while` loop.
- **Space:** `O(n)` — worst case the entire input sits on the stack (e.g. a
  strictly increasing input for a next-greater query).

A common convention is to store **indices** (not values) on the stack, so you
can recover both the value (`arr[i]`) and the distance/width (`j - i`).

## Problems

| # | Problem | Difficulty | Summary |
|---|---------|------------|---------|
| 1 | [Next Greater Element I](problem-01-next-greater-element-i/PROBLEM.md) | Easy | For each value in a subset, find its next greater element in a second array using a decreasing stack + hash map. |
| 2 | [Daily Temperatures](problem-02-daily-temperatures/PROBLEM.md) | Medium | For each day, how many days until a warmer temperature — classic index-stack "next greater" distance problem. |
| 3 | [Online Stock Span](problem-03-online-stock-span/PROBLEM.md) | Medium | Streaming: count consecutive prior days with price <= today using a stack of (price, span) pairs. |
| 4 | [Next Greater Element II](problem-04-next-greater-element-ii/PROBLEM.md) | Medium | Next greater element in a **circular** array; sweep the array twice with one stack. |
| 5 | [Largest Rectangle in Histogram](problem-05-largest-rectangle-in-histogram/PROBLEM.md) | Hard | Maximal rectangle area under bars using an increasing stack of indices to find each bar's span. |
| 6 | [Trapping Rain Water](problem-06-trapping-rain-water/PROBLEM.md) | Hard | Water trapped between bars, computed layer-by-layer with a decreasing stack of boundaries. |
