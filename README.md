# 🧠✨ DSA Problem-Solving Workspace (a.k.a. The Grindset Bunker)

> "Big O? More like Big Oof." — every dev at 2am

Welcome, brave leetcode-r. You have entered a **no-cap, fully-loaded, 302-algorithm-deep** workspace built for one purpose only: turning you from "I forgot what a stack is" (rip, no pun intended) to "I explained a segment tree to my cat and she got it." 🐱📈

This repo is basically the gym, except instead of protein shakes you're drinking **time complexity** and instead of gains you get **that sweet, sweet green LeetCode streak**. 🔥 We just went through a whole glow-up arc too — stacks, queues, deques, and hashing rolled in and the whole thing got 134 algorithms thicker. Bigger workspace, same unhinged energy.

## 📁 vibe check: how this workspace is organized

Every algorithm lives under `problems/<category>/<difficulty>/<algorithm>/` — think of it as the algorithm's studio apartment. Each folder is either:

- **Practice algorithms** 🏋️ — a `README.md` (the syllabus) plus **5+ problem folders**, each with:
  - `PROBLEM.md` — the problem statement, constraints, and worked examples (aka "the vibe of the question")
  - `solution.py` — an **empty template** (signature + type hints + docstring), staring at you, judging you, waiting
  - `SOLUTION.md` — the answer key: brute-force, optimal, complexities, edge cases (the "I gave up and peeked" file — no shame)
- **Study-only topics** 📖 — a single `STUDY.md` deep-dive for the theory nerds (used for results with no standalone coding problem, we still respect the lore)

> **Workflow, bestie:** read `PROBLEM.md` → attempt `solution.py` like the main character you are → cry a little → check `SOLUTION.md` → glow up. ✨

## 📊 the numbers don't lie

