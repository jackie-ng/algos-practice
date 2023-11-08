class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        
        def isPalidrome(s): 
            
            l, r = 0, len(s) - 1
            while l < r:
                if (s[l] != s[r]):
                    return False
                else:
                    l = l+1
                    r = r-1
            return True
            
        
        for i in range(len(words)):
            if isPalidrome(words[i]):
                return words[i]
            else:
                continue
        return ""
        
            
        
        
        
        

# ["abc","car","ada","racecar","cool"]
                
