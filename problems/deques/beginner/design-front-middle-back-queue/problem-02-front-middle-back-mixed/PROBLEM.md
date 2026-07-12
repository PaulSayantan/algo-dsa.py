# Front Middle Back Queue — Mixed Operations

**Difficulty:** Medium

**Source:** LeetCode 1670 — Design Front Middle Back Queue (variant sequence)

## Description

Run a mixed sequence of pushes and pops on the Front-Middle-Back queue, including popping from an empty queue and pushing to the middle of both even- and odd-sized queues, to verify the front-middle rule for both insertion (`len // 2`) and removal (`(len - 1) // 2`).

## Hint

Track the list state after each op; middle insert lands at len//2, middle pop removes (len-1)//2.
