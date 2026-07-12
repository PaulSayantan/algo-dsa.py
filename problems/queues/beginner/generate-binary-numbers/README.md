# Generate Binary Numbers

Seed a queue with `"1"` and repeatedly dequeue a string `s`, emit it, then enqueue `s+"0"` and `s+"1"`. Because the queue processes shorter strings before longer ones, the emitted sequence is exactly the binary representations of 1, 2, 3, … in order. It is a tidy first taste of BFS-style generation using a queue as the frontier.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Generate Binary Numbers from 1 to N](problem-01-generate-binary-numbers/PROBLEM.md) | Queue as BFS frontier | Easy |
| 2 | [N-th Generated Binary Number](problem-02-nth-binary-number/PROBLEM.md) | Level-order indexing | Easy |
| 3 | [Generate All Binary Strings of Length N](problem-03-binary-strings-length-n/PROBLEM.md) | Fixed-length prefix frontier | Easy |
| 4 | [First N Numbers Using Only Digits 1 and 2](problem-04-numbers-with-digits-one-two/PROBLEM.md) | Two-symbol alphabet BFS | Easy |
| 5 | [Binary Numbers in a Range](problem-05-binary-numbers-in-range/PROBLEM.md) | Level-order range slice | Easy |
