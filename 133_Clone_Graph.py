# 2015-04-16  dfs  Runtime: 165 ms

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        self.newNodes = {} # key node.label, value node 
        return self.dfs(node)
    
    def dfs(self, sourceNode):
        newNode = UndirectedGraphNode(sourceNode.label)
        self.newNodes[newNode.label] = newNode
        for neighborNode in sourceNode.neighbors:
            if neighborNode.label not in self.newNodes: 
                self.dfs(neighborNode)
            newNode.neighbors.append(self.newNodes[neighborNode.label])
        return newNode