# 2015-06-20   Runtime: 396 ms
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for char in word:
            current = current.child[char]
        current.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for char in word:
            if current.child.get(char) is None: return False
            current = current.child[char]
        return current.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if current.child.get(char) is None: return False
            current = current.child[char]
        return True