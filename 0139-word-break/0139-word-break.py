class Solution:
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