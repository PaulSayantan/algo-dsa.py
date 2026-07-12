# Design Front Middle Back Queue

This design problem stresses precise index arithmetic at three access points — front, middle, and back. The subtle rule is the middle: when the queue holds an even number of elements the "middle" is the **front** of the two central positions (floor). Concretely, `pushMiddle` inserts at index `len // 2` and `popMiddle` removes index `(len - 1) // 2`. A production implementation keeps two balanced deques for O(1) ops; here correctness of the semantics is the focus.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design Front Middle Back Queue](problem-01-front-middle-back-queue/PROBLEM.md) | Front/middle/back indexing | Medium |
| 2 | [Front Middle Back Queue — Mixed Operations](problem-02-front-middle-back-mixed/PROBLEM.md) | Even/odd middle rule | Medium |
| 3 | [Front Middle Back Queue — Peek Operations](problem-03-front-middle-back-peek/PROBLEM.md) | Non-destructive front/middle/back reads | Easy |
| 4 | [Drain a Queue From the Middle](problem-04-drain-middle-order/PROBLEM.md) | Repeated popMiddle order | Easy |
| 5 | [Build a Queue by Middle Insertion](problem-05-build-by-middle-insert/PROBLEM.md) | Repeated pushMiddle order | Easy |
