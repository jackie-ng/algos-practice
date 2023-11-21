class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        
        # continues until the input integer x becomes zero
        while x:
            lastDigit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
            # Update x by removing its last digit
            x = int(x / 10)  # (python dumb) -1 // 10 = -1

            # Check if adding the current digit to the reversed result would cause an overflow or underflow
            if res > MAX // 10 or (res == MAX // 10 and lastDigit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and lastDigit < MIN % 10):
                return 0
            res = (res * 10) + lastDigit

        return res