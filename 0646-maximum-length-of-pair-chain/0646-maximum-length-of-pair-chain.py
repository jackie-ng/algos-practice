class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs in ascending order based on the second element (end value).
        pairs.sort(key=lambda x: x[1])
        """
        Explanation:
        Sorting by the end value ensures we process pairs in an order where the end of
        one pair can potentially be the beginning of the next pair in the chain. This 
        facilitates building the longest chain efficiently.
        """

        # Initialize variables
        curr = float('-inf')  # Represents the current end of the considered chain (initially negative infinity)
        ans = 0              # Stores the length of the longest chain found so far

        for pair in pairs:
            # Check if the current pair's starting value is greater than the current end of the chain.
            if pair[0] > curr:
                ans += 1  # If yes, it's a new chain, increment the count
                curr = pair[1]  # Update the current end with the end of the new pair

        return ans
    
    def findLongestChainDP(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1] * n
        ans = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        return ans