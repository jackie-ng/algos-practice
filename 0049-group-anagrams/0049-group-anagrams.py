# from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Defining a dictionary with values as a list (mapping charCount to list of Anagrams)
        print(res)
        for s in strs:
            count = [0] * 26 # a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # print(res[tuple(count)], "s:", s)
            res[tuple(count)].append(s) # list cannot be keys =>  tuple
            
        return res.values()
    
#     def groupAnagrams(self, strs):
#         d = {}
        
#         for i in range(len(strs)):
#             print(sorted(strs[i]))
#             x = ''.join(sorted(strs[i]))
#             if x not in d:
#                 d[x] = [strs[i]]
#             else:
#                 d[x].append(strs[i])
#         return d.values()
    
# Time Complexity — O(n*len(array item))
# Space Complexity — O(n)