class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursive + stack
        # only add open parenthesis if open < n
        # only add a closing parenthesis if close < open
        # valid IF open = close = n
        stack = []
        
        res = []
        
        def backtrack(open, close):
            if open == close == n: # finished. Stack contains proper parenthesis
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop() #update the stack since we only have a single stack variable
            if close < open: #add closing parenthesis => make sure that close < open
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()
                
        backtrack(0, 0) # pass 0 for the initial open and close count
        return res
