class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
#         memo = {}  # (index, total) -> # of ways

#         def backtrack(i, total):
#             if i == len(nums):
#                 return 1 if total == target else 0
#             if (i, total) in memo:
#                 return memo[(i, total)]
#             # add the value at index i + subtract the value at index i
#             memo[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])    
#             return memo[(i, total)]

#         return backtrack(0, 0)
        
        # dp
        # Two variables: index + sum
        # Cannot determine the range of sum, therefore, use a map (sum : ways) to keep
        # Update map for each index interation
        
        lookup = collections.Counter()
        lookup[nums[0]] += 1
        lookup[-nums[0]] += 1
        print("lookup", lookup)
        for i in range(1, len(nums)):
            # parepare a new map for the next iteration
            nextLookup = collections.Counter()
            print("nextLookup", nextLookup)
            # for each iteration, update each possible sum and it's count 
            for s in lookup:
                # current to be possitive
                nextLookup[s + nums[i]] += lookup[s]
                # current to be negative
                nextLookup[s - nums[i]] += lookup[s]
            # assign the new map to be the current map
            lookup = nextLookup
        return lookup[target]