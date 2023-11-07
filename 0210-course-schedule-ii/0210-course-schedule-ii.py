from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj = [[] for i in range(numCourses)]
        visited = [0] * numCourses
        indeg = [0] * numCourses
        res = []
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            
        q = deque()
        
        for i in range(numCourses):
            for j in adj[i]:
                indeg[j] += 1
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            res.append(node)
            for i in adj[node]:
                if indeg[i] != 0:
                    indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)

        return res if len(res) == numCourses else []

