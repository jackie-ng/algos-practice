"""
- for this question, we have to go through every character and check if its a valid palindromic substring:
    we would have a helper function to check if its palindrome. 
    but remember, we have to check even and odd length
- then we would increment and check if its valid palidromic substring again until the end of the string
"""
class Solution:
    def countSubstrings(self, s):
        if not s:
            return 0
        ans = 0
        def expandCenter(i, j,s):
            count = 0
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    return count
                i-=1
                j+=1
                count+=1
            return count
        for i in range(len(s)):
            ans += expandCenter(i, i, s)
            ans += expandCenter(i, i+1, s)
        return ans






        



        # (s, i, i) for odd -> spread out to the left and right
        # (s, i, i+1) for even -> spread out to the left and right
#time complexity: O(N^2)
#space complexity: O(N) because of the call stack?