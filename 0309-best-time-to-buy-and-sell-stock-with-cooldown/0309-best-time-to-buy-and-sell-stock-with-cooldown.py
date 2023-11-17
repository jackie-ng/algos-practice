class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         # State: Buying or Selling?
#         # If Buy -> i + 1
#         # If Sell -> i + 2

#         memo = {}  # key=(i, buying) val=max_profit

#         def dfs(i, buying):
#             # Base case: reached the end of the array
#             if i >= len(prices):
#                 return 0
            
#             # Check if the result is already memoized, return the max profit
#             if (i, buying) in memo:
#                 return memo[(i, buying)]
            
#             # Case 1: Do nothing (cooldown) after we sell or buy
#             cooldown = dfs(i + 1, buying)
            
#             # Case 2: Buy the stock
#             if buying:
#                 # if we in the buying state => we now move into NOT buying state
#                 # minus the prices[i]. Now we changed to the state to find the max profit of the remainder
#                 buy = dfs(i + 1, not buying) - prices[i] 
#                 memo[(i, buying)] = max(buy, cooldown)
#             # Case 3: Sell the stock
#             else:
#                 # i + 2 because we HAVE to take a cool down day
#                 sell = dfs(i + 2, not buying) + prices[i]
#                 memo[(i, buying)] = max(sell, cooldown)
#             return memo[(i, buying)]

#         return dfs(0, True)
    
    
#             for price in prices:
#                 # Alternative: the calculation is done in parallel.
#                 # Therefore no need to keep temporary variables
#                 #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

#                 pre_sold = sold
#                 sold = held + price
#                 held = max(held, reset - price)
#                 reset = max(reset, pre_sold)

#             return max(sold, reset)

            if not prices:
                return 0

            n = len(prices)

            # Initialize the states
            buy = [0] * n
            sell = [0] * n
            cooldown = [0] * n

            # Initial values for the first day
            buy[0] = -prices[0]
            sell[0] = 0
            cooldown[0] = 0

            for i in range(1, n):
                # Update buy state
                buy[i] = max(cooldown[i - 1] - prices[i], buy[i - 1])

                # Update sell state
                sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])

                # Update cooldown state
                cooldown[i] = max(cooldown[i - 1], sell[i - 1])

            # The maximum profit is the maximum of sell and cooldown on the last day
            return max(sell[n - 1], cooldown[n - 1])