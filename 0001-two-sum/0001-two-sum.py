class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: Make an array copy
        # copy_nums = nums.copy()
        # nums.sort()
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     sum = nums[left] + nums[right]
        #     if sum == target:
        #         break
        #     elif sum > target:
        #         right -= 1
        #     else:
        #         left += 1
        # result = []
        # for i in range(len(nums)):
        #     if copy_nums[i] == nums[left]:
        #         result.append(i)
        #     elif copy_nums[i] == nums[right]:
        #         result.append(i)
        # return result
        # --------------------------
        # Solution 2: Hash table 2 pass
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # # [2,7,11,15] target = 9
        # # {2: 0, 7: 1, 11: 2, 15: 3}
        # for i in range(len(nums)):
        #     different = target - nums[i]
        #     if different in hashmap and hashmap[different] != i:
        #         return [i, hashmap[different]]
        # ---------------------------
        # Solution 3: Hash table 1 pass
        hashmap = {}
        for i in range(len(nums)):
            different = target - nums[i]
            if different in hashmap and hashmap[different] != i:
                return [i, hashmap[different]]
            else:
                hashmap[nums[i]] = i