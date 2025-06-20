class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Solution 1: Hashmap
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for j in countS:
        #     if countS[j] != countT.get(j, 0):
        #         return False
        # return True
        ## Solution 2: Frequency array
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        print(freq)
        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        return True