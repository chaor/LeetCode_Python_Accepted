# 2015-05-09  Runtime: 88 ms
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # build graph
        self.G = [{'status':'untouched', 'neighbors':[]} for i in xrange(numCourses)]
        for edge in prerequisites:
            self.G[edge[1]]['neighbors'].append(edge[0])
        
        # DFS, use 'untouched', 'visiting', 'visited' to mark nodes,
        # during DFS if a 'visiting' node is reached, then there's a cycle
        # 碰到了一个‘visiting’状态的节点，说明有环
        for node in xrange(numCourses):
            if self.G[node]['status'] == 'visiting': return False
            if self.G[node]['status'] == 'untouched' and not self.dfs(node): return False
        return True
    
    def dfs(self, node):
        self.G[node]['status'] = 'visiting'
        for neighbor in self.G[node]['neighbors']:
            if self.G[neighbor]['status'] == 'visiting': return False
            if self.G[neighbor]['status'] == 'untouched' and not self.dfs(neighbor): return False 
        self.G[node]['status'] = 'visited'
        return True