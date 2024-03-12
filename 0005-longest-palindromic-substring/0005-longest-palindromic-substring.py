class Solution:
    def longestPalindrome(self, s: str) -> str:
#         ### Expand from the middle ###
#         res = ""

#         # loop through every single character in s
#         for i in range(len(s)):
#            # Loop through odd/even length substring
#             for l, r in ((i,i), (i,i+1)): # odd and even length
#                 # while l,r pointers are inbound and is palindrome
#                 # expand res inclusively if the length is now longer
#                 while l >= 0 and r < len(s) and s[l] == s[r]:
#                     if (r - l + 1) > len(res):
#                         res = s[l:r + 1]
#                     l -= 1
#                     r += 1

#         return res
    
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        
        # Every individual character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # check for palindromes of length 2 to find the start index 
        # and then expand from the middle
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        
        # check for palidrome sub with length > 3
        # the purpose is to expand the length of the palindrome substring
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                # dp[i+1][j-1] = the start and end of a panlidrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]