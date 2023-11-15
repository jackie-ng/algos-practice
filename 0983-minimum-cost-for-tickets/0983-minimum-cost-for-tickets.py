class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    #     1. i in days list:
    # we have three option:
    # a) 1-pass:dp[i] = dp[i-1] + costs[0]
    # b) 7-pass: dp[i] = dp[i-7] + costs[1]
    # c) 30-pass:dp[i] = dp[i-30] + costs[2]
    # in order to avoid negative index:
    # a) 1-pass:dp[i] =dp[max(0,i-1)] + costs[0]
    # b) 7-pass: dp[i] = dp[max(0,i-7)] + costs[1]
    # c) 30-pass:dp[i] = dp[max(0,i-30)] + costs[2]
    # 2. i not in days:
    # dp[i] = dp[i-1]
    # which simply means we don't have to spend money, and total costs remains same
            dp=[0 for i in range(days[-1] + 1)]
            dy = set(days)
            for i in range(days[-1]+1):
                if i not in dy: 
                    dp[i]=dp[i-1]
                else: 
                    dp[i]=min(dp[max(0,i-7)]+costs[1],
                              dp[max(0,i-1)]+costs[0],
                              dp[max(0,i-30)]+costs[2])
            return dp[-1]
        
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         memo = {}
        
#         def dfs(i):
#             if i == len(days):
#                 return 0
#             if i in memo:
#                 return memo[i]
#             memo[i] = float("inf")
            
#             for d, c in zip([1, 7, 30], costs):
#                 j = i # check if day is inbound
#                 while j < len(days) and days[j] < days[i] + d:
#                     j += 1
#                 memo[i] = min(memo[i], c + dfs(j))
#             return memo[i]
        
#         return dfs(0)
    
