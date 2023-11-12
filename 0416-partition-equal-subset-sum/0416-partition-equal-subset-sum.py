class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set() # for unique values
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t) # save the previous values
            dp = nextDP # reassign dp to the next DP set
            # print(dp)
        return True if target in dp else False