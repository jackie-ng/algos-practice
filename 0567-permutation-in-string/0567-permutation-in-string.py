from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Initialize the frequency count for s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Initialize the sliding window with the first len(s1) characters of s2
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # Check if the initial window is a permutation of s1
        if window_count == s1_count:
            return True
        
        # Slide the window through s2
        for i in range(len(s1), len(s2)):
            # Remove the leftmost character of the previous window
            left_char = s2[i - len(s1)]
            window_count[ord(left_char) - ord('a')] -= 1
            
            # Add the new rightmost character to the window
            right_char = s2[i]
            window_count[ord(right_char) - ord('a')] += 1
            
            # Check if the current window matches s1's frequency count
            if window_count == s1_count:
                return True
        
        return False