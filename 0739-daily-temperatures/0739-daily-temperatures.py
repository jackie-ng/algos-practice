class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        # Monotonic Stack
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([t, i])
            
        return res