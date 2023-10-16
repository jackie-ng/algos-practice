class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) } # each course set to empty list
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet = all course along the curr DFS path
        visitSet = set()
        
        def dfs(crs):
            ## base case ##
            if crs in visitSet: # detect a loop
                return False
            if preMap[crs] == []: # this course has no prereq
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]: 
                if not dfs(pre): return False ## if 1 course cannot be completed => return False
            
            visitSet.remove(crs) #finish visiting => remove from visitSet
            preMap[crs] = [] # to avoid repeated work since we checked it before
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True