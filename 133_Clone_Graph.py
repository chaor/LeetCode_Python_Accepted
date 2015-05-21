# 2015-05-21
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

###########DFS  Runtime: 204 ms##############
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        self.d = {} # key is original node, value is copy node
        return self.dfs(node)
        
    # @param n, a undirected graph node
    # @return a its copy
    def dfs(self, n):
        if n in self.d: return self.d[n]
        self.d[n] = UndirectedGraphNode(n.label)
        for neighbor in n.neighbors:
            self.d[n].neighbors.append(self.dfs(neighbor))
        return self.d[n]

############BFS  Runtime: 172 ms###############
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        queue = collections.deque([node])
        d = {node: UndirectedGraphNode(node.label)} # key is original node, value is its copy
        while queue:
            # the poped node must be already in the dictionary d.
            poped = queue.popleft()
            for neighbor in poped.neighbors:
                if neighbor in d: d[poped].neighbors.append(d[neighbor])
                else:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    d[neighbor] = neighborCopy
                    d[poped].neighbors.append(neighborCopy)
                    # only put new found nodes into queue, otherwise we will get infinite loop, think two-node graph 0 -- 1
                    queue.append(neighbor)
        return d[node]