class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        # dp
        # Two variables: index + sum
        # Cannot determine the range of sum, therefore, use a map (sum : ways) to keep
        # Update map for each index interation
        
        lookup = collections.Counter()
        lookup[nums[0]] += 1
        lookup[-nums[0]] += 1
        
        for i in range(1, len(nums)):
            # parepare a new map for the next iteration
            nextLookup = collections.Counter()
            # for each iteration, update each possible sum and it's count 
            for s in lookup:
                # current to be possitive
                nextLookup[s + nums[i]] += lookup[s]
                # current to be negative
                nextLookup[s - nums[i]] += lookup[s]
            # assign the new map to be the current map
            lookup = nextLookup
            
        return lookup[S]