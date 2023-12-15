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
        
        
# Intuition
# res = sum(A[i] * f(i))
# where f(i) is the number of subarrays,
# in which A[i] is the minimum.

# To get f(i), we need to find out:
# left[i], the length of strict bigger numbers on the left of A[i],
# right[i], the length of bigger numbers on the right of A[i].

# Then,
# left[i] + 1 equals to
# the number of subarray ending with A[i],
# and A[i] is single minimum.

# right[i] + 1 equals to
# the number of subarray starting with A[i],
# and A[i] is the first minimum.

# Finally f(i) = (left[i] + 1) * (right[i] + 1)

# For [3,1,2,4] as example:
# left + 1 = [1,2,1,1]
# right + 1 = [1,3,2,1]
# f = [1,6,2,1]
# res = 3 * 1 + 1 * 6 + 2 * 2 + 4 * 1 = 17

# Explanation
# To calculate left[i] and right[i],
# we use two increasing stacks.

# It will be easy if you can refer to this problem and my post:
# 901. Online Stock Span
# I copy some of my codes from this solution.

# Complexity
# All elements will be pushed twice and popped at most twice
# Time O(n)
# Space O(n)
        
        # res = 0
        # n = len(A)
        # for i in xrange(n):
        #     l,r = A[i],A[i]
        #     for j in xrange(i, n):
        #         l = min(l, A[j])
        #         r = max(r, A[j])
        #         res += r - l
        # return res