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
        ans = ""
        def helper(root):
            nonlocal ans
            if not root:
                ans += '_,'
            else:
                ans += str(root.val)
                ans += ','
                helper(root.left)
                helper(root.right)
        helper(root)
        return ans[:len(ans)-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        q = deque(data.split(","))
        def helper():
            nonlocal q
            if not q:
                return None
            x = q.popleft()
            if x == '_':
                ans = None
            else:
                ans = TreeNode(int(x))
                ans.left = helper()
                ans.right = helper()
            return ans
        return helper()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))