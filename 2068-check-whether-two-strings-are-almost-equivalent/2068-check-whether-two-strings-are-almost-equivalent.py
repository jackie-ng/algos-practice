class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
#         dic = {}
        
#         for char in word1:
#             dic[char] = dic.get(char, 0) + 1
#         for char in word2:
#             dic[char] = dic.get(char, 0) - 1
        
#         dicFreq = max(abs(val) for val in dic.values())
#         return dicFreq <= 3
    
        dic = Counter(word1)
        for char in word2:
            dic[char] -= 1
        return max(abs(val) for val in dic.values()) <= 3