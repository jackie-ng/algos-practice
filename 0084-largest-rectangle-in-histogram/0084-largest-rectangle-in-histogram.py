class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            
            # If stack is not empty and the top value of the stack HEIGHT is greater than the height that we just reached
            # => pop our stack/pop the height
            # => check the max rectangle we can create from that height
            # => extend the current height that we're at backwards
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                # area = height * width
                # width = i - index
                # i: current index we're at
                # index: index we just pop
                maxArea = max(maxArea, height * (i - index))
                # as this height > h (h: the height we're visiting) => we can extend our start index backwards to the index that we just popped
                start = index
                
                #### adding element to the stack ####
            stack.append((start, h))
                
        ## There're still entries in our stack => these were able to be extended all the way to the end of the histogram so we still have to compute their heights
        for i, h in stack:
            maxArea = max(maxArea, h * ((len(heights) - i))) ## extend all the way to the END of the histogram => length of histogram - start value i that was stored in the stack
        return maxArea
                