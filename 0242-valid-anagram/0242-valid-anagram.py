class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # build 2 hash maps: O(s + t), O(1)
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #0 is a default value if s[i] does not exist in the hashmap
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False
        return True
            
#         freq = [0] * 26
#         for i in range(len(s)):
#             freq[ord(s[i]) - ord('a')] += 1
#             freq[ord(t[i]) - ord('a')] -= 1
        
#         for i in range(len(freq)):
#             if freq[i] != 0:
#                 return False
        
#         return True
    
#         for c in countS:
#             if countS[c] != countT[c]:
#                 return False
            
#         return True

           
    
    
    