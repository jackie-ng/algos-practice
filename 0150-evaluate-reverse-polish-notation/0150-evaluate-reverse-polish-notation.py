class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif  c == "-":
                # pop twice
                a, b = stack.pop(), stack.pop()
                # take the one pop second and subtract to the one that popped first
                stack.append(b - a)
            elif  c == "*":
                stack.append(stack.pop() * stack.pop())
            
            elif  c == "/":
                 # pop twice
                a, b = stack.pop(), stack.pop()
                # take the one pop second and divide to the one that popped first
                # then round it
                stack.append(int(b / a))
            else: #it's a number => convert it into a number
                stack.append(int(c))
        return stack[0]