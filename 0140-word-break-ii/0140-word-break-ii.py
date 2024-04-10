class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # https://leetcode.com/problems/word-break-ii/discuss/744674/Diagrammatic-Python-Intuitive-Solution-with-Example
        memo = {}
        def wordsEndingIn(i):
            # Base case: if i reach the end of the string
            if i == len(s):
                return [""]
            # if i is already in memo, return memo[i]
            if i in memo:
                return memo[i]
        
      # - Check all the substring from i to j-1 (exclusive)
      # - If it's a word, get all possible sentences ending at index 'j' (remaining string)
      # - If the remaining string is not empty => append current word + " " + remaining string
      # - If the remaining string is empty => append current word
            ans = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    for tail in wordsEndingIn(j):
                        if tail != '':
                            ans.append(s[i:j] + " " + tail) 
                        else:
                            ans.append(s[i:j])
            memo[i] = ans
            return ans
        return wordsEndingIn(0)