# Design Browser History

**Difficulty:** Easy

**Source:** LeetCode 1472 — Design Browser History

## Description

Design a browser history for a single tab. You start on the `homepage` and can
visit other URLs, go `back` in history, or move `forward`.

Implement the `BrowserHistory` class:

- `BrowserHistory(homepage)` — initializes the object with the tab's `homepage`.
- `visit(url)` — visits `url` from the current page. This clears all the forward
  history.
- `back(steps)` — moves `steps` back in history, then returns the current URL. If
  you can only move `x` (`x < steps`) steps back, you move only `x` steps and
  return the current URL.
- `forward(steps)` — moves `steps` forward in history, then returns the current
  URL. If you can only move `x` (`x < steps`) steps forward, you move only `x`
  steps and return the current URL.

## Examples

### Example 1

```
Input:
["BrowserHistory", "visit", "visit", "back", "back", "forward", "visit", "forward", "back"]
[["home.com"], ["a.com"], ["b.com"], [1], [1], [1], ["c.com"], [1], [2]]

Output:
[null, null, null, "a.com", "home.com", "a.com", null, "c.com", "home.com"]
```

**Explanation:** After visiting `a.com` then `b.com`, `back(1)` returns `a.com`
and `back(1)` again returns `home.com`. `forward(1)` returns `a.com`. Visiting
`c.com` clears the forward history, so `forward(1)` stays on `c.com`, and
`back(2)` walks back to `home.com`.

## Hint

Use two stacks: a back stack and a forward stack around the current page. `visit`
pushes the current page onto the back stack and clears the forward (redo) stack;
`back`/`forward` move the current page between the two stacks.
