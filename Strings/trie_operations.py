# Algorithm: Trie (Prefix Tree)
# Insert/Search/Delete: O(m) — m = length of word
# Space Complexity: O(n * m) — n words of average length m

class TrieNode:
    def __init__(self):
        self.children  = {}
        self.is_end    = False
        self.count     = 0    # words passing through this node


class Trie:
    """
    Prefix tree supporting insert, search, delete,
    prefix counting, and autocomplete suggestions.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into the trie. O(m)"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if exact word exists. O(m)"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word has this prefix. O(m)"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def count_words_with_prefix(self, prefix: str) -> int:
        """Return count of words that start with prefix. O(m)"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count

    def autocomplete(self, prefix: str) -> list[str]:
        """Return all words that start with prefix. O(m + k) k=results"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []

        def dfs(curr_node, current_word):
            if curr_node.is_end:
                results.append(prefix[:-len(current_word)] + current_word
                                if current_word else prefix)
            for ch, child in curr_node.children.items():
                dfs(child, current_word + ch)

        dfs(node, "")
        return sorted(results)

    def delete(self, word: str) -> bool:
        """
        Delete word from trie. Returns True if deleted, False if not found.
        Cleans up nodes that are no longer needed.
        """
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            ch = word[depth]
            if ch not in node.children:
                return False
            should_delete = _delete(node.children[ch], word, depth + 1)
            if should_delete:
                del node.children[ch]
                return not node.is_end and len(node.children) == 0
            return False

        return _delete(self.root, word, 0)


if __name__ == "__main__":
    trie = Trie()
    words = ["apple","app","application","apply","apt","banana","band","bandana"]
    for w in words:
        trie.insert(w)

    print(trie.search("apple"))             # True
    print(trie.search("ap"))               # False (prefix only)
    print(trie.starts_with("ap"))          # True
    print(trie.count_words_with_prefix("app"))  # 4
    print(trie.autocomplete("app"))        # ['app','apple','application','apply']
    print(trie.autocomplete("ban"))        # ['banana','band','bandana']

    trie.delete("apple")
    print(trie.search("apple"))            # False
    print(trie.search("app"))             # False
    print(trie.starts_with("appl"))       # True (application, apply still there)
