class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * len(s)
#         for i in range(len(s)):
#             for word in wordDict:
#                 # Handle out of bounds case
#                 if i < len(word) - 1:
#                     continue

#                 if i == len(word) - 1 or dp[i - len(word)]:
#                     if s[i - len(word) + 1:i + 1] == word:
#                         dp[i] = True
#                         break
#         return dp[-1]
    
#         memo = {}
#         def topDown(i):
#             # Base case: if the index can reach the end of the string, it can be segmented
#             if i == len(s):
#                 return True
#             # if the result for the current index is already memoized, return
#             if i in memo:
#                 return memo[i]
#             # Recursive case: Iterate through s. i: start, j: end
#             for j in range(i + 1, len(s) + 1):
#                 if s[i:j] in wordDict and topDown(j):
#                     memo[i] = True
#                     return True
#             memo[i] = False
#             return False
#         return topDown(0)
  
        n = len(s)
        words = set(wordDict)
        print(words)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
    
            