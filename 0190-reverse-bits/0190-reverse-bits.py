class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # Iterate through each bit position (32 bits in total)
        for i in range(32):
            # Extract the i-th bit from n
            bit = (n >> i) & 1
            # Set the corresponding bit in the result (res) by shifting it to the correct position
            res = res | (bit << (31 - i))
        # Return the reversed integer
        return res