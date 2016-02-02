# 2016-02-02  Runtime: 40 ms
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i, N, result = 0, len(words), []
        while i < N:
            # decide how many words to be put in one line
            oneLine, j, currWidth, positionNum, spaceNum = [words[i]], i + 1, len(words[i]), 0, maxWidth - len(words[i])
            while j < N and currWidth + 1 + len(words[j]) <= maxWidth:
                oneLine.append(words[j])
                currWidth += 1 + len(words[j])
                spaceNum -= len(words[j])
                positionNum, j = positionNum + 1, j + 1
            i = j
            # decide the layout of one line
            if i < N and positionNum:
                spaces = [' ' * (spaceNum / positionNum + (k < spaceNum % positionNum)) for k in range(positionNum)] + ['']
            else: # last line or the line only has one word
                spaces = [' '] * positionNum + [' ' * (maxWidth - currWidth)]
            result.append(''.join([s for pair in zip(oneLine, spaces) for s in pair]))
        return result
