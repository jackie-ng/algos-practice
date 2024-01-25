class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
            buy[i] = max(
                cooldown[i - 1] - prices[i], # not buy
                buy[i - 1]) # buy

            # Update sell state
            sell[i] = max(
                buy[i - 1] + prices[i], #not sell
                sell[i - 1]) # sell

            # Update cooldown state
            cooldown[i] = max(cooldown[i - 1], sell[i - 1])

        # The maximum profit is the maximum of sell and cooldown on the last day
        return max(sell[n - 1], cooldown[n - 1])
    
