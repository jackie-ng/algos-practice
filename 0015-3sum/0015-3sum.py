class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        [-4, -1, -1, 0, 1, 2]
        [0, 1, 2, 3, 4, 5, 6]
        
        for index, value in enumerate(nums):
            # We don't want to reuse the same value in the same position twice
            # if it's not the first value in the input array 
            # and the value is equal to the value as before (nums[1] = nums[2] = -1)
            # => continue to the next iteration for the remaining portion of the array 
            #         [-4, -1, -1, 0, 1, 2]
            #         [0, 1, 2, 3, 4, 5, 6]
            #          i  l(i+1)         r(len-1)
            if index > 0 and value == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    # Update the pointers
                    # skipping if we found the duplicate of l and we dont need to check (nums[1] = nums[2] = -1)
					# the duplicate of r cause it will automatically skip the duplicate by the adjustment of l and r
                    l += 1 # 
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res