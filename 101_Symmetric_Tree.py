# 2015-09-24  recursively:56 ms  iteratively:53 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, root)
        
    def check(self, n1, n2):
        if not n1 and not n2: return True
        if not (n1 and n2): return False
        return n1.val == n2.val and self.check(n1.left, n2.right) and self.check(n1.right, n2.left)

###########################################

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        # thanks to https://leetcode.com/discuss/26372/python-iterative-way-using-a-queue
        if not root: return True
        Q = collections.deque([root.left, root.right])
        while Q:
            node1, node2 = Q.popleft(), Q.popleft()
            if not (node1 or node2): continue # both None
            if not (node1 and node2): return False
            if node1.val != node2.val: return False
            Q.append(node1.left)
            Q.append(node2.right)
            Q.append(node1.right)
            Q.append(node2.left)
        return True