class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        
        # abs(a) >= abs(b) --> 
        # a determines the sign
        sign = 1 if a > 0 else -1
        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign