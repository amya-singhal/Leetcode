# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.i = 0
        def createInorder(root):
            if not root:
                # self.inorder.append(None)
                return
            createInorder(root.left)
            self.inorder.append(root)
            createInorder(root.right)
        createInorder(root)                 
        

    def next(self) -> int:
        nextPointer = self.inorder[self.i].val
        self.i += 1
        return nextPointer
        
    def hasNext(self) -> bool:
        if len(self.inorder) <= self.i:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()