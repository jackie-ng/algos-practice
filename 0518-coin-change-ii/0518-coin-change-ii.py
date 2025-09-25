"""
Objective: count how many different combinations of the given coins (unlimited copies each) sum exactly to amount. Order does not matter: [2,1,1,1] and [1,2,1,1] are the same combination.
Key insights (simple):
- We need to avoid counting permutations. A common trick: process coins in a fixed order and at each step decide how many of the current coin to take (or equivalently: either take the current coin and stay at the same index, or skip it and move to the next coin).
- Let f(i, remain) = number of ways to make remain using coins from index i to end (coins[i:], in fixed order). Then for coin coins[i]:
    - either we skip it: f(i+1, remain)
    - or we use it at least once: f(i, remain - coins[i]) (we can still use coin i again)
- So f(i, remain) = f(i+1, remain) + f(i, remain - coins[i]) (when coins[i] <= remain).
- Base case: remain == 0 → 1 way (choose nothing). remain < 0 → 0 ways. If we run out of coins (i == n) and remain > 0 → 0 ways.

***Proof for the recurrence relation
Define f(i, r) = number of combinations to make remaining amount r using coins from index i to n-1 (where coins are considered in a fixed order).
For a given state (i, r):
- If we skip coin i, the number of combinations is f(i+1, r).
- If we take coin i (possible only if coins[i] <= r), then after taking one coin i we still need to make r - coins[i] using coins i..n-1, so number of combinations contributed is f(i, r - coins[i]).
These two choices are disjoint (because skip means zero copies of coin i, take means at least one copy), so we add them:
- f(i, r) = f(i+1, r) + f(i, r - coins[i])   (if coins[i] <= r)
- f(i, r) = f(i+1, r)                         (if coins[i] > r)

Base cases:

- f(i, 0) = 1 for any i (one way to make 0: choose nothing).
- f(n, r) = 0 for r > 0 (no coins left but positive remaining).
- f(i, r) = 0 for r < 0 (invalid).

This recurrence follows from the principle of optimal substructure and partitioning the solution space by the number of copies of coin i.
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Count combinations to make 'amount' using coins (order does not matter).
        Uses dictionary-based memoization with detailed comments.
        """
    # # Number of coin types
    # n = len(coins)
    # # Memoization dictionary to cache the result for state (index, remaining)
    # # Key: (i, remain) -> Value: number of combinations to make 'remain' using coins[i:]
    # memo = {}
    # def dp(i, remain):
    #     """
    #     Returns the number of combinations to make 'remain' using coins from index i onward.
    #     """
    #     # Base case: exact match — one valid combination (choose nothing)
    #     if remain == 0:
    #         return 1
    #     # Base case: remain became negative — no valid combination
    #     if remain < 0:
    #         return 0
    #     # Base case: no coins left but remain > 0 — impossible to form remain
    #     if i == n:
    #         return 0
    #     # If the state is already computed, return cached value to avoid recomputation
    #     if (i, remain) in memo:
    #         return memo[(i, remain)]
    #     # Option 1: skip the current coin (move to next coin)
    #     ways_skip = dp(i + 1, remain)
    #     # Option 2: use the current coin (stay at same index, reduce remaining)
    #     # We only attempt this if the coin value is not greater than remain.
    #     ways_use = 0
    #     if coins[i] <= remain:
    #         ways_use = dp(i, remain - coins[i])
    #     # Total ways is sum of both disjoint choices
    #     total_ways = ways_skip + ways_use
    #     # Memoize the computed result for (i, remain)
    #     memo[(i, remain)] = total_ways
    #     return total_ways
    # # Start from coin index 0 and target amount
    # return dp(0, amount)
        """
        -----------------
        The standard bottom-up DP for "coin change II" (count combinations) can be implemented as:
        2D DP: dp[i][r] = ways to make r using coins from i..n-1. This uses O(n*amount) memory.
        Optimized 1D DP: dp[r] = ways to make r using coins processed so far. 
        To avoid counting permutations, iterate coins in outer loop and amounts in inner loop from coin to amount.
        """
        # dp[r] will store the number of combinations to make amount r
        # Initialize with 0 (no ways known yet)
        dp = [0] * (amount + 1)

        # Base case: There's exactly 1 way to make amount 0 — choose nothing
        dp[0] = 1

        # Process coins one by one. Outer loop over coins ensures combinations are counted
        # in a canonical order (prevents permutations from being counted).
        for coin in coins:
            # For current coin, update all reachable amounts from coin to amount
            # We go from coin up to amount (increasing), because dp[a] depends on dp[a - coin]
            for a in range(coin, amount + 1):
                # If there are dp[a - coin] ways to make (a - coin) using coins processed so far
                # then by adding current coin we get dp[a - coin] additional ways to make a.
                dp[a] += dp[a - coin]
                # Note: we do not use min or other operations — we are counting ways,
                # and addition accumulates the number of distinct combinations.

        # dp[amount] now contains the number of combinations to make 'amount'
        return dp[amount]