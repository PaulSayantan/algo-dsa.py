# FIFO Simulation

Many scheduling and service problems are just a FIFO queue driven forward one step at a time: pull the item at the front, do a bounded amount of work, and either finish it or send it to the back. Modeling round-robin printing or a ticket line this way turns a fiddly word problem into a short, obviously correct loop over a `deque`.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Round-Robin Print Spooler](problem-01-print-spooler/PROBLEM.md) | Round-robin FIFO | Easy |
| 2 | [Time Needed to Buy Tickets](problem-02-time-to-buy-tickets/PROBLEM.md) | Queue-driven simulation | Easy |
| 3 | [Students Unable to Eat Lunch](problem-03-students-unable-to-eat-lunch/PROBLEM.md) | Serve-or-rotate FIFO | Easy |
| 4 | [Task Dispatch Log](problem-04-task-dispatch-log/PROBLEM.md) | Round-robin dispatch trace | Easy |
| 5 | [Buffet Serving Station](problem-05-buffet-serving-station/PROBLEM.md) | Serve-or-rotate with depleting resource | Easy |
