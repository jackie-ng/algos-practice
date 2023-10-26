class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            
            res = max(res, r - l + 1)
        return res
                