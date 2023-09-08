class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# class Codec:
#     def encode(self, strs):
#         """Encodes a list of strings to a single string."""
#         return 'π'.join(strs)
        
#     def decode(self, s):
#         """Decodes a single string to a list of strings."""
#         return s.split('π')