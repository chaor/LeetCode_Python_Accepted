# 2015-04-18  Runtime: 750 ms

class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        wordLength = len(beginWord)
        # store tuple (word, transformation times) in a queue, use BFS
        Q = collections.deque([(beginWord, 1)])
        while Q:
            word, transformationTimes = Q.popleft()
            for i in xrange(wordLength):
                for oneLetter in 'abcdefghijklmnopqrstuvwxyz':
                    if oneLetter == word[i]: continue
                    newWord = word[:i] + oneLetter + word[i+1:]
                    if newWord == endWord: return transformationTimes + 1
                    if newWord in wordDict:
                        Q.append((newWord, transformationTimes + 1))
                        wordDict.remove(newWord)
        return 0