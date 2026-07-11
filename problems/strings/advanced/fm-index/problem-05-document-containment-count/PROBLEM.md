# Document Containment Count

**Difficulty:** Hard

Source: Document listing / document-count problem over a concatenated corpus
(FM-Index built on a `$`-separated collection; the counting variant of Muthukrishnan's document listing)

## Description

You are given a collection of `D` documents (strings) and query patterns. Build a
single FM-Index over the whole corpus, then for each pattern `P` return the
number of **distinct documents** that contain `P` as a substring. A document that
contains `P` several times still counts once.

The standard construction concatenates the documents with a **unique separator**
between them so that no pattern can span two documents, then indexes the result.
A locate query over the FM-Index yields every occurrence position in the
concatenation; mapping each position back to its document and counting the
distinct documents gives the answer.

Design a class constructed once from the list of documents that exposes a
`document_count(P)` method.

## Constraints

- `1 <= D <= 10^4`
- Total corpus length (sum of document lengths) `<= 2 * 10^5`.
- Documents and patterns consist of lowercase English letters.
- The separator character (e.g. `#`) and terminal sentinel (e.g. `$`) do **not**
  appear inside any document; the separator sorts below letters and the terminal
  sorts below the separator.
- A pattern that occurs in no document returns `0`.

## Examples

### Example 1
```
Input:
  documents = ["banana", "ananas", "cabana"]
  queries = ["ana", "ban", "nas", "cab", "xyz"]
Output:
  [3, 2, 1, 1, 0]
Explanation:
  "ana" appears in "banana", "ananas", and "cabana"           -> 3 documents
  "ban" appears in "banana" and "cabana" (c-a-BAN-a)          -> 2 documents
  "nas" appears only in "ananas"                              -> 1 document
  "cab" appears only in "cabana"                              -> 1 document
  "xyz" appears in none                                       -> 0 documents
```

### Example 2
```
Input:
  documents = ["abcabc", "bcd", "xyzabc"]
  queries = ["abc", "bc", "c"]
Output:
  [2, 3, 3]
Explanation:
  "abc" appears in "abcabc" (twice, still one doc) and "xyzabc"  -> 2 documents
  "bc"  appears in all three: "abcabc", "bcd", "xyzabc"          -> 3 documents
  "c"   appears in all three                                     -> 3 documents
  (Occurrences inside a single document collapse to one count.)
```

## Hint

Concatenate the documents with a unique separator, then build an **FM-Index** and
run **backward search + locate**. Precompute document start offsets; for each
located position, binary-search the offsets to find its document id, and count
the number of *distinct* document ids. The separator guarantees no match crosses a
document boundary.