- **302** algorithms & techniques covered (yes, we counted, yes, we're tired, yes we added more)
- **1380** practice problems (statement + empty template + solution guide, fully loaded)
- **3** study-only deep dives for the theory sickos

> "It's giving comprehensive." — this README, about itself

## 🗺️ Contents (the map to enlightenment)

- [Arrays](#-arrays-the-og-data-structure)
- [Strings](#-strings-text-but-make-it-algorithmic)
- [Matrix (2D Arrays)](#-matrix-2d-arrays-arrays-but-they-had-a-baby)
- [Stacks](#-stacks-lifo-but-make-it-fashion)
- [Queues](#-queues-fifo-the-only-fair-line-in-life)
- [Deques](#-deques-queues-that-swing-both-ways)
- [Hashing](#-hashing-trust-me-bro-the-data-structure)
- [Cross-Cutting Paradigms](#-cross-cutting-paradigms-the-thinking-patterns)

---

## 🔢 Arrays (the OG data structure)

> "Arrays are just houses for your numbers, and some of these houses are on fire." 🔥🏠

### 🐣 Beginner — "wait, this is easy?"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Linear Search** | Practice | 5 | [open](problems/arrays/beginner/linear-search/README.md) |
| **Binary Search** | Practice | 6 | [open](problems/arrays/beginner/binary-search/README.md) |
| **Two Pointers (opposite ends)** | Practice | 6 | [open](problems/arrays/beginner/two-pointers-opposite-ends/README.md) |
| **Two Pointers (same direction / fast-slow)** | Practice | 5 | [open](problems/arrays/beginner/two-pointers-same-direction-fast-slow/README.md) |
| **Sliding Window (fixed size)** | Practice | 6 | [open](problems/arrays/beginner/sliding-window-fixed-size/README.md) |
| **Prefix Sum (1D)** | Practice | 6 | [open](problems/arrays/beginner/prefix-sum-1d/README.md) |
| **Suffix Sum / Suffix Product** | Practice | 5 | [open](problems/arrays/beginner/suffix-sum-suffix-product/README.md) |
| **Kadane's Algorithm** | Practice | 6 | [open](problems/arrays/beginner/kadanes-algorithm/README.md) |
| **Bubble Sort** | Practice | 5 | [open](problems/arrays/beginner/bubble-sort/README.md) |
| **Selection Sort** | Practice | 5 | [open](problems/arrays/beginner/selection-sort/README.md) |
| **Insertion Sort** | Practice | 5 | [open](problems/arrays/beginner/insertion-sort/README.md) |
| **Frequency Counting (Hash Map)** | Practice | 6 | [open](problems/arrays/beginner/frequency-counting-hash-map/README.md) |
| **Running Min / Max / Aggregate** | Practice | 6 | [open](problems/arrays/beginner/running-min-max-aggregate/README.md) |
| **Reverse In-Place** | Practice | 6 | [open](problems/arrays/beginner/reverse-in-place/README.md) |
| **Rotate Array (reversal trick)** | Practice | 5 | [open](problems/arrays/beginner/rotate-array-reversal-trick/README.md) |

### 🎓 Intermediate — "okay we're cooking now"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Sliding Window (variable size)** | Practice | 6 | [open](problems/arrays/intermediate/sliding-window-variable-size/README.md) |
| **Merge Sort** | Practice | 6 | [open](problems/arrays/intermediate/merge-sort/README.md) |
| **Quick Sort** | Practice | 6 | [open](problems/arrays/intermediate/quick-sort/README.md) |
| **Quickselect** | Practice | 5 | [open](problems/arrays/intermediate/quickselect/README.md) |
| **Median of Medians** | Practice | 5 | [open](problems/arrays/intermediate/median-of-medians/README.md) |
| **Heap Sort** | Practice | 6 | [open](problems/arrays/intermediate/heap-sort/README.md) |
| **Counting Sort** | Practice | 5 | [open](problems/arrays/intermediate/counting-sort/README.md) |
| **Radix Sort** | Practice | 5 | [open](problems/arrays/intermediate/radix-sort/README.md) |
| **Bucket Sort** | Practice | 5 | [open](problems/arrays/intermediate/bucket-sort/README.md) |
| **Binary Search on Answer** | Practice | 5 | [open](problems/arrays/intermediate/binary-search-on-answer/README.md) |
| **Lower/Upper Bound (bisect)** | Practice | 5 | [open](problems/arrays/intermediate/lower-upper-bound-bisect/README.md) |
| **Search in Rotated Sorted Array** | Practice | 5 | [open](problems/arrays/intermediate/search-in-rotated-sorted-array/README.md) |
| **Exponential (Galloping) Search** | Practice | 5 | [open](problems/arrays/intermediate/exponential-galloping-search/README.md) |
| **Interpolation Search** | Practice | 5 | [open](problems/arrays/intermediate/interpolation-search/README.md) |
| **Dutch National Flag (3-way partition)** | Practice | 5 | [open](problems/arrays/intermediate/dutch-national-flag-3-way-partition/README.md) |
| **Cyclic Sort** | Practice | 6 | [open](problems/arrays/intermediate/cyclic-sort/README.md) |
| **Merge Intervals** | Practice | 5 | [open](problems/arrays/intermediate/merge-intervals/README.md) |
| **Meeting Rooms / Interval Scheduling** | Practice | 6 | [open](problems/arrays/intermediate/meeting-rooms-interval-scheduling/README.md) |
| **Prefix Sum + Hash Map** | Practice | 6 | [open](problems/arrays/intermediate/prefix-sum-hash-map/README.md) |
| **Difference Array** | Practice | 6 | [open](problems/arrays/intermediate/difference-array/README.md) |
| **Monotonic Stack** | Practice | 6 | [open](problems/arrays/intermediate/monotonic-stack/README.md) |
| **Monotonic Deque** | Practice | 6 | [open](problems/arrays/intermediate/monotonic-deque/README.md) |
| **Two-Pointer Merge** | Practice | 6 | [open](problems/arrays/intermediate/two-pointer-merge/README.md) |
| **Boyer–Moore Voting** | Practice | 5 | [open](problems/arrays/intermediate/boyer-moore-voting/README.md) |
| **Floyd's Cycle Detection (Tortoise & Hare)** | Practice | 5 | [open](problems/arrays/intermediate/floyds-cycle-detection-tortoise-hare/README.md) |
| **Kadane's — Maximum Circular Subarray** | Practice | 5 | [open](problems/arrays/intermediate/kadanes-maximum-circular-subarray/README.md) |
| **Fisher–Yates Shuffle** | Practice | 5 | [open](problems/arrays/intermediate/fisher-yates-shuffle/README.md) |
| **Reservoir Sampling** | Practice | 5 | [open](problems/arrays/intermediate/reservoir-sampling/README.md) |
| **Coordinate Compression** | Practice | 6 | [open](problems/arrays/intermediate/coordinate-compression/README.md) |

### 💀 Advanced — "this is where friendships end"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Binary Indexed Tree (Fenwick Tree)** | Practice | 6 | [open](problems/arrays/advanced/binary-indexed-tree-fenwick-tree/README.md) |
| **Segment Tree** | Practice | 5 | [open](problems/arrays/advanced/segment-tree/README.md) |
| **Segment Tree with Lazy Propagation** | Practice | 5 | [open](problems/arrays/advanced/segment-tree-with-lazy-propagation/README.md) |
| **Segment Tree Beats** | Practice | 5 | [open](problems/arrays/advanced/segment-tree-beats/README.md) |
| **Sparse Table** | Practice | 5 | [open](problems/arrays/advanced/sparse-table/README.md) |
| **Sqrt Tree** | Practice | 5 | [open](problems/arrays/advanced/sqrt-tree/README.md) |
| **Merge Sort Tree** | Practice | 5 | [open](problems/arrays/advanced/merge-sort-tree/README.md) |
| **Square Root Decomposition** | Practice | 5 | [open](problems/arrays/advanced/square-root-decomposition/README.md) |
| **Mo's Algorithm** | Practice | 5 | [open](problems/arrays/advanced/mos-algorithm/README.md) |
| **Persistent Segment Tree** | Practice | 5 | [open](problems/arrays/advanced/persistent-segment-tree/README.md) |
| **Wavelet Tree** | Practice | 6 | [open](problems/arrays/advanced/wavelet-tree/README.md) |
| **Ternary Search** | Practice | 5 | [open](problems/arrays/advanced/ternary-search/README.md) |
| **Top-K via Heap** | Practice | 6 | [open](problems/arrays/advanced/top-k-via-heap/README.md) |
| **Count Inversions (merge sort)** | Practice | 5 | [open](problems/arrays/advanced/count-inversions-merge-sort/README.md) |
| **Longest Increasing Subsequence (patience / binary search)** | Practice | 6 | [open](problems/arrays/advanced/longest-increasing-subsequence-patience-binary-search/README.md) |
| **Sweep Line (1D events)** | Practice | 5 | [open](problems/arrays/advanced/sweep-line-1d-events/README.md) |
| **Maximum Subarray via Divide & Conquer** | Practice | 5 | [open](problems/arrays/advanced/maximum-subarray-via-divide-conquer/README.md) |
| **Convex Hull Trick / Li Chao Tree** | Practice | 5 | [open](problems/arrays/advanced/convex-hull-trick-li-chao-tree/README.md) |
| **Meet in the Middle** | Practice | 5 | [open](problems/arrays/advanced/meet-in-the-middle/README.md) |
| **Two-Pointer on Sorted Sums (k-sum)** | Practice | 6 | [open](problems/arrays/advanced/two-pointer-on-sorted-sums-k-sum/README.md) |
| **Sqrt Decomposition on Queries (offline)** | Practice | 5 | [open](problems/arrays/advanced/sqrt-decomposition-on-queries-offline/README.md) |
| **Order-Statistics Tree** | Practice | 5 | [open](problems/arrays/advanced/order-statistics-tree/README.md) |

---

## 🔤 Strings (text but make it algorithmic)

> "I don't always process strings, but when I do, it's O(n) or I'm rewriting it." — probably you, eventually

### 🐣 Beginner

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Naive Pattern Matching** | Practice | 5 | [open](problems/strings/beginner/naive-pattern-matching/README.md) |
| **Character Frequency Count** | Practice | 6 | [open](problems/strings/beginner/character-frequency-count/README.md) |
| **Anagram Check (sort or count)** | Practice | 5 | [open](problems/strings/beginner/anagram-check-sort-or-count/README.md) |
| **Palindrome Check (two pointers)** | Practice | 5 | [open](problems/strings/beginner/palindrome-check-two-pointers/README.md) |
| **Reverse Words / String** | Practice | 6 | [open](problems/strings/beginner/reverse-words-string/README.md) |
| **String Tokenization / Split** | Practice | 5 | [open](problems/strings/beginner/string-tokenization-split/README.md) |
| **Case Conversion & ASCII Arithmetic** | Practice | 5 | [open](problems/strings/beginner/case-conversion-ascii-arithmetic/README.md) |
| **Run-Length Encoding** | Practice | 6 | [open](problems/strings/beginner/run-length-encoding/README.md) |
| **Sliding Window on Strings** | Practice | 5 | [open](problems/strings/beginner/sliding-window-on-strings/README.md) |

### 🎓 Intermediate

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **KMP (Knuth–Morris–Pratt)** | Practice | 5 | [open](problems/strings/intermediate/kmp-knuth-morris-pratt/README.md) |
| **Z-Algorithm** | Practice | 5 | [open](problems/strings/intermediate/z-algorithm/README.md) |
| **Rabin–Karp** | Practice | 5 | [open](problems/strings/intermediate/rabin-karp/README.md) |
| **Boyer–Moore (string search)** | Practice | 6 | [open](problems/strings/intermediate/boyer-moore-string-search/README.md) |
| **Rolling Hash / Polynomial Hashing** | Practice | 5 | [open](problems/strings/intermediate/rolling-hash-polynomial-hashing/README.md) |
| **Wagner–Fischer (Edit Distance DP)** | Practice | 5 | [open](problems/strings/intermediate/wagner-fischer-edit-distance-dp/README.md) |
| **Trie (Prefix Tree)** | Practice | 6 | [open](problems/strings/intermediate/trie-prefix-tree/README.md) |
| **Longest Common Prefix (vertical/binary)** | Practice | 5 | [open](problems/strings/intermediate/longest-common-prefix-vertical-binary/README.md) |
| **Longest Palindromic Substring (expand around center)** | Practice | 5 | [open](problems/strings/intermediate/longest-palindromic-substring-expand-around-center/README.md) |
| **Longest Common Subsequence (DP)** | Practice | 6 | [open](problems/strings/intermediate/longest-common-subsequence-dp/README.md) |
| **Edit Distance (Levenshtein)** | Practice | 5 | [open](problems/strings/intermediate/edit-distance-levenshtein/README.md) |
| **String DP (regex/wildcard matching)** | Practice | 5 | [open](problems/strings/intermediate/string-dp-regex-wildcard-matching/README.md) |
| **Group Anagrams (hashing signature)** | Practice | 6 | [open](problems/strings/intermediate/group-anagrams-hashing-signature/README.md) |
| **Manacher's Algorithm** | Practice | 5 | [open](problems/strings/intermediate/manachers-algorithm/README.md) |
| **Suffix Array (prefix-doubling / DC3)** | Practice | 6 | [open](problems/strings/intermediate/suffix-array-prefix-doubling-dc3/README.md) |
| **Bit-mask / Bitset String Matching (Shift-And / Shift-Or)** | Practice | 5 | [open](problems/strings/intermediate/bit-mask-bitset-string-matching-shift-and-shift-or/README.md) |

### 💀 Advanced — "certified string sicko territory"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Aho–Corasick Automaton** | Practice | 6 | [open](problems/strings/advanced/aho-corasick-automaton/README.md) |
| **Commentz-Walter Algorithm** | Study | — | [open](problems/strings/advanced/commentz-walter-algorithm/STUDY.md) |
| **Hirschberg's Algorithm** | Practice | 5 | [open](problems/strings/advanced/hirschbergs-algorithm/README.md) |
| **Suffix Automaton** | Practice | 6 | [open](problems/strings/advanced/suffix-automaton/README.md) |
| **Suffix Tree (Ukkonen)** | Practice | 5 | [open](problems/strings/advanced/suffix-tree-ukkonen/README.md) |
| **Suffix Array + LCP (Kasai's algorithm)** | Practice | 5 | [open](problems/strings/advanced/suffix-array-lcp-kasais-algorithm/README.md) |
| **Generalized Suffix Structures** | Practice | 5 | [open](problems/strings/advanced/generalized-suffix-structures/README.md) |
| **Double Hashing / Anti-Hash** | Practice | 5 | [open](problems/strings/advanced/double-hashing-anti-hash/README.md) |
| **Palindromic Tree (Eertree)** | Practice | 5 | [open](problems/strings/advanced/palindromic-tree-eertree/README.md) |
| **Booth's Algorithm** | Practice | 5 | [open](problems/strings/advanced/booths-algorithm/README.md) |
| **Lyndon Factorization (Duval's algorithm)** | Practice | 5 | [open](problems/strings/advanced/lyndon-factorization-duvals-algorithm/README.md) |
| **Main–Lorentz Algorithm** | Practice | 5 | [open](problems/strings/advanced/main-lorentz-algorithm/README.md) |
| **Burrows–Wheeler Transform (BWT)** | Practice | 5 | [open](problems/strings/advanced/burrows-wheeler-transform-bwt/README.md) |
| **FM-Index** | Practice | 5 | [open](problems/strings/advanced/fm-index/README.md) |
| **Bitap / Fuzzy Matching** | Practice | 5 | [open](problems/strings/advanced/bitap-fuzzy-matching/README.md) |

---

## 🧩 Matrix (2D Arrays) (arrays but they had a baby)

> "It's not a maze, it's a matrix, and yes I will get lost in both." 🌀

### 🐣 Beginner

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Row/Column Traversal** | Practice | 5 | [open](problems/matrix/beginner/row-column-traversal/README.md) |
| **Transpose** | Practice | 5 | [open](problems/matrix/beginner/transpose/README.md) |
| **Rotate 90° (transpose + reverse)** | Practice | 5 | [open](problems/matrix/beginner/rotate-90-transpose-reverse/README.md) |
| **Spiral Traversal** | Practice | 5 | [open](problems/matrix/beginner/spiral-traversal/README.md) |
| **Diagonal / Zig-Zag Traversal** | Practice | 5 | [open](problems/matrix/beginner/diagonal-zig-zag-traversal/README.md) |
| **Boundary / Perimeter Traversal** | Practice | 5 | [open](problems/matrix/beginner/boundary-perimeter-traversal/README.md) |
| **Staircase / Saddleback Search** | Practice | 5 | [open](problems/matrix/beginner/staircase-saddleback-search/README.md) |
| **Set Matrix Zeroes** | Practice | 5 | [open](problems/matrix/beginner/set-matrix-zeroes/README.md) |
| **Flood Fill (basic DFS/BFS)** | Practice | 6 | [open](problems/matrix/beginner/flood-fill-basic-dfs-bfs/README.md) |

### 🎓 Intermediate

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Grid DFS / BFS** | Practice | 6 | [open](problems/matrix/intermediate/grid-dfs-bfs/README.md) |
| **Number of Islands / Connected Components** | Practice | 6 | [open](problems/matrix/intermediate/number-of-islands-connected-components/README.md) |
| **Multi-Source BFS** | Practice | 6 | [open](problems/matrix/intermediate/multi-source-bfs/README.md) |
| **Lee Algorithm** | Practice | 5 | [open](problems/matrix/intermediate/lee-algorithm/README.md) |
| **2D Prefix Sum (Integral Image)** | Practice | 6 | [open](problems/matrix/intermediate/2d-prefix-sum-integral-image/README.md) |
| **2D Difference Array** | Practice | 5 | [open](problems/matrix/intermediate/2d-difference-array/README.md) |
| **Binary Search in Fully-Sorted Matrix** | Practice | 5 | [open](problems/matrix/intermediate/binary-search-in-fully-sorted-matrix/README.md) |
| **Dynamic Programming on Grid** | Practice | 5 | [open](problems/matrix/intermediate/dynamic-programming-on-grid/README.md) |
| **Maximal Rectangle / Largest Square** | Practice | 6 | [open](problems/matrix/intermediate/maximal-rectangle-largest-square/README.md) |
| **Largest All-Zero Submatrix** | Practice | 5 | [open](problems/matrix/intermediate/largest-all-zero-submatrix/README.md) |
| **Matrix Exponentiation** | Practice | 6 | [open](problems/matrix/intermediate/matrix-exponentiation/README.md) |
| **Union–Find on Grid** | Practice | 5 | [open](problems/matrix/intermediate/union-find-on-grid/README.md) |
| **Backtracking on Grid** | Practice | 5 | [open](problems/matrix/intermediate/backtracking-on-grid/README.md) |
| **Dijkstra / 0-1 BFS on Weighted Grid** | Practice | 5 | [open](problems/matrix/intermediate/dijkstra-0-1-bfs-on-weighted-grid/README.md) |
| **A\* Search** | Practice | 5 | [open](problems/matrix/intermediate/a-search/README.md) |

### 💀 Advanced

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Broken-Profile / Plug DP (bitmask over columns)** | Practice | 5 | [open](problems/matrix/advanced/broken-profile-plug-dp-bitmask-over-columns/README.md) |
| **Hungarian Algorithm** | Practice | 5 | [open](problems/matrix/advanced/hungarian-algorithm/README.md) |
| **Gaussian Elimination** | Practice | 5 | [open](problems/matrix/advanced/gaussian-elimination/README.md) |
| **Gauss–Jordan Elimination** | Practice | 5 | [open](problems/matrix/advanced/gauss-jordan-elimination/README.md) |
| **LU Decomposition** | Practice | 5 | [open](problems/matrix/advanced/lu-decomposition/README.md) |
| **Strassen's Matrix Multiplication** | Study | — | [open](problems/matrix/advanced/strassens-matrix-multiplication/STUDY.md) |
| **Coppersmith–Winograd (and successors)** | Study | — | [open](problems/matrix/advanced/coppersmith-winograd-and-successors/STUDY.md) |
| **Floyd–Warshall** | Practice | 5 | [open](problems/matrix/advanced/floyd-warshall/README.md) |
| **Min-Plus (Tropical) Matrix Multiplication** | Practice | 5 | [open](problems/matrix/advanced/min-plus-tropical-matrix-multiplication/README.md) |
| **2D Segment Tree / 2D BIT** | Practice | 6 | [open](problems/matrix/advanced/2d-segment-tree-2d-bit/README.md) |
| **2D Sparse Table** | Practice | 5 | [open](problems/matrix/advanced/2d-sparse-table/README.md) |
| **Kadane 2D (max sum submatrix)** | Practice | 5 | [open](problems/matrix/advanced/kadane-2d-max-sum-submatrix/README.md) |
| **Max-Flow / Min-Cut on Grid** | Practice | 5 | [open](problems/matrix/advanced/max-flow-min-cut-on-grid/README.md) |
| **Rotating Calipers on Point Grids** | Practice | 5 | [open](problems/matrix/advanced/rotating-calipers-on-point-grids/README.md) |
| **Convolution / FFT on 2D data** | Practice | 5 | [open](problems/matrix/advanced/convolution-fft-on-2d-data/README.md) |

---

## 📚 Stacks (LIFO but make it fashion)

> "Last in, first out — the algorithm equivalent of always eating the top cookie off the plate." 🍪

### 🐣 Beginner — "push, pop, repeat"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Array-Based Stack** | Practice | 5 | [open](problems/stacks/beginner/array-based-stack/README.md) |
| **Balanced Parentheses / Bracket Matching** | Practice | 5 | [open](problems/stacks/beginner/balanced-parentheses-bracket-matching/README.md) |
| **Base Conversion via Stack** | Practice | 5 | [open](problems/stacks/beginner/base-conversion-stack/README.md) |
| **Delete Adjacent Duplicates** | Practice | 5 | [open](problems/stacks/beginner/delete-adjacent-duplicates/README.md) |
| **Linked-List-Based Stack** | Practice | 5 | [open](problems/stacks/beginner/linked-list-based-stack/README.md) |
| **Next Greater Element (Introductory)** | Practice | 5 | [open](problems/stacks/beginner/next-greater-element-intro/README.md) |
| **Postfix (Reverse Polish Notation) Evaluation** | Practice | 5 | [open](problems/stacks/beginner/postfix-rpn-evaluation/README.md) |
| **Prefix (Polish Notation) Evaluation** | Practice | 5 | [open](problems/stacks/beginner/prefix-polish-evaluation/README.md) |
| **Reverse via Stack** | Practice | 5 | [open](problems/stacks/beginner/reverse-via-stack/README.md) |
| **Undo / Redo Stacks** | Practice | 5 | [open](problems/stacks/beginner/undo-redo-stacks/README.md) |

### 🎓 Intermediate — "the histogram arc"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Asteroid Collision** | Practice | 5 | [open](problems/stacks/intermediate/asteroid-collision/README.md) |
| **Basic Calculator** | Practice | 5 | [open](problems/stacks/intermediate/basic-calculator/README.md) |
| **Decode String (Nested)** | Practice | 5 | [open](problems/stacks/intermediate/decode-string-nested/README.md) |
| **Expression Tree Construction** | Practice | 5 | [open](problems/stacks/intermediate/expression-tree-construction/README.md) |
| **Iterative Tree Traversals** | Practice | 5 | [open](problems/stacks/intermediate/iterative-tree-traversals/README.md) |
| **Largest Rectangle in Histogram** | Practice | 5 | [open](problems/stacks/intermediate/largest-rectangle-in-histogram/README.md) |
| **Min / Max Stack (O(1))** | Practice | 5 | [open](problems/stacks/intermediate/min-max-stack-o1/README.md) |
| **Monotonic Stack** | Practice | 5 | [open](problems/stacks/intermediate/monotonic-stack/README.md) |
| **Queue Using Two Stacks** | Practice | 5 | [open](problems/stacks/intermediate/queue-using-two-stacks/README.md) |
| **Remove K Digits / Smallest Result** | Practice | 5 | [open](problems/stacks/intermediate/remove-k-digits/README.md) |
| **Shunting-Yard / Infix Conversion** | Practice | 5 | [open](problems/stacks/intermediate/shunting-yard-infix-conversion/README.md) |
| **Simplify Unix Path** | Practice | 5 | [open](problems/stacks/intermediate/simplify-unix-path/README.md) |
| **Sort a Stack** | Practice | 5 | [open](problems/stacks/intermediate/sort-a-stack/README.md) |
| **Stack Using Two Queues** | Practice | 5 | [open](problems/stacks/intermediate/stack-using-two-queues/README.md) |
| **Trapping Rain Water (Stack)** | Practice | 5 | [open](problems/stacks/intermediate/trapping-rain-water-stack/README.md) |
| **Valid Parentheses Variations** | Practice | 5 | [open](problems/stacks/intermediate/valid-parentheses-variations/README.md) |

### 💀 Advanced — "SCC sicko hours"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **132 Pattern Detection** | Practice | 1 | [open](problems/stacks/advanced/132-pattern/README.md) |
| **All Nearest Smaller Values (ANSV)** | Practice | 1 | [open](problems/stacks/advanced/all-nearest-smaller-values/README.md) |
| **Articulation Points & Bridges** | Practice | 2 | [open](problems/stacks/advanced/articulation-points-bridges/README.md) |
| **Cartesian Tree Construction (O(n))** | Practice | 1 | [open](problems/stacks/advanced/cartesian-tree-construction/README.md) |
| **Full Expression Evaluator (precedence + unary)** | Practice | 1 | [open](problems/stacks/advanced/expression-evaluator-precedence-unary/README.md) |
| **Gabow's SCC (Two Stacks)** | Practice | 1 | [open](problems/stacks/advanced/gabow-scc/README.md) |
| **Maximal Rectangle in Binary Matrix** | Practice | 1 | [open](problems/stacks/advanced/maximal-rectangle-binary-matrix/README.md) |
| **Min-Stack Aggregate Generalization** | Practice | 1 | [open](problems/stacks/advanced/min-stack-aggregate-generalization/README.md) |
| **Persistent Stack** | Practice | 1 | [open](problems/stacks/advanced/persistent-stack/README.md) |
| **Pratt Parsing / Operator-Precedence Parsing** | Practice | 1 | [open](problems/stacks/advanced/pratt-parsing/README.md) |
| **Retroactive Stack** | Practice | 1 | [open](problems/stacks/advanced/retroactive-stack/README.md) |
| **Stack-Sortable Permutations** | Practice | 2 | [open](problems/stacks/advanced/stack-sortable-permutations/README.md) |
| **Sum of Subarray Minimums / Maximums** | Practice | 2 | [open](problems/stacks/advanced/sum-of-subarray-minimums-maximums/README.md) |
| **Tarjan's Strongly Connected Components** | Practice | 1 | [open](problems/stacks/advanced/tarjan-scc/README.md) |

---

## 🎟️ Queues (FIFO, the only fair line in life)

> "First come, first served — the one place in your life where cutting the line is a felony." 🚔

### 🐣 Beginner — "wait your turn"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Array-Based Queue** | Practice | 5 | [open](problems/queues/beginner/array-based-queue/README.md) |
| **Circular Queue / Ring Buffer** | Practice | 5 | [open](problems/queues/beginner/circular-queue-ring-buffer/README.md) |
| **FIFO Simulation** | Practice | 5 | [open](problems/queues/beginner/fifo-simulation/README.md) |
| **Generate Binary Numbers** | Practice | 5 | [open](problems/queues/beginner/generate-binary-numbers/README.md) |
| **Josephus Problem** | Practice | 5 | [open](problems/queues/beginner/josephus-problem/README.md) |
| **Linked-List-Based Queue** | Practice | 5 | [open](problems/queues/beginner/linked-list-based-queue/README.md) |
| **Reverse a Queue** | Practice | 5 | [open](problems/queues/beginner/reverse-a-queue/README.md) |

### 🎓 Intermediate — "BFS enters the chat"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Bidirectional BFS** | Practice | 5 | [open](problems/queues/intermediate/bidirectional-bfs/README.md) |
| **Breadth-First Search (BFS)** | Practice | 5 | [open](problems/queues/intermediate/breadth-first-search/README.md) |
| **Grid BFS / Lee Algorithm** | Practice | 5 | [open](problems/queues/intermediate/grid-bfs-lee-algorithm/README.md) |
| **Kahn's Algorithm (Topological Sort)** | Practice | 5 | [open](problems/queues/intermediate/kahns-topological-sort/README.md) |
| **Level-Order Traversal** | Practice | 5 | [open](problems/queues/intermediate/level-order-traversal/README.md) |
| **Moving Average from Data Stream** | Practice | 5 | [open](problems/queues/intermediate/moving-average-data-stream/README.md) |
| **Multi-Source BFS** | Practice | 5 | [open](problems/queues/intermediate/multi-source-bfs/README.md) |
| **Recent Counter / Request Throttling** | Practice | 5 | [open](problems/queues/intermediate/recent-counter-throttling/README.md) |
| **Round-Robin Scheduling** | Practice | 5 | [open](problems/queues/intermediate/round-robin-scheduling/README.md) |
| **Snakes and Ladders / Board BFS** | Practice | 5 | [open](problems/queues/intermediate/snakes-and-ladders-board-bfs/README.md) |
| **Task Scheduler / Cooldown** | Practice | 5 | [open](problems/queues/intermediate/task-scheduler-cooldown/README.md) |
| **Word Ladder / State-Space BFS** | Practice | 5 | [open](problems/queues/intermediate/word-ladder-state-space-bfs/README.md) |

### 💀 Advanced — "max-flow, minimal chill"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Aho–Corasick Failure-Link BFS Build** | Practice | 1 | [open](problems/queues/advanced/aho-corasick-failure-link-bfs/README.md) |
| **Calendar / Event-Queue Simulation** | Practice | 1 | [open](problems/queues/advanced/calendar-event-queue-simulation/README.md) |
| **Dial's Algorithm (Bucket Queue)** | Practice | 1 | [open](problems/queues/advanced/dials-algorithm-bucket-queue/README.md) |
| **Dijkstra (Priority Queue)** | Practice | 2 | [open](problems/queues/advanced/dijkstra-priority-queue/README.md) |
| **Dinic's Algorithm** | Practice | 1 | [open](problems/queues/advanced/dinics-algorithm/README.md) |
| **Edmonds–Karp (Max-Flow)** | Practice | 1 | [open](problems/queues/advanced/edmonds-karp-max-flow/README.md) |
| **Hopcroft–Karp (Bipartite Matching)** | Practice | 1 | [open](problems/queues/advanced/hopcroft-karp-bipartite-matching/README.md) |
| **Indexed / Addressable Priority Queue** | Practice | 1 | [open](problems/queues/advanced/indexed-addressable-priority-queue/README.md) |
| **Monotonic-Queue DP Optimization** | Practice | 1 | [open](problems/queues/advanced/monotonic-queue-dp-optimization/README.md) |
| **Monotonic Queue (Min / Max)** | Practice | 2 | [open](problems/queues/advanced/monotonic-queue-min-max/README.md) |
| **Push–Relabel (FIFO)** | Practice | 1 | [open](problems/queues/advanced/push-relabel-fifo/README.md) |
| **Top-K / K-Way Merge** | Practice | 2 | [open](problems/queues/advanced/top-k-k-way-merge/README.md) |
| **Two-Heap Streaming Median** | Practice | 1 | [open](problems/queues/advanced/two-heap-streaming-median/README.md) |
| **0-1 BFS** | Practice | 1 | [open](problems/queues/advanced/zero-one-bfs/README.md) |

---

## 🔄 Deques (queues that swing both ways)

> "Push front, push back, pop wherever — deques don't do commitment." 🎭

### 🐣 Beginner — "double-ended and thriving"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Circular-Array Deque** | Practice | 5 | [open](problems/deques/beginner/circular-array-deque/README.md) |
| **Deque as Stack or Queue** | Practice | 5 | [open](problems/deques/beginner/deque-as-stack-or-queue/README.md) |
| **Design Front Middle Back Queue** | Practice | 5 | [open](problems/deques/beginner/design-front-middle-back-queue/README.md) |
| **Doubly-Linked-List Deque** | Practice | 5 | [open](problems/deques/beginner/doubly-linked-list-deque/README.md) |
| **Palindrome Check via Deque** | Practice | 5 | [open](problems/deques/beginner/palindrome-check-deque/README.md) |

### 🎓 Intermediate — "sliding window's favorite sidekick"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **First Unique / Non-Repeating in a Stream** | Practice | 5 | [open](problems/deques/intermediate/first-unique-in-stream/README.md) |
| **Monotonic Deque — Sliding Window Max/Min** | Practice | 5 | [open](problems/deques/intermediate/monotonic-deque-sliding-window/README.md) |
| **Sliding-Window Aggregate with Two Monotonic Deques** | Practice | 5 | [open](problems/deques/intermediate/sliding-window-aggregate/README.md) |
| **Sliding-Window Metrics (Range with Two Deques)** | Practice | 5 | [open](problems/deques/intermediate/sliding-window-metrics/README.md) |
| **0-1 BFS with a Deque** | Practice | 5 | [open](problems/deques/intermediate/zero-one-bfs-deque/README.md) |

### 💀 Advanced — "persistent, functional, unbothered"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Constrained Subsequence Sum** | Practice | 1 | [open](problems/deques/advanced/constrained-subsequence-sum/README.md) |
| **Double-Ended Priority Queue (Min-Max Heap)** | Practice | 1 | [open](problems/deques/advanced/double-ended-priority-queue/README.md) |
| **Functional Deque (Steque)** | Practice | 1 | [open](problems/deques/advanced/functional-deque-steque/README.md) |
| **Jump Game VI** | Practice | 1 | [open](problems/deques/advanced/jump-game-vi/README.md) |
| **Monotonic-Deque DP (General)** | Practice | 1 | [open](problems/deques/advanced/monotonic-deque-dp-general/README.md) |
| **Persistent Deque** | Practice | 1 | [open](problems/deques/advanced/persistent-deque/README.md) |
| **Shortest Subarray with Sum ≥ K** | Practice | 1 | [open](problems/deques/advanced/shortest-subarray-sum-at-least-k/README.md) |
| **Sliding-Window Median** | Practice | 1 | [open](problems/deques/advanced/sliding-window-median/README.md) |

---

## 🗝️ Hashing (trust me bro, the data structure)

> "O(1) lookup, if the hash gods are feeling generous." 🎰

### 🐣 Beginner — "the map is the territory"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Bijection Mapping (Isomorphic / Pattern)** | Practice | 5 | [open](problems/hashing/beginner/bijection-mapping/README.md) |
| **Complement Lookup / Two Sum** | Practice | 6 | [open](problems/hashing/beginner/complement-lookup-two-sum/README.md) |
| **Duplicate Detection** | Practice | 6 | [open](problems/hashing/beginner/duplicate-detection/README.md) |
| **First-Seen / Last-Seen Index** | Practice | 6 | [open](problems/hashing/beginner/first-last-seen-index/README.md) |
| **Frequency Map (Counting)** | Practice | 6 | [open](problems/hashing/beginner/frequency-map/README.md) |
| **Frequency-of-Frequencies** | Practice | 5 | [open](problems/hashing/beginner/frequency-of-frequencies/README.md) |
| **Group Anagrams / Canonical Signature** | Practice | 5 | [open](problems/hashing/beginner/group-anagrams-canonical/README.md) |
| **Hash Set Membership Testing** | Practice | 6 | [open](problems/hashing/beginner/hash-set-membership/README.md) |
| **Set Algebra (Union / Intersection / Difference)** | Practice | 5 | [open](problems/hashing/beginner/set-algebra/README.md) |
| **Value-to-Index Mapping** | Practice | 6 | [open](problems/hashing/beginner/value-to-index-map/README.md) |

### 🎓 Intermediate — "collision course"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **At Most / Exactly K Distinct** | Practice | 5 | [open](problems/hashing/intermediate/at-most-k-distinct/README.md) |
| **Coordinate / Tuple Hashing** | Practice | 5 | [open](problems/hashing/intermediate/coordinate-tuple-hashing/README.md) |
| **Design: Hash-Backed Structures** | Practice | 5 | [open](problems/hashing/intermediate/design-hash-structures/README.md) |
| **Hash Maps for Graphs & Trees** | Practice | 5 | [open](problems/hashing/intermediate/hashmap-graph-tree/README.md) |
| **Hash-Set Simulation & Cycle Detection** | Practice | 5 | [open](problems/hashing/intermediate/hashset-simulation/README.md) |
| **Longest Consecutive Sequence** | Practice | 5 | [open](problems/hashing/intermediate/longest-consecutive-sequence/README.md) |
| **Matrix / Grid Hashing** | Practice | 5 | [open](problems/hashing/intermediate/matrix-grid-hashing/README.md) |
| **Minimum / Constrained Covering Window** | Practice | 5 | [open](problems/hashing/intermediate/minimum-window/README.md) |
| **Pair / K-Sum Counting with Frequencies** | Practice | 5 | [open](problems/hashing/intermediate/pair-counting-frequencies/README.md) |
| **Prefix Difference / Balance Hashing** | Practice | 5 | [open](problems/hashing/intermediate/prefix-balance-hashing/README.md) |
| **Prefix Modulo Hashing** | Practice | 5 | [open](problems/hashing/intermediate/prefix-modulo-hashmap/README.md) |
| **Prefix Sum Earliest-Index Map** | Practice | 5 | [open](problems/hashing/intermediate/prefix-sum-earliest-index/README.md) |
| **Prefix Sum + Hash Map (Frequency)** | Practice | 5 | [open](problems/hashing/intermediate/prefix-sum-hashmap/README.md) |
| **Prefix XOR + Hash Map** | Practice | 5 | [open](problems/hashing/intermediate/prefix-xor-hashmap/README.md) |
| **Sliding Window + Frequency Map** | Practice | 5 | [open](problems/hashing/intermediate/sliding-window-frequency/README.md) |
| **Design: Stateful Hash-Map Systems** | Practice | 5 | [open](problems/hashing/intermediate/stateful-design-maps/README.md) |

### 💀 Advanced — "certified hash sicko territory"

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Bloom Filter** | Practice | 2 | [open](problems/hashing/advanced/bloom-filter/README.md) |
| **Consistent Hashing (Ring)** | Practice | 2 | [open](problems/hashing/advanced/consistent-hashing/README.md) |
| **Count-Min Sketch** | Practice | 2 | [open](problems/hashing/advanced/count-min-sketch/README.md) |
| **Double Hashing (Anti-Collision)** | Practice | 3 | [open](problems/hashing/advanced/double-hashing-anti-collision/README.md) |
| **HyperLogLog / Cardinality Estimation** | Practice | 2 | [open](problems/hashing/advanced/hyperloglog/README.md) |
| **LFU Cache** | Practice | 2 | [open](problems/hashing/advanced/lfu-cache/README.md) |
| **Longest Duplicate Substring (Binary Search + Rolling Hash)** | Practice | 3 | [open](problems/hashing/advanced/longest-duplicate-substring/README.md) |
| **LRU Cache** | Practice | 2 | [open](problems/hashing/advanced/lru-cache/README.md) |
| **MinHash & SimHash (Similarity)** | Practice | 3 | [open](problems/hashing/advanced/minhash-simhash/README.md) |
| **Perfect Hashing (FKS / Minimal)** | Practice | 2 | [open](problems/hashing/advanced/perfect-hashing/README.md) |
| **Polynomial Prefix Hashing (Substring Equality)** | Practice | 3 | [open](problems/hashing/advanced/polynomial-string-hashing/README.md) |
| **Rabin-Karp Pattern Matching** | Practice | 3 | [open](problems/hashing/advanced/rabin-karp/README.md) |
| **Rendezvous & Jump Consistent Hashing** | Practice | 3 | [open](problems/hashing/advanced/rendezvous-jump-hashing/README.md) |
| **Subtree Serialization / Duplicate Subtrees** | Practice | 3 | [open](problems/hashing/advanced/subtree-serialization-hashing/README.md) |
| **Tree Isomorphism / Canonical Hashing** | Practice | 3 | [open](problems/hashing/advanced/tree-isomorphism-hashing/README.md) |
| **Visited-State Hashing (BFS/DFS State-Space)** | Practice | 3 | [open](problems/hashing/advanced/visited-state-search/README.md) |
| **Zobrist Hashing (Board State)** | Practice | 2 | [open](problems/hashing/advanced/zobrist-hashing/README.md) |

---

## 🧠 Cross-Cutting Paradigms (the thinking patterns)

> "These aren't algorithms, they're personality types." — a very tired CS student

| Algorithm | Type | Problems | Link |
|---|---|---|---|
| **Brute Force / Complete Search** | Practice | 5 | [open](problems/paradigms/brute-force-complete-search/README.md) |
| **Greedy** | Practice | 5 | [open](problems/paradigms/greedy/README.md) |
| **Divide and Conquer** | Practice | 6 | [open](problems/paradigms/divide-and-conquer/README.md) |
| **Dynamic Programming (memoization / tabulation)** | Practice | 6 | [open](problems/paradigms/dynamic-programming-memoization-tabulation/README.md) |
| **Range / Interval DP** | Practice | 6 | [open](problems/paradigms/range-interval-dp/README.md) |
| **Digit DP** | Practice | 6 | [open](problems/paradigms/digit-dp/README.md) |
| **Bitmask DP** | Practice | 5 | [open](problems/paradigms/bitmask-dp/README.md) |
| **Backtracking** | Practice | 6 | [open](problems/paradigms/backtracking/README.md) |
| **Recursion** | Practice | 6 | [open](problems/paradigms/recursion/README.md) |
| **Two Pointers** | Practice | 6 | [open](problems/paradigms/two-pointers/README.md) |
| **Sliding Window** | Practice | 6 | [open](problems/paradigms/sliding-window/README.md) |
| **Hashing** | Practice | 5 | [open](problems/paradigms/hashing/README.md) |
| **Bit Manipulation** | Practice | 6 | [open](problems/paradigms/bit-manipulation/README.md) |
| **Binary Search on Answer** | Practice | 6 | [open](problems/paradigms/binary-search-on-answer/README.md) |
| **Sorting as Preprocessing** | Practice | 6 | [open](problems/paradigms/sorting-as-preprocessing/README.md) |
| **Prefix / Suffix Precomputation** | Practice | 6 | [open](problems/paradigms/prefix-suffix-precomputation/README.md) |
| **Monotonic Stack / Queue** | Practice | 5 | [open](problems/paradigms/monotonic-stack-queue/README.md) |
| **Union-Find (Disjoint Set Union)** | Practice | 6 | [open](problems/paradigms/union-find-disjoint-set-union/README.md) |
| **Heap / Priority Queue** | Practice | 6 | [open](problems/paradigms/heap-priority-queue/README.md) |
| **Meet in the Middle** | Practice | 5 | [open](problems/paradigms/meet-in-the-middle/README.md) |
| **Offline Query Processing** | Practice | 5 | [open](problems/paradigms/offline-query-processing/README.md) |
| **Randomization** | Practice | 6 | [open](problems/paradigms/randomization/README.md) |
| **Amortized Analysis Techniques** | Practice | 6 | [open](problems/paradigms/amortized-analysis-techniques/README.md) |

---

## 🎯 The Vibes (a.k.a. rules of engagement)

1. Don't just read `SOLUTION.md`. That's not learning, that's a hostage situation with your own brain.
2. `O(n²)` is not a personality trait. Optimize it. 💅
3. Every failed test case is just the algorithm's way of saying "communicate better." 🗣️
4. If you skip `PROBLEM.md` and go straight to `solution.py`, that's on god, not on us.
5. Segment trees are scary until they're not. Then they're just... still kinda scary but in a fun way.

## 🏆 Final Boss Energy

> "I came, I `git clone`'d, I conquered (some of) the time complexity." 🏁

Go forth. Solve things. Make peace with recursion. And remember — every `TLE` (Time Limit Exceeded) is just the universe asking you to be a little more iconic with your loops. 💫

**No cap, this repo has your back.** 🫡