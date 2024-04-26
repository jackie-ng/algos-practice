class Solution:
    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0: 
                return True

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            
            return False
        
        return dp(len(s) - 1)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                wordStart = i - len(word)
                wordEnd = len(word) - 1
                if wordStart < -1:
                    continue
                
                if i == wordEnd or dp[wordStart]:
                    if s[wordStart+1 : i+1] == word:
                        dp[i] = True
                        break
        return dp[-1]