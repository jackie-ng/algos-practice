class Solution:
    """
    1. Initialize an empty stack and an answer array filled with zeros.
    2. Iterate through each temperature with its index:
    │
    ├── While stack is not empty and current temperature > temperature at stack's top index:
    │     │→ Pop the top index from the stack.
    │     │→ Calculate days waited: current index - popped index.
    │     │→ Update answer[popped index] = days waited.
    │
    └── Push current index onto the stack.
    3. Return the answer array.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        
        return answer
            