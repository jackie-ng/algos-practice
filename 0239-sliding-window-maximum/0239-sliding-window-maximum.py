class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        for i in range(len(nums)):
            # Remove elements that are out of the current window from the front
            while q and q[0] < i - k + 1:
                q.popleft()

            # Remove elements that are smaller than the current element from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add the current index to the deque
            q.append(i)

            # Add the maximum element to the result for each window
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
