# # Two Hash Maps
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # Check for obvious fail case
#         if len(ransomNote) > len(magazine): return False
        
#         magazine_counts = collections.Counter(magazine)
#         ransom_note_counts = collections.Counter(ransomNote)
        
#         # print(magazine_counts)
#         # print(ransom_note_counts)
        
#         # For each *unique* character in the ransom note:
#         for char, count in ransom_note_counts.items():
#             # Check that the count of char in the magazine is equal
#             # or higher than the count in the ransom note.
#             magazine_count = magazine_counts[char]
#             if magazine_count < count:
#                 return False
            
#         # if we got this far, we can build the note
#         return True

# One Hash Map
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Check for obvious fail case
        if len(ransomNote) > len(magazine): return False
        letters = collections.Counter(magazine)
        
        for c in ransomNote:
            # if there are none of c left, return False
            if letters[c] <= 0: return False
            # remove one of c from the counter
            letters[c] -= 1
        # if we got this far, we can build the note
        return True