class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
#         i = 0
#         while i < len(words) - 1:
#             if sorted(words[i]) == sorted(words[i + 1]):
#                 words.remove(words[i + 1])
#                 continue
#             i += 1
#         return words
    
        res = [words[0]]
        for i in range(1,len(words)):
            if Counter(res[-1]) != Counter(words[i]):
                res.append(words[i])
        return res