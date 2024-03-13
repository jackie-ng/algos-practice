class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initiate a set to filter out duplicate characters in the current substring
        # we will use two pointers method in this problem
        # As long as s[r] is already in setDistinct, we will 
        setDistinct = set()
        res = 0
        # Start l = 0, r = 0.
        l = 0
        for r in range(len(s)):
            # as long as the current character is already in the set
            # which means it's a duplicate character (Let's say s[l] = s[r])
            # => remove s[l] from setDistinct, move pointer by 1
            while s[r] in setDistinct:
                setDistinct.remove(s[l])
                l += 1
            # if it's not a duplicate character in the right side, add it to setDistinct
            # expand the window r-l+1
            setDistinct.add(s[r])
            res = max(res, r-l+1)
            
        return res
        
