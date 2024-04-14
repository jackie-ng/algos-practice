class Solution:
    def findNumberOfLISMemo(self, nums: List[int]) -> int:
        n = len(nums)
        length = [0] * n
        count = [0] * n
        result = 0

        def dfs(i):
            if length[i] != 0:
                return

            length[i] = 1
            count[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    dfs(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = 0
        for i in range(n):
            dfs(i)
            max_length = max(max_length, length[i])

        for i in range(n):
            if length[i] == max_length:
                result += count[i]

        return result
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        This function finds the number of longest increasing subsequences (LIS) in a given list of integers using Dynamic Programming.

        Args:
        nums: A list of integers.

        Returns:
        The number of LIS in the input list.
        """

        # Get the length of the input list
        n = len(nums)
        # Initialize two lists:
        #  - length: stores the length of the LIS ending at each index (nums[i])
        #  - count: stores the number of LIS of the current length (length[i]) ending at index i
        length = [1] * n # Initialize all lengths to 1 (single element LIS initially)
        count = [1] * n # Initialize all counts to 1 (assuming 1 LIS of length 1 for each element)
        
        # Iterate through each element in the list (nums[i])
        for i in range(n):
            # Iterate through elements before the current element (nums[j])
            for j in range(i):
                # Check if the element before (nums[j]) is less than the current element (nums[i])
                if nums[j] < nums[i]:
                    # If the potential LIS ending at i is longer than the current length
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1 # Update the length at i to the new longer length
                        count[i] = 0 # Reset the count at i to 0 (new starting point for this length)
                    # If the potential LIS ending at i has the same length
                    if length[j] + 1 == length[i]:
                        count[i] += count[j] # Increment the count at i to account for another LIS of the same length
        # Find the maximum length of any LIS seen so far
        max_length = max(length)
        # Initialize a variable to store the final result (number of LIS with maximum length)
        result = 0
        # Iterate through the list again
        for i in range(n):
            # Check if the length at the current index (i) is equal to the maximum length
            if length[i] == max_length:
                # Add the count at the current index to the result (number of LIS with max length)
                result += count[i]
        # Return the total number of LIS with the maximum length
        return result