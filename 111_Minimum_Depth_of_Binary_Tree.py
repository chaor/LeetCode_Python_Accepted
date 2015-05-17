# 2015-05-17  Runtime: 80 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

############Another Solution############
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
    	# level-order traversal (BFS) works well for highly unbalanced tree
    	# It will return as long as a leaf node is reached
        if not root: return 0
        depth, queue, rightMost = 1, collections.deque([root]), root
        while queue:
            poped = queue.popleft()
            if not (poped.left or poped.right): return depth
            if poped.left: queue.append(poped.left)
            if poped.right:queue.append(poped.right)
            if poped == rightMost:
                depth += 1
                rightMost = poped.right if poped.right else poped.left