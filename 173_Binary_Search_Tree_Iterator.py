2014-01-09  Runtime: 148 ms

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # inorder traversal, O(h) memory means we need to store the most left branch
    # 中序遍历，O(h)的内存限制暗示要存储最左边的一串节点
    
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushMostLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.stack else False

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        if node.right:
            self.pushMostLeft(node.right)
        return node.val
        
    # @param current node, push most left nodes to stack
    def pushMostLeft(self, curNode):
        while curNode:
            self.stack.append(curNode)
            curNode = curNode.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())