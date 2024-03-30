class Solution:
    def minCostClimbingStairsMemo(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            one = cost[i-1] + dfs(i-1)
            two = cost[i-2] + dfs(i-2)
            
            memo[i] = min(one, two)
            return memo[i]
        return dfs(len(cost))
    
    def minCostClimbingStairsBU(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            one = min_cost[i-1] + cost[i-1]
            two = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(one, two)
        return min_cost[-1]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = two = 0
        for i in range(2, len(cost) + 1):
            one, two = min(one + cost[i-1], two + cost[i-2]), one
        return one
    