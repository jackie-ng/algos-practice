class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        setDistinct = set()
        
        for r in range(len(s)):
            while s[r] in setDistinct:
                setDistinct.remove(s[l])
                l += 1
            setDistinct.add(s[r])
            res = max(res, r-l+1)
        return res