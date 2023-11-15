class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
#         # Memoization
#         stoneSum = sum(stones)
#         target = ceil(stoneSum / 2)

#         def dfs(i, total): # total so far
#             if total >= target or i == len(stones):
#                 # otherPile = stoneSum - total, abs(total - (stoneSum - total)) = smash them
#                 return abs(total - (stoneSum - total)) 
#             if (i, total) in memo:
#                 return memo[(i, total)]

#             memo[(i, total)] = min(dfs(i + 1, total), # not include cur val
#                                  dfs(i + 1, total + stones[i])) # include cur val at i
#             return memo[(i, total)]

#         memo = {}
#         return dfs(0, 0)

        # Tabulation
    
        memo = {0}
        sumA = sum(stones)
        for a in stones:
            memo |= {a + i for i in memo}
        return min(abs(sumA - i - i) for i in memo)
    
#         dp = {0}
#         for a in stones:
#             dp = {a + x for x in dp} | {abs(a - x) for x in dp}
#         return min(dp)

