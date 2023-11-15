class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def canBreak(start):
            # If the start index reaches the end of the string, it can be segmented
            if start == len(s):
                return True

            # If the result for the current start index is already memoized, return it
            if start in memo:
                return memo[start]

            # Iterate through the string from the current start index
            for end in range(start + 1, len(s) + 1):
                # Check if the substring from start to end is in the word dictionary
                if s[start:end] in wordDict and canBreak(end):
                    # Memoize the result and return True
                    memo[start] = True
                    return True

            # If no valid segmentation is found, memoize the result and return False
            memo[start] = False
            return False

        # Start the recursion from the beginning of the string
        return canBreak(0)        
    
#         dp = [False] * len(s)
#             for i in range(len(s)):
#                 for word in wordDict:
#                     # Handle out of bounds case
#                     if i < len(word) - 1:
#                         continue

#                     if i == len(word) - 1 or dp[i - len(word)]:
#                         if s[i - len(word) + 1:i + 1] == word:
#                             dp[i] = True
#                             break

#             return dp[-1]