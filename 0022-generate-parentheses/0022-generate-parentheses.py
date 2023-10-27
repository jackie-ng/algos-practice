class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parentheses if open < n
        # only add a closing parenthesis if close < open
        # valid if open == close == n
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            # valid
            if openN == closeN == n:
                validVal = "".join(stack)
                res.append(validVal)
                return
            # add "("
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            # add ")"
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res