# Round-Robin Print Spooler

**Difficulty:** Easy

**Source:** Classic — round-robin scheduling simulation

## Description

A printer serves jobs round-robin. Each job is `[job_id, pages]`. In one turn the printer prints up to `quantum` pages of the front job; if the job still has pages left it goes to the back of the queue, otherwise it is done. Given the initial `jobs` (in queue order) and the `quantum`, return the list of `job_id`s in the order they finish.

## Examples

### Example 1

```
Input:  jobs = [[1, 3], [2, 1], [3, 2]], quantum = 1
Output: [2, 3, 1]
```

**Explanation:** Job 2 (1 page) finishes first, then job 3, then job 1.

## Hint

deque of [id, pages_left]; subtract min(quantum, pages), re-enqueue if any remain, else record it.
