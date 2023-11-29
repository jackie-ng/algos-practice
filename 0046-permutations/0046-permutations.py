class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # base case
        if len(nums) == 1:
            return [nums[:]]
        # recursive case
        for i in range(len(nums)):
            n = nums.pop(0)
            subsets = self.permute(nums)
            for subset in subsets:
                subset.append(n)
            res.extend(subsets)
            # clean up
            nums.append(n)
        return res

# - The code uses a for loop to iterate over each element of the list `nums`.
# - Inside the loop, it pops an element (`n`) from the list and recursively generates all permutations of the remaining elements (`subsets`).
# - For each subset in the permutations, it appends the popped element `n` to create a new permutation.
# - These new permutations are added to the result list (`res`) using the `extend` method.
# - After the loop, the popped element n is appended back to the list nums. This step is necessary to restore the original state of the list before the next iteration.