# 2015-11-11  Runtime: 88 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, Sum, oneAnswer):
            if not node:
                return
            if not node.left and not node.right:
                if Sum == node.val:
                    result.append(oneAnswer + [node.val])
                return
            dfs(node.left, Sum - node.val, oneAnswer + [node.val])
            dfs(node.right, Sum - node.val, oneAnswer + [node.val])    
                        
        result = []
        dfs(root, sum, [])
        return result