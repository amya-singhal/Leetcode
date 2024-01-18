# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # None --> '_'
    def serialize(self, root):
        s = ""
        def helper(root):
            nonlocal s
            if not root:
                s += '_'
                return
            s += str(root.val)
            s += ","
            helper(root.left)
            s += ","
            helper(root.right)
        helper(root)
        return s
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
      
    def deserialize(self, data):
        que = deque(data.split(","))
        def helper(que):
            element = que.popleft()
            if element == '_':
                return None
            answer = TreeNode(int(element))
            answer.left = helper(que)
            answer.right = helper(que)
            return answer
        return helper(que)
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))