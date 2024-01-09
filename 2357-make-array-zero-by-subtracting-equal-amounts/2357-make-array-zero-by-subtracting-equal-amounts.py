class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
#         Same elements, are always same
#         -> Deduplicate

#         Different elements, are always different until 0
#         -> Counts unique elements
        return len(set(nums) - {0})