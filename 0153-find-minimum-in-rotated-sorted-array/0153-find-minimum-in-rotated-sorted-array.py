# 1. Find the mid element of the array.
# 2. If mid element > first element of array this means that we need to look for the inflection point on the right of mid.
# 3. If mid element < first element of array this that we need to look for the inflection point on the left of mid.
# 4 . We stop our search when we find the inflection point, when either of the two conditions is satisfied:
# nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
# nums[mid - 1] > nums[mid] Hence, mid is the smallest.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if nums[l] < nums[r] => set the result to the minimum compare to the left most element. Then, break out of the loop
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2 # set middle value
            res = min(res, nums[m]) # update the result by getting minimum between the res itself and the value of the mid point 
            # to determine if we want to search the left or the right side
            # the mid value is in the LEFT portion if the value of the middle index is greater or equal to the value of the left most 
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res 