# 2016-02-06  79 tests, 92 ms
# Thanks to https://leetcode.com/discuss/84659/short-ruby-python-java-c
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d, stack, result = collections.defaultdict(list), ['JFK'], []
        for depart, arrive in sorted(tickets, reverse = True):
            d[depart].append(arrive)
        while stack:
            while d[stack[-1]]:
                stack.append(d[stack[-1]].pop())
            result.append(stack.pop())
        return result[::-1]
