"""
The SCS can be constructed using the Longest Common Subsequence (LCS) of str1 and str2.
Why? Because:
- Any common characters in the LCS only need to appear once in the supersequence.
- Characters outside the LCS must be included in order to preserve both strings as subsequences.
Strategy:
- Find the LCS of str1 and str2.
- Merge the two strings around the LCS:
    + Walk through both strings, adding non-LCS characters along the way.
    + Add the LCS character once, then continue.
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = self.compute_lcs(str1, str2)

        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            # If characters match, they are part of LCS
            # Add the matching character to SCS
            # Move diagonally up-left in DP table
            if str1[i-1] == str2[j-1]:
                scs.append(str1[i-1])
                i -= 1
                j -= 1
            # If top cell has larger LCS value
            # Add character from str1
            # Move up in DP table
            elif dp[i-1][j] > dp[i][j-1]:
                scs.append(str1[i-1])
                i -= 1
            # If left cell has larger or equal LCS value
            # Add character from str2
            # Move left in DP table
            else:
                scs.append(str2[j-1])
                j -= 1

        # Add remaining characters if one string is exhausted
        while i > 0:
            scs.append(str1[i-1])
            i -= 1
        while j > 0:
            scs.append(str2[j-1])
            j -= 1

        scs.reverse()
        return ''.join(scs)

    # compute the LCS table (bottom-up DP) for str1 and str2.
    def compute_lcs(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp
