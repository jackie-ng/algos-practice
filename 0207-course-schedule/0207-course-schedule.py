class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         preMap = { i:[] for i in range(numCourses)}
#         for crs, pre in prerequisites:
#             preMap[crs].append(pre)
#         visit = []
#         def dfs(crs):
#             # Found a cycle => False
#             if crs in visit:
#                 return False
#             # Visited all courses without detecting a cycle => True
#             if preMap[crs] == []:
#                 return True
            
#             visit.append(crs)
#             for pre in preMap[crs]:
#                 if not dfs(pre):
#                     return False
#             visit.remove(crs)
#             preMap[crs] = []
#             return True
        
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return False
            
#         return True
    
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # Construct indegree table
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        # Append node(s) with 0 indegree to the queue
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        nodesVisited = 0
    
        while queue:
            node = queue.popleft()
            nodesVisited += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return nodesVisited == numCourses