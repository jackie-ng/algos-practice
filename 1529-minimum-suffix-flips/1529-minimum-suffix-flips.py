class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        status = '0'
        
        # loop through the target 
        # if the status != target: increment flips, switch the status
        for c in target:
            if c != status:
                flips += 1
                status = '0' if c == '0' else '1'
        return flips
# The first observation is,
# A[0] will only be flipped if i = 0.
# So if A[0] is 1 at first, we have to flip at i = 0.
# res++.

# For A[1], A[1] will be flipped if i = 0 or i = 1.
# Now we already know the operation at i = 0,
# A[1] will only be flipped if i = 1.

# The rule is,
# If res is odd, the current bit is flipped.
# If res is even, the current bit stays no change.
# if A[i] is 1, need to be flipped,
# if A[i] is 0, not need to flip.
# We keep doing that, and we can know the all operations for each i.

# time complexity O(N),
# space complexity O(1)