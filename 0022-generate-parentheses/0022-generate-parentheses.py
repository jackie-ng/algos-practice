class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []
        def backtrack(openN, closeN):
            #valid
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