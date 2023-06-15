# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        s = ""
        if not root:
            return s
        def dfs(root):
            nonlocal s
            if not root:
                s = s + '!,'
                return
            s  = s + str(root.val) + ','
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return s
        """Encodes a tree to a single string.
       
        :type root: TreeNode
        :rtype: str
        """
       

    def deserialize(self, data):
        if len(data) == 0:
            return None
        q = data.split(",")
        global x
        x = 0
        """Decodes your encoded data to tree.
       
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            global x
            if q[x] == '!':
                return None
            ans = TreeNode(q[x])
            x += 1
            ans.left = helper()
            x +=1
            ans.right = helper()
            return ans
        return helper()

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans