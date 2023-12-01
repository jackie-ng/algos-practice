class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ### Top Down ###
    
        memo = {}
        
        def dfs(amount):
            if amount in memo: 
                return memo[amount]
            if amount == 0: 
                return 0
            if amount < 0: 
                return float("inf")
            memo[amount] = min([1 + dfs(amount - coin) for coin in coins])
            return memo[amount]
        
        res = dfs(amount)
        return res if res < float("inf") else -1
        
                
        
#         ### Bottom Up ###
       
#         # Values in this array equal the number of coins needed to achieve the cost of the index
#         dp = [amount + 1] * (amount + 1)
#         dp[0] = 0
#         # Loop through every needed amount
#         for a in range(1, amount + 1):
#             # Loop through every needed coin value
#             for c in coins:
#                 # check if the coin is not bigger than the current amount
#                 if a - c >= 0: # if the amount is non-negative
#                     dp[a] = min(dp[a], 1 + dp[a-c]) ## coins needed to make the amount before adding the current coin to it (+1 to add the cur coin) 
                    
#         return dp[amount] if dp[amount] != amount+1 else -1