class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        totalOdds = sum([i%2 for i in count.values()])
        return len(s) if totalOdds <= 1 else len(s)-totalOdds+1