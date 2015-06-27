# 2015-06-27  Runtime: 500 ms
# thanks to https://leetcode.com/discuss/36259/tree-solutions-18-20-lines
class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        current = self.root
        for char in word:
            current = current.setdefault(char, {})
        current['$'] = '$'  # this is the end flag

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        dicts = [self.root]
        for char in word:
            newDicts = []
            if char == '.':
                for d in dicts:
                    for key in d.keys():
                        if key != '$': newDicts.append(d[key])
                dicts = newDicts
                continue
            for d in dicts:
                if char in d: newDicts.append(d[char])
            dicts = newDicts
        return any(['$' in d for d in dicts])

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")