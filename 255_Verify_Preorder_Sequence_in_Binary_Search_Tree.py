# 2015-12-26  59 tests, 104 ms
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # thanks to https://leetcode.com/discuss/51543/java-o-n-and-o-1-extra-space
        stack, lower_bound = [], float('-inf')
        for p in preorder:
            if p < lower_bound:
                return False
            while stack and p > stack[-1]:
                # stack.pop() means this node has been visited, go to its right subtree
                lower_bound = stack.pop()
            stack.append(p)
        return True
