# First Unique / Non-Repeating in a Stream

To report the first element seen exactly once so far — updated after every insertion — pair a **frequency map** with a **deque of candidates** in arrival order. Push each new element to the back and bump its count; the answer is the front of the deque after lazily popping any front whose count has grown past one. Because a value is only ever discarded from the front once (when it stops being unique), the amortized cost per query is O(1), making the whole stream O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [First Non-Repeating Character in a Stream](problem-01-first-unique-char-stream/PROBLEM.md) | Stream first-unique char | Medium |
| 2 | [First Unique Number](problem-02-first-unique-number/PROBLEM.md) | Design: deque + count map | Medium |
| 3 | [First Unique Character in a String](problem-03-first-unique-char-index/PROBLEM.md) | First-unique index via candidate deque | Medium |
| 4 | [First Non-Repeating Word in a Stream](problem-04-first-non-repeating-word/PROBLEM.md) | Per-step first-unique token | Medium |
| 5 | [First Unique Stream Tracker](problem-05-first-unique-per-insertion/PROBLEM.md) | Design: deque + running unique count | Medium |
