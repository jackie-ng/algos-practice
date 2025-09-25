"""
Objective: find the minimum number of coins (unlimited supply of each coin) needed to sum exactly to amount. If impossible, return -1.
Key insights (intuition):
- Let f(x) = fewest coins needed to make amount x.
- To make amount (x), pick a first coin c[0] and then you still need to make x - c[0]. So f(x) = 1 + f(x - c) for whichever c gives the minimum total.
- This naturally gives a recurrence that looks at smaller amounts — perfect for dynamic programming.
- Base case: f(0) = 0 (zero coins to make amount 0).
- If after exploring all choices some subamount is impossible, we treat it as infinity (or a sentinel) so it won't be chosen.

*** Proof for the recurrence relation

Define f(x) = minimum number of coins required to make amount x. Consider x > 0. If we use a coin c as the next coin toward x, then we need 1 coin (the c) plus an optimal way to make x - c, which is f(x - c). Because we can choose any coin c that is <= x, the optimal choice gives:
f(x) = 1 + min_{c in coins, c <= x} f(x - c)

Base cases:

f(0) = 0 (no coins needed).
If x < 0 we define f(x) = +∞ (impossible).
This recurrence follows directly from optimal substructure: an optimal solution for x contains an optimal solution for x - c (otherwise we could replace it and improve).
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # Memoization dictionary to store the minimum coins required for a given remaining amount
        # memo = {}

        # def dp(remaining):
        #     """
        #     Returns the minimum number of coins needed to make up 'remaining'.
        #     If it is not possible, returns float('inf').
        #     """

        #     # Base case: if remaining is exactly 0, no coins are needed
        #     if remaining == 0:
        #         return 0
            
        #     # Base case: if remaining goes negative, this path is invalid
        #     if remaining < 0:
        #         return float('inf')

        #     # If we have already solved this subproblem, return the stored answer
        #     if remaining in memo:
        #         return memo[remaining]

        #     # Initialize with infinity (we'll try to minimize this)
        #     min_coins = float('inf')

        #     # Try using each coin and compute the minimum coins required
        #     for coin in coins:
        #         result = dp(remaining - coin)  # recursive call with reduced amount
        #         if result != float('inf'):
        #             # If valid, update min_coins with the smaller option
        #             min_coins = min(min_coins, result + 1)

        #     # Store the computed result in memo dictionary
        #     memo[remaining] = min_coins
        #     return min_coins

        # # Solve for the full amount
        # ans = dp(amount)

        # # If the answer is infinity, it means no combination works
        # return ans if ans != float('inf') else -1
        # --------------------------------------
        # A large number to represent "infinity" (an impossible case).
        # We use this instead of float('inf') because we'll be doing arithmetic.
        INF = 10**9

        # dp[i] will hold the minimum number of coins required to make amount i
        # Initialize all values as INF, meaning "unreachable" initially.
        dp = [INF] * (amount + 1)

        # Base case: To make amount 0, we need 0 coins.
        dp[0] = 0

        # Build the dp table from amount = 1 up to the target amount
        for a in range(1, amount + 1):
            # Try every coin and check if it can be used to form 'a'
            for c in coins:
                if c <= a:  
                    # If coin c can be used (does not exceed current amount)
                    # Check if the sub-amount (a - c) is reachable
                    # If reachable, update dp[a] with the better (smaller) option
                    dp[a] = min(dp[a], dp[a - c] + 1)

        # After filling dp, if dp[amount] is still INF, it means no solution exists
        return dp[amount] if dp[amount] < INF else -1
