"""
abcabcbb 
    --> longest = abc --> longest length is 3

abcabcbb

c a b
window = 3

pwwkew
window = p w w 
we use while because we want to run until there are no duplicates anymore! 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = 0
        hash_set = set()
        for r in range(len(s)):
            # if s[r] is already seen, shrink the window
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            max_length = max(max_length, r-l+1)
        return max_length
        