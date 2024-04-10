class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        
        # each character is a palindrome itself
        for i in range(n):
            dp[i][i] = True
        
        # check for palindrome having length = 2
        # and then expand from the middle
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]
        
        # check for palindrome with length > 3
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # dp[i+1][j-1] = the start and end of a panlidrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]