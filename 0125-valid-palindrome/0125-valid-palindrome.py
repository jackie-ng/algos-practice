class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        # a b b a
        # 0     3
        while i < j:
            #technically i <= j is gonna be the same
            while i < j and not s[i].isalnum():
                i+=1
            while i < j and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
    #O(N//2) time complexity
    #O(1) space 