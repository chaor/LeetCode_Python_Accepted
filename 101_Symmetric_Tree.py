# 2015-04-04  recursively:85 ms  iteratively:53 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        return self.checkSym(root.left, root.right)
        
    def checkSym(self, L, R):
        if not (L or R): return True  # both None
        if not (L and R): return False  # one None, one has value
        if L.val != R.val: return False
        return self.checkSym(L.left, R.right) and self.checkSym(L.right, R.left)

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