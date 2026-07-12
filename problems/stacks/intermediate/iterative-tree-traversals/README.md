# Iterative Tree Traversals

Recursion uses the call stack implicitly; you can make that stack explicit to traverse a tree iteratively (and avoid recursion-depth limits). Inorder walks left then pushes ancestors, preorder emits on the way down, and postorder is a reversed 'root-right-left' walk — each an O(n) stack routine.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Binary Tree Inorder Traversal](problem-01-inorder/PROBLEM.md) | Iterative inorder | Medium |
| 2 | [Binary Tree Preorder Traversal](problem-02-preorder/PROBLEM.md) | Iterative preorder | Medium |
| 3 | [Binary Tree Postorder Traversal](problem-03-postorder/PROBLEM.md) | Iterative postorder | Medium |
| 4 | [Binary Search Tree Iterator](problem-04-bst-iterator/PROBLEM.md) | Controlled iterative inorder (left-spine stack) | Medium |
| 5 | [Kth Smallest Element in a BST](problem-05-kth-smallest-in-a-bst/PROBLEM.md) | Iterative inorder with early stop | Medium |
