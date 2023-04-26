class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #value: index
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        print(hashmap)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:        
#         copy_nums = nums.copy()
        
#         left = 0
#         right = len(nums) - 1
        
#         while left < right:
#             sum = nums[left] + nums[right]

#             if sum == target:
#                 break
#             elif sum > target:
#                 right -= 1
#             else:
#                 left += 1
                
#         result = []
#         for i in range(len(nums)):
#             if nums[left] == copy_nums[i]:
#                 result.append(i)
#             elif nums[right] == copy_nums[i]:
#                 result.append(i)
                
#         return result