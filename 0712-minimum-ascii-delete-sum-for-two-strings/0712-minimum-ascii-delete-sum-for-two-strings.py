class Solution:
    def minimumDeleteSumMemo(self, s1: str, s2: str) -> int:
    
        # Dictionary to store the result of each sub-problem
        memo = {}

        # Return minimum cost to make s1[0...i] and s2[0...j] equal
        def dfs(i, j):

            # If both strings are empty, then no deletion is required
            if i < 0 and j < 0:
                return 0
            
            # If already computed, then return the result from the dictionary
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If any one string is empty, delete all characters of the other string
            if i < 0:
                memo[(i, j)] = ord(s2[j]) + dfs(i, j-1)
                return memo[(i, j)]
            if j < 0:
                memo[(i, j)] = ord(s1[i]) + dfs(i-1, j)
                return memo[(i, j)]
            
            # Call sub-problem depending on s1[i] and s2[j]
            # Save the computed result.
            if s1[i] == s2[j]:
                memo[(i, j)] = dfs(i-1, j-1)
            else:
                memo[(i, j)] = min(
                    ord(s1[i]) + dfs(i-1, j),
                    ord(s2[j]) + dfs(i, j-1)
                )

            return memo[(i, j)]

        # Return the result of the main problem
        return dfs(len(s1)-1, len(s2)-1)
    
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # Prepare the two-dimensional array
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the base case values
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        # Fill the remaining cells using the Bellman Equation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = min(
                        ord(s1[i-1]) + dp[i-1][j], # select the char in s1
                        ord(s2[j-1]) + dp[i][j-1]  # select the char in s2
                    )
        
        # Return the answer for entire input strings
        return dp[m][n]