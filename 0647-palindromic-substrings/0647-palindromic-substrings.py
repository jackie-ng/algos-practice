class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        
        for i in range(n):
            dp[i][i] = True
        
        count = n # each character is a palidromic substring by itself
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1
        
        
        for length in range(2, n):
            for i in range(n-length):
                j = i+length
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        
        return count