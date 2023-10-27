class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # Monotonic Decreasing Stack: stack in decreasing order
        res = [0] * len(temp)
        stack = [] # pair value: [i, temp]
        
        for i, t in enumerate(temp):
            # check if stack is empty and the value of the current t is > stack[-1]
            while stack and t > stack[-1][1]:
                stackInd, stackT = stack.pop()
                # add the index differences to the corresponding position in res
                res[stackInd] = (i - stackInd)
            stack.append([i, t])
        return res