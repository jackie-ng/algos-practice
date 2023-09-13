class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #Naive approach
        # newStr = ""
        # for char in s:
        #     if char.isalnum():
        #         newStr += char.lower()
        # return newStr == newStr[::-1] #[::-1] syntax to reverse a string
        ## => create extra memory by creating new string and reverse the string => O(2n) => O(n)
        
        #Better approach: Two Pointers, using ASCII value to determine if a char is alpha numerical
        
        l, r = 0, len(s) - 1
        # The pointers has not met each other yet
        while l < r: 
            #Check if the char is inbound and not alphaNum 
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            # if a single pair is NOT equal, return immediately
            if s[l].lower() != s[r].lower():
                return False 
            # Update the pointers for the next position
            l += 1
            r -= 1
        return True
    
    def alphaNum(self, c):
        # ord() func will extract the ASCII value of a char
        # compare if the 'c' character is in range
        # return true => alphanum, false => otherwise
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )