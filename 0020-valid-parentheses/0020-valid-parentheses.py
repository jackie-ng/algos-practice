class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in hash: # opening parentheses
                if stack and stack[-1] == hash[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)
                
        return True if not stack else False