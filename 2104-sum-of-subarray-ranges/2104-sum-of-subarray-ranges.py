class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        res = 0
        inf = float('inf')
        A = [-inf] + nums + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + nums + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
        
        
        # res = 0
        # n = len(A)
        # for i in xrange(n):
        #     l,r = A[i],A[i]
        #     for j in xrange(i, n):
        #         l = min(l, A[j])
        #         r = max(r, A[j])
        #         res += r - l
        # return res