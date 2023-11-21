class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        
        # abs(a) >= abs(b) --> 
        # a determines the sign
        sign = 1 if a > 0 else -1
        
        if a * b >= 0: # both a and b have the same sign
            # where x > y
            # Update x to be the XOR of x and y, and update y to be the left shift of the bitwise AND of x and y. 
            # This simulates the addition of x and y without carrying. (x + y)
            while y:
                x, y = x ^ y, (x & y) << 1
        else: # a and b have different sign
            # where x > y
            # Update x to be the XOR of x and y, and update y to be the left shift of the bitwise AND of the bitwise negation of x and y. 
            # This simulates the subtraction of y from x (x - y)
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign