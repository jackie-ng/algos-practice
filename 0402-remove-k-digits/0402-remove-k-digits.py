class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        This function removes at most 'k' digits from the non-negative integer 'num' such that the new number is the smallest possible.

        Args:
            num: The input string representing a non-negative integer.
            k: The number of digits to remove at most.

        Returns:
            The smallest possible string formed by removing at most 'k' digits from 'num'.
        """

        numStack = []  # Stack to store digits during processing

        # Iterate through each digit in the input string
        for digit in num:
            # Keep removing digits from the stack if:
            # - We still have digits to remove (k > 0)
            # - The stack is not empty
            # - The digit at the top of the stack (numStack[-1]) is greater than the current digit
            while k > 0 and numStack and numStack[-1] > digit:
                numStack.pop()  # Remove the larger digit
                k -= 1  # Decrement the number of digits to remove

            # Append the current digit to the stack
            numStack.append(digit)

        # Handle edge cases:
        # - If k digits were not removed completely (k > 0), remove them from the end of the stack.
        finalStack = numStack[:-k] if k else numStack  # Keep all digits if k is 0
        # - Remove leading zeros from the final string.

        # Return the smallest number formed (or "0" if all digits were removed)
        return "".join(finalStack).lstrip('0') or "0"
