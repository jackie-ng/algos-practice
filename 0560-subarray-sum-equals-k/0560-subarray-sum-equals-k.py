"""
1. Prefix Sum and Hash Map: Use a hash map to store the frequency of prefix sums encountered during the iteration.
2. Current Sum: Maintain a running sum of elements as we iterate through the array.
3. Check for Target: For each element, check if current_sum - k exists in the hash map. If it does, it means there are subarrays ending at the current index that sum to k.
4. Update Hash Map: Update the hash map with the current sum to keep track of its frequency.

Time Complexity:
- O(n) - Single pass through the array.
Space Complexity:
O(n) - In the worst case, the hash map can store up to n distinct prefix sums.
"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = {0: 1}  # Initialize with prefix sum 0 occurring once
        current_sum = 0
        for num in nums:
            current_sum += num
            # If (current_sum - k) exists in prefix_sum, it means there are subarrays ending here summing to k
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            # Update the prefix_sum map with the current_sum
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count