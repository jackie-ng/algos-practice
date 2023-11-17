class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
                return 0

        # Initialize variables to keep track of the first and second buy and sell
        buy1, sell1, buy2, sell2 = float('inf'), 0, float('inf'), 0

        for price in prices:
            # Update the first buy and sell
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)

            # Update the second buy and sell
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        # Return the maximum profit after two transactions
        return sell2