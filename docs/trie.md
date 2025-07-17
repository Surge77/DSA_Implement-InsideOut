# Trie Data Structure (Prefix Tree) — Practical Reference

## 1. What is a Trie?

* Trie (pronounced “try”) is a tree-like data structure for storing collections of strings, optimized for prefix-based operations.
* Each path from root to node represents a prefix; full words are marked at leaf or inner nodes.

## 2. Core Use Cases

* **Autocomplete**: Suggest words as a user types.
* **Spell-check**: Efficiently check if a word (or prefix) exists.
* **IP Routing / DNS**: Longest-prefix match queries.
* **Word games**: Fast prefix/word search.

## 3. Key Operations & Complexities

| Operation              | Time Complexity | Space Complexity | Description                                            |
| ---------------------- | --------------- | ---------------- | ------------------------------------------------------ |
| Insert(word)           | O(L)            | O(L)             | L = length of word. Adds word, creates nodes if needed |
| Search(word)           | O(L)            | O(1)             | True if exact word exists                              |
| StartsWith(prefix)     | O(L)            | O(1)             | True if any word starts with prefix                    |
| Delete(word)           | O(L)            | O(L) (stack)     | Removes word, may prune unused nodes                   |
| List Words With Prefix | O(P + N·L)      | O(N·L)           | P=prefix, N=words w/ prefix, L=avg len                 |
| Serialize/Deserialize  | O(N·L)          | O(N·L)           | Save/load full structure to string                     |

## 4. Practical Implementation Details

* For **a-z only**: Use a fixed-size array (26) for children.
* For larger alphabets: Use dict/map (with tradeoff: speed vs memory).
* TrieNode should have a boolean flag: `is_end_of_word`.
* Insert/search is *case-sensitive* by default — normalize input as needed.
* Does not support fast substring search (only prefix-based).
* Large Tries can use a lot of memory; optimize only when needed.

## 5. Gotchas & Practical Advice

* **Shared Prefixes**: Words with the same prefix reuse nodes — memory efficient for languages.
* **Deleting words**: Safely remove only if node isn’t needed for another word.
* **Serialization**: Needed for saving/loading (see custom format or use JSON for large apps).
* **Recursion stack**: Large or deep Tries may hit recursion limits in DFS methods; rewrite to iterative if needed.
* **Edge Cases**: Empty strings, non-alphabetic characters — define clear behavior in your code.
* **Do not use built-ins** for children if practicing for interviews or to fully understand low-level structure.
* **Trie vs. HashMap**: Use Trie if you need prefix queries; use dict/set if only full-word lookups.

## 6. When *Not* to Use a Trie

* For *only* exact match (no prefixes), use a HashSet/Map instead.
* When data is huge but prefix queries are rare (memory usage is high).
* For full substring search, consider Suffix Trees/Automata, not Tries.

## 7. Serialization Example (Custom Format)

* Save each node: `[is_word_flag][children_count][char1][child1_subtree][char2][child2_subtree]...`
* Example: For "cat" and "car": `1 01 c 0 01 a 0 02 t 1 00 r 1 00`

## 8. Extensions & Advanced Features

* Wildcard search (e.g. "ca?") — backtracking variant.
* Count words under a prefix.
* Longest prefix match for routing, search, NLP.
* Store metadata at nodes (frequency, suggestions, etc).

## 9. Clean Minimal Example (a-z TrieNode)

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
```

## 10. Real-World Usage Tips

* Normalize input: lowercasing, strip spaces, validate chars.
* For millions of words, measure and optimize memory only if bottlenecked.
* Profile recursion if inserting/searching very deep strings.
* Use serialize/deserialize to snapshot the Trie for fast reload.
* For interactive/autocomplete apps, use `words_with_prefix` with result limit for performance.

## 11. Interview/Code Review Checklist

* Is code clean and readable, with clear helper methods?
* Are all standard operations present?
* Is delete logic correct for shared prefixes?
* Does it handle non-existent deletions gracefully?
* Can you add features (wildcard, metadata) if needed?

---

**Trie = best for fast prefix lookups and autocomplete. Don’t use it everywhere, but when you need fast prefix queries, it’s unbeatable.**
