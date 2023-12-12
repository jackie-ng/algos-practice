class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum = 0
        dic = {0: 1}
        for i in range(len(nums)):
            sum += nums[i]
            diff = sum-k
            # if diff in dic, add diff, else, add 0
            res += dic.get(diff, 0) 
            # at key "sum": val starts at 0, increment by 1
            dic[sum] = dic.get(sum, 0)+1 
        return res
    

# Time Complexity :
#     O(N) -> Where N is the size of the array and we are iterating over the array once

# Space Complexity:
#     O(N) -> Creating a hashmap/dictionary
