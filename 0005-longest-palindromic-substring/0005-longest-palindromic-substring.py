class Solution:
    def longestPalindrome(self, s: str) -> str:
#         ### Expand from the middle ###
#         res = ""

#         for i in range(len(s)):
#             for l, r in ((i,i), (i,i+1)): # odd and even lengths
#                 while l >= 0 and r < len(s) and s[l] == s[r]:
#                     if (r - l + 1) > len(res):
#                         res = s[l:r + 1]
#                     l -= 1
#                     r += 1

#         return res
    
        ### DP ###

        n = len(s)

        # Create a table to store whether a substring is a palindrome
        dp = [[False] * n for _ in range(n)]

        start = 0  # Start index of the longest palindromic substring
        max_length = 1  # Length of the longest palindromic substring

        # Every individual character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i  # Update start index
                max_length = 2  # Update length

        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Check if the substring from i to j is a palindrome
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j]:
                    start = i  # Update start index
                    max_length = length  # Update length

        # Return the longest palindromic substring
        return s[start:start + max_length]
