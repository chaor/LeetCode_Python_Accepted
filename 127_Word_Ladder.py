# 2015-09-30  Runtime: 456 ms
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # queue will store (word, number of transitions)
        queue, wordLen = collections.deque([(beginWord, 1)]), len(beginWord)
        while queue:
            w = queue.popleft()
            for i in xrange(wordLen):
                firstHalf, secondHalf = w[0][:i], w[0][i + 1:]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = firstHalf + ch + secondHalf
                    if newWord == endWord: return w[1] + 1
                    if newWord in wordList:
                        queue.append((newWord, w[1] + 1))
                        wordList.remove(newWord)
        return 0