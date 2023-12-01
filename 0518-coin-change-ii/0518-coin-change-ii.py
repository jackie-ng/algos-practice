class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
#         # MEMOIZATION
#         # Time: O(n*m)
#         # Memory: O(n*m)
#         memo = {}

#         def dfs(i, remaining_amount):
#             if remaining_amount == amount:
#                 return 1 # One way to make up the amount is not choosing any coin.

#             if remaining_amount > amount or i == len(coins):
#                 return 0 # No more coins or the amount is negative, no valid combination.
#             if (i, remaining_amount) in memo:
#                 return memo[(i, remaining_amount)]

#             memo[(i, remaining_amount)] = dfs(i, remaining_amount + coins[i]) + dfs(i + 1, remaining_amount)
#             return memo[(i, remaining_amount)]

#         return dfs(0, 0)

        # # DYNAMIC PROGRAMMING
        # # Time: O(n*m)
        # # Memory: O(n*m)
        # dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        # dp[0] = [1] * (len(coins) + 1)
        # for a in range(1, amount + 1):
        #     for i in range(len(coins) - 1, -1, -1):
        #         ## update its value by copying the value from the cell to the right
        #         dp[a][i] = dp[a][i + 1]
        #         ## current coin can be included without exceeding the amount. 
        #         ## add the value from the cell above and to the left (dp[a - coins[i]][i]) to the current cell.
        #         if a - coins[i] >= 0:
        #             remaining = a - coins[i]
        #             dp[a][i] += dp[remaining][i]
        # return dp[amount][0]

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                # not including any coin by copying the coin over from the previous table dp to nextDP
                nextDP[a] = dp[a]
                # including the current coin
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]