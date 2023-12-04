from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

#         preMap = { i:[] for i in range(numCourses)}
        
#         for crs, pre in prerequisites:
#             preMap[crs].append(pre)
#         # a course has 3 possible states:
#         # unvisited -> crs not added to output or cycle
#         # visiting -> crs no added to output, but added to cycle
#         # visited -> crs has been added to output
#         res = []
#         visit, cycle = set(), set()
        
#         def dfs(crs):
#             if crs in cycle:
#                 return False
#             if crs in visit:
#                 return True
            
#             cycle.add(crs)
            
#             for pre in preMap[crs]:
#                 if not dfs(pre):
#                     return False
#             cycle.remove(crs)
#             visit.add(crs)
#             res.append(crs)
#             return True
                
                                
#         for crs in range(numCourses):
#             if not dfs(crs):
#                 return []
            
#         return res 

        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        # visited=[0]*numCourses
        indeg=[0]*numCourses
        res=[]
        q=deque()
        for i in range(numCourses):
            for j in adj[i]:
                indeg[j]+=1
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        while q:
            u=q.popleft()
            res.append(u)
            for i in adj[u]:
                if indeg[i]!=0:
                    indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        if len(res)!=numCourses:
            return []
        return res