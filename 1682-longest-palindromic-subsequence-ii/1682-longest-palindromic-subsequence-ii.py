# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:        
#         n = len(s)
#         prev = [0] * n
        
#         for i in range(n - 1, -1, -1):
#             curr = [0] * n
#             curr[i] = 1
#             for j in range(i + 1, n):
#                 if s[i] == s[j]:
#                     curr[j] = 2 + prev[j - 1]
#                 else:
#                     curr[j] = max(prev[j], curr[j - 1])
#             prev = curr
#         return curr[-1]
    
    
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [(0, None)] * n
        for i in range(n - 1, -1, -1):
            curr = [(0, None)] * n
            for j in range(i + 1, n):
                if s[i] == s[j] != prev[j - 1][1]:
                    curr[j] = (2 + prev[j - 1][0], s[i])
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return curr[-1][0]
    
# https://leetcode.com/problems/longest-palindromic-subsequence-ii/discuss/1403796/Python-O(n-2)-time-O(n)-space