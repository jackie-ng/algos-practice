class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # # 2 pass
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     different = target - nums[i]
        #     if different in hashmap and hashmap[different] != i:
        #         return [i, hashmap[different]] 
            
        # 1 pass
        for i in range(len(nums)):
            different = target - nums[i]
            if different in hashmap and hashmap[different] != i:
                return [i, hashmap[different]]
            else:
                hashmap[nums[i]] = i

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