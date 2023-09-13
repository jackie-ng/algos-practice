class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Naive approach
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1] #[::-1] syntax to reverse a string
            