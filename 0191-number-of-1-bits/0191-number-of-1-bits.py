class Solution:
    def hammingWeight(self, n: int) -> int:
        # big O(32) -> O(1)
        res = 0
        while n:
            res += n % 2
            n = n >> 1 # bit shift to the right by 1
#             n &= n - 1
#             res += 1
        return res