# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]] 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        n = len(nums)
        a = nums.copy()

        nums.sort()

        l = 0
        r = n - 1

        while l < r:
            sum = nums[l] + nums[r]

            if sum == target:
                break
            elif sum > target:
                r -= 1
            else:
                l += 1

        v = []

        for i in range(n):
            if nums[l] == a[i]:
                v.append(i)
            elif nums[r] == a[i]:
                v.append(i)

        return v