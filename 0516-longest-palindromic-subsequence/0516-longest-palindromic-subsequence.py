# Time: O(n^2) Space: O(n^2) - For all three solutions
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:   
        # Dynamic Programming
        dp = [ [0] * (len(s) + 1) for i in range(len(s) + 1)]
        res = 0
        
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2 # i == j => each character is a palindrome itself
                    if i >= 1:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i >= 1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res


#         # Memoization
#         memo = {}
        
#         # (i, j) is start and end of the palindrome
#         def dfs(i, j):
#             # if i, j are out of bound
#             if i < 0 or j == len(s):
#                 return 0
#             # if i, j are already memoized
#             if (i, j) in memo:
#                 return memo[(i, j)]
            
#             # if the palindrome is found, expand the length
#             if s[i] == s[j]:
#                 length = 1 if i == j else 2 # i == j => each character is a palindrome itself
#                 memo[(i, j)] = length + dfs(i - 1, j + 1)
#             else:
#                 memo[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
#             return memo[(i, j)]
        
#         for i in range(len(s)):
#             dfs(i, i) # odd length
#             dfs(i, i + 1) # even length

#         return max(memo.values())
        
# # LCS Solution
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         return self.longestCommonSubsequence(s, s[::-1])
        
    
#     def longestCommonSubsequence(self, s1: str, s2: str) -> int:
#         N, M = len(s1), len(s2)
#         dp = [[0] * (M+1) for _ in range(N+1)]

#         for i in range(N):
#             for j in range(M):
#                 if s1[i] == s2[j]:
#                     dp[i+1][j+1] = 1 + dp[i][j]
#                 else:
#                     dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
#         return dp[N][M]