# 2014-01-18  Runtime: 58 ms

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(i) for i in num]
        # what's this lambda function? for input string x, y
        # if x + y > y + x, return -1
        # if x + y < y + x, return 1
        # if x + y == y + x, return 0
        num.sort(cmp = lambda x, y: (x + y < y + x) - (x + y > y + x))
        # Boolean operators and and or are so-called short-circuit operators
        # return value of a short-circuit operator is the last evaluated argument
        return ''.join(num).lstrip('0') or '0'