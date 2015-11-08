# 2015-11-07  Runtime: 640 ms
class WordDictionary(object):
    class TrieNode(object):
        def __init__(self):
            self.d = collections.defaultdict(WordDictionary.TrieNode)
            self.isWord = False

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            cur = cur.d[ch]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        Q, N = collections.deque([(self.root, 0)]), len(word)
        while Q:
            node, i = Q.popleft()
            if i == N:
                if node.isWord:
                    return True
            elif word[i] == '.':
                for key in node.d:
                    Q.append((node.d[key], i + 1))
            elif word[i] in node.d:
                Q.append((node.d[word[i]], i + 1))
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")