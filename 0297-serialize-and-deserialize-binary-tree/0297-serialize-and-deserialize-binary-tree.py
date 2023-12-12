# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(node):
            # Base case
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals_array = data.split(",")
        self.i = 0
        
        def dfs():
            if vals_array[self.i] == "N":
                self.i += 1 # Move the index pointer to the next value
                return None
            node = TreeNode(int(vals_array[self.i])) # Create a new TreeNode with the current integer value

            self.i += 1 # Move the index pointer to the next value
            
            # Recursively deserialize the left and right subtrees
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))