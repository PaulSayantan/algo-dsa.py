# Recent Counter / Request Throttling

Counting events within a sliding time window is a queue problem: enqueue each event's timestamp and, on every query, dequeue timestamps that have fallen outside the window. The queue length is the count of recent events.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Number of Recent Calls](problem-01-number-of-recent-calls/PROBLEM.md) | Sliding-time-window queue | Easy |
| 2 | [Design Hit Counter](problem-02-design-hit-counter/PROBLEM.md) | Sliding-time-window queue | Medium |
| 3 | [Sliding Window Rate Limiter](problem-03-sliding-window-rate-limiter/PROBLEM.md) | Sliding-window-log throttling | Medium |
| 4 | [Logger Rate Limiter](problem-04-logger-rate-limiter/PROBLEM.md) | Per-key window + queue eviction | Medium |
| 5 | [Throttling Gateway](problem-05-throttling-gateway/PROBLEM.md) | Multi-window request throttling | Medium |
