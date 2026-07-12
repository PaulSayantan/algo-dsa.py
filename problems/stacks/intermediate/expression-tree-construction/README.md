# Expression Tree Construction

From a postfix token stream you can build a binary expression tree with a stack of subtrees: push a leaf for each operand, and for each operator pop two subtrees, make them its children, and push the new subtree. Evaluating the tree bottom-up reproduces the expression's value.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Build & Evaluate an Expression Tree](problem-01-evaluate-expression-tree-from-postfix/PROBLEM.md) | Subtree stack | Medium |
| 2 | [Postfix to Fully Parenthesized Infix](problem-02-postfix-to-fully-parenthesized-infix/PROBLEM.md) | Inorder walk of subtree stack | Medium |
| 3 | [Infix to Postfix via Expression Tree](problem-03-build-tree-from-infix-to-postfix/PROBLEM.md) | Precedence + subtree stack | Medium |
| 4 | [Build & Evaluate a Prefix Expression Tree](problem-04-evaluate-prefix-expression-tree/PROBLEM.md) | Right-to-left subtree stack | Medium |
| 5 | [Detect a Duplicate Subexpression](problem-05-duplicate-subexpression-detection/PROBLEM.md) | Subtree signatures | Medium |
