# Accounts Merge

**Difficulty:** Medium

**Source:** LeetCode 721 — Accounts Merge

## Description

Each account is `[name, email1, email2, ...]`. Two accounts belong to the same person if they share any email. Merge them: return, for each person, `[name, *sorted_emails]`. Return the list of merged accounts sorted.

## Examples

### Example 1

```
Input:  two John accounts sharing b@x.com
Output: one merged John
```

## Hint

Union-find over emails; group by root; prepend the owner name; sort emails and the list.
