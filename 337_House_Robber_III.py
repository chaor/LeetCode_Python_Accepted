# 2016-03-21  124 tests, 80 ms
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            # return (subtree max money if not rob this node, subtree max money)
            if not node: return 0, 0
            max_l_ignore, max_l = dfs(node.left)
            max_r_ignore, max_r = dfs(node.right)
            return max_l + max_r, max(max_l + max_r, node.val + max_l_ignore + max_r_ignore)

        return dfs(root)[1]
