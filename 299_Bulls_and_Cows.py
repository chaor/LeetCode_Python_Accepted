# 2015-12-15  151 tests, 68 ms
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        number, countA, countB = [0] * 10, 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
            else:
                s, g = ord(secret[i]) - ord('0'), ord(guess[i]) - ord('0')
                if number[s] < 0: countB += 1
                if number[g] > 0: countB += 1
                number[s] += 1
                number[g] -= 1
        return str(countA) + 'A' + str(countB) + 'B'