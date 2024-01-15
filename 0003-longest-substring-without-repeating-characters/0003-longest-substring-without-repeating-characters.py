class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSub = 0
        setDistinct = set()
        l = 0
        
        for r in range(len(s)):
            while s[r] in setDistinct:
                setDistinct.remove(s[l])
                l += 1
            setDistinct.add(s[r])
            # l -= 1
            maxSub = max(maxSub, r - l + 1)
        
        return maxSub