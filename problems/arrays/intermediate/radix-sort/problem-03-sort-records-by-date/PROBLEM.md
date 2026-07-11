# Sort Records by Date

**Difficulty:** Medium

**Source:** Classic (CLRS, Section 8.3 — multi-key stable sort; the "sort cards
by columns" application)

## Description

You are given a list of date records, each a tuple `(day, month, year)`
representing a calendar date. Sort the records into chronological order: primary
key is `year`, then `month`, then `day` (all ascending).

The catch: implement this by sorting on **one field at a time** using a stable
sort, in the spirit of radix sort applied to multi-field keys. Each field is a
small bounded integer (day in `1..31`, month in `1..12`), so a stable counting
sort per field is ideal.

If two records represent the exact same date, keep their original relative order
(the overall sort must be **stable**).

## Constraints

- `1 <= records.length <= 10^5`
- Each record is `(day, month, year)` with:
  - `1 <= day <= 31`
  - `1 <= month <= 12`
  - `1900 <= year <= 2100`
- Records are not guaranteed distinct; equal dates must preserve input order.

## Examples

### Example 1

```
Input:  records = [(15, 3, 2021), (2, 3, 2021), (15, 1, 2021)]
Output: [(15, 1, 2021), (2, 3, 2021), (15, 3, 2021)]
Explanation: Same year 2021, so order by month: January (1) first, then the two
March (3) records ordered by day (2 before 15).
```

### Example 2

```
Input:  records = [(1, 1, 2020), (31, 12, 2019), (1, 1, 2019)]
Output: [(1, 1, 2019), (31, 12, 2019), (1, 1, 2020)]
Explanation: Year dominates: both 2019 dates come before the 2020 date, and
within 2019, January (month 1) precedes December (month 12).
```

### Example 3

```
Input:  records = [(5, 6, 2000), (5, 6, 2000), (4, 6, 2000)]
Output: [(4, 6, 2000), (5, 6, 2000), (5, 6, 2000)]
Explanation: Only the day differs (4 before 5); the two identical (5, 6, 2000)
records keep their original relative order, demonstrating stability.
```

## Hint

Use **Radix Sort** across the fields: run a stable counting sort on the least
significant field (day) first, then month, then the most significant field
(year). Stability of each pass is what makes the final multi-key order correct.
