class Solution:
    def numDecodings(self, s: str) -> int:
        memo = { len(s) : 1 }
        
        def dfs(i):
            if i in memo:
                return memo[i]
            ### if it's not the end of the string
            # invalid
            if s[i] == "0": 
                return 0
            
            # valid
            res = dfs(i + 1)
            if(i + 1 < len(s) and # if the digit is inbound
               (s[i] == "1" or  # if the num is from 10-19
                s[i] == "2" and s[i + 1] in "0123456")): # if the num is from 20-26 
                
                res += dfs(i + 2)
            memo[i] = res
            return res
        
        return dfs(0)
                