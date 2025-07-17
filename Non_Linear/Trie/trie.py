class TrieNode:
    def __init__(self):
        # Array of 26 children: one for each lowercase letter
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch: str) -> int:
        """
        Converts a character 'a'-'z' to a 0-based index.
        """
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        - Time: O(L), where L = length of word
        - Space: O(L), new nodes only for new characters
        """
        node = self.root
        for ch in word:
            idx = self._char_to_index(ch)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end_of_word = True


    def search(self, word: str) -> bool:
      """
      Returns True if the word exists in the Trie as a complete word, else False.
      - Time: O(L), where L = length of word
      - Space: O(1)
      """
      node = self.root
      for ch in word:
          idx = self._char_to_index(ch)
          if node.children[idx] is None:
              return False  # Path breaks: word not present
          node = node.children[idx]
      return node.is_end_of_word  # Only True if word ends here
    

    def starts_with(self, prefix: str) -> bool:
      """
      Returns True if any word in the Trie starts with the given prefix.
      - Time: O(L), where L = length of prefix
      - Space: O(1)
      """
      node = self.root
      for ch in prefix:
          idx = self._char_to_index(ch)
          if node.children[idx] is None:
              return False  # Path breaks: no word with this prefix
          node = node.children[idx]
      return True  # Successfully followed all prefix characters


    def words_with_prefix(self, prefix: str) -> list[str]:
        """
        Returns a list of all words in the Trie that start with the given prefix.
        Time: O(P + N*L) (P = prefix length, N = #words, L = avg word length under prefix)
        Space: O(N*L) for result list and call stack
        """
        def dfs(node: TrieNode, path: str, results: list):
            if node.is_end_of_word:
                results.append(path)
            for idx in range(26):
                child = node.children[idx]
                if child:
                    dfs(child, path + chr(idx + ord('a')), results)

        # First, find node matching the prefix
        node = self.root
        for ch in prefix:
            idx = self._char_to_index(ch)
            if node.children[idx] is None:
                return []  # Prefix not in Trie
            node = node.children[idx]
        results = []
        dfs(node, prefix, results)
        return results
    

    def count_words_with_prefix(self, prefix: str) -> int:
        """
        Returns the count of words in the Trie that start with the given prefix.
        Time: O(P + N·L), P=prefix length, N=words under prefix, L=avg length
        Space: O(H), H=height of Trie under prefix node (recursion stack)
        """
        def dfs_count(node: TrieNode) -> int:
            count = 1 if node.is_end_of_word else 0
            for child in node.children:
                if child:
                    count += dfs_count(child)
            return count

        # Find the node at the end of the prefix
        node = self.root
        for ch in prefix:
            idx = self._char_to_index(ch)
            if node.children[idx] is None:
                return 0  # Prefix not in Trie
            node = node.children[idx]
        return dfs_count(node)


    def delete(self, word: str) -> bool:
        """
        Deletes a word from the Trie. Returns True if the word was present and is now unmarked.
        """
        deleted = False

        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            nonlocal deleted
            if node is None:
                return False
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                deleted = True  # Mark as found and deleted
                return not any(node.children)
            idx = self._char_to_index(word[depth])
            child = node.children[idx]
            should_delete_child = _delete(child, word, depth + 1)
            if should_delete_child:
                node.children[idx] = None
                return not node.is_end_of_word and not any(node.children)
            return False

        _delete(self.root, word, 0)
        return deleted
          
    
    def longest_prefix_match(self, query: str) -> str:
        """
        Returns the longest word in the Trie that is a prefix of query.
        - Time: O(L), L = length of query
        """
        node = self.root
        longest = 0
        for i, ch in enumerate(query):
            idx = self._char_to_index(ch)
            if idx < 0 or idx >= 26 or node.children[idx] is None:
                break
            node = node.children[idx]
            if node.is_end_of_word:
                longest = i + 1
        return query[:longest]


    def serialize(self) -> str:
        """
        Serializes the Trie into a string.
        Preorder: for each node, record:
          - 1/0 for is_end_of_word
          - two-digit child count
          - For each child: character + child's serialization
        """
        def serialize_node(node):
            result = []
            result.append('1' if node.is_end_of_word else '0')
            # Count children
            count = sum(child is not None for child in node.children)
            result.append(f"{count:02d}")
            # Serialize children
            for idx, child in enumerate(node.children):
                if child:
                    result.append(chr(idx + ord('a')))
                    result.append(serialize_node(child))
            return ''.join(result)
        return serialize_node(self.root)

    def deserialize(self, data: str) -> None:
        """
        Deserializes the string and rebuilds the Trie.
        """
        self.root = TrieNode()
        def deserialize_node(it):
            node = TrieNode()
            node.is_end_of_word = (next(it) == '1')
            # Read two digits for child count
            count = int(next(it) + next(it))
            for _ in range(count):
                ch = next(it)
                idx = self._char_to_index(ch)
                node.children[idx] = deserialize_node(it)
            return node

        it = iter(data)
        self.root = deserialize_node(it)



