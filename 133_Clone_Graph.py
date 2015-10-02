# 2015-10-1
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

############ BFS  Runtime: 84 ms ###############
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return None
        d = {node.label: UndirectedGraphNode(node.label)} # key is label, value is node
        queue = collections.deque([node])
        while queue:
            poped = queue.popleft()  # poped node must be in d
            for neighbor in poped.neighbors:
                if neighbor.label not in d: # new node found!
                    d[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                d[poped.label].neighbors.append(d[neighbor.label])    
        return d[node.label]