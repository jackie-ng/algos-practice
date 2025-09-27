"""
1) a character is also considered a palindrome. 
2) even length
3) odd length 
palindromic substring with a twist:
to keep track of the max size of possible substring


"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## Memoization
        # n = len(s)
        # if n == 0:
        #     return ""
        # @cache
        # def isPal(i: int, j: int) -> bool:
        #     if i >= j:
        #         return True
        #     if s[i] != s[j]:
        #         return False
        #     return isPal(i+1, j-1)
        # best_i, best_len = 0, 1
        # for i in range(n):
        #     for j in range(i, n):
        #         if isPal(i, j):
        #             cur_len = j - i + 1
        #             if cur_len > best_len:
        #                 best_i, best_len = i, cur_len
        # return s[best_i : best_i + best_len] 
        # Expand around center:
        n = len(s)
        if n == 0:
            return n
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            start = l + 1
            length = r - l - 1
            return start, length

        best_start, best_len = 0, 1
        for center in range(n):
            #odd length palindroms
            start, length = expand(center, center)
            if length > best_len:
                best_start, best_len = start, length
            #even length palindroms
            start, length = expand(center, center + 1)
            if length > best_len:
                best_start, best_len = start, length
        return s[best_start : best_start + best_len]