# Implement Queue using Stacks

**Difficulty:** Easy

**Source:** LeetCode 232 — Implement Queue using Stacks

## Description

Implement a first-in-first-out (FIFO) queue using only two stacks. The implemented
queue should support all the standard functions of a normal queue (`push`, `peek`,
`pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` — Pushes element `x` to the back of the queue.
- `int pop()` — Removes the element from the front of the queue and returns it.
- `int peek()` — Returns the element at the front of the queue.
- `boolean empty()` — Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard stack operations — that is, only `push to top`,
  `peek/pop from top`, `size`, and `is empty` are legal.
- Depending on your language, the stack may not be supported natively. You may
  simulate a stack using a list or deque as long as you only use a stack's standard
  operations.

**Follow-up:** Can you implement the queue such that each operation is **amortized**
O(1) time complexity? In other words, performing `n` operations will take overall
O(n) time even though a single operation may take longer.

## Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid (the queue is non-empty when they are
  called).

## Examples

### Example 1

```
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output:
[null, null, null, 1, 1, false]
```

Explanation:
```
MyQueue q = new MyQueue();
q.push(1);   // queue is: [1]
q.push(2);   // queue is: [1, 2]  (leftmost is front)
q.peek();    // returns 1
q.pop();     // returns 1, queue is: [2]
q.empty();   // returns false (2 is still there)
```

### Example 2

```
Input:
["MyQueue", "push", "pop", "empty"]
[[], [7], [], []]

Output:
[null, null, 7, true]
```

Explanation:
```
MyQueue q = new MyQueue();
q.push(7);   // queue is: [7]
q.pop();     // returns 7 (the only element), queue is: []
q.empty();   // returns true (nothing left)
```

## Hint

Use **Amortized Analysis Techniques**. Keep two stacks — an "in" stack for pushes and
an "out" stack for pops. Only transfer elements from `in` to `out` when `out` is empty.
Each element is moved between stacks at most once, so although a single `pop` can cost
O(n), the average cost over a sequence of operations is O(1).
