# 2015-12-27  68 tests, 80 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        p, res, stack, distSum = root, collections.deque(), [], 0
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            x = stack.pop()
            if len(res) < k:
                res.append(x.val)
                distSum += abs(x.val - target)
            else:
                newDistSum = distSum - abs(res[0] - target) + abs(x.val - target)
                if newDistSum < distSum:
                    res.popleft()
                    res.append(x.val)
                    distSum = newDistSum
            p = x.right
        return list(res)
