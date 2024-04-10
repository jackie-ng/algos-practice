class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = set()
        for char in s:
            if char not in counts:
                counts.add(char)
            else:
                counts.remove(char)
        return len(counts) <= 1