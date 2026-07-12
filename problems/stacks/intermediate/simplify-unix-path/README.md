# Simplify Unix Path

Canonicalizing an absolute Unix path is a stack problem: split on `/`, push each real directory name, treat `.` and empty parts as no-ops, and pop on `..` (going up). Re-joining the stack yields the shortest equivalent path.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Simplify Path](problem-01-simplify-path/PROBLEM.md) | Path component stack | Medium |
| 2 | [Crawler Log Folder](problem-02-crawler-log-folder/PROBLEM.md) | Depth as stack size | Medium |
| 3 | [Relative Path Between Directories](problem-03-relative-path-between-directories/PROBLEM.md) | Common-prefix of two path stacks | Medium |
| 4 | [Design File System Navigator](problem-04-file-system-navigator/PROBLEM.md) | Stateful cd/pwd path stack | Medium |
| 5 | [Sandboxed Path Resolution](problem-05-sandboxed-path-resolution/PROBLEM.md) | Root-jailed path stack | Medium |
