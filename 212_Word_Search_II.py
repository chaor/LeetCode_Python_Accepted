# 2015-06-27  Runtime: 512 ms
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        # thanks to https://leetcode.com/discuss/36411/27-lines-uses-complex-numbers, really don't know how to say
        # build Trie
        root = {}
        for word in words:
            current = root
            for char in word:
                current = current.setdefault(char, {})
            current['isWord'] = True
        board = {x + y * 1j: char for x, row in enumerate(board) for y, char in enumerate(row)}
        
        # dfs
        result = []
        def search(node, z, word):
            if node.pop('isWord', False): result.append(word)
            char = board.get(z)
            if char in node:
                board[z] = '.'
                for k in xrange(4): search(node[char], z + 1j ** k, word + char)
                board[z] = char
            
        for z in board: search(root, z, '')
        return result