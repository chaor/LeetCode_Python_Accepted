# 2015-12-16   47 tests, 232 ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # thanks to https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def solve(node):
            if node:
                res.append(str(node.val))
                solve(node.left)
                solve(node.right)
            else:
                res.append('#')
            
        res = []
        solve(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build():
            val = valueGen.next()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        
        valueGen = iter(data.split())
        return build()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))