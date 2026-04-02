class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)  # влево
        else:
            root.right = self.insertIntoBST(root.right, val)  # вправо
        
        return root