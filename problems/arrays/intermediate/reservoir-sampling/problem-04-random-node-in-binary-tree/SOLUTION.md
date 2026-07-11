# Solution — Random Node in a Binary Tree

## Brute Force

Traverse once to collect all node values into an array (or first count `n`, then walk to
the random index). Then return a random element.

```python
class Solution:
    def __init__(self, root):
        self.vals = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            self.vals.append(node.val)
            if node.left:  stack.append(node.left)
            if node.right: stack.append(node.right)

    def get_random(self):
        return random.choice(self.vals)
```

- **Time:** `O(n)` to flatten in the constructor; `O(1)` per `get_random`.
- **Space:** `O(n)` for the stored values.

Perfectly good when the tree fits in memory and you can afford to buffer it, but it
requires either counting or storing all `n` nodes — which the problem forbids for the
optimal solution.

## Optimal Approach (Reservoir Sampling, k = 1)

Do **one** traversal (DFS or BFS — order is irrelevant). Maintain a running counter `i`
and a `chosen` value. At the `i`-th visited node, set `chosen = node.val` with probability
`1/i`. After the traversal, return `chosen`.

### Why it is correct

Number the nodes `1..n` in visitation order. Node `j` is the final answer iff it is
adopted at step `j` and never overwritten afterwards:

```
P(node j chosen) = (1/j) · (1 - 1/(j+1)) · ... · (1 - 1/n)
                 = (1/j) · (j/(j+1)) · ... · ((n-1)/n)
                 = (1/j) · (j/n)                 # telescoping
                 = 1/n
```

Because the identity holds for **any** visitation order, the tree's structure and the
traversal strategy do not matter — every node gets probability `1/n`.

### Step-by-step

1. Initialize `chosen = None`, `count = 0`.
2. Traverse the tree (iterative DFS shown below to keep space `O(h)` for the stack; a
   recursive DFS works too).
3. For each visited node: `count += 1`; with probability `1/count` set
   `chosen = node.val`.
4. Return `chosen`.

### Reference implementation

```python
import random
from typing import Optional


class Solution:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.root = root            # no counting, no flattening

    def get_random(self) -> int:
        chosen = None
        count = 0
        stack = [self.root] if self.root else []
        while stack:
            node = stack.pop()
            count += 1
            if random.randint(1, count) == 1:   # keep with prob 1/count
                chosen = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return chosen
```

- **Time:** `O(n)` per `get_random` (one full traversal).
- **Space:** `O(1)` sampler state; the traversal itself uses `O(h)` for the explicit
  stack (`h` = tree height), or the call stack for recursion — inherent to visiting a
  tree and independent of the sampling.

## Key Insights & Edge Cases

- **Traversal order is a free variable.** The `1/i` rule makes the distribution uniform
  regardless of whether you do preorder, inorder, postorder, or BFS. Pick whatever is
  convenient.
- **Single node:** at `count = 1` it is chosen with probability `1`, so a one-node tree
  always returns that value.
- **Skewed / degenerate trees** (essentially a linked list) are handled identically — this
  is exactly the LeetCode 382 linked-list case.
- **1/count, not 1/depth.** The replacement probability is tied to the number of nodes
  *visited so far*, never to depth or subtree size.
- **Space caveat:** the "O(1) extra space" refers to the sampler; visiting a tree needs
  `O(h)` stack space. If you truly need `O(1)` total, a Morris traversal can visit nodes
  without a stack, and the same `1/i` rule still applies.
