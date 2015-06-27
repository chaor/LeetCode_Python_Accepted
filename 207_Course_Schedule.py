# 2015-06-27  Runtime: 56 ms
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # thanks to https://leetcode.com/discuss/35605/two-ac-solution-in-java-using-bfs-and-dfs-with-explanation
        # initialize the graph
        incomingEdgeCount, outgoingEdge = [0 for i in xrange(numCourses)], [[] for i in xrange(numCourses)]
        for p in prerequisites:
            outgoingEdge[p[1]].append(p[0])
            incomingEdgeCount[p[0]] += 1
        
        # BFS, if a node's incomingEdgeCount == 0, then visit it and delete it from graph
        order, queue = [], collections.deque()
        for i in xrange(numCourses):
            if incomingEdgeCount[i] == 0: queue.append(i)
        while queue:
            visitedCourse = queue.popleft()
            order.append(visitedCourse)
            for to in outgoingEdge[visitedCourse]:
                incomingEdgeCount[to] -= 1
                if incomingEdgeCount[to] == 0: queue.append(to)
        return True if len(order) == numCourses else False