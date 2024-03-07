class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        
        for n in nums:
            # find the start of the sequence
            if (n-1) not in numSet:
                # res += 1
                            
            # create a variable to hold the range of that sequence --- range = 0
                range = 0
                while (n + range) in numSet:
                # increment the range
                    range += 1
                res = max(res, range)
        return res
                

            # if n + range in numSet (ie 4 + 0, range = 1, 1+1=2)
            # res = max(res, range)