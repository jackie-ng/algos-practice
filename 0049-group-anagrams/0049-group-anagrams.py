class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the characters in the word to form the key
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

        return list(anagrams.values())
        # res = defaultdict(list) # Defining a dictionary with values as a list (mapping charCount to list of Anagrams)
        # for s in strs:
        #     count = [0] * 26 # a ... z
            
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
            
        #     # print(res[tuple(count)], "s:", s)
        #     res[tuple(count)].append(s) # list cannot be keys =>  tuple
            
        # return list(res.values())
