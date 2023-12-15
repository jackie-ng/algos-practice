class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         In a sorted list of words,
# for any word A[i],
# all its sugested words must following this word in the list.

# For example, if A[i] is a prefix of A[j],
# A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]

# Explanation
# With this observation,
# we can binary search the position of each prefix of search word,
# and check if the next 3 words is a valid suggestion.


# Complexity
# Time O(NlogN) for sorting
# Space O(logN) for quick sort.

# Time O(logN) for each query
# Space O(query) for each query
# where I take word operation as O(1)
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res
    
#        products.sort() # time O(nlogn)
#         array_len = len(products)
#         ans = []
#         input_char = ""

#         for chr in searchWord:
#             tmp = []
#             input_char += chr
#             insertion_index = self.binary_search(products, input_char) # find where input_char can be inserted in-order in the products array
#             for word_ind in range(insertion_index, min(array_len, insertion_index+3)): # check the following 3 words, if valid
#                 if products[word_ind].startswith(input_char):
#                     tmp.append(products[word_ind])
#             ans.append(tmp)
#         return ans

#     def binary_search(self, array, target): # bisect.bisect_left implementation
#         lo = 0
#         hi = len(array)

#         while lo < hi:
#             mid = (lo + hi) //2
#             if array[mid] < target: lo = mid + 1
#             else: hi = mid
#         return lo


# class Node :
#     def __init__(self):
#         self.children = {}
#         self.endHere = 0
#         self.suggestions = []

# class Trie :
#     def __init__(self,maxSuggest):
#         self.maxSuggest = maxSuggest
#         self.root = Node()
        
#     def addString(self,string):
#         curr = self.root
#         for k in string:
#             if k not in curr.children :
#                 curr.children[k] = Node()
#             curr = curr.children[k]
#             self.addSuggestion(curr,string)     # add string as suggestion of curr char
#         curr.endHere +=1
        
#     def addSuggestion(self,node,word):
#         if len(node.suggestions) < self.maxSuggest :
#             node.suggestions.append(word)
        
#     def searchSuggestions(self,string):
#         res = [[] for _ in range(len(string))]
#         curr = self.root
#         for idx,k in enumerate(string):
#             if k not in curr.children:
#                 break
#             curr = curr.children[k]
#             res[idx] = curr.suggestions
#         return res
            

# def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#     products.sort()
    
#     maxSuggest = 3
#     trie = Trie(maxSuggest)
    
#     for product in products:
#         trie.addString(product)
    
#     res = trie.searchSuggestions(searchWord)
#     return res