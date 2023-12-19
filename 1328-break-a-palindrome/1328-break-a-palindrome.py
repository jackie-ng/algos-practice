class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # Greedy approach:
        # Since it's a palindrome, we can check half of the string
        # + Split the string in half
        # + "a" is lexicographically smallest 
        #### => check if it's equal "a" => replace it with "b" (next lexicographically smallest)
        #### => Check if it's NOT equal "a" => replace a string to "a"
        n = len(palindrome)
        for i in range(n//2):
            if palindrome[i] != "a": 
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b" if n > 1 else ""
    
