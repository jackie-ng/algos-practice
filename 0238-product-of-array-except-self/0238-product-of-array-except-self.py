class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, - 1, - 1):
            res[i] *= postfix        
            postfix *= nums[i]
        return res
        
        
        
        
#          lets change 1, 2, 3, 4 positions to symbols like a, b, c, d, so multiplying will be:
# prefix:
# ->
# |       a       |   a*b   | a*b*c | a*b*c*d |
# postfix:
# <-
# | a*b*c*d | b*c*d |   c*d   |      d        |

# the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
# |    b*c*d  | a*c*d | a*b*d |   a*b*c   |

# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(range(0, 30, 5))
# [0, 5, 10, 15, 20, 25]
# >>> list(range(0, 10, 3))
# [0, 3, 6, 9]
# >>> list(range(0, -10, -1))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> list(range(0))
# []
# >>> list(range(1, 0))
# []