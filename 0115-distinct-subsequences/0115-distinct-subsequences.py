class Solution:
    def numDistinctMemo(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i, j):
            """
            This recursive function performs dynamic programming to count the number of distinct subsequences of string 't' found in string 's'

            Args:
              i: Index of the character currently being considered in string 's'
              j: Index of the character currently being considered in string 't'

            Returns:
              The number of distinct subsequences of 't' found in 's' starting from indices i and j
            """

            """ BASE CASE
            - Reached the end of string 's' (i == len(s))
            - Reached the end of string 't' (j == len(t))
            - Remaining length of 's' is less than the remaining length of 't' (insufficient characters in 's' to form the rest of 't')
            In all these cases, there are zero distinct subsequences, so return 0 (represents an empty subsequence)
            """
            if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
                return int(j == len(t))  # This is True only if j reaches the end of t (meaning the entire t is a subsequence)

            """
            - If we've already encountered this combination of indices (i, j) while exploring other subsequences,
          the answer (number of distinct subsequences) is already stored in the memo dictionary.
            - This avoids redundant calculations by reusing previously found results.
            """
            if (i, j) in memo:
                return memo[(i, j)]

            """ Recursive call considering the next character in 's' (i + 1)
            - This explores the possibility of excluding the current character (s[i]) from the subsequence.
            - The recursive call moves forward in 's' (i + 1) but keeps 'j' fixed in 't'.
            """
            res = dfs(i + 1, j)

            # If the characters at current indices (i, j) match
            if s[i] == t[j]:
                """
                - If the characters match, there's a possibility that the current character (s[i]) can be part of a subsequence.
                - Add the result of another recursive call (dfs(i + 1, j + 1)) to 'res'.
                - This call considers including the current character (s[i]) in the subsequence and moves forward in both strings (i + 1, j + 1).
                """
                res += dfs(i + 1, j + 1)

            # Cache the answer for the current subproblem (i, j) and return the final count
            memo[(i, j)] = res
            return res

        # Start the dynamic programming process from the beginning (i = 0, j = 0)
        return dfs(0, 0)
            
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        # Dynamic Programming table
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Base case initialization
        for i in range(m+1):
            dp[i][0] = 1

        """redundant, as we have initialised dp table with full of zeros"""
#         for i in range(1, n+1): 
#             dp[0][i] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] += dp[i-1][j] 			#if current character is skipped
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]	#if current character is used

        return dp[-1][-1]