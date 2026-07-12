# Monotonic Stack

A monotonic stack keeps its elements sorted (increasing or decreasing) by popping every element that would break the order before pushing a new one. Each element is pushed and popped at most once, so a whole family of 'next/previous greater or smaller' problems collapses from O(n²) to O(n). The moment you pop an element, the incoming element is its answer.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Daily Temperatures](problem-01-daily-temperatures/PROBLEM.md) | Next-warmer distance | Medium |
| 2 | [Online Stock Span](problem-02-online-stock-span/PROBLEM.md) | Span via merged pops | Medium |
| 3 | [Previous Smaller Element](problem-03-previous-smaller-element/PROBLEM.md) | Previous smaller | Medium |
| 4 | [Next Greater Element II](problem-04-next-greater-element-ii/PROBLEM.md) | Circular next greater | Medium |
| 5 | [Remove K Digits](problem-05-remove-k-digits/PROBLEM.md) | Greedy digit removal | Medium |
